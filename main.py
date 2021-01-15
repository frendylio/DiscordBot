############
# Libraries needed
############
import discord
import os
import requests #HTTP request
import json #Returns data
import random
from keep_alive import keep_alive

# Create instance of a client
client = discord.Client()

#########################
# Test
#########################
sad_words = ["#Spencer", "#Diwen","#Willy", "#Keenan", "#Frendy", "Dino"]

random_BS = ["You are The BEST!", "Where is Diwen :("]

#########################
# Helper Functions
#########################
def get_quote(msg):
  # Get HTTP response
  response = requests.get("https://type.fit/api/quotes")

  # Convert into json
  json_data = json.loads(response.text)
  quote = json_data[random.randint(0, 1643)]["text"] + ' \n By: ' + msg
  return quote

# Registe an event
# Asynchronous libraries, We will use callbacks

################################################
# Called when the Bot is ready to be used
################################################
@client.event
async def on_ready():
  # format replaces the 0. with the client/user
  print("Hello, Joe's Best was added by {0.user}".format(client))

################################################
# Called when the Bot receive an message
################################################
@client.event
async def on_message(message):
  # If the message from the bot, ignore
  if message.author == client.user:
    return
  
  msg_one = message.content.lower()
  msg = message.content

  # If the message is a command
  if "joe" in msg_one:
    # Respond message
    await message.channel.send('Mama')
  elif msg.startswith("#Test"):
    quote = get_quote()
    await message.channel.send(quote)

  elif any(word in msg for word in sad_words):
    quote = get_quote(msg)
    await message.channel.send(quote)    
     # await message.channel.send(random.choice(random_BS))    

################################################
# Environment Variables
################################################
keep_alive()
client.run(os.getenv('TOKEN'))