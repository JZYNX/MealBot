from config import collection

async def get_favourites(message):
    # Get the user's favorites from the MongoDB collection
    user_favorites = collection.find_one({'user_id': message.author.id})
    if user_favorites:
        favorites = user_favorites['favs']
        if favorites:
            response = '\n'.join(favorites)
        else:
            response = "You don't have any favorites yet."
    else:
        response = "You don't have any favorites yet."

    # Send the response as a message
    await message.channel.send(response)

async def remove(message):
    # Get the meal that user wants to remove
    try:
        remove_meal = ''.join(f' {i}' for i in message.content.split()[1:])[1:]
    except (ValueError, IndexError):
        await message.channel.send("Please specify the name of the favorite to remove, e.g. '?remove pancakes'.")
        return

    # Get the user's favorites from the MongoDB collection
    user_favorites = collection.find_one({'user_id': message.author.id})
    if user_favorites:
        favorites = user_favorites['favs']
        if remove_meal.lower() in favorites:
            collection.update_one(
                {'user_id': message.author.id},
                {'$pull': {'favs': remove_meal}}
            )
            response = f"{remove_meal} has been removed from your favorites."
        else:
            response = f"Invalid remove. Your favorites list does not contain this meal."
    else:
        response = "You don't have any favorites yet."

    # Send the response as a message
    await message.channel.send(response)

