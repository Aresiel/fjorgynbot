from discord.ext import commands
import helpers
from jishaku.paginators import PaginatorEmbedInterface

def setup(bot):
    bot.add_cog(ProseEdda(bot))


class ProseEdda(commands.Cog, name="Prose Edda"):
    def __init__(self, bot):
        self.bot = bot
        self.paginator = commands.Paginator(max_size=1000)
        with open("prose_edda.txt") as f:
            for line in f.readlines():
                self.paginator.add_line(line)

    @commands.command(brief="Read the prose edda")
    async def edda(self, ctx):
        interface = PaginatorEmbedInterface(ctx.bot, self.paginator, owner=ctx.author)
        await interface.send_to(ctx)
