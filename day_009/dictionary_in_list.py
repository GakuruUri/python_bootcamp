country = input("Add country name.")
visits = int(input("Visits"))
list_of_cities = eval(input("List of cities"))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    
    {
        "country": "Russia",
        "visits": 2,
        "cities": ["Moscow", "Saint Petersburg"]
    }
]


def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    
    travel_log.append(new_country)
    
    
    add_new_country(country, visits, list_of_cities)
    
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")