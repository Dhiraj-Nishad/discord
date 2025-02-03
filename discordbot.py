import asyncio
import discord

# Create a Discord client instance
client = discord.Client()

# Global variables to store source and target channel IDs
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
    # Only forward messages from the source channel
    if message.channel.id == source_channel_id and message.author != client.user:
        target_channel = client.get_channel(target_channel_id)
        if target_channel is not None:
            try:
                # Format and send the forwarded message
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
