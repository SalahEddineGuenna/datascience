# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd

# Importing our datasets we need to work with
locations = pd.read_csv('datasets/locations.csv')
movies = pd.read_csv('datasets/imdb_movies.csv')

movies = movies[movies['avg_vote'] > 6]

# Printing few lines to get idea about our dataframes
movies_locations = pd.merge(movies, locations, left_on='title', right_on='Title')

movies_locations['worldwide_gross_income'] = movies_locations['worldwide_gross_income'].fillna(0)
movies_locations['Locations'] = movies_locations['Locations'].fillna('null')
movies_locations['worldwide_gross_income'] = movies_locations['worldwide_gross_income'].str.strip('$')
movies_locations['worldwide_gross_income'] = movies_locations['worldwide_gross_income'].astype(float)

san_fran_movies = movies_locations[movies_locations['Locations'].str.contains('San Francisco')].sort_values(
                'worldwide_gross_income', ascending=False)

san_fran_movies.drop_duplicates()

sf_hits = san_fran_movies[['Locations', 'title', 'year']][:10]
sf_hits.set_index('Locations', drop=True, inplace=True)
print(sf_hits)

