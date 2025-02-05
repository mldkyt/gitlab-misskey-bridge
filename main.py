import os

import discord
import requests
from discord import Message, Intents
from dotenv import load_dotenv


intents = Intents.all()
client = discord.Bot(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.display_name}!')

@client.event
async def on_message(msg: Message):
    if msg.author == client.user:
        return

    if len(msg.embeds) == 0:
        return

    message = "$[x2 Activity on [git.mldchan.dev](https://git.mldchan.dev/):]\n\n"

    if str(msg.channel.id) == os.getenv("CHANNEL_ID"):
        message += f"{msg.embeds[0].description}\n\n"
        date = msg.embeds[0].timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
        message += f"{date}"

    print('Making post:', message)

    requests.post(f"https://{os.getenv("MISSKEY_INSTANCE")}/api/notes/create", json={
        "text": message
    }, headers={
        'Authorization': f'Bearer {os.getenv("MISSKEY_TOKEN")}'
    })

def main():
    load_dotenv()
    print("Starting bot")
    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()

