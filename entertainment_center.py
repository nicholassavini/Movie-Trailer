import fresh_tomatoes
import media
import omdb

pulp_fiction = media.Movie("Pulp Fiction",
                        "Some gangsters do some gangster shit, while a boxer runs away.",
                        "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                        "https://www.youtube.com/watch?v=wZBfmBvvotE")

midnight_in_paris = media.Movie("Midnight in Paris",
                        "A writer lives out his fantasy of experiencing the 1920s in Paris.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")

empire_strikes_back = media.Movie("Star Wars: The Empire Strikes Back",
                        "A young jedi tries to take down the Empire.",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=96v4XraJEPI")

aladdin = media.Movie("Aladdin",
                        "A young thief becomes a prince in order to win a princess' heart.",
                        "https://upload.wikimedia.org/wikipedia/en/5/58/Aladdinposter.jpg",
                        "https://www.youtube.com/watch?v=U8XtRQ5yOVE")

life_aquatic = media.Movie("The Life Aquatic with Steve Zissou",
                        "A marine on an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
                        "https://www.youtube.com/watch?v=yh401Rmkq0o")

clerks = media.Movie("Clerks",
                        "Follows the day of a convenience store clerk, who's not even supposed to be there today!",
                        "https://upload.wikimedia.org/wikipedia/en/6/65/Clerks_movie_poster%3B_Just_because_they_serve_you_---_.jpg",
                        "https://www.youtube.com/watch?v=Mlfn5n-E2WE")

#movies = [pulp_fiction, midnight_in_paris, empire_strikes_back, aladdin, life_aquatic, clerks]
movie_names = ["Pulp Fiction", "Midnight in Paris", "Star Wars: Episode V - The Empire Strikes Back", "Aladdin",
               "The Life Aquatic with Steve Zissou", "Clerks"]
movies = []
for name in range(0, 6):
    movie_info = omdb.get(title=movie_names[name])
    movie = media.Movie(movie_names[name], movie_info['plot'], movie_info['poster'],"blank")
    movies.append(movie)

fresh_tomatoes.open_movies_page(movies)



