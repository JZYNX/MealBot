import random, requests
MAX_INGREDIENTS = 20

def handle_response(msg):
    p_msg = msg.lower()

    if p_msg == '?hello':
        return 'Hey there!'

    if p_msg == '?roll':
        return str(random.randint(1,6))

    if p_msg == '?help':
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
        elif p_msg == 'random' or p_msg == 'r':
            return ('```?random\n'
                    'Returns information on a random meal.```')
        elif p_msg == 'search' or p_msg == 's':
            return ('```?search\n'
                    'Requires additional parameter for query.\n'
                    'May require more vague queries for proper search.\n'
                    'Usage: ?search chicken```')
        elif p_msg == 'category' or p_msg == 'c':
            return ('```?category\n'
                    'Requires additional parameter for category type.\n'
                    'List of categories include:\n'
                    'Beef, Breakfast, Chicken, Dessert, Goat, Lamb, Miscellaneous, Pasta, '
                    'Pork, Seafood, Side, Starter, Vegan, Vegetarian.\n'
                    'Usage: ?category Beef```')
    return
    