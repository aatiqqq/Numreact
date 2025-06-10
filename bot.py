import os
import re
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands
from keep_alive import keep_alive 

intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True
intents.guilds = True


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
        emojis = message.guild.emojis

        if emojis:
            emoji = random.choice(emojis)

        await message.add_reaction(emoji)
    
    content = message.content.strip()
    if re.match(r'^[\d\s+\-*/().]+$', content):
        try:
            expr = content.replace(' ', '')
            result = eval(expr, {"__builtins__": {}}, {})
            if result is not None and result == int(result):
                emojis = message.guild.emojis
  
                if emojis:
                    emoji = random.choice(emojis)
                await message.add_reaction(emoji)
        except:
            pass

    await bot.process_commands(message)

load_dotenv()
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))
