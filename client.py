#!/usr/bin/env python3
import discord
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = discord.Client(intents=intents)

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

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_raw_reaction_add(reaction):
    channel = client.get_channel(846096128348782635) # rules channel
    message = await channel.fetch_message(reaction.message_id)
    member = client.guilds[0].get_member(int(reaction.user_id))
    if member.bot:
        return
    if message.channel != channel:
        print("bye")
        print(message.channel.id)
        return
    else:
        Role = discord.utils.get(client.guilds[0].roles, name=core_roles[str(reaction.emoji)])
        CoreRole = discord.utils.get(client.guilds[0].roles, name='member')
        await member.add_roles(CoreRole)
        await member.add_roles(Role)

@client.event
async def on_raw_reaction_remove(reaction):
    Channel = client.get_channel(846096128348782635) # rules channel
    message = await Channel.fetch_message(reaction.message_id)
    if message.channel != Channel:
        print("bye")
        print(message.channel.id)
        return
    else:
        Role = discord.utils.get(client.guilds[0].roles, name=core_roles[str(reaction.emoji)])
        await client.guilds[0].get_member(int(reaction.user_id)).remove_roles(Role)

client.run(os.getenv("BOT_TOKEN"))