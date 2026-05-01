class Movie:
    def __init__(self, title, description, genres, runtime, content_rating=None, num_votes=None):
        self.title = title
        self.description = description
        self.genres = genres
        self.runtime = runtime
        self.content_rating = content_rating
        self.num_votes = num_votes

    def __str__(self):
        return (
            f"{self.title}\n"
            f"Genres: {self.genres} | Runtime: {self.runtime} min | Rated: {self.content_rating}\n"
            f"{self.description}\n"
        )

