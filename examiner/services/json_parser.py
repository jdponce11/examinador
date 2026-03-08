from examiner.models.question import *

def json_parse_questions(questions, exam_type):
    formatted_questions = []
    if exam_type == 'open_ended':
        #QUestions from chunk is a list of dictionaries from the json parsed output of the AI
        for question in questions:
            formatted_question = Question_openended(question["pregunta"], question["respuesta_sugerida"])
            formatted_questions.append(formatted_question)
    elif exam_type == 'multiple_choice':
        for question in questions:
            formatted_question = Question_multiplechoice(question["pregunta"], question["opciones"], question["respuesta"])
            formatted_questions.append(formatted_question)

    return formatted_questions