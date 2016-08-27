#!/usr/bin/env python2
import fresh_tomatoes
import tmdbsimple
import media


# After creating an account at themoviedatabase.org, you can add your API
# Key below
tmdbsimple.API_KEY = ""


def get_movie_info(ids):
    """ Takes the ids of each movie and fetches data from
    themoviedatabase.org
    """
    for x in range(0, 6):
        movie = movie = tmdbsimple.Movies(movie_ids[x])
        # Provides basic movie data
        movie_info = movie.info()
        # Provides the movie trailer
        movie_videos = movie.videos()
        create_movie = media.Movie(movie.title,
                                    "https://image.tmdb.org/t/p/w300_and_h450_bestv2/" +  # NOQA
                                   movie_info['poster_path'],
                                    "https://youtu.be/" +
                                   movie_videos['results'][0]['key'])
        movies.append(create_movie)


# Movie ids refer to the ids found for each movie on themoviedatabase.org
movie_ids = [680, 59436, 1891, 812, 421, 2292]
movies = []

get_movie_info(movie_ids)
# Uses the list of Movie instances to generate an HTML file that shows trailers
fresh_tomatoes.open_movies_page(movies)
