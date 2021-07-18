import discord
import sqlite3
import asyncio
from discord.ext import commands
from cogwatch import Watcher

async def start_watcher(nonsense):
    watcher = Watcher(nonsense, path="nonsense.py")
    await watcher.start()

class Events(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.Cog.listener()
    async def on_ready(self):
        nonBase = sqlite3.connect('nonSense.sqlite')
        nonCursor = nonBase.cursor()
        
        asyncio.create_task(start_watcher(self.nonsense))
        print('Nonsense is online..interesting.')
        statuss = 'Who are you? Who am I? | n?help'
        await self.nonsense.change_presence(activity=discord.Game(statuss))

    @commands.Cog.listener()
    async def on_disconnect(self):
        print('Nonsense disconnected, looks like he doesn\'t exist anymore..WAIT NO THATS NONSENSE!!')

def setup(nonsense):
    nonsense.add_cog(Events(nonsense))