class Student:

    #academic_history = [{courses_attempted: grade}]
    #current_enrollments = [(course code, semester, year)]
    #study_plan = [(course code, semester, year)]
        #The study plan excludes the courses that the student has already passed, and courses that he is currently enrolled in.
    def __init__(self, name, student_id, dob, program_code, status, academic_history = {}, current_enrollments = [], study_plan =[]):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.program_code = program_code
        self.status = status
        self.academic_history = academic_history
        self.current_enrollments = current_enrollments
        self.study_plan = study_plan


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def set_dob(self, dob):
        self.dob = dob

    def get_dob(self):
        return self.dob
    
    def set_program_code(self, program_code):
        self.program_code = program_code

    def get_program_code(self):
        return self.program_code
    
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_academic_history(self, academic_history = {}):
        self.academic_history = academic_history

    def get_academic_history(self):
        return self.academic_history

    def set_current_enrollments(self, current_enrollments = []):
        self.current_enrollments = current_enrollments

    def get_current_enrollments(self):
        return self.current_enrollments

    def set_study_plan(self, study_plan = []):
        self.study_plan = study_plan

    def get_study_plan(self):
        return self.study_plan



    def __str__(self):        
        formatted_str = "\n\nStudent name: " + self.name
        formatted_str += "\nStudent ID: " + self.student_id
        formatted_str += "\nDate of birth: " + self.dob 
        formatted_str += "\nProgram code: " + self.program_code 
        formatted_str += "\nStatus: " + self.status 
        return formatted_str

    def display_academic_history(self):
        print('\nAcademic history:')
        for key in self.academic_history:
            print(key + ': ' + self.academic_history[key]) 

    def display_currenet_enrollment(self):
        print('\nCurrent enrollments')
        for i in self.current_enrollments:
            j = i.split('|')
            print('Course code:', j[0], 'Semester:', j[1], 'Year:', j[2])

    def display_study_plan(self):
        print('\nFuture study plan')
        for i in self.study_plan:
            j = i.split('|')
            print('Course code:', j[0], 'Semester:', j[1], 'Year:', j[2])

    def enrol(self, enrol_c, prerequisite, available_semester):
        current= []
        feature = []
        for i in self.current_enrollments:
            j = i.split('|')
            current.append(j[0])
        for a in self.study_plan:
            b = a.split('|')
            feature.append(b[0])
        if enrol_c in self.academic_history.keys():
            print('Course already been completed.')
        elif enrol_c in current:
            print('Course is currently undertaking.')
        elif enrol_c not in feature:
            print('Course is not in your study plan')
        elif enrol_c in feature:
            if (prerequisite != 'None') and (prerequisite not in self.academic_history.keys()) and (prerequisite not in current):
                print('Prerequisite not met.')
            else:
                while True:
                    try:
                        enrol_year= int(input("Enter year to enrol, enter '0' to exit: "))
                        if enrol_year == 0:
                            return
                        elif enrol_year < 2021 and enrol_year != 0:
                            print('Please enter a valid year, starting from 2022.')
                        elif enrol_year > 2021:
                            print('Available semester: ', available_semester)
                            enrol_s = input("Enter semester to enrol (S1 or S2), enter '0' to go exit: ").upper()
                            while enrol_s != '0' and enrol_s != 'S1' and enrol_year != 'S2':
                                enrol_s = input("Enter semester to enrol (S1 or S2), enter '0' to go exit: ").upper()
                            if enrol_s == '0':
                                return
                            if enrol_s not in available_semester:
                                print('Please choose an available semester.')
                            else:
                                self.current_enrollments.append(enrol_c + '|' + enrol_s + '|' + str(enrol_year))
                                print('Successfully enrolled')
                                return 
                    except:
                        print('Invalid input')      

    def unenrol(self, unenrol_c):
        i = 0
        while i <= len(self.current_enrollments) -1:
            j = self.current_enrollments[i].split('|')
            if j[0] == unenrol_c:
                print('Confirm to unenrol', unenrol_c)
                confirm = input("Type 'yes' or 'no': ").lower()
                if confirm == 'no':
                    return
                elif confirm =='yes':
                    self.current_enrollments.remove(self.current_enrollments[i])
                    print('Successfully dropped course', unenrol_c)
                    return
            i +=1
        print('Course is not currently enrolled.')    
        return


