import os
import re
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.isdigit():
        await message.add_reaction('<:emoji_67:1367207033777946744 >')
    
    content = message.content.strip()
    if re.match(r'^[\d\s+\-*/().]+$', content):
        try:
            expr = content.replace(' ', '')
            result = eval(expr, {"__builtins__": {}}, {})
            if result is not None and result == int(result):
                await message.add_reaction('<:emoji_67:1367207033777946744 >')
        except:
            pass

    await bot.process_commands(message)

load_dotenv()
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))
#aatiq

