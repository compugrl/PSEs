def get_highest_rated(restaurants):
    highest_rating = 0.0
    highest_rated = {}

    if len(restaurants) == 0:
        return None

    for i in range(len(restaurants)):
        for restaurant in restaurants:
            if restaurants[i]["rating"] > highest_rating:
                highest_rated = restaurants[i]
    
    return highest_rated



restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
# restaurants = [{"name": "Crow's Nest", "rating": 1}]
# restaurants = []

result = get_highest_rated(restaurants)
print(result)