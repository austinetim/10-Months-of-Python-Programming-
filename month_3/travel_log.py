travel_log = [
    {
        "country": "France", 
        "cites_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 14
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]

# Function to add to the travel log list

# def add_new_country(country, total_visits, cities_visited):
#    travel_log.append({
#       "country": country,
#       "cities_visited": cities_visited,
#       "total_visits": total_visits
#    },)

# Another Method

def add_new_country(country, total_visits, cities_visited):
   # When working wiith dictionaries, always create an empty dictionary
   new_country = {}
   # Append new values to the empty dictionary
   new_country["country"] = country
   new_country["total_visits"] = total_visits
   new_country["cities_visited"] = cities_visited
   travel_log.append(new_country,)


add_new_country("Russia", 2, ["Moscow", "Saint PetersBurg"])

print(travel_log)