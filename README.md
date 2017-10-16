ud036_StarterCode - Online Bollywood movie trailers
This project provides a utility to create an online movie information like year in which the movie was released, the plot or the story line of the movie and enables the user to watch the trailer for the movie.

Getting Started

Clone this project in to local folder on your computer and run the 'entertainment_center.py' class which opens the movie listing webpage. The movies displayed on the webpage can be changed by modifying the movie objects in 'entertainment_center.py' file.

Prerequisites

Install python on your computer from https://www.python.org/downloads/
Download the latest version of Python based on the operating system, based on your computer, from the above link and install it.
Open and check if the IDLE - Python GUI is working properly.

Setting up and running the project

Download or clone the project from GitHub into any local folder of your choice.
Open the entertainment_center.py file from the Python IDLE.
Run this file to open the webpage which displays bollywood (Indian) movie listing.
Once the movie listing opens in the browser, list of movie tiles are displayed with the movie name, poster image and the year in which the movie is released.
Hovering on the movie tile, displays the plot of the movie.
Clicking on the poster image, plays the trailer of the movie.

To change the movies displayed in the webpage, new movie objects can be initialized in 'entertainment_center.py' as shown below:

paa = media.Movie("Paa", "2009", "A father tries to help his son cope with a rare condition that causes the young boy to age beyond his years.", "https://upload.wikimedia.org/wikipedia/en/1/17/Paaposter.jpg", "https://www.youtube.com/watch?v=mTjEWy4InQ4")
the arguments being, Movie name, Year in which the movie was released, plot or story line, Poster image url, youtube trailer url for the movie respectively.
And the newly initialized object should be added to the list 'movies'
'open_movies_page()' in 'fresh_tomatoes.py' is called to create the webpage with the movie listing.

Any new attribute to the movie can be added in the Movie class in the 'media.py' file.

To change the format, styling or layout of the webpage, 'fresh_tomatoes.py' can be modified.


Versioning

GitHub is used for versioning. 

Authors

Udacity - Initial work 
Contributors -
Mrinal Kanukolanu


Acknowledgments

The project is developed my modifying fresh_tomatoes.py provided by Udacity.
The plot and story line is taken from IMDB and wikipedia websites.
Poster images are taken from wikipedia.
Trailers are from YouTube
Google search engine was used for any other information about the movie