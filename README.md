# thoth
An artificial intelligence chatbot for Discord that uses OpenAI's GPT-3 language model.

*Thoth, (Greek), Egyptian Djhuty, in Egyptian religion, a god of the moon, of reckoning, of learning, and of writing*


# How do I set it up?

Thoth can be configured exactly how you want it. You can change everything from it's name to it's personality.

## Prequisites
- Create a discord bot application, and get it's token. Make one [here](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications). Make sure the application has message content intent privileges. Invite the bot to a server.
- Create an openAI account, then get an API key [here](https://beta.openai.com/account/api-keys).
- Install the `git` and `python` packages provided by your distribution.
- Install the `discord` and `openai` pip packages with `pip install discord openai`

## Download the code
thoth can be downloaded with the command `git clone https://github.com/Mizosu97/thoth`. Everything will be downloaded into a folder called `thoth`.

Inside the `thoth` folder is a python file called `bot.py`. This is the main file you'll be working with.

## Configuring the bot
thoth needs to be configured to function correctly.

1. Open the `bot.py` file in a text editor. Locate the configuration section.

2. Set `BOT_NAME` to whatever you want the bot's name to be. I suggest making this the same as the discord bot's username. 
**Example:** `BOT_NAME = "thoth"`

3. Set `BOT_DESCRIPTION` to a description of the bot. This description controls how the bot acts, its behavior, and its personality. In the description, you MUST refer to the bot by it's name, not just "the bot".
**Example:** `BOT_DESCRIPTION = "thoth is a smug, highly intelligent AI chatbot who likes to make jokes."`

4. Set `openai.api_key` to your OpenAI API key.

5. Set `DISCORD_TOKEN` to your discord bot token.

6. Set `DISCORD_BOT_ID` to the bot's ID. This can be found by right-clicking the bot's profile in a server, and clicking "Copy ID".


## Using the bot

Run the bot with `python bot.py`.

To communicate with the bot in discord, ping it and type your message.
**Example:** `@thoth Hi, how are you?`

Make sure to read the OpenAI TOS.
