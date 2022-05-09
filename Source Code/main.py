import os
import discord
import requests
import json
import random
from replit import db

sad_Words = ["sad", "trash", "depressed", "stupid"]

starter_encouragements = ["Never Gonna Give You Up -Rick", "Its Okay Everyone Here Has The Same Feelings -Ian Joshua Dela Paz", "Please be quiet im trying to read a book here -Ken Lamar Nova", "I love my xbox -Aarav"]

my_secret = os.environ['TOKEN']

client = discord.Client()

def get_quote():
  response = requests.get
  ("http://zenquotes.io/api/random/quotes")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] +  " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements
    
@client.event
async def on_ready(encouraging_message):
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('sudo hello'):
    await message.channel.send('Hello...What can I do for you today?')

  if msg.startswith('sudo inspire'):
    await message.channel.send('I ran out of quotes -Rick Astley')

  

  if any(word in msg for word in sad_Words):
    await message.channel.send(random.choice(starter_encouragements))

client.run('')