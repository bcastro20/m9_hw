import unittest
import pandas as pd

from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')


        book_name= 'harry potter'
        book_rating = 1
        
        setup.add_book(book_name, book_rating)

        self.assertTrue(any(setup.book_list['book_name']==book_name))


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')

        book_name= 'Lorax'
        book_rating = 5
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

        setup.add_book(book_name, book_rating)
        setup.add_book(book_name, book_rating)

        self.assertEqual(setup.num_books_read(),1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')

        book_name= 'games'
        book_rating = 2
        
        setup.add_book(book_name, book_rating)

        self.assertTrue(setup.has_read(book_name))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')

        book_name= 'roar'

        self.assertFalse(setup.has_read(book_name))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')

        book_name= 'juice'
        book_rating = 3
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

        setup.add_book(book_name, book_rating)
        book_name= 'fries'
        book_rating = 1
        setup.add_book(book_name, book_rating)

        self.assertEqual(setup.num_books_read(),2)

        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        setup = BookLover('b c', 'bc@virginia.edu', 'nonfiction')

        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        book_name= 'w'
        book_rating = 3
        setup.add_book(book_name, book_rating)
        
        book_name= 'pop'
        book_rating = 1
        setup.add_book(book_name, book_rating)
 
        book_name= 'soda'
        book_rating = 5
        setup.add_book(book_name, book_rating)
        
        testfavs = setup.fav_books()
        
        for rating in testfavs['book_rating']:
            self.assertTrue(rating > 3)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)

