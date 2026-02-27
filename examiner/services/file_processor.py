import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def convert_epub_to_txt(book_instance):
    complete_text = ''
    epub_book = epub.read_epub(book_instance.pathtofile)
    for doc in epub_book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(doc.get_body_content(), 'html.parser')
        complete_text += '\n'.join([para.get_text() for para in soup.find_all('p')])
    
    return complete_text