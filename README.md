# Movies
Site connected with the movie db 

The function get_data_movie_by_id(id) has an input the id of a movie and returns a dictionary with all the information about that movie. 

The function get_image_url(link, size="w500") has as first input the part of the link of the image which starts with a slash (/). The second input is the desired size of the image, which is set as default w500, so only if the size should be different we have to give a second input, i.e. about the size. This function returns the whole link of the image. 

The functiom search_movie(movie_name, page=1, adult=False) has as first input the name of a movie for which we want to get the information. The second input is the page we want to look at, which is set as default to be 1. The third input is whether the movie is allowed to be watched only by adults, which is set as default to be False, i.e. it is not strictly only for adults. This function replaces all poster paths with the whole link and returns a dictionary with all the information about the given movie. 

The function get_actor_url(id) has as input the id of an actor and returns the url link with the information about that actor. 

The function get_cast(movie_id) has as input the id of a movie, it gets the results from the corresponding link, replaces the profile path and the actor url with the corresponding whole link and returns the dictionary with all the information about that movie. 