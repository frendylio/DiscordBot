############
# Libraries needed
############
import discord
import os
import requests #HTTP request
import json #Returns data
import random
from keep_alive import keep_alive

# For music
import youtube_dl
import os
from discord.ext import commands 
# pip install PyNaCl

# Create instance of a client
client = discord.Client()
client = commands.Bot(command_prefix=['!Eggplant '])

#########################
# Test
#########################
sad_words = ["#Spencer", "#Diwen","#Willy", "#Keenan", "#Frendy", "#Dino", "#Vito", "#Luis"]

random_BS = ["You are The BEST!", "Where is Diwen :("]

#########################
# Helper Functions
#########################
def get_quote(msg):
  # Get HTTP response
  response = requests.get("https://type.fit/api/quotes")

  # Convert into json
  json_data = json.loads(response.text)
  quote = json_data[random.randint(0, 1643)]["text"] + ' \nBy: ' + msg
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
  
  # We add this to  allow event and command messages
  await client.process_commands(message)
  
  # If the message from the bot, ignore
  if message.author == client.user:
    return
  
  msg_one = message.content.lower()
  msg = message.content
 # name = message.author.name

  # If the message is a command
  if "joe" in msg_one:
    # Respond message
    await message.channel.send('Mama')
  elif msg.startswith("#Test"):
    quote = get_quote(client.user.name)
    await message.channel.send(quote)

  elif msg in sad_words:
    quote = get_quote(msg[1:])
    await message.channel.send(quote) 
    
  elif msg == "$Willy":
    quote = os.getenv('Willy')
    quote = "<@" + quote + ">"
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 

  elif msg == "$Vito":
    quote = os.getenv('Vito')
    quote = "<@" + quote + ">"
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote)     

  elif msg == "$Luis":
    quote = os.getenv('Luis')
    quote = "<@" + quote + ">"
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote) 
    await message.channel.send(quote)      

  # elif any(word in msg for word in sad_words):
  #   quote = get_quote(name)
  #   await message.channel.send(quote)    
     # await message.channel.send(random.choice(random_BS))    

################################################
# Music Bot 
# ctx = context
################################################

####################
# Play music
####################
@client.command()
async def play(ctx, url : str = "https://www.youtube.com/watch?list=RDckZlj2p8W9M&v=ckZlj2p8W9M"):

  #########
  # Check if there is a file
  #########
  song_there = os.path.isfile("song.mp3")
  try:
      if song_there:
          os.remove("song.mp3")
  except PermissionError:
      await ctx.send("Wait for Joe to finish playing with his Eggplant or use the 'stop' command")
      return

  #Channel
  channel = "timeout"
  if not channel:
      await ctx.send("Joe Sad, Cannot play with your Eggplant because you are not in a Voice Channel.")
      return  
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)

  # jOIN VOICE Channel
  await voiceChannel.connect()

  #Voice client
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  
  ##########
  # Downlaod from youtube_dl
  ##########
  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
      
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
        os.rename(file, "song.mp3")

  await voice.play(discord.FFmpegPCMAudio("song.mp3"))  

####################
# Leave Channel
####################
@client.command()
async def leave(ctx):

  #Voice client
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  
  # Leave  VOICE Channel
  if voice:
    await voice.disconnect()    
  else:
      await ctx.send("Joe's Best is too busy with his eggplant. He is not even in the channel! There is no place to leave.")

####################
# Pause Channel
####################
@client.command()
async def pause(ctx):

  #Voice client
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  
  # Pause VOICE Channel
  if voice.is_playing():
    voice.pause()
  else:
      await ctx.send("Joe's Best finished playing with his eggplant. There  is nothing to pause.")      

####################
# resume Channel
####################
@client.command()
async def resume(ctx):

  #Voice client
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  
  # Resume VOICE Channel
  if voice.is_paused():
    voice.resume()
  else:
      await ctx.send("Joe's Best is playing with his eggplant. You hear his moaning. There is nothing to resume")       


################################################
# Environment Variables
################################################
keep_alive()
client.run(os.getenv('TOKEN'))