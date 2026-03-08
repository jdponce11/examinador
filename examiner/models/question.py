class Question_multiplechoice():
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    def __repr__(self):
        return f"Question_multiplechoice('{self.question}', '{self.options}', '{self.answer}')"

class Question_openended():
    def __init__(self, question, proposed_answer):
        self.question = question
        self.proposed_answer = proposed_answer
    def __repr__(self):
        return f"Question_openended('{self.question}', '{self.proposed_answer}')"
