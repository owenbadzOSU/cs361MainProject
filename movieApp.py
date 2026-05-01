
import csv
import Movie
import ast
def movieApp(interest, runtime):

    movies = load_movies("imdb_top_250_movies_clean.csv")
    print("===================================")
    print("       MOVIE RECOMMENDER APP")
    print("===================================\n")
    print("WELCOME!\n")
    print("This application is design to help you find new movies to watch based on your interests!\n")
    print("Enter 1 to select what type of movies you are interested in\n")
    print("Enter 2 to get a list of movies\n")
    print("Enter 3 to see instructions for how to use this app\n")
    print("Note: If this is you first time using this app, you have to enter 1 to select what type of movies you are interested in first or else the app will not recomend you movies\n")

    a = True
    while a:

        answer = input("Enter your choice: ")

        if answer == "1":
            a = False
            interests()
        elif answer == "2":
            a = False
            if interest == 0:
                error()
            
            recomender(interest, runtime, movies)
        elif answer == "3":
            a = False
            instructions(interest, runtime)
        else:
            print("Did not enter a valid option, try again\n")

def recomender(interest, runtime, movies):
    iMovies = []
    for movie in movies:
        if set(movie.genres) & set(interest):
            iMovies.append(movie)

    recMovies = []

    for movie in iMovies:
        
        if runtime == 1:
            if movie.runtime < 90:
                recMovies.append(movie)
        elif runtime == 2:
            if movie.runtime > 90 and movie.runtime < 120:
                recMovies.append(movie)
        elif runtime == 3:
            if movie.runtime > 120:
                recMovies.append(movie)
        else:
            recMovies.append(movie)
        
    printList(interest, runtime, recMovies)


def printList(interest, runtime, recMovies):

    print("===================================")
    print("       MOVIE RECOMMINDATIONS")
    print("===================================\n")

    print("Based on your interests, here are some movies you might want to watch:\n")

    if len(recMovies) == 0:
        print("There was no movies based on your preferences, check that you enter your preferences correctly.")
    else:

        for i in range(min(5, len(recMovies))):
            message = str(i + 1) + ". " + recMovies[i].title
            print(message)
        

        print("\n")
        print("Enter the number of a movie to view details or by typing the title of the movie EX: '" + recMovies[0].title + "'")
    
    print("Type 'back' to return to the welcome page\n")
    while True:

        answer = input("Input: ")
        if answer == "back":
            movieApp(interest, runtime)
            return
        elif any(movie.title == answer for movie in recMovies):
            selected = next(movie for movie in recMovies if movie.title.lower() == answer.lower())
            details(interest, runtime, selected, recMovies)
            return
        elif answer.isdigit() and 1 <= int(answer) <= 5:
            index = int(answer) - 1
            details(interest, runtime, recMovies[index], recMovies)
            return
        else:
            print("Invalid input, try again")


def details(interest, runtime, movie, recMovies):
    print("===================================")
    print("          MOVIE DETAILS")
    print("===================================\n")

    for key, value in movie.__dict__.items():
        print(key, ":", value)

    print("\n")
    print("Enter any key to go back to the movie list")
    answer = input("Input: ")
    printList(interest, runtime, recMovies)

        
    
    







def error():
    print("===================================")
    print("       MOVIE RECOMMENDER APP")
    print("===================================\n")
    print("!!! You did not enter in what type of movies you are interested in !!!\n")
    answer = input("Enter any key to go back to the home page: ")
    movieApp(0,0)
    return
    


def interests():
    print("===================================")
    print("        INTEREST SELECTION ")
    print("===================================\n")
    print("Select the genres that you are interested in\n")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Horror")
    print("5. Scfi")
    print("6. Romance\n")
    print("Select a genre by entering in the number. To select multiple genres have it seperated by a space.\n\n")
    

    print("===================================")
    print("        RUNTIME PREFERENCE ")
    print("===================================\n")
    print("Select your ideal runtime:\n")
    print("1. < 90 minutes")
    print("2. 90-120 minutes")
    print("3. > 120 minutes")
    print("4. No preference\n")
    print("Type the number of your choice")
    print("Note: choosing a runtime filter may limit the number of results\n")
    answer1 = input("Interests Input: ").lower().split()
    answer2 = input("Runtime Input: ")

    genre_map = {
        "1": "Action",
        "2": "Comedy",
        "3": "Drama",
        "4": "Horror",
        "5": "Sci-Fi",
        "6": "Romance"
    }

    valid_genres = {
        "action": "Action",
        "comedy": "Comedy",
        "drama": "Drama",
        "horror": "Horror",
        "sci-fi": "Sci-Fi",
        "scifi": "Sci-Fi", 
        "romance": "Romance"
    }

    selected = []

    for choice in answer1:
        if choice in genre_map:
            selected.append(genre_map[choice])
        elif choice in valid_genres:
            selected.append(valid_genres[choice])
        else:
            print(f"Ignored invalid genre: {choice}")

    
    selected = list(set(selected))


    movieApp(selected, int(answer2))
    return



def instructions(interest, runtime):
    print("===================================")
    print("          INSTRUCTIONS")
    print("===================================\n")
    print("TO DO:\n")
    print("1. Go to the interests section")
    print("2. Enter in what genres you are interested in and your ideal runtime")
    print("3. Go to the movie recomender section to get a list of movies")
    print("4. Select a movie that you are intrested in to get more details about it")
    print("Note: Feel free to edit your interests and runtime to get a new selection of movies!\n")
    print("Press any key to go back to the welcome page\n")
    answer = input("Enter your selection here: ")
    movieApp(interest, runtime)
    return









def load_movies(file_path):
    movies = []

    with open(file_path, newline='' ,encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            movie = Movie.Movie(
                title=row.get("title"),
                description=row.get("description"),
                genres=ast.literal_eval(row.get("genres")),
                runtime=int(row.get("runtime_minutes", 0)),
                content_rating=row.get("content_rating"),
                num_votes=int(row.get("num_votes", 0))
            )

            movies.append(movie)

    return movies





movieApp(0,0)
