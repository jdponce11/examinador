from examiner.models.book import Book
from examiner.models.chunk import Chunk
from examiner.services.file_processor import convert_epub_to_txt 
from examiner.services.chunker import divide_book 
from examiner.services.ai_utils import generate_client
from examiner.services.ai_utils import generate_questions
from examiner.prompts import exam_types

#These are user defined parameters (in the future they'll be chosen from the frontend)

path_linux = "/home/jose/Documents/Proyectos/examinador/Chicas_muertas.epub"
path_windows = r"C:\Users\josep\Documents\Proyectos\examinador\Chicas_muertas.epub"
book = Book("Chicas Muertas", "Silvia Almada", path_windows)
model = "gpt-5-nano"
num_questions = 2 
prompt_for_question = exam_types['multiple_choice']

openAIClient = generate_client()
book.text = convert_epub_to_txt(book.pathtofile)
#num_chunks = estimate_chunks_per_model(model, book.text)
chunks = divide_book(book, 2)
questions = generate_questions(book, chunks, num_questions, prompt_for_question, openAIClient, model)


print(questions)
