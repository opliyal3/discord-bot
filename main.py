import discord
from discord.ext import commands
import json
from datetime import datetime, time, timedelta
import asyncio

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
        await ctx.send(f'Created a channel named {name}')


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked from the server')


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


when = time(18, 0, 0)
channel_id = 1


async def timing_send():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    await channel.send('your message here')


async def task():
    now = datetime.utcnow()
    if now.time() > when:
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)
    while True:
        now = datetime.utcnow()
        target_time = datetime.combine(now.date(), when)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)
        await timing_send()
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)


if __name__ == "__main__":
    with open('setting.json', 'r', encoding='utf-8') as jfile:
        jdata = json.load(jfile)

    bot.loop.create_task(task())
    bot.run(jdata['TOKEN'])
