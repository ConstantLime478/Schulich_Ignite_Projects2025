class Student:
    questions = 0 
    def __init__ (self, name):
        self.name = name
        
    def add_homework(self, num_questions):
        self.questions += num_questions
    
    def get_num_questions(self):
        return str(self.questions)