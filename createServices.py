import pandas as pd
from geopy.distance import geodesic


def find_and_map_closest_municipality(station, municipalities, station_mun_map):
    station_coords = (station['geo_lat'], station['geo_lng'])
    min_distance = float('inf')
    closest_municipality = None

    for _, municipality in municipalities.iterrows():
        mun_coords = (municipality['latitude'], municipality['longitude'])
        distance = geodesic(station_coords, mun_coords).kilometers
        if distance < min_distance:
            min_distance = distance
            closest_municipality = municipality['municipality']

    # Add the closest municipality to the station_mun_map
    station_mun_map.append((station['code'], closest_municipality))


# Function to calculate the sum of populations for a list of cities
def calculate_population_sum(cities, city_population_map):
    return sum(city_population_map.get(city, 0) for city in cities)


def create_station_municipality_csv():
    stations = pd.read_csv("data/stations-2020-01.csv")
    municipalities = pd.read_csv("data/municipalities_v7.csv")

    # Only consider stations in the Netherlands
    stations = stations[stations['country'] == "NL"]
    municipalities = municipalities[municipalities["year"] == 2018]

    # Initialize a list to hold tuples of (station, closest_municipality)
    station_mun_map = []

    # Apply the function to each station
    stations.apply(find_and_map_closest_municipality, municipalities=municipalities, station_mun_map=station_mun_map,
                   axis=1)

    # Create a DataFrame from the station_mun_map
    station_mun_df = pd.DataFrame(station_mun_map, columns=['station', 'municipality'])
    station_mun_df["type"] = "services"

    # Save the DataFrame to a CSV file
    station_mun_df.to_csv("network_data/services_rel.csv", index=False)


if __name__ == "__main__":
    create_station_municipality_csv()
