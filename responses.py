import random

def handle_response(msg):
    p_msg = msg.lower()

    if p_msg == 'hello':
        return 'Hey there!'

    if p_msg == 'roll':
        return str(random.randint(1,6))
    
    if p_msg == '!help':
        return '`Help message.`'
    
    return 'Unknown command. use !help for list of commands.'