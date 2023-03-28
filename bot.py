import discord
import responses
import json

with open('config.json') as f:
    data = json.load(f)

async def send_msg(msg, user_msg, is_private):
    ''' 
    Handle response from user message and send response to DM or discord server
    '''
    try:
        response = responses.handle_response(user_msg)
        await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    '''
    Run bot
    '''
    TOKEN = data['token']
    client = discord.Client()

    @client.event
    # when bot is started
    async def on_ready():
        print(f'{client.user} is now running!')
    
    client.run(TOKEN)




