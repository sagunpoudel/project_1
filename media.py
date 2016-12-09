# First, import the webbrowser module.
import webbrowser
class Movie():
	"""This class is used to create the movie objects such as title, storyline, image_url, trailer of youtube"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer = trailer_youtube

# The show_trailer function here calls the open method of the webbrowser module's function, and passes the
# trailer link to it as an argument.
	def show_trailer(self):
		webbrower.open(self.trailer)