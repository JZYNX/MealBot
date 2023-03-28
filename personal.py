from config import personal_collection
import discord

def display_meal(data):
    meal_name = data['name']
    meal_image = data['photo_url']
    meal_instructions = data['instructions']
    ingredients = data['ingredients']

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

async def create_meal(message, bot):
    # Send a message asking the user to enter the name of the recipe
    await message.channel.send("Please enter the name of your recipe.")
    # Wait for the user's response
    name_message = await bot.wait_for('message', check=lambda m: m.author == message.author)
    # Send a message asking the user to enter the ingredients
    await message.channel.send("Please enter the ingredients for your recipe, separated by commas.")   
    # Wait for the user's response
    ingredients_message = await bot.wait_for('message', check=lambda m: m.author == message.author)
    # Split the ingredients string into a list
    ingredients = ingredients_message.content.split(',')
    # Send a message asking the user to enter the instructions for the recipe
    await message.channel.send("Please enter the instructions for your recipe.")
    # Wait for the user's response
    instructions_message = await bot.wait_for('message', check=lambda m: m.author == message.author)
    # Send a message asking the user to upload a photo of the recipe
    await message.channel.send("Please upload a photo of your recipe.")
    # Wait for the user's response
    photo_message = await bot.wait_for('message', check=lambda m: m.author == message.author and m.attachments)
    # Get the URL of the photo
    photo_url = photo_message.attachments[0].url
    # Create a new recipe document in the MongoDB collection
    recipe = {
        'name': name_message.content,
        'ingredients': ingredients,
        'instructions': instructions_message.content,
        'photo_url': photo_url,
        'user_id': message.author.id
    }
    personal_collection.insert_one(recipe)
    
    # Send a message confirming that the recipe has been created
    await message.channel.send("Your recipe has been created!")

async def get_personal_meals(message):
    user_id = message.author.id
    recipe_list = []
    recipes = personal_collection.find({'user_id': user_id})
    if recipes:
        # display names of meals for category
        for recipe in recipes:
            recipe_list.append(f"{recipe['name']}: {recipe['ingredients']}")
        recipe_str = '\n'.join(recipe_list)
        await message.channel.send(f"Here are your recipes:\n{recipe_str}")
    else:
        await message.channel.send("Could not find any personal meals.")
        return 

async def get_personal_meal(message):
    pass    
