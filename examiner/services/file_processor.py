import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from markdown_pdf import Section, MarkdownPdf

def convert_epub_to_txt(epub_path):
    complete_text = ''
    epub_book = epub.read_epub(epub_path)
    for doc in epub_book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(doc.get_body_content(), 'html.parser')
        complete_text += '\n'.join([para.get_text() for para in soup.find_all('p')])
    
    return complete_text


def generate_exam(questions, titulo, exam_type):
    pdf = MarkdownPdf(toc_level=2, optimize=True)
    header = Section(f"""# Examen - {titulo}""")
    pdf.add_section(header)
    for question_no, question in enumerate(questions, start=1):
        md_section = Section(format_question_md(question, question_no, exam_type), toc=False)
        pdf.add_section(md_section)

    pdf.save(f"exam_{titulo}.pdf")

def format_question_md(question, question_no, exam_type):
    if exam_type == 'open_ended':
        md = f"""
        ## Pregunta {question_no}

        {question.question}

        --- 

        """
    elif exam_type == 'multiple_choice':
        md = f"""
        ## Pregunta {question_no}

        {question.question}

        <ol>
        <li> {question.options["A"]} </li>
        <li> {question.options["B"]} </li>
        <li> {question.options["C"]} </li>
        <li> {question.options["D"]} </li>
        </ol>

        ---

        """
    return md