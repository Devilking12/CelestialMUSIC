import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from DAXXMUSIC import app



# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAIoB2YaKVnKFofq1z1UT5rKmOFVfRXJAAIICwACfM6wVEDwWL1bR5_CHgQ",
        "CAACAgUAAxkBAAIoC2YaKefYsJgpm-2aCnIctf5hyBmOAAJWCgACDqRRVymzrzFgaWZqHgQ",
        "CAACAgUAAxkBAAIoEGYaKoDAjxlgECZXJnnYWlQG5QjBAAKyBwACIWLxVP1hH6P4jzDhHgQ",
        "CAACAgUAAxkBAAIoD2YaKlXgZY6-rezFHSPw9vXc9FjrAAJ1CAACn07gV5zq8pvlYHScHgQ",
        "CAACAgUAAxkBAAIoDmYaKlHx8aT5WlARCD_w_8tb9JSCAAKGCAAC9XcIVB_qgKaFvkPRHgQ",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪", 
        "💤",
        
    ]
    return random.choice(emojis)
