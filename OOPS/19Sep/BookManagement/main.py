from modelsbook import Book


def read_books(count):
	books = []

	for number in range(1, count + 1):
		print(f"Enter details for book {number} (id name author price):")
		details = input().split()
		book_id = details[0]
		author = details[-2]
		price = details[-1]
		book_name = " ".join(details[1:-2])
		books.append(Book(int(book_id), book_name, author, float(price)))

	return books


def display_books(books, include_author=True):
	for book in books:
		if include_author:
			print(book)
		else:
			print(f"{book.book_id} {book.book_name} {book.price:g}")


def main():
	books = read_books(5)

	print("\nAll Books")
	display_books(books)

	book_id = int(input("\nEnter book id to search: "))
	found_book = next(
		(book for book in books if book.book_id == book_id),
		None,
	)
	print("\nBook Found")
	print(found_book if found_book else "Book not found")

	author = input("\nEnter author to search: ").strip()
	print(f"\nBooks by {author}")
	display_books(
		[book for book in books if book.author.lower() == author.lower()],
		include_author=False,
	)

	print("\nBooks with price greater than 500")
	for book in books:
		if book.price > 500:
			print(book.book_name)

	most_expensive = max(books, key=lambda book: book.price)
	print("\nMost Expensive Book")
	print(f"{most_expensive.book_name} = {most_expensive.price:g}")

	average_price = sum(book.price for book in books) / len(books)
	print("\nAverage Price")
	print(f"{average_price:g}")


if __name__ == "__main__":
	main()
