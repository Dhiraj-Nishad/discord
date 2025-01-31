import asyncio
import discord
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Discord client with intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intents
app = discord.Client(intents=intents)

async def login():
    """Handle login by entering username and password."""
    # Note: You cannot log in using username and password with discord.py.
    # Instead, use the bot token directly.
    print("You should not enter username and password. Please use the bot token.")
    return

async def send_message(channel):
    """Send a message to Discord with a 5-second delay between sends."""
    await app.wait_until_ready()  # Wait until the bot is ready
    try:
        # Example of sending a message to a specific channel
        channel = app.get_channel(channel_id)  # Replace with your channel ID
        await channel.send("Hello from the bot!")  # Replace with your message
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    """Main function to handle Discord bot interactions."""
    print("Welcome to your Discord bot. Type 'login' to access Discord directly.")
    
    try:
        await login()  # Call login (this will just print a message)
        
        channel_id = int(input("Enter the channel ID where you want to send messages: "))  # Get channel ID from user
        
        messages = []
        while True:
            try:
                await send_message(channel_id)  # Pass the channel ID variable
                print(f"Message sent in channel ID {channel_id}.")
                await asyncio.sleep(5)  # Use asyncio.sleep instead of time.sleep for async context
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Goodbye.")

if __name__ == "__main__":
    app.run(os.getenv("DISCORD_TOKEN"))  # Run the bot using the token from .env file
