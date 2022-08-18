import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def echo(ctx, *, message):
    await ctx.send(f'{message}')


@bot.command()
async def create(ctx, *, name=None):
    guild = ctx.message.guild
    if name is None:
        await ctx.send('Sorry, but you have to insert a name. Try again, but do it like this: `>create [channel name]`')
    else:
        await guild.create_text_channel(name)
        await ctx.send(f"Created a channel named {name}")


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked from the server.')


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


bot.run(jdata['TOKEN'])
