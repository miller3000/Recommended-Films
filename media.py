import webbrowser

"""Movie class sets instance variables for films in
entertainment_center.py.
From movie_trailer_website, which can be executed from
entertainment_center.py.

Args: All are strings. Self-explanatory names.
    movie_title: If foreign, use common English-language translation.
    movie_storyline: One descriptive sentence with period, generated
        by author.
    poster_image: URL accessing wikimedia images.
    trailer: URL accessing YouTube; in cases where trailer was not on
        YouTube, author uploaded media to YT.
    release_date: year only, taken from Wikipedia or IMDB.
    country: "U.S." is abbreviated. Taken from Wikipedia.
    director: First name last name. Use common U.S. spelling of foreign
        names.

Function: Opens YouTube link from within Python-generated HTML.
"""


class Movie():
"""Collects data for specific films to display on website. Method
displays video from trailer URL in film instances.

Attributes match args, in order, as listed in comments above.
"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer,
                 release_date, country, director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.release_date = release_date
        self.country = country
        self.director = director

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


"""Copyright 2017 Andrew Miller

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

 
