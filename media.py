import webbrowser

#Establish Movie class to import to entertainment_center.py, apply to specific film instances.

#Attributes of Movie class:
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer,
                 release_date, country, director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.release_date = release_date
        self.country = country
        self.director = director

#Function to open YouTube link from within my page:
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
 
