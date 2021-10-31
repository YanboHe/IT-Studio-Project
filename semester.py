class Semester:
    # course_offerings = [course_name, max_number, [enrolled_students]
    def __init__(self, semester, course_offerings = []):
        self.semester = semester
        self.course_offerings = course_offerings


    def set_semester(self, semester):
        self.semester = semester

    def get_semester(self):
        return self.semester

    def set_course_offerings(self, course_offerings):
        self.course_offerings = course_offerings

    def get_course_offerings(self):
        return self.course_offerings


    def __str__(self):
        formatted_str = "\n\nSemester: " + self.semester
        return formatted_str

    def display_course_offerings(self):
        for c in self.course_offerings[1:]:
            j =  c.split('|')
            print('\nCourse name:', j[0], 'Maximum student:', j[1])
            print('Current enrolled students: ', end='')
            for i in j[2].split('-'):
                print(i, end='')
        pass


