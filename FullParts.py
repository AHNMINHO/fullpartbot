import discord

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


client.run("NjE5OTk5ODYxMDI2MTkzNDA4.XXQZ8w.oj-7HfHBMgy_frW80xdKv3rshYk")
