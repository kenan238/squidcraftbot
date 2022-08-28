import discord
from discord.ext import commands
import random

error_messages = ["No perms?", "You got no perms", "haha **no** (permissions)", "You don't have permissions to do this", "h-hiii you cant execute this command uwu"]

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, phrase):
        await ctx.message.delete()
        await ctx.send(phrase)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pin(self, ctx, messageId: discord.Message):
        if messageId.pinned:
            await messageId.unpin()
            await ctx.reply("Unpinned message.")
            return
        await messageId.pin()
        await ctx.reply("Pinned message.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, message: discord.Message):
        await message.delete()
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title=f"Kicked {member.name + member.discriminator}", color=0xda7dff)
        embed.description = f"Reason: {reason}"
        await member.send(f"You were kicked from {ctx.guild.name}, {f'Reason: {reason}' if reason is not None else 'No reason was given.'}")
        await ctx.reply(embed=embed)
        await member.kick(reason=reason if reason is not None else 'No reason was given.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title=f"Banned {member.name + member.discriminator}", color=0xda7dff)
        embed.description = f"Reason: {reason}"
        await member.send(f"You were banned from {ctx.guild.name}, {f'Reason: {reason}' if reason is not None else 'No reason was given.'}")
        await ctx.reply(embed=embed)
        await member.ban(reason=reason if reason is not None else 'No reason was given.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def pardon(self, ctx, member: int):
        bans = await ctx.guild.bans()
        banned_users = [user.user.id for user in bans]
        if member in banned_users:
            await ctx.guild.unban(bans[banned_users.index(member)].user)
            await ctx.reply(f"Member pardoned.")   
        else:
            await ctx.reply("User does not appear to be banned.")
    
    @pardon.error
    async def pardon_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.reply("Error pardoning member.")
