# thoth
An artificial intelligence chatbot for Discord that uses OpenAI's GPT-3 language model.

*Thoth, (Greek), Egyptian Djhuty, in Egyptian religion, a god of the moon, of reckoning, of learning, and of writing*


# How do I set it up?

Thoth can be configured exactly how you want it. You can change everything from it's name to it's personality.

## Prequisites
- Create a discord bot application, and get it's token. Make one [here](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications). Make sure the application has message content intent privileges.
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
