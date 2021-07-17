import discord
from discord.ext import commands
import asyncio

class errorHandler(commands.Cog):

    def __init__(self, nonsense):
        self.nonsense = nonsense

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.BadArgument):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionError):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionFailed):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionNotFound):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.MissingRole):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.BotMissingRole):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.NotOwner):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.MessageNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.UserNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.send(error)
            print(error)
            return

        elif isinstance(error, commands.GuildNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send(error)
            print(error)
            return
        
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
            print(error)
            return

        else:

            raise error

def setup(nonsense):
    nonsense.add_cog(errorHandler(nonsense))