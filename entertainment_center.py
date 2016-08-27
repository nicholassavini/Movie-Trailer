#!/usr/bin/env python
import fresh_tomatoes
import tmdbsimple
import media


tmdbsimple.API_KEY = "55cea4314826ba3b2d476431860d756f"


def get_movie_info(ids):
    for x in range(0, 6):
        movie = movie = tmdbsimple.Movies(movie_ids[x])
        movie_info = movie.info()
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
fresh_tomatoes.open_movies_page(movies)

