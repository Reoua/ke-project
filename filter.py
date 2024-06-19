import pandas as pd


def rename_column_in_csv(file_path, old_column_name, new_column_name):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Rename the specified column
    df.rename(columns={old_column_name: new_column_name}, inplace=True)

    # Save the DataFrame back to the same CSV file, replacing the original file
    df.to_csv(file_path, index=False)


# Example usage
file_path = 'network_data/stations_node.csv'
old_column_name = 'geo_lng'
new_column_name = 'longitude'

rename_column_in_csv(file_path, old_column_name, new_column_name)
