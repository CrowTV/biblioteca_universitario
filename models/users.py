class User:
    def __init__(self, name, last_name, email, phone_number, career, faculty,CI,direcction,age):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.career = career
        self.faculty = faculty
        self.CI = CI
        self.direcction = direcction
        self.age = age
        
class Student(User):
    def __init__(self, name, last_name, email, phone_number, career, faculty,CI,direcction,age,semester):
        super().__init__(name, last_name, email, phone_number, career, faculty,CI,direcction,age)
        self.semester = semester
        self.professor = None
        
class Professor(User):
    def __init__(self, name, last_name, email, phone_number, career, faculty,CI,direcction,age):
        super().__init__(name, last_name, email, phone_number, career, faculty,CI,direcction,age)

        