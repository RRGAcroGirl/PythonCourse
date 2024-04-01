# Write a program that asks the user for a number of the trilogy (1, 2 or 3) and the number of the film
# in this trilogy (1, 2 or 3). Print the title of the film corresponding to the user selection.

star_wars_movies = [  
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],  
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],   
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy = int(input("Please enter a number (1, 2 or 3) of the Star Wars trilogy:"))
film = int(input("Please enter a number (1, 2 or 3) of film in this trilogy:"))

if trilogy < 1 or trilogy > 3 or film < 1 or film > 3:
   print("Sorry, your entry is invalid.")
   
else:
    print(star_wars_movies[trilogy - 1][film - 1])