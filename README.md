# Andy's Recommended Films

This is source code to generate a simple personal website in Python from the command line (on Mac, `python entertainment_center.py`), without a server. The [functioning website](http://htmlpreview.github.io/?https://github.com/miller3000/movie_trailer_website/blob/master/fresh_tomatoes.html) is intended for my friends and I to review films we'd like to watch in the months to come. Features include poster images, directors, release years, countries of origin, and viewable trailers.

_Version and documentation authored October 2017_

## Contents

- [entertainment_center.py](../master/entertainment_center.py): Executes program, launches HTML in browser, stores movie data
- [media.py](../master/media.py): Module defining Movie class
- [fresh_tomatoes.py](../master/fresh_tomatoes.py): Provides styling and scripts for HTML

Upon running program, compiled .pyc files and .html file are generated, and are now part of this repo.

## Installation

To clone and run this application, you'll need Git and Python (2.7 or later) installed on your computer. From your command line:

```# Clone this repository
$ git clone https://github.com/miller3000/movie_trailer_website

# Go into the repository
$ cd movie_trailer_website

# Compile and run program
$ python entertainment_center.py
```

## For Users

After downloading, the current [HTML page](http://htmlpreview.github.io/?https://github.com/miller3000/movie_trailer_website/blob/master/fresh_tomatoes.html) should fully function as-is in Chrome and other current browsers.

To add more films, edit `entertainment_center.py` by following the comments listing film attributes. After revision, the HTML can be regenerated from the command line (on Mac, `python entertainment_center.py`).

## Improvements / Issues

YouTube links are never permanently reliable, and another video hosting or access option would be ideal, especially for international users. As of October 2017, "Scene at the Sea" trailer can only be viewed from youtube.com in the U.S., due to copyright issues. To move beyond YouTube hosting, or to embed other services (Mubi, Vimeo), fresh_tomatoes would need to be significantly revised.

Please submit bugs and feature requests to [@miller3000](https://github.com/miller3000/).

## To-do

- [ ] Test in all major browsers
- [ ] Improve styling in Bootstrap and CSS - e.g., row layout can be awkward on window resizing
- [ ] Modify movie_tiles in fresh_tomatoes to allow link functionality from text below poster images
- [ ] Design and insert copyright attribution for posters and trailers without adding clutter to design

_Next-level:_
- [ ] An "About" section to provide context for choice of films
- [ ] Film data should be moved to separate file or database, especially if film selection increases
- [ ] Broaden scope and functionality in media and entertainment_center, perhaps using APIs
- [ ] Add web interface for users to add films to site, or for sorting

## Credits

This code was developed from tutorials and starter code provided by Udacity. fresh_tomatoes.py was originally forked from https://github.com/udacity/ud036_StarterCode.

## License

Copyright 2017 Andrew Miller

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

