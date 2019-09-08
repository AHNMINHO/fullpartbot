import discord
import os


client = discord.client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("FullParts전용BOT")
    await client.change_presence(status=discord.Status.online, activity=game)
    

@client.event
async def on_message(message):
    if message.content.startswish("안녕"):
        await message.channel.send("안녕")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

