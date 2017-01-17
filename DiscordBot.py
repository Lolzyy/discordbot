import discord
import random
import cleverbot
from cleverbot import Cleverbot

client = discord.Client()



with open('cita.txt', 'r') as myfile:
    content = myfile.readlines()
_arrayM = [
    "Anna",
    "Vanna",
    "Fortunata",
    "Liliana",
    "Troia"
]

_arrayR = [
    "Top",
    "Mid",
    "Jungle",
    "ADC",
    "Support"
]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#messages
@client.event
async def on_message(message):
    if message.content.startswith('!citazione'): #return random msg from file list
        index = random.randint(0, len(content)-1)
        await client.send_message(message.channel, content[index])
    elif message.content.startswith('!mamma'):
        index2 = random.randint(0, len(_arrayM)-1) #return random string from array
        await client.send_message(message.channel, _arrayM[index2])
    elif message.content.startswith('!ruolo'):
        index3 = random.randint(0, 5)
        await client.send_message(message.channel, _arrayR[index3])
    elif message.content.startswith('!bot'):
        domanda = message.content.replace('!bot', '')
        cb = Cleverbot()
        risposta = cb.ask(domanda)
        await client.send_message(message.channel, risposta)

client.run('')
