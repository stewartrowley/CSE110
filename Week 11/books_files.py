with open("books.txt") as book_file:
    for line in book_file:
        book = line.strip()

        # Print the book out to the screen
        print(book)

