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
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    # when bot is started
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    # when bot detects msg
    async def on_msg(msg):
        if msg.author == client.user:
            # avoid bot creating commands
            return 

        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f'{username} said: "{user_msg}" ({channel})')

        # prefix command for private msg
        if user_msg[0] == '?':
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, is_private=True)
        else:
            await send_msg(msg, user_msg, is_private=False)


    
    client.run(TOKEN)




