"""
City hopper express!
"""




city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}


#dest_cities = input('Where would you like to begin? ')


def road_trip(city):
    hop_city = city_to_accessible_cities[city]
    dest_cities = city_to_accessible_cities
    for city_hop in city_to_accessible_cities:
        if city_hop in hop_city:
            print(city_to_accessible_cities)
        elif city_hop == city:
            continue
        elif city_hop not in dest_cities:
            continue
        else:
            print('INVALID')
    return dest_cities

dest_cities = input("What city are you in: ")
start_city = city_to_accessible_cities[dest_cities]
print(start_city)
for city in start_city:
    print(city_to_accessible_cities[city])

