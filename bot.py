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
    TOKEN = "MTExOTYzMTE5OTg0MTgyMDc2NQ.Gk48GO.XRt4pDvHVOsuQDBi-mm8jJLmRNW1yL2OYSMN-E" # Our Discord Token
    client = discord.Client(intents=discord.Intents.default()) #Preparing to run the bot. Mayber [ERROR1] is here.

    @client.event
    async def on_ready(): #To see if it iniciated properly
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message): #Whenever a message is sent, he is going to see the user who sent it, the message and the channel
        if message.author == client.user:
            return
        username = str(message.author) # Get user's username
        user_message = str(message.content) # Get user's message [ERROR1 = THE BOT IS NOT GETTING THE MESSAGE, HE CAN'T GET TO ANY MESSAGES]
        channel = str(message.channel) # Get user's channel

        print(f"{username} said: '{user_message}' in ({channel})") # Just for debug purposes

        await send_message(message, user_message) # Send message in discord chat

    client.run(TOKEN) # Run the bot