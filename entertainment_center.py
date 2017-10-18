import media
import fresh_tomatoes

"""Assigns arguments to seven Movie class variables from media.py.
Collects films in a list to pass into fresh_tomatoes.open_movies_page,
which generates HTML and opens web browser.

Code from movie_trailer_website, which can be executed from
entertainment_center.py.

Films added to file intermittently to fit project purpose of listing
"Andy's recommended films".  

Args (from media.py):
    title
    storyline
    poster_image_url
    youtube_trailer_url
    release_date
    country
    director
"""

mulholland_drive = media.Movie("Mulholland Drive",
                               "An actress comes to Hollywood and finds a " +
                                   "world of nightmares.",
                               "https://upload.wikimedia.org/wikipedia/en/0/" +
                                   "0f/Mulholland.png",
                               "https://www.youtube.com/watch?v=jbZJ487oJlY",
                               "2001",
                               "U.S.",
                               "David Lynch")

celine_and_julie = media.Movie("Celine and Julie Go Boating",
                               "Two friends in Paris try to change the " +
                                   "world around them.",
                               "https://upload.wikimedia.org/wikipedia/en/3" +
                                   "/34/Celine_and_Julie_Go_Boating_poster.jpg",
                               "https://www.youtube.com/watch?v=dCGmSYjp7fE",
                               "1974",
                               "France",
                               "Jacques Rivette")

tokyo_story = media.Movie("Tokyo Story",
                          "An aging couple visits their grown children in a " +
                              "time of change.",
                          "https://upload.wikimedia.org/wikipedia/en/5/5f/" +
                              "Tokyo_Story_poster.jpg",
                          "https://www.youtube.com/watch?v=J_LXe4PIKtQ",
                          "1953",
                          "Japan",
                          "Yasujiro Ozu")

scene_sea = media.Movie("Scene at the Sea",
                        "A man in a young deaf couple finds fulfillment in " +
                            "surfing.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8c/" +
                            "Kitanoz3rd.jpg",
                        "https://www.youtube.com/watch?v=6FKiIqunBHc",
                        "1991",
                        "Japan",
                        "Takeshi Kitano")

woman_dunes = media.Movie("Woman in the Dunes",
                          "Two strangers are trapped in a sand pit in a " +
                              "mysterious village.",
                          "https://upload.wikimedia.org/wikipedia/en/1/11/" +
                              "Woman_in_the_Dunes_poster.jpg",
                          "https://www.youtube.com/watch?v=Gtv9p6cAWAA",
                          "1964",
                          "Japan",
                          "Hiroshi Teshigahara")

tokyo_olympiad = media.Movie("Tokyo Olympiad",
                             "Documentary on life at the 1964 Summer " +
                                 "Olympics in Tokyo.",
                             "https://upload.wikimedia.org/wikipedia/en/0/" +
                                 "03/Tokyoolympiadposter.jpg",
                             "https://youtu.be/GBfBzDRxRlI",
                             "1965",
                             "Japan",
                             "Kon Ichikawa")

ikiru = media.Movie("Ikiru",
                    "A dying man searches for meaning in his life.",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/" +
                        "3/3a/Ikiru_poster.jpg/800px-Ikiru_poster.jpg",
                    "https://www.youtube.com/watch?v=Lc4y-asVh3c",
                    "1952",
                    "Japan",
                    "Akira Kurosawa")

tetsuo = media.Movie("Tetsuo: The Iron Man",
                     "A salaryman transforms into a monster made of scrap " +
                         "metal.",
                     "https://upload.wikimedia.org/wikipedia/en/6/6e/" +
                         "Tetsuoposter.jpg",
                     "https://www.youtube.com/watch?v=usXZPAw3ycA",
                     "1989",
                     "Japan",
                     "Shinya Tsukamoto")

blood_lake = media.Movie("Blood Lake",
                         "Teenagers on vacation at the lake encounter a " +
                             "murderer.",
                         "https://images-na.ssl-images-amazon.com/images/M/" +
                             "MV5BMTMwOTU5MTYyOV5BMl5BanBnXkFtZTcwNTEzNTMyMQ" +
                             "@@._V1_.jpg",
                         "https://youtu.be/9sl-dR1Sbrs",
                         "1987",
                         "U.S.",
                         "Tim Boggs")
                   
movies = [mulholland_drive, celine_and_julie, tokyo_story, scene_sea,
          woman_dunes, tokyo_olympiad, ikiru, tetsuo, blood_lake]

#Method takes list movies as arg, and outputs HTML
#(fresh_tomatoes.html) to open in browser."""
fresh_tomatoes.open_movies_page(movies)


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

