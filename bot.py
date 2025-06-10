import discord
import random
import os
import re
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# This regex matches valid arithmetic expressions like: 5+5, 8 - 3, 4 * 2
ARITHMETIC_REGEX = re.compile(r'^\s*[\d\s+\-*/()]+$')

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip()

    # Check if it's a number or a valid arithmetic expression
    if content.isdigit() or ARITHMETIC_REGEX.fullmatch(content):
        emojis = message.guild.emojis

        if emojis:
            emoji = random.choice(emojis)
            try:
                await message.add_reaction(emoji)
            except discord.HTTPException:
                print(f"Couldn't react with emoji: {emoji}")
        else:
            print("No custom emojis found.")

    await bot.process_commands(message)

load_dotenv()
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))  # Load token from environment variable
