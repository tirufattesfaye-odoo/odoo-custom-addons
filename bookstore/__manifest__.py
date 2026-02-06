{
    'name': "bookstore",
    'version': '1.0',
    'summary': 'The Bookstore module helps to show book details including title, author, publisher published_date, '
               'book_age and cover of the books. It allows users to categorize books by publisher and author,'
               ' and the books can be searched by title and they can be filtered by book age. ',
    'depends': ['base', 'mail'],
    'author': 'Tirufat Tesfaye',
    'category': 'sales',
    'sequence': 0,
    'data': [
           'security/ir.model.access.csv',
           'views/book_views.xml',
           'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
