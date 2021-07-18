import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

class Formational(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.command()
    async def help(self, ctx):
        """ Gives you info on everything, I guess? """

        Normalized = discord.Embed(title='Help Command', color=discord.Colour.blue())

        Normalized.add_field(name='Hello', value='Nonsense says hello and gives very little information?')

        Formational = discord.Embed(title='Help Command', color=discord.Colour.blue())

        Formational.add_field(name='Help', value='Gives you info on everything, I guess?')

        embeds = [
            Formational,
            Normalized
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

def setup(nonsense):
    nonsense.add_cog(Formational(nonsense))