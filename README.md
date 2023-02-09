# Thoth
Developed by [The Duat](https://entertheduat.org).

*Thoth, (Greek), Egyptian Djhuty, in Egyptian religion, a god of the moon, of reckoning, of learning, and of writing.*

**Thoth** is a framework for setting up AI chatbots for Discord. It uses OpenAI's GPT-3 language model for generating human-like conversation realistic enough to pass the Turing test\*.

The more you converse with Thoth, the more it learns. It saves the chatlogs, and looks back on them for reference. Thoth will learn it's own name, and your Discord username without being directly told what it is.

Multiple people are able to converse with Thoth at the same time. It learns to differentiate different people, and even learns their usernames.

Thoth sometimes struggles with remembering certain elements of the conversation.

\*Depends on the BOT\_DESCRIPTION.


# How do I set it up?

**It is easier to set up Thoth on a Linux-based operating system.**

Thoth can be configured exactly how you want it. You can change everything from it's name to it's personality.

## Prequisites
- Create a discord bot application, and get it's token. Make one [here](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications). Make sure the application has message content intent privileges. Invite the bot to a server.
- Create an [OpenAI account](https://openai.com/), then get an API key [here](https://beta.openai.com/account/api-keys). Creating an account is free.
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
