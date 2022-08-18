import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def echo(message):
    if message.author == client.user:
        return

    if message.content:
        await message.channel.send(message.content)


client.run()
