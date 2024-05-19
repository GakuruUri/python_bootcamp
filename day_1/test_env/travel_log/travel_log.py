travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "dijon"]
    },

    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },

    {
        "country": "Russia",
        "visits": 5,
        "cities": ["Moscow", "Saint Petersburg"]
    }
]

def add_new_country(name, times_visited, cities_visited):
    """Adds a new country to the list of countries"""
    new_country = {}

    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)

    add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2] ['country']} {travel_log[2]['visits']} times")
























