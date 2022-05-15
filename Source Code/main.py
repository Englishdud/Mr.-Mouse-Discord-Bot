import os
import discord
import requests
import json
import random
from replit import db

sad_Words = ["sad", "trash", "depressed", "stupid"]

random_Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "666", "777"]

starter_encouragements = ["Never Gonna Give You Up -Rick",
                          "Its Okay Everyone Here Has The Same Feelings -Ian Joshua Dela Paz",
                          "Please be quiet im trying to read a book here -Ken Lamar Nova", "I love my xbox -Aarav"]

my_secret = os.environ['TOKEN']

client = discord.Client()


def get_quote():
    response = requests.get
    ("http://zenquotes.io/api/random/quotes")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
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

    if msg.startswith('sudo 1 + 1'):
        await message.channel.send('7')

    if "calculate" in message.content or "Calculate" in message.content:
        i = message.content.split("calculate ", 1)[1]
        number = random.choice(random_Numbers)
        letter = 'd'

        for ii in i:
            try:
                number == ii
            except:
                try:
                    if letter == "*":
                        number *= float(ii)
                        print
                    elif letter == "-":
                        number -= float(ii)
                    elif letter == "+":
                        number += float(ii)
                    elif letter == "/":
                        number /= float(ii)
                    if int(ii) != ii:
                        ii = letter
                except:
                    try:
                        if ii == "*":
                            ii == letter
                        elif ii == "-":
                            ii == letter
                        elif ii == "+":
                            ii == letter
                        elif ii == "/":
                            ii == letter
                    except:
                        break

        await message.channel.send(number)

    if any(word in msg for word in sad_Words):
        await message.channel.send(random.choice(starter_encouragements))


client.run('')