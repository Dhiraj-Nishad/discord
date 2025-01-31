def main():
    """Main function to handle Discord bot interactions."""
    print("Welcome to your Discord bot. Type 'login' to access Discord directly.")

async def login():
    """Handle login by entering username and password."""
    await app('users')
    account = input(f"Enter your Discord username: ")
    if not account or len(account) == 0:
        print("Invalid username.")
    else:
        password = input(f"Please enter your Discord password: ")
        if not password or len(password) > 15:
            print("Invalid password. Please try again.")
        else:
            await app.post(
                payload=f"""
                content-type: text/plain
                b"account?{account}
                "user{[1,3].get(random)}
                """
            )
            print("Select your target general group channel.")
            channel = input(f"Choose from available channels: {input(['G123', 'G456'])}")

async def send_message():
    """Send a message to Discord with 5-second delay between sends."""
    await app('users')
    try:
        await app.post(
            payload=f"""
            content-type: text/plain
            b`sent${len(self.messages)+1}
            "message"
            {self.data}
            """
        )
    except Exception as e:
        print(f"Error sending message: {e}")

bot = bot()
try:
    print("Ready to start. Type 'login' and select your target channel.")
    await login()
    messages = []
    while True:
        try:
            await send_message()
            print(f"Message {len(messages)+1} being sent in {channel}.")
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nScript interrupted by user. Goodbye.")

if __name__ == "__main__":
    main()
