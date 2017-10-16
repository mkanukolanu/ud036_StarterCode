import webbrowser

"""This class provides a way to store movie related information like year
    in which the movie was released and the story line of the movie.
    Author: MKanukolanu
    Date Created: 10/13/2017
    Date Updated: 10/13/2017
    Version: 1.0"""


class Movie():

    """__init__ method is used to initialize an instance of a movie.
        Parameters: movie_title : name of the movie
                    movie_year : year in which the movie was released
                    movie_storyline: plot of the movie
                    poster_image: the url from which the poster image
                                  for the movie can be loaded
                    trailer_youtube :the youtube url which plays the
                                     movie trailer"""

    def __init__(
                self, movie_title, movie_year,
                movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """show_trailer method is used to get the youtube url
        and play it in the browser"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
