import discord
client = discord.Client()
@client.event
async def on_ready():
print('we have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
if message.author == clinet.user:
return
if message.content.startswith('$hello'):
await message channel.send('Hello!')
client.run($ python3 Example_bot.py
