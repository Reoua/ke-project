import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/municipalities_v7.csv")
    data = data[data["year"] == 2018]
    columns_keep = ["municipality", "province", "population", "latitude", "longitude"]
    new_data = data[columns_keep]
    new_data.to_csv("network_data/municipalities_node.csv", index=False)
