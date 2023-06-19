# File to manage the bot itself

import discord
import responses



async def send_message(message, user_message): # Here we have an function to send an message
    try:
        response = responses.handle_response(user_message) # Here he is analysing the sentence to have an appropriate response (see responses.py)
        await message.author.send(response) if False else await message.channel.send(response) # Here he sends the message to the channel that the person wrote the message
    except Exception as e:
        print(e)


def run_discord_bot():
    
    TOKEN = "" # Our Discord Token. REMEMBER TO TAKE THIS OUT BEFORE UPLOADING CODE
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    client = discord.Client(intents=intents) # Preparing to run the bot. 

    @client.event
    async def on_ready(): #To see if it iniciated properly
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message): # Whenever a message is sent, he is going to see the user who sent it, the message and the channel
        if message.author == client.user:
            return
        username = str(message.author) # Get user's username
        user_message = str(message.content) # Get user's message 
        channel = str(message.channel) # Get user's channel

        print(f"{username} said: '{user_message}' in ({channel})") # Just for debug purposes

        await send_message(message, user_message) # Send message in discord chat

    client.run(TOKEN) # Run the bot