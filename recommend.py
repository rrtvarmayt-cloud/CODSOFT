movies = {
    "Titanic": ["Avatar", "The Notebook", "Romeo + Juliet"],
    "Avengers": ["Iron Man", "Thor", "Captain America"],
    "Inception": ["Interstellar", "Tenet", "Shutter Island"],
    "Bahubali": ["RRR", "Magadheera", "Eega"],
    "KGF": ["Salaar", "Pushpa", "Vikram"]
}

movie = input("Enter a movie name: ")

if movie in movies:
    print("\nRecommended movies:")

    for recommendation in movies[movie]:
        print("-", recommendation)

else:
    print("Sorry, movie not found.")