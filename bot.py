import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive
from http.server import BaseHTTPRequestHandler, HTTPServer

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
        await message.add_reaction('🐪')

    await bot.process_commands(message)


load_dotenv()
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))  # Load token from environment variable

port = int(os.environ.get('PORT', '8080'))

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

if __name__ == "__main__":
    server_address = ('', port)  # '' means listen on all interfaces
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"🌍 Fake server running on port {port}")
    httpd.serve_forever()