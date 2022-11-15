import os
import discord
import openai


# configuration

BOT_NAME = ""

BOT_DESCRIPTION = ""

openai.api_key = ""

DISCORD_TOKEN = ""

DISCORD_BOT_ID = ""

# configuration





intents = discord.Intents.all()
client = discord.Client(intents=intents)


completion = openai.Completion()


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = BOT_DESCRIPTION
    prompt = f'{chat_log}User: {question}\n{BOT_NAME}: '
    res = completion.create(prompt=prompt, engine="davinci", stop=['User', '\n', BOT_NAME], temperature=0.9, top_p=1, frequency_penalty=0.8, presence_penalty=0.1, best_of=1, max_tokens=512)
    ans = res.choices[0].text.strip()
    return ans




@client.event
async def on_ready():   
    print("Were ready to rumble!")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("<@!" + DISCORD_BOT_ID + "> ") or msg.content.startswith("<@" + DISCORD_BOT_ID + ">"):
        response = ask(msg.content.split(" ", 1)[1])
        print(response)
        await msg.channel.send(response)


client.run(DISCORD_TOKEN)

