import random

def handle_response(msg):
    p_msg = msg.lower()

    if p_msg == 'hello':
        return 'Hey there!'

    if p_msg == 'roll':
        return str(random.randint(1,6))
    
    if p_msg == 'help':
        return ("```> Hi There!\n"
                "I'm a discord bot that will provide you with all the "
                "culinary knowledge you need to be a michelin chef!\n"
                "Do ?help <command> for extend information on a command.\n"
                "Basic functions\n"
                "?hello, ?roll```")

    if p_msg.startswith('?help '):
        p_msg = p_msg[6:]
        if p_msg == 'hello':
            return '```?hello\nBot will say greet you back :)```'
        elif p_msg == 'roll':
             return '```?roll\nBot will return a number between 1 and 6.```'