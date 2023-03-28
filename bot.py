import discord
import responses
import json
import mealDB

with open('config.json') as f:
    data = json.load(f)

async def send_message(message, user_message, is_private):
    ''' 
    Handle response from user message and send response to DM or discord server
    '''
    try:
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        return 

def run_bot():
    '''
    Run bot
    '''
    TOKEN = data['token']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    # when bot is started
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    # when bot detects message
    async def on_message(message):
        if message.author == client.user:
            # avoid bot creating commands
            return 

        username = message.author
        user_message = message.content
        channel = message.channel

        # log user message
        print(f'{username} said: "{user_message}" ({channel})')

        # meal API commands
        if user_message == '?random' or user_message == '?r':
            await mealDB.random_meal(message)
        if user_message.startswith('?search') or user_message.startswith('?s'):
            await mealDB.search_meal(message)
        if user_message.startswith('?category') or user_message.startswith('?c'):
            await mealDB.get_meals_by_category(message)

        # user help commands
        if user_message == '?help':
            # send to channel 
            await channel.send('Check out your direct messages for a list of commands!')
            # send to user's DM
            await send_message(message, user_message, is_private=True)
        elif user_message.startswith('?help '):
            await send_message(message, user_message, is_private=False)
        elif user_message.startswith('?') and len(user_message) > 1:
            # command
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)




