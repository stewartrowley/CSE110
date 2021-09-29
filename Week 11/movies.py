with open("movie_info.txt") as movie_file:
    for movie in movie_file:
        

        clean_movie = movie.strip()
        parts = clean_movie.strip()

        title = parts[0]


        print(title)
      