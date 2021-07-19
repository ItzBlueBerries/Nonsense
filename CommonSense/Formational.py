import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

class Formational(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.command()
    async def help(self, ctx):
        """ Gives you info on everything, I guess? """

        Normalized = discord.Embed(title='Normalized', color=discord.Colour.blue())

        Normalized.add_field(name='Hello', value='`Nonsense says hello and gives very little information?`')
        Normalized.add_field(name='Advertisement', value='`Things I want to advertise?`')
        Normalized.add_field(name='Friends', value='`My bot friends. :)`')

        Formational = discord.Embed(title='Formational', color=discord.Colour.blue())

        Formational.add_field(name='Help', value='Gives you info on everything, I guess?')

        Modmissions = discord.Embed(title='Modmissions', color=discord.Colour.blue())

        Modmissions.add_field(name='Kick', value='`Kicks mentioned user?`')
        Modmissions.add_field(name='Ban', value='`Bans mentioned user?`')

        embeds = [
            Formational,
            Normalized,
            Modmissions
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

def setup(nonsense):
    nonsense.add_cog(Formational(nonsense))