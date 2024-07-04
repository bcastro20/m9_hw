from booklover.booklover import BookLover

test = BookLover('b c', 'bc@virginia.edu', 'nonfiction')


book_name= 'harry potter'
book_rating = 1

test.add_book(book_name, book_rating)  
print(test.num_books_read())
