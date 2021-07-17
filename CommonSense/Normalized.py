import discord
from discord.ext import commands

class Normalized(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.command()
    @commands.is_owner()
    async def testing(self, ctx):
        """ Reserved for bot/nonsense testing. """
        await ctx.send('Testing for Nonsense...hey I\'m Nonsense!')

    @commands.command()
    @commands.is_owner()
    async def hello(self, ctx):
        """ Nonsense says hello and gives very little information? """
        await ctx.send('Hi? I\'m Nonsense. I assume your not going to leave me alone so just use `n?help` to find my commands, thank you I guess?')

def setup(nonsense):
    nonsense.add_cog(Normalized(nonsense))