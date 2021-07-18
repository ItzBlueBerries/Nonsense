import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

class Slash(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

def setup(nonsense):
    nonsense.add_cog(Slash(nonsense))