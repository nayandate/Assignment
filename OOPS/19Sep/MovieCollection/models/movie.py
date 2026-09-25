class Movie:
    def __init__(self, movie_id, movie_name, genre, rating, ticket_price):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.genre = genre
        self.rating = rating
        self.ticket_price = ticket_price

    def __str__(self):
        return (
            f"{self.movie_id} {self.movie_name} {self.genre} "
            f"{self.rating:.1f} {self.ticket_price:g}"
        )
