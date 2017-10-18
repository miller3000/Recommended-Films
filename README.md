# Andy's Recommended Films

This is source code for a simple personal website, generated in Python. The site is intended for my friends and I to review films we'd like to watch in the months to come. It contains basic info about the films and links to trailers.

There are no special instructions to install, beyond forking and cloning this GitHub repository.

This code was developed from tutorials and existing code provided by Udacity.

## For Users

The [HTML page](../fresh_tomatoes.html) should fully function in Chrome and other current browsers, with no additional dependencies. Without the given HTML, the program can be launched from the command line using entertainment_center.py (on Mac, `python entertainment_center.py`), which will generate the [HTML](../fresh_tomatoes.html) in this repository and open it in your browser.

## For Contributors

[fresh_tomatoes.py](../fresh_tomatoes.py) generates the HTML using webbrowser, os, and re modules. To call fresh_tomatoes and open the web browser, run [entertainment_center.py](../entertainment_center.py) from your command line or IDE. [media.py](../media.py) defines the Movie class, and entertainment_center.py includes all film data. These files could be expanded for greater scope, data, and functionality at a later date.

## Improvements / Issues

YouTube links are never permanently reliable, and another video hosting or access option would be ideal.
As of October 2016, "Scene at the Sea" trailer can only be viewed from YouTube due to copyright issues. To move beyond YouTube hosting, or to embed other services (Mubi, Vimeo), fresh_tomatoes would need to be significantly revised.

## To-do

- [ ] Test in all major browsers
- [ ] Improve styling in Bootstrap and CSS - e.g., row layout can be awkward on window resizing
- [ ] Modify movie_tiles in fresh_tomatoes to allow link functionality from text below poster images
- [ ] Design and insert copyright attribution for posters and trailers without adding clutter to design

_Next-level:_
- [ ] An "About" section to provide context for choice of films
- [ ] Film data should be moved to separate database or file, especially if film set increases
- [ ] Add user input to add films to site, or sort, from web interface

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

