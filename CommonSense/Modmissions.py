import discord
import AOFKJASKAGJKAGJKAL
from discord.ext import commands

class Modmissions(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.group()
    async def mod(self):
        """ Group doesn't need name, lol. """
        return
    
    @mod.command()
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        """ Bans mentioned user? """

        await member.ban(reason=reason)

        ban = discord.Embed(title='Banned?', description=f'***{member.mention}*** *is gone I think, your welcome.*\n***Reason:*** *{reason}*', color=AOFKJASKAGJKAGJKAL.random_color)

        await ctx.send(embed=ban)

    @mod.command()
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        """ Kicks mentioned user? """

        await member.kick(reason=reason)

        kick = discord.Embed(title='Kicked?', description=f'***{member.mention}*** *is gone I think, your welcome.*\n***Reason:*** *{reason}*', color=AOFKJASKAGJKAGJKAL.random_color)

        await ctx.send(embed=kick)

def setup(nonsense):
    nonsense.add_cog(Modmissions(nonsense))