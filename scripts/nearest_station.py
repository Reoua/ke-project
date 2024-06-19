import pandas as pd
from sklearn.neighbors import BallTree
from geopy.distance import great_circle

# Sample data (replace this with your actual DataFrame)
data = {
    'station_id': [1, 2, 3, 4],
    'latitude': [51.5074, 51.5099, 51.5114, 51.5139],
    'longitude': [-0.1278, -0.1282, -0.1297, -0.1302],
    'users': [0, 100, 0, 200]
}

# df = pd.DataFrame(data)

df = pd.read_csv("mun_stat_pop.csv")
# Split stations into two DataFrames based on users
stations_with_users = df[df['tot_pop'] > 0]
stations_without_users = df[df['tot_pop'] == 0]


# Function to calculate Haversine distance
def haversine_distance(coord1, coord2):
    return great_circle(coord1, coord2).kilometers


# Build a BallTree for stations with users
coords = stations_with_users[['geo_lat', 'geo_lng']].values
tree = BallTree(coords, leaf_size=15, metric='haversine')

# Find the closest station with users for each station without users
closest_users = []
for index, row in stations_without_users.iterrows():
    station_coord = row[['geo_lat', 'geo_lng']].values.reshape(1, -1)
    dist, ind = tree.query(station_coord, k=1)
    closest_station_index = ind[0][0]
    closest_station = stations_with_users.iloc[closest_station_index]
    closest_users.append({
        'station_id': row['id'],
        'closest_station_id': closest_station['id'],
        'distance': dist[0][0]
    })

# Convert result to DataFrame
closest_users_df = pd.DataFrame(closest_users)

closest_station_counts = closest_users_df['closest_station_id'].value_counts()

print("Count of stations being the closest to other stations:")
print(closest_station_counts)

if __name__ == "__main__":
    data = pd.read_csv("station_daily_capacity.csv")
    data = data[data["country"] == "NL"]
    data.to_csv("network_data/stations_node.csv", index=False)
