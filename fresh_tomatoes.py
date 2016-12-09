import webbrowser
import os
import re
import csv

# Creating a template folder for HTML tags to make the script more readable.
# For this we use _*.html partial file inside the template folder that are executed from the read_template class of csv module
def read_template(template):
    """ returns html string from `templates/_<template>.html` """
    return ''.join([row for row in open('templates/_{}.html'.format(template),
                                        'r').readlines()])

# styles and scripting for the page
main_page_head = read_template('header')

# the main page layout and title bar
main_page_content = read_template('content')

# a single movie entry html template
movie_tile_content = read_template('movie_section')


# Styles and scripting for the page

# The main page layout and title bar


# A single movie entry html template

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_tile_content=movie.storyline,
            trailer_youtube_id=movie.trailer
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
  