
class Program:
    def __init__(self, program_code, credit, core_courses = [], elective_courses = []):
        self.program_code = program_code
        self.credit = credit
        self.core_courses = core_courses
        self.elective_courses = elective_courses

    def set_program_code(self, program_code):
        self.program_code = program_code

    def get_program_code(self):
        return self.program_code

    def set_credit(self, credit):
        self.credit = credit

    def get_credit(self):
        return self.semester

    def set_core_courses(self, core_courses =[]):
        self.core_courses = core_courses

    def get_core_courses(self):
        return self.core_courses

    def set_elective_courses(self, elective_courses=[]):
        self.elective_courses = elective_courses

    def get_elective_courses(self):
        return self.elective_courses

    def display_study_plan(self):
        print('\nCurrent enrollments')
        for i in self.current_enrollments:
            j = i.split('|')
            print('Course code:', j[0], 'Semester:', j[1], 'Year:', j[2])

    def __str__(self):
        formatted_str = "\n\nProgram code: " + self.program_code
        formatted_str += "\nCredit: " + self.credit 
        for c in self.core_courses:
            course, prerequisite = c.split('-')
            formatted_str += '\nCourse code: ' + course + '  Prerequisite: ' + prerequisite
        for c in self.elective_courses:
            course, prerequisite = c.split('-')
            formatted_str+= '\nCourse code: ' + course + '  Prerequisite: ' + prerequisite
        return formatted_str
