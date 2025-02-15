import random
import typing

import discord
from discord.ext import commands


class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Heads or tails, what'll it be?")
    async def coinflip(self, ctx: commands.Context):
        result = random.choice(tuple([0, 1]))
        await ctx.send("Heads" if result == 1 else "Tails")

    @commands.command(description="Gives you a random number. (Default: 0 - 10)")
    async def rng(self, ctx: commands.Context, min: typing.Optional[int]=0, max: typing.Optional[int]=10):
        """
        Parameters
        ------------
        min
            The lowest possible number
        max
            The highest possible number
        """
        if max == min:
            await ctx.send(min)
            return

        if max < min:
            max, min = (min, max)

        result = random.randrange(min, max)
        await ctx.send(result)

async def setup(bot):
    await bot.add_cog(math(bot))