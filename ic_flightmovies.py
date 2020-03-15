def can_two_movies_fill_flight_novice(movie_lengths, flight_length):
    if len(movie_lengths) == 0: return False

    for idx in range(len(movie_lengths)):
        el = movie_lengths[idx]
        print("index[" + str(idx) + "] = " + str(el))
        for r_idx in range(len(movie_lengths[idx + 1:])):
            r_el = movie_lengths[r_idx]
            if (el + r_el) == flight_length:
                return True

    return False



def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_list_length = len(movie_lengths)
    if movie_list_length == 0: return False

    #movies = {el for el in movie_lengths}
    movies = dict()
    for i,val in enumerate(movie_lengths):
        if (val in movies): movies[val] +=1
        else: movies[val] = 1
    print(movies)

    idx = 0

    for key in movie_lengths:  # Use a list instead of a view
        first_movie = key
        first_movie_value = movies[key]
        if (first_movie_value > 1):
            movies[key] = first_movie_value - 1
        else:
            # de duplicate
            del movies[key]

        second_movie = flight_length - first_movie
        print("first movie = " + str(first_movie) + ", second movie = " + str(second_movie))
        if (second_movie in movies):
            return True
    return False






movie_lengths = [1, 3, 5, 11, 8, 11, 4, 6, 4]
flight_length = 10
print(can_two_movies_fill_flight(movie_lengths, flight_length))


#print(can_two_movies_fill_flight_novice([4, 3, 2], 5))
#print(can_two_movies_fill_flight_novice([3, 8], 6))
# for key in list(movies.keys()):  # Use a list instead of a view
