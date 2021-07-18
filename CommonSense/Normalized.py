import discord
import random
import AOFKJASKAGJKAGJKAL
from discord import channel
from discord import errors
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
    async def hello(self, ctx):
        """ Nonsense says hello and gives very little information? """
        await ctx.send('Hi? I\'m Nonsense. I assume your not going to leave me alone so just use `n?help` to find my commands, thank you I guess?')

    @commands.command(aliases=['ads'])
    async def advertisement(self, ctx):
        """ Things I want to advertise? """

        # Invite Links
        VISUAL = 'https://discord.gg/vwZP83zN6b'
        FBTS = 'https://discord.gg/tWNAUsf5MW'

        # Other Shit
        colorig = AOFKJASKAGJKAGJKAL.random_color

        channel = ctx.channel

        await channel.send('Are you sure about this? This is advertisment. `(Reply with yes to allow.)`')

        def check(m):
            return m.content == 'yes' and m.channel == channel

        msg = await self.nonsense.wait_for('message', check=check)

        embed = discord.Embed(title='Advertisements', description='Advertisements I like advertising?', colour=colorig)

        embed.add_field(name='Visual Discord Code', value=f'This is my creators coding server, they include coding help there along with I also am tested there sometimes, [link here.]({VISUAL})')
        embed.add_field(name='Fruitsy Bot Testing Server', value=f'The bot testing server that my creator owns, also where I was created, [link here.]({FBTS})')

        await channel.send(embed=embed)

    # @commands.command(aliases=['colour'])
    # async def color(self, ctx):
    #     """ Your favorite color I guess? I don't know. """

    #     chan = ctx.channel
    #     args = None

    #     await chan.send('Whats your favorite color/colour?')

    #     def checkit(me):
    #         return me.content == f'{args}' and me.channel == chan

    #     okiethenlol = await self.nonsense.wait_for('message', check=checkit)

    #     await chan.send('{} is a cool color/colour I guess.'.format(okiethenlol))

def setup(nonsense):
    nonsense.add_cog(Normalized(nonsense))