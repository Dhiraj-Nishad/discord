import asyncio
import discord
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Discord client
intents = discord.Intents.default()
intents.messages = True  # Adjust intents as needed
app = discord.Client(intents=intents)

async def login():
    """Handle login by entering username and password."""
    await app.login(os.getenv("DISCORD_TOKEN"))  # Ensure you have a token in your .env file
    account = input(f"Enter your Discord username: ")
    if not account or len(account) == 0:
        print("Invalid username.")
    else:
        password = input(f"Please enter your Discord password: ")
        if not password or len(password) > 15:
            print("Invalid password. Please try again.")
        else:
            # Simulate a post request (you may need to adjust this logic)
            await app.post(
                payload=f"""
                content-type: text/plain
                b"account?{account}
                "user{[1,3].get(random)}
                """
            )
            print("Select your target general group channel.")
            channel = input(f"Choose from available channels: {input(['G123', 'G456'])}")

async def send_message(channel):
    """Send a message to Discord with a 5-second delay between sends."""
    await app.wait_until_ready()  # Wait until the bot is ready
    try:
        await app.post(
            payload=f"""
            content-type: text/plain
            b`sent${len(messages)+1}
            "message"
            {self.data}
            """
        )
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    """Main function to handle Discord bot interactions."""
    print("Welcome to your Discord bot. Type 'login' to access Discord directly.")
    
    try:
        print("Ready to start. Type 'login' and select your target channel.")
        await login()
        
        messages = []
        while True:
            try:
                await send_message(channel)  # Pass the channel variable
                print(f"Message {len(messages)+1} being sent in {channel}.")
                await asyncio.sleep(5)  # Use asyncio.sleep instead of time.sleep for async context
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Goodbye.")

if __name__ == "__main__":
    asyncio.run(main())
