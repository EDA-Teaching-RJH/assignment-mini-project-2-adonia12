import re #imports regular expression module 
import csv #imports the csv module for th file handling 

class movie:  #class that represents a single movie 
    def __init__(self, title, genre, rating):
        self.title = title  # movie title 
        self.genre = genre    # movie genre
        self.rating = rating  #movie rating 

class movierecs:   #a class that manages movie recommendations 
    def __init__(self):
        self.movies = []  #list to store movies names

    def loadmovies(self, filename):  #loads movies from the csv file 
        with open(filename, mode='r') as file:
            reader = csv.reader(file)  #opens the file to read mode 
            next(reader)  #skips the header row 
            for row in reader:   # iterates through each row in the csv file, creates a movie object in each row and adds it too the movies list 
                self.movies.append(movie(row[0], row[1], float(row[2]))) 

    def savemovies(self, filename):  #saves the movies to the csv file 
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)  #openns the file in write mode 
            for movie in self.movies:  #iterates thought the list of movies 
                writer.writerow([movie.title, movie.genre, movie.rating])  #writes each moie attribute to the csv file 

    def recommend(self, user_genre):   #method to recommend movies based on  the genre the user inputs  
        pattern = re.compile(user_genre, re.IGNORECASE)    #for case sensitive search 
        recommendation = [movie.title for movie in self.movies if pattern.search(movie.genre)]   #creates a list of movies that match the genre  
        return recommendation  #returnns the list of recommended movies 

if __name__ == "__main__":     #Main block 
    recommender = movierecs()  #creats the movie recs class 
    recommender.loadmovies('movies.csv')  #loads the list of movies into the csv file  

    user_input = input("Enter a genre to get movie recommendation:  ") #asks the user to input a genre 
    recommended_movies = recommender.recommend(user_input)               # creates a list of recommeded movies 

    if recommended_movies:            #displays the recommended movies to the user 
        print("Movies recommended: ")   #prints the movies recommended
        for movie in recommended_movies:
            print(movie)

    else:
        print("No movies found for the given genre")   #informs user if no movies were found in the genre searched  

    recommender.savemovies('updated_movies.csv')   #saves the movies list to a csv file 
