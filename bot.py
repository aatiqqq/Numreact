import os
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
        await message.add_reaction('🐄')

    await bot.process_commands(message)


load_dotenv()
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))  # Load token from environment variable