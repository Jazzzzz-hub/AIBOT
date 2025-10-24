# AIBOT
Language: Python Dependencies:  Built-in socket library (for IRC)  openai (or any AI API you prefer)  You’ll just need your OpenAI API key and server details.

How to Run It
1. Install Python 3 (most systems already have it).
2. Install the OpenAI library:
pip install openai
3. Edit the configuration section:
Replace irc.yourserver.net with your Bahamut server hostname (or localhost if you’re testing locally).
Put your OpenAI API key in the openai.api_key line.
Set your desired CHANNEL (e.g. #channel).
4. Run the bot:
python3 aibot.py
5. Usage
In your IRC channel, type:
!ask what is Bahamut IRCD?
Nickname: Bahamut IRCD is a C-based IRC daemon originally developed for DALnet...
