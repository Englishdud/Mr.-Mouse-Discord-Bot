import os
import discord
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('sudo hello'):
    await message.channel.send('Hello...What can I do for you today?')

client.run(my_secret)