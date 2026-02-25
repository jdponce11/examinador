from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


#Let user specify path to book (.epub)

#Convert the book to text

#Divide the book into chunks

#For each chunk, make 2 exam questions

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1",
    input=""
)

print(response.output_text)