import discord
import asyncio

# Define intents and create a client instance.
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content if needed

client = discord.Client(intents=intents)

# Global variables for source and target channel IDs.
source_channel_id = None
target_channel_id = None

@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")

    # Prompt for the source and target channel IDs.
    global source_channel_id, target_channel_id
    try:
        source_channel_id = int(input("Enter the Source channel/group ID: "))
        target_channel_id = int(input("Enter the Target channel/group ID: "))
    except ValueError:
        print("Please enter valid numeric IDs!")
        await client.close()

@client.event
async def on_message(message):
    # Only forward messages from the specified source channel.
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

# Replace 'YOUR_BOT_TOKEN' with the actual token from your Discord Developer Portal.
client.run("YOUR_BOT_TOKEN")
