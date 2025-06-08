
# 🐄 Discord Custom Emoji Reaction Bot

A lightweight and fun Discord bot built using Python and `discord.py` that reacts to digit-only messages with a user-defined emoji. Originally created by **Muhammad Rahim** and **Aatiq**.

## 🚀 Features

- Reacts to messages that contain **only digits** (e.g., `99`, `123`) with a **custom emoji** of your choice.
- Ignores messages from other bots.
- Built-in support for Discord command extensions (`discord.ext.commands`).
- Easy to **customize the reaction emoji** — the 🐐 emoji is just the default example.

## 🛠️ Tech Stack

- Python 3.10+
- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 📁 Project Structure

```

bot/
│
├── .env                  # Contains the Discord bot token
├── bot.py                # Main bot logic
└── README.md             # You're reading it!

````

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo


2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory with the following content:

   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot**

   ```bash
   python bot.py
   ```

## 🎨 Customizing the Emoji Reaction

By default, the bot reacts with a 🐐 emoji.
To change this, simply update the emoji string in the `bot.py` file:

```python
# Change this line in on_message event
await message.add_reaction('🐐')  # Replace 🐐 with any emoji you want
```

For example:

```python
await message.add_reaction('🔥')
```

Supports both standard and custom server emojis (make sure your bot has access to custom emojis).

## ✅ Example

**User:** `22`
**Bot:** reacts with 🐐 (or your selected emoji)

**User:** `hello22`
**Bot:** does nothing


## 👨‍💻 Authors

* Muhammad Rahim — [REBELHERE](https://github.com/Rebelhere)
* Aatiq — [CARLBOT](https://github.com/aatiqqq)

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

---

