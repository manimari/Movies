# Movies
Site connected with the movie db 

________________________

Instructions : 

You should download the files. 

You should complete the API_KEY and the SECRET_KEY at the .env file. 

At a terminal you should write python .\server.py 

In the browser you should hit http://localhost:5000 and search for movies. 

________________________

The function get_data_movie_by_id(id) has an input the id of a movie and returns a dictionary with all the information about that movie. 

________________________

The function get_image_url(link, size="w500") has as first input the part of the link of the image which starts with a slash (/). The second input is the desired size of the image, which is set as default w500, so only if the size should be different we have to give a second input, i.e. about the size. This function returns the whole link of the image. 

________________________

The functiom search_movie(movie_name, page=1, adult=False) has as first input the name of a movie for which we want to get the information. The second input is the page we want to look at, which is set as default to be 1. The third input is whether the movie is allowed to be watched only by adults, which is set as default to be False, i.e. it is not strictly only for adults. This function replaces all poster paths with the whole link and returns a dictionary with all the information about the given movie. 

________________________

The function get_actor_url(id) has as input the id of an actor and returns the url link with the information about that actor. 

________________________

The function get_cast(movie_id) has as input the id of a movie, it gets the results from the corresponding link, replaces the profile path and the actor url with the corresponding whole link and returns the dictionary with all the information about that movie. 


________________________

We have the register system, which is the endpoint http://localhost:5000/users/register with both methods POST and GET. 

If the method is POST : 

The email, password, name and last name is asked by the user. After the user has given these information, these data are given as input at the function insert_one_user. This function tries to insert the new user into the database. If everything works properly the function returns True. If something goes wrong the function returns False. 
If the function returns False then the output from the register template is generated. 
If the function returns True. i.e. the new user is added, then we are redirected to the login system.  

Is the method is GET : 

The output from the register template is generated. 


________________________

We have the login system, which is the endpoint http://localhost:5000/users/login with both methods POST and GET.  

If the method is POST : 

The email and the password is asked by the user. Using the function get_user_by_email, which has as input the database and the email, we check if the given email exists in the database. 
If the email exists in the database then the given password is checked, i.e. if the password given by the user is equal to the one that is in the database. If the password is not correct then the output of the login template is generated and a message that the password is wrong appears. 
If the password is correct then we are redirected to the endpoint http://localhost:5000/users/get_all . 
If the given email doesn't exist in the database then the output of the login template is generated and a message that the email is wrong appears. 

If the method is GET : 

If the given email exists then we are redirected to the endpoint http://localhost:5000/users/get_all else the output of the login template is generated. 


________________________

At the register template there is a link to get to the login system, if a user wants to be redirected there and also the other way around, at the login template there is a link to get to the register system, if a user wants to be redirected there. 


________________________ 

We have the logout system, which is the endpoint http://localhost:5000/users/logout . The user's email is removed from the session and we are redirected to the login system. 

________________________ 

We have the endpoint http://localhost:5000/movies/search . 

If we are logged in : 

If we give at the search box the name of a movie then this movie is searched by the function search_movie(search, page=1, adult=False) and it returns an array of the movie data with the given name. If the given name doesn't exist then the variable search is equal to None and the array is empty. In each case the output of the search_movies template is generated considering the movie_array. This html generates a card with the image of each movie of the given name, the title, the overview and a button to see more which redirect us to the endpoint http://localhost:5000/movies/<id> where id is the movie_id. This endpoint uses the function get_data_movie_by_id(id) to get an array with the data for the specific movie and the output of the movie template is generated considering the array with the data of the movie and the cast of that movie, which is the output of the function get_cast(id). 
The movie.html shows the image, the title, the overview and the cast of that movie. 

If we are not logged in, then we are redirected to the login system. 

________________________  

We have the endpoint http://localhost:5000/actors/<id> where id is the id of an actor. 

If we are logged in , this endpoint uses the function get_actor_url(id) to get the url of that actor and the function get_actor_data(actor_url) to get an array with the data for the specific actor and the output of the actor template is generated considering the array with the data of the actor. 
The actor.html shows the image, the name, the biography and the birthday of that actor. 

If we are not logged in, then we are redirected to the login system. 

________________________   


We have the endpoint http://localhost:5000/users/user .  

If we are logged in : 

The output of the user template is generated. We can see the information of the user, i.e. the name, the last name and the email address. There are also two options, to change the password and to delete the account. Clicking on the corresponding option we are redirected to the respective endpoint (http://localhost:5000/users/change_password/ or http://localhost:5000/users/delete_account/). 
At the option to change the password the user should input the old password and twice the new password. After checking if the old password is correct and if the new password is the same at both inputs then the password is changed and this is done by the model change_password_by_email. In each case the output of the change_password template is generated. 
At the option to delete the account the user should verify that the account should be deleted. This is done by the model delete_account_by_email. The output of the delete_account template is generated. The user's email is removed from the session and we are redirected to the register system. 


If we are not logged in, then we are redirected to the login system. 
________________________   

The image that we have that at the base_page is from taken from Google and especially from https://www.google.com/search?q=movies+logo&tbm=isch&ved=2ahUKEwiIlfXvy_r4AhXM5KQKHexFC88Q2-cCegQIABAA&oq=movies+logo&gs_lcp=CgNpbWcQAzIFCAAQgAQyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB46BggAEB4QCFAAWNsLYIsNaAJwAHgAgAHbAogBzgqSAQcwLjMuMC4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=7zTRYsjhJczJkwXsi634DA#imgrc=ojHPSuirZLfgZM . 