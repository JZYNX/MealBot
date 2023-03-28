import requests, discord, responses

def display_meal(data):
    meal_name = data['strMeal']
    meal_image = data['strMealThumb']
    meal_instructions = data['strInstructions']
    ingredients = []

    # loop through ingredients
    for i in range(1, 21):
        ingredient = data.get(f'strIngredient{i}')
        measure = data.get(f'strMeasure{i}')

        if ingredient and measure:
            ingredients.append(f'{ingredient} - {measure}')

    if len(meal_instructions) > 1024:
        # split instructions into chunks (discord max of 1024 in field)
        chunks = [meal_instructions[i:i+1024] for i in range(0, len(meal_instructions), 1024)]

    # format returned msg
    embed = discord.Embed(title=meal_name)
    embed.set_image(url=meal_image)
    embed.add_field(name="Ingredients", value = '\n'.join(ingredients), inline=False)
    if len(meal_instructions) > 1024:
        # add chunks as separate fields
        for i, chunk in enumerate(chunks):
            embed.add_field(name=f'Instructions (Part {i + 1})', value=chunk, inline=False)
    else:
        embed.add_field(name=f'Instructions', value=meal_instructions, inline=False)
    
    return embed

async def random_meal(msg):
    '''
    returns random meal 
    '''
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()['meals'][0]
    embed = display_meal(data)
    # send message to channel
    await msg.channel.send(embed = embed)
    
async def search_meal(msg):
    query = ''.join(f' {i}' for i in msg.content.split()[1:])[1:]
    if not query:
        response = responses.handle_response('?help s')
        await msg.channel.send(response)
        return None
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}')
    data = response.json()['meals']
    if not data:
        await msg.channel.send("Could not find any meals. Try searching for something else.")
        return None
    
    # get first meal from search results
    meal = data[0]
    embed = display_meal(meal)
    await msg.channel.send(embed = embed)

async def get_meals_by_category(msg):
    if len(msg.content.split()) <= 1:
        response = responses.handle_response('?help c')
        await msg.channel.send(response)
        return None
    category = msg.content.split()[1]   
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}')
    data = response.json()['meals']

    if not data:
        await msg.channel.send("Could not find this category. ?help c for list of categories.")
        return None
    
    # display names of meals for category
    await msg.channel.send(f"```{[meal['strMeal'] for meal in data]}```")