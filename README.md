# Movies
Site connected with the movie db 

The function get_data_movie_by_id(id) has an input the id of a movie and returns a dictionary with all the information about that movie. 

The function get_image_url(link, size="w500") has as first input the part of the link of the image which starts with a slash (/). The second input is the desired size of the image, which is set as default w500, so only if the size should be different we have to give a second input, i.e. about the size. This function returns the whole link of the image. 

The functiom search_movie(movie_name, page=1, adult=False) has as first input the name of a movie for which we want to get the information. The second input is the page we want to look at, which is set as default to be 1. The third input is whether the movie is allowed to be watched only by adults, which is set as default to be False, i.e. it is not strictly only for adults. This function replaces all poster paths with the whole link and returns a dictionary with all the information about the given movie. 

The function get_actor_url(id) has as input the id of an actor and returns the url link with the information about that actor. 

The function get_cast(movie_id) has as input the id of a movie, it gets the results from the corresponding link, replaces the profile path and the actor url with the corresponding whole link and returns the dictionary with all the information about that movie. 


We have the register system, which is the endpoint http://localhost:5000/users/register with both methods POST and GET. 

If the method is POST : 

The email, password, name and last name is asked by the user. After the user has given these information, these data are given as input at the function insert_one_user. This function tries to insert the new user into the database. If everything works properly the function returns True. If something goes wrong the function returns False. 
If the function returns False then the output from the register template is generated. 
If the function returns True. i.e. the new user is added, then we are redirected to the login system.  

Is the method is GET : 

The output from the register template is generated. 


We have the login system, which is the endpoint http://localhost:5000/users/login with both methods POST and GET.  

If the method is POST : 

The email and the password is asked by the user. Using the function get_user_by_email, which has as input the database and the email, we check if the given email exists in the database. 
If the email exists in the database then the given password is checked, i.e. if the password given by the user is equal to the one that is in the database. If the password is not correct then the output of the login template is generated and a message that the password is wrong appears. 
If the password is correct then we are redirected to the endpoint http://localhost:5000/users/get_all . 
If the given email doesn't exist in the database then the output of the login template is generated and a message that the email is wrong appears. 

If the method is GET : 

If the given email exists then we are redirected to the endpoint http://localhost:5000/users/get_all else the output of the login template is generated. 


At the register template there is a link to get to the login system, if a user wants to be redirected there and also the other way around, at the login template there is a link to get to the register system, if a user wants to be redirected there. 