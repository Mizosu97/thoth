import os
import discord
import openai

openai.api_key = ""

TOKEN = ""
client = discord.Client()

completion = openai.Completion()

start_chat_log = " "

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}User: {question}\nmwaoo: '
    response = completion.create(prompt=prompt, engine="davinci", stop=['User', '\n', 'mwaoo'], temperature=0.9, top_p=1, frequency_penalty)




@client.event
async def on_ready():
    print("Were ready to rumble!")


