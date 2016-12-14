# First, import the webbrowser module.
import webbrowser
class Movie():
	"""This class is used to create the movie objects such as title, storyline, image_url, trailer of youtube"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_id):
		""""[This function represents as a constructor in Python]"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_id = trailer_youtube_id

		# The show_trailer function here calls the open method of the webbrowser module's function, and passes the
		# trailer link to it as an argument.
	def show_trailer(self):
		webbrower.open(self.trailer)
		