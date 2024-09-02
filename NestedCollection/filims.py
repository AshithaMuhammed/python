movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


#Q1:total number of movies

# movies_count=len(movies)
# print(movies_count)

#Q2 movies with genre Drama

# genres_filter=[m.get("title") for m in movies if "Drama" in m.get("genres")]
# print(genres_filter)

#Q3: latest movie
# def get_year(mov):
#     return mov.get("year")
# latest_movie_data=max(movies,key=get_year)
# latest_movies=[m.get("title")for m in movies if m.get("year")==latest_movie_data.get("year")]
# print(latest_movies)

#Q4: top movie (movie with higest rating)
# def get_rating(mov):
#     return mov.get("rating")
# top_movies_data=max(movies,key=get_rating)
# top_rating_movies=[m.get("title")for m in movies if m.get("rating")==top_movies_data.get("rating")]
# print(top_rating_movies)

# Q5: movies with language malayalam
# malayalam_movies=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)

#Q6:movies released after year 2016
# movies_released=[m.get("title")for m in movies if m.get("year")>2016]
# print(movies_released)

#Q7: movie with lowest rating
# def get_rating(mov):
#     return mov.get("rating")
# lowest_rating_data=min(movies,key=get_rating)
# lowest_rating=[m.get("title") for m in movies if m.get("rating")==lowest_rating_data.get("rating")]
# print(lowest_rating)

#Q8:malyalam movies with genere action
# genres_filter=[m.get("title") for m in movies if "Action" in m.get("genres") and m.get("language")=="Malayalam"]
# print(genres_filter)

#Q9:movies released in same years

# genres_filter=[m.get("title") for m in movies if m.get("year")]
# print(genres_filter)

# def get_year(mov):            #ERROR
#     return mov.get("year")
# same_year_data=sorted(movies,key=get_year,reverse=True)
# same_year=[m.get("title") for m in movies if m.get("year")==same_year_data.get("year")]
# print(same_year)

#Q10:oldest movie                  #ERROR
def get_year(mov):           
    return mov.get("year")
movie_dictionary={}
for m in movies:
    release_year=m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))
    else:
        movie_dictionary[release_year]=[m.get("title")]
print(movie_dictionary)
oldest_movie_data=min(movies,key=get_year)
oldest_movie_names=[m.get("title") for m in movies if m.get("year")==oldest_movie_data.get("year")]
print("oldest_movie_names")

#number of movies released in each year
# years=[m.get("year") for m in movies]
# print(years)
# year_count={y:years.count(y) for y in years}
# print(year_count)


#list of genres:drama,action,comedy              ERROR
# def get_genres(mov):
#     return mov.get("genres")
# genres={g for m in movies for g in m.get("genres")}
# print{genres}

# # all genres
# all_genres=[g for m in movies for g in m.get("genres")]
# genres_count={g:all_genres.count(g) for g in all_genres}
# print(genres_count)


# #drama,action,comedy
# sorted_movies=sorted(movies,key)