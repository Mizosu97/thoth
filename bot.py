import os
import discord
import openai

openai.api_key = ""

TOKEN = ""

intents = discord.Intents.all()
client = discord.Client(intents=intents)


completion = openai.Completion()

scl = ""

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = scl
    prompt = f'{chat_log}User: {question}\nmeiosu: '
    res = completion.create(prompt=prompt, engine="davinci", stop=['User', '\n', 'meiosu'], temperature=0.9, top_p=1, frequency_penalty=0.8, presence_penalty=0.1, best_of=1, max_tokens=512)
    ans = res.choices[0].text.strip()
    return ans




@client.event
async def on_ready():   
    print("Were ready to rumble!")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("<@!1041846368681074718> ") or msg.content.startswith("<@1041846368681074718>"):
        response = ask(msg.content.split(" ", 1)[1])
        print(response)
        await msg.channel.send(response)


client.run(TOKEN)

