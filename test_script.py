from examiner.models.book import Book
from examiner.services.file_processor import convert_epub_to_txt 

path = r"C:\Users\josep\Documents\Proyectos\examinador\Chicas_muertas.epub"
book = Book("Chicas Muertas", "Silvia Almada", path)

book.text = convert_epub_to_txt(book)

print(f"Book: {book.name} by {book.author}")
print(f"First 200 characters: {book.text[:6010]}")
