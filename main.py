import os
import discord
from discord.ext import commands

TOKEN = 'MTAyMzUyMzE4MjEwOTUyMzk4OQ.Glwp0P.OFsFDTUmV8Gg2dNcSzIn3RtwCYjJtE2Bw81Icw'
intents = intents = discord.Intents.all()

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix=">",
                   description="Helper bot",
                   intents=intents)

# Runs when Bot Succesfully Connects


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')


@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user:
        return

    #if message.content == 'hola':
    #await message.channel.send(f'{message.content,message.type,message.attachments[0].url}')
    await message.channel.send(message.attachments[0].url)

    await bot.process_commands(message)
    await message.delete()


bot.run(TOKEN)
