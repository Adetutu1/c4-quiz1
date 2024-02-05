import pandas as pd

file = pd.read_csv("/home/user/CSS_2024/Project/assignment/movie_dataset.csv")

print(file)

file.dropna(inplace=True)

# question 1

highest_rated_movie = file.loc[file['Rating'].idxmax()]
print(highest_rated_movie)

# question 2
print(file.describe())

average_revenue = file['Revenue (Millions)'].mean()
print(average_revenue)

# question 3
data_2015_2017 = file[(file['Year']>=2015) & (file['Year'] <=2017)]
print(data_2015_2017)

average_revenue_2015_2017 = data_2015_2017['Revenue (Millions)'].mean()
print(average_revenue_2015_2017)

print(data_2015_2017.describe())

# question 4, number of movie released 2016

source_file = pd.read_csv("/home/user/CSS_2024/Project/assignment/movie_dataset.csv")

number_movie_2016 = (source_file['Year']==2016).sum()
print(number_movie_2016)

# question 5
number_movies_chris_nolan = (source_file['Director']=="Christopher Nolan").sum()
print(number_movies_chris_nolan)

# question 6

number_movies_ratings_8 = (source_file['Rating']>=8.0).sum()
print(number_movies_ratings_8)

# question 7
median_chris_nolan_rating = source_file[source_file['Director']=='Christopher Nolan']['Rating'].median()
print(median_chris_nolan_rating)

# question 8
movies_by_year = source_file.groupby("Year")
average_rating_by_year = movies_by_year['Rating'].mean()

year_with_highest_rating = average_rating_by_year.idxmax()
print(year_with_highest_rating)

# question 9
movies_2006 = (source_file['Year']==2006).sum()
movies_2016 = (source_file['Year']==2016).sum()

diff_2006_2016_movies = movies_2016 - movies_2006
percentage_increase = diff_2006_2016_movies*100/movies_2006
print(percentage_increase)

# question 10
actors = source_file['Actors'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).to_frame('Actor')
common_actor = actors['Actor'].mode()
print(common_actor)

# question 11
unique_genre = source_file['Genre'].str.split(',').explode().str.strip()
unique_genre_number = unique_genre.nunique()
print(unique_genre_number)
