import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_message(message, *args):
    if message.author == client.user:
        return
    if message.content == '.picom':
        await message.channel.send('Here are my commands\n .ping \ .pong to play\n\U0001F3D3 to play with emojis\nInvite me to your server now! : https://discord.com/api/oauth2/authorize?client_id=985492601073455104&permissions=8&scope=bot')
    if message.content == '.ping':
        await message.channel.send('.pong')
    if message.content == '.pong':
        await message.channel.send('.ping')
    if message.content == '\U0001F3D3':
        await message.channel.send('\U0001F3D3')

client.run(TOKEN)