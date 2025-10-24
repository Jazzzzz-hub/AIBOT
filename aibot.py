import socket
import time
import openai

# === CONFIGURATION ===
SERVER = "irc.yourserver.net"   # Your Bahamut IRCD address or localhost
PORT = 6667                     # IRC port
NICK = "AIBot"
IDENT = "AIBot"
REALNAME = "AI Assistant Bot"
CHANNEL = "#startrek"           # Channel to join
OWNER = "Owner-Nick"               # Your nick (optional, for owner commands)

openai.api_key = "YOUR_API_KEY"  # Put your OpenAI API key here

# === IRC SETUP ===
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to {SERVER}:{PORT}...")
irc.connect((SERVER, PORT))
irc.send(f"NICK {NICK}\r\n".encode())
irc.send(f"USER {IDENT} 0 * :{REALNAME}\r\n".encode())
time.sleep(3)
irc.send(f"JOIN {CHANNEL}\r\n".encode())
print(f"Joined {CHANNEL}")

# === MAIN LOOP ===
def send(msg):
    """Send a message to the IRC server."""
    irc.send((msg + "\r\n").encode())

def reply(channel, text):
    """Send a message to the channel."""
    send(f"PRIVMSG {channel} :{text}")

while True:
    data = irc.recv(2048).decode(errors="ignore").strip()
    if not data:
        continue
    print(data)

    # Respond to PING to stay connected
    if data.startswith("PING"):
        send(f"PONG {data.split()[1]}")

    # Detect messages
    if "PRIVMSG" in data:
        nick = data.split('!')[0][1:]
        channel = data.split('PRIVMSG')[1].split(':')[0].strip()
        message = data.split('PRIVMSG')[1].split(':', 1)[1].strip()

        # Command: !ask <question>
        if message.lower().startswith("!ask "):
            question = message[5:]
            reply(channel, f"{nick}: Thinking... 🤔")

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": question}],
                    max_tokens=150,
                    temperature=0.7,
                )
                answer = response.choices[0].message.content.strip()
                for line in answer.split('\n'):
                    reply(channel, f"{nick}: {line}")
            except Exception as e:
                reply(channel, f"{nick}: Error - {str(e)}")
