import discord
from discord.ext import commands
import DiscordUtils

class Formational(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Help Command', color=discord.Colour.red())

        embed.s

def setup(nonsense):
    nonsense.add_cog(Formational(nonsense))