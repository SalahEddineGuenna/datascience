# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd

# Importing our datasets we need to work with
locations = pd.read_csv('datasets/locations.csv')
movies = pd.read_csv('datasets/imdb_movies.csv')
sf = pd.read_csv('datasets/Film_Locations_in_San_Francisco.csv')

movies = movies[movies['avg_vote'] > 6]

movies_locations = movies.merge(locations, left_on='title', right_on='Title', how='inner')

print("dataframe columns typs:")
print(movies_locations.dtypes)
print('==================')
print('number of na values in the dataframe : ')

print(movies_locations.isna().sum())

# dropping na value from the dataframe
movies_locations = movies_locations.dropna()
sf = sf.dropna()

print('***************************************************************')
print('number of na values in the dataframe after: ')

print(movies_locations.isna().sum())
print('***************************************************************')
print(movies_locations[['Title', 'Locations', 'worldwide_gross_income']].head())

movies_locations['worldwide_gross_income'] = movies_locations['worldwide_gross_income'].str.strip('$ ').astype(int)
movies_locations = movies_locations.sort_values(by='worldwide_gross_income', ascending=False)
print('***************************************************************')
print(movies_locations[['Title', 'Locations', 'worldwide_gross_income']].head())

# movies_locations = movies_locations[movies_locations['Locations'] == sf['Locations']]

print('***************************************************************')
print(sf.dtypes)

print(sf[sf['Locations'] == movies_locations['Locations']].head())
