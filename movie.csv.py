import csv   #imports the csv module 
movie_data = [          #list of all movies recommendations, genre, and rating  
    ["title", "genre", "rating"],  # Header row
    ["Inception", "Sci-Fi", "8.8"],
    ["Hit man", "Crime", "9.2"],
    ["How to train your dragon", "Animation", "8.3"],
    ["The Conjuring ", "Horror", "8.8"],
    ["The Dark Knight", "Action", "9.0"],
    ["Forrest Gump", "Drama", "8.8"],
    ["Ted", "Comedy", "8.8"],
    ["The Dictator", "Comedy", "8.8"],
    ["Annabell ", "Horror", "8.8"],
    ["Pulp Fiction", "Crime", "8.9"],
    ["The Matrix", "Sci-Fi", "8.7"],
]

with open("movies.csv", mode="w", newline="") as file:  # Creates and write the CSV file
    writer = csv.writer(file)    #opens the file in write mode 
    writer.writerows(movie_data)   #writes all the movie data in file  

print("movies.csv has been created!")   #confirmation message