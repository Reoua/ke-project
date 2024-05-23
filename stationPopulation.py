import pandas as pd
from geopy.distance import geodesic


# Function to find the closest station for each city and populate the station_city_map
def find_and_map_closest_station(city, stations, station_city_map):
    city_coords = (city['lat'], city['lng'])
    min_distance = float('inf')
    closest_station = None

    for _, station in stations.iterrows():
        station_coords = (station['geo_lat'], station['geo_lng'])
        distance = geodesic(city_coords, station_coords).kilometers
        if distance < min_distance:
            min_distance = distance
            closest_station = station['name_long']
    # Add the city to the closest station's list
    station_city_map[closest_station].append(city['city'])

# Function to calculate the sum of populations for a list of cities
def calculate_population_sum(cities, city_population_map):
    return sum(city_population_map.get(city, 0) for city in cities)


if __name__ == "__main__":
    stations = pd.read_csv("stations-2020-01.csv")
    cities = pd.read_csv("nl.csv")
    del stations['name_short']
    del stations['name_medium']
    # Only consider stations in the Netherlands
    stations = stations[stations['country'] == "NL"]

    # Map cities to closest station

    # Initialize a dictionary to hold lists of cities for each station
    station_city_map = {station: [] for station in stations['name_long']}
    # Apply the function to each city
    cities.apply(find_and_map_closest_station, stations=stations, station_city_map=station_city_map, axis=1)
    print(station_city_map)
    # Map the list of cities to the corresponding stations in the stations_df
    stations['Cities'] = stations['name_long'].map(station_city_map)

    # Use cities to get population per station

    # Create a dictionary for quick lookup of city populations
    city_population_map = cities.set_index('city')['population_proper'].to_dict()

    # Apply the function to the 'Cities' column in the stations DataFrame
    stations['Total_Population'] = stations['Cities'].apply(calculate_population_sum, city_population_map=city_population_map)

    # Sort stations by 'Total_Population' in descending order
    sorted_stations = stations.sort_values(by='Total_Population', ascending=False)

