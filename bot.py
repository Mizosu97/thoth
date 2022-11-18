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

chat_log = BOT_DESCRIPTION
def ask(question, auth, chats):
    prompt = f'{chats}\nUser {auth}: {question}\n{BOT_NAME}: '
    res = completion.create(prompt=prompt, engine="davinci", stop=['User'], temperature=0.9, top_p=1, frequency_penalty=0.8, presence_penalty=0.1, best_of=1, max_tokens=512)
    ans = res.choices[0].text.strip()
    global chat_log 
    chat_log = chat_log + f'\nUser {auth}: {question}'
    return ans




@client.event
async def on_ready():   
    print(BOT_NAME + " is now active!")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("<@!" + DISCORD_BOT_ID + "> ") or msg.content.startswith("<@" + DISCORD_BOT_ID + ">"):
        response = ask(msg.content.split(" ", 1)[1], msg.author.name, chat_log)
        print("----------------------------------------------------")
        print("[ " + msg.author.name + " ]>> " + msg.content)
        print(" ")
        print("[ " + BOT_NAME + " ]>> " + response)
        print(" ")
        await msg.channel.send(response)
    elif msg.content.startswith(";;chatlogs"):
        print(chat_log)


client.run(DISCORD_TOKEN)

