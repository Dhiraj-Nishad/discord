import asyncio
import discord

# Define and enable intents
intents = discord.Intents.default()
intents.message_content = True  # Enable this if you need to read the content of messages

# Create a Discord client instance with intents enabled
client = discord.Client(intents=intents)

# Global variables to store the source and target channel IDs
source_channel_id = None
target_channel_id = None

@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")
    # Prompt for source and target channel IDs once connected
    global source_channel_id, target_channel_id
    try:
        source_channel_id = int(input("Enter the Source channel/group ID: "))
        target_channel_id = int(input("Enter the Target channel/group ID: "))
    except ValueError:
        print("Please enter valid numeric IDs!")
        await client.close()

@client.event
async def on_message(message):
    # Only forward messages from the source channel that are not from your own account
    if message.channel.id == source_channel_id and message.author != client.user:
        target_channel = client.get_channel(target_channel_id)
        if target_channel is not None:
            try:
                forward_text = f"Forward from {message.author}: {message.content}"
                await target_channel.send(forward_text)
                print(f"Forwarded a message from {message.author}")
            except Exception as e:
                print(f"Error while sending message: {e}")
        else:
            print("Target channel not found!")

async def main():
    # Get user credentials
    email = input("Enter your Discord email: ")
    password = input("Enter your Discord password: ")

    try:
        # Log in using email and password (selfbot login)
        await client.login(email, password)
        await client.connect()
    except Exception as e:
        print(f"Error during login or connection: {e}")

# Start the client event loop
asyncio.run(main())
