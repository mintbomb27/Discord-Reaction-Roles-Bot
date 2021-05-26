#!/usr/bin/env python3
import discord
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='ggwp ')

core_roles = {
        '<:Emojis_20:846806288800415744>':'2020',
        '<:Emojis_19:846806288675504179>':'2019',
        '<:Emojis_18:846806289187078145>':'2018',
        '<:Emojis_17:846806288909729792>':'2017',
        '<:Emojis_16:846806288955867233>':'2016',
        '<:Emojis_15:846806289295867945>':'2015',
        '<:Emojis_14:846806288519266355>':'2014',
        '<:Emojis_13:846806288533028874>':'2013',
        '😵':'Boomer'
    }

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def post(ctx):
    channel = bot.get_channel(846096128348782635)
    message = await channel.send("""Yo, welcome!:partying_face:

The idea behind setting up this community is to bring together all generations of IEEE-VIT together under one roof. Feel free to interact and have fun.

**React to this message with the last digits of your joining year to get roles.**

kthxbye""")
    for emoji in list(core_roles.keys()):
        await message.add_reaction(emoji)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello I'm alive!")

bot.run(os.getenv("BOT_TOKEN"))
bot.add_command(post)
bot.add_command(hello)