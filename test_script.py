from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from examiner.models.book import Book
from examiner.models.chunk import Chunk
from examiner.services.file_processor import convert_epub_to_txt 
from examiner.services.chunker import divide_book 

path = r"C:\Users\josep\Documents\Proyectos\examinador\Chicas_muertas.epub"
book = Book("Chicas Muertas", "Silvia Almada", path)

book.text = convert_epub_to_txt(book)
chunks = divide_book(book, 10)


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


response = client.responses.create(
    model="gpt-4.1",
    instructions="Eres un bot que devuelve preguntas de examen, de respuesta corta, para clase de literatura, luego de que un alumno leyó un libro. Haz una pregunta sobre la siguiente sección del libro, y dame una respuesta de ejemplo",
    input="Sección del libro: "+chunks[3].content
)


print(response.output_text)

