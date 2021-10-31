
class Course:
    def __init__(self, course_code, title, credit, prerequisite, available_semester = []):
        self.course_code = course_code
        self.title = title
        self.credit = credit
        self.prerequisite = prerequisite
        self.available_semester = available_semester

    def set_course_code(self, course_code):
        self.course_code = course_code

    def get_course_code(self):
        return self.course_code
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_credite(self, credit):
        self.credit = credit

    def get_credit(self):
        return self.credit

    def set_prerequisite(self, prerequisite):
        self.prerequisite = prerequisite

    def get_prerequisite(self):
        return self.prerequisite

    def set_available_semester(self, available_semester = []):
        self.available_semester = available_semester

    def get_available_semester(self):
        return self.available_semester

    def __str__(self):
        formatted_str = "\n\nCourse code: " + self.course_code
        formatted_str += "\nTitle: " + self.title
        formatted_str += "\nCredit: " + self.credit 
        formatted_str += "\nPrerequisite: " + self.prerequisite 
        if self.available_semester[0] == '':
            formatted_str += '\nAvailable semester: ' + self.available_semester[1]
        elif self.available_semester[1] =='':
            formatted_str += '\nAvailable semester: ' + self.available_semester[0]
        else:
            formatted_str += '\nAvailable semester: ' + self.available_semester[0] + ', ' + self.available_semester[1]
        return formatted_str

