# Imports and Froms

import discord
import aiosqlite3
import asyncio
import os
import sqlite3
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from loggerpy import Logger, Level

# Log Stuff

logger = Logger()

# DotEnv

load_dotenv(find_dotenv())

NONSENSE_TOKEN = os.getenv("NONSENSE_TOKEN")
NONSENSE_PREFIX = os.getenv("NONSENSE_PREFIX")

# Other Functions

nonsense = commands.Bot(command_prefix=NONSENSE_PREFIX, help_command=None)
slash = SlashCommand(nonsense, sync_commands=True)

# Other Variable Shitz

guild_ids = [
    856094103045144576,
    865936964439638042
]

# Cog Stuff

@nonsense.command()
@commands.is_owner()
async def load(ctx, extension):
    nonsense.load_extension(f'CommonSense.{extension}')
    await ctx.send(f'{extension} successfully loaded.')

@nonsense.command()
@commands.is_owner()
async def unload(ctx, extension):
    nonsense.unload_extension(f'CommonSense.{extension}')
    await ctx.send(f'{extension} successfully unloaded.')

@nonsense.command()
@commands.is_owner()
async def reload(ctx, extension):
    nonsense.unload_extension(f'CommonSense.{extension}')
    nonsense.load_extension(f'CommonSense.{extension}')
    await ctx.send(f'{extension} successfully reloaded.')

for filename in os.listdir('./CommonSense'):
    if filename.endswith('.py'):
        nonsense.load_extension(f'CommonSense.{filename[:-3]}')

# Slash Command Stuff Lol

@slash.slash(name='hello', description='Nonsense says hello and gives very little information?', guild_ids=guild_ids)
async def hello(ctx):
    await ctx.send('Hi? I\'m Nonsense. I assume your not going to leave me alone so just use `n?help` to find my commands, thank you I guess?')

# Button Testing Shit

# @nonsense.command(name='button-test')
# async def button_test(ctx):
#     buttons = [
#         create_button(style=ButtonStyle.blue, label="lol"),
#         create_button(style=ButtonStyle.green, label="testing bro")
#     ]
#     action_row = create_actionrow(*buttons)

#     await ctx.send('ay', components=[action_row])

nonsense.run(NONSENSE_TOKEN)