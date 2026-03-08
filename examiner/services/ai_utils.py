from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

def generate_client():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return client

def generate_response(client, model, instructions, input):
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=input
    )
    return response.output_text

def generate_questions(book, chunks, num_questions, prompt_for_question, openAIClient, model):
    questions_per_chunk = num_questions//len(chunks)
    if (questions_per_chunk < 1) or num_questions % len(chunks) != 0:
        raise Error("Invalid number of questions for exam, has to be multiple of chunks.")
    book_metadata = "Título: " + book.name + "\n" + "Autor: " + book.author + "\n"
    question_prompt_w_metadata = book_metadata + prompt_for_question
    questions = []
    for chunk in chunks:
        question_prompt_w_num_and_meta = (
            question_prompt_w_metadata +
            '\n' +
            f'Genera una lista con la estructura JSON arriba, con {questions_per_chunk} elementos, '
            f'es decir, {questions_per_chunk} diferentes preguntas para esta sección'
        )
        question_json = generate_response(openAIClient, model, question_prompt_w_num_and_meta, "sección del libro: "+ chunk.content)
        questions.append(question_json)

    return questions

