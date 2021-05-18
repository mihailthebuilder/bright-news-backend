# Bright News
Web app that analyses the positivity of a news site. Made with a React frontend and a Django backend. Link to live site: https://mihailthebuilder.github.io/bright-news-web-frontend/

**Note**: The front-end sits on a different repo, see [this](#architecture) for more. The scoring algorithm hasn't been designed (or tested) for sites that either aren't in English, or aren't focused on providing news content.

# Table of contents
- [Bright News](#bright-news)
- [Table of contents](#table-of-contents)
- [Front-end](#front-end)
  - [Architecture](#architecture)
  - [Pages](#pages)
    - [Landing](#landing)
    - [Results](#results)
  - [Other](#other)
- [Back-end](#back-end)

# Front-end

## Architecture

The front-end is a React SPA that sits on a [different repo](https://github.com/mihailthebuilder/bright-news-web-frontend) and is hosted with GitHub Pages. 

I decided to keep it separate from the back-end because I felt it would create unnecessary complexity. Django pushes a server-side rendering approach, with HTML components delivered independently one of the other. This is more ideal for sites that deliver a lot of content.

However, the client-side is very light on content that's not generated by the scoring algorithm. I also have completely different sections in the HTML interacting with each other.

## Pages

The SPA is made up of 3 "pages": [Landing](#landing), [Results](#results) and [About](#about). The same URL is being used across all 3; the state and DOM event interactions decide which page is actually shown. 

I did consider using [React Router](https://reactrouter.com/) in order to have the URL appropriate reflect the page. The downside was that I would've had to build rules for when someone directly accesses the Results page URL.

### Landing


### Results

## Other

# Back-end