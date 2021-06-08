import discord
import os
import requests
import json
import time
from keep_alive import keep_alive

client = discord.Client()
msg = message.content

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


def on_quote():
    response = requests.get('https://v2.jokeapi.dev/joke/Dark')
    json_data = json.loads(response.text)

    return (json_data)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$'):
        await message.channel.send(
            "There's no command like this , dummy {0}".format(message.author))
    elif message.content.startswith('$hello'):
        await message.channel.send('Shut up noob')

    elif message.content.startswith('$hi'):
        await message.channel.send('Hi NERD!')

    elif message.content.startswith('$dark'):
        quote = on_quote()
        await message.channel.send(quote['setup'])
        time.sleep(3)
        await message.channel.send(quote['delivery'])
    
    elif msg.startswith('$help'):
      await msg.send('Current commands available:\n n1) $hi \n 2) $hello \n 3) $dark')


keep_alive()
client.run(os.environ['token'])
