# Import the modules

import pandas as pd

FILEPATH = "riga_housing_11062023.csv"

# Read the DataFrame

def extract_data(filepath=FILEPATH):

    df = pd.read_csv(filepath)

    # Checking everything loaded correctly

    # Dropping duplicates
    df.drop_duplicates(inplace=True)
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df.dropna(subset=['longitude'], inplace=True)

    df = df.loc[df['longitude'] < 24.3]
    df = df.loc[df['longitude'] > 23.90]
    df = df.loc[df['latitude'] > 56.85]
    df = df.loc[df['latitude'] < 57.1]

    return df
