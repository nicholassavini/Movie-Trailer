# Fresh Tomatoes

## Introduction

Fresh Tomatoes is a program written in Python 2.7 that displays the Title, Movie Poster, and Movie Trailer for any 6 movies that you choose (currently set to my favorite 6 movies). 

## Installation

Fresh Tomates uses the tmdbsimple 1.4.0 library in order to get information for each movie. It can be installed with pip by running the following command:
```sh
pip install tmdbsimple
```
It can also be installed by downloading .tar.gz file from [PyPi](https://pypi.python.org/pypi/tmdbsimple), or the source can be downloaded on [GitHub](https://github.com/celiao/tmdbsimple).

After tmdbsimple is installed, the entertainment_center.py file can be ran, and the index.html page will be generated.

## Adding Your Own Movies

The selected movies are stored in the "movie_ids" list in the "entertainment_center.py" file, and can be modified to show your own favorite movies. The ids in that list correspond to those movies' ids on [themoviedatabase.org](http://themoviedatabase.org).