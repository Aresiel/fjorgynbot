from discord.ext import commands
import helpers


def setup(bot):
    bot.add_cog(Utility(bot))


class Utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="The bot's ping")
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(self.bot.latency*1000)}ms')
