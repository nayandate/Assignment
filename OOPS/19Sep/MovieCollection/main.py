from models.movie import Movie


def read_movies(count):
	movies = []

	for number in range(1, count + 1):
		print(
			f"Enter details for movie {number} "
			"(id name genre rating ticket_price):"
		)
		details = input().split()
		movie_id = details[0]
		genre = details[-3]
		rating = details[-2]
		ticket_price = details[-1]
		movie_name = " ".join(details[1:-3])
		movies.append(
			Movie(
				int(movie_id),
				movie_name,
				genre,
				float(rating),
				float(ticket_price),
			)
		)

	return movies


def main():
	movies = read_movies(5)

	print("\nAll Movies")
	for movie in movies:
		print(movie)

	print("\nMovies with rating greater than 8:")
	for movie in movies:
		if movie.rating > 8:
			print(f"{movie.movie_name} {movie.rating:.1f}")

	print("\nAction Movies:")
	for movie in movies:
		if movie.genre.lower() == "action":
			print(movie.movie_name)

	highest_rated = max(movies, key=lambda movie: movie.rating)
	print("\nHighest Rated Movie:")
	print(f"{highest_rated.movie_name} {highest_rated.rating:.1f}")

	print("\nMovies with ticket price greater than 300:")
	for movie in movies:
		if movie.ticket_price > 300:
			print(f"{movie.movie_name} {movie.ticket_price:g}")

	average_rating = sum(movie.rating for movie in movies) / len(movies)
	print("\nAverage Movie Rating:")
	print(f"{average_rating:.2f}")

	movie_id = int(input("\nSearch Movie Id: "))
	found_movie = next(
		(movie for movie in movies if movie.movie_id == movie_id),
		None,
	)
	print("\nMovie Found:")
	print(found_movie if found_movie else "Movie not found")


if __name__ == "__main__":
	main()
