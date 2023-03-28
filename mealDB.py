import requests, discord

async def random_meal(msg):
    '''
    returns random meal 
    '''
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()['meals'][0]
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

    # send message to channel
    await msg.channel.send(embed = embed)

async def search_meal(msg):
    await print(msg.content.split())