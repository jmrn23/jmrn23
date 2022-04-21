from distutils import extension
import discord 
import os 
from discord.ext import commands

dir_path = os.path.dirname(os.path.realpath(__file__))

client=commands.Bot(command_prefix="!")

for filename in os.listdir(dir_path + "\\bot"):
    if(filename.endswith('.py')):
         client.load_extension(f'bot.{filename[:-3]}')

client.run("YOUR TOKEN")

