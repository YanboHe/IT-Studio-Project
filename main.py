import csv
from course import Course
from program import Program
from student import Student
from semester import Semester


# def login_menu():
#     print('Welcom to School Enrollment System')
#     print('1. Student login')
#     print('2. System login')
#     print('3. Exit Program')

#     option = int(input("Please select a number option:"))
#     while option <1 or option >3:
#         option = int(input("Please select a valid number option:"))
#     if option == 1:
#         studentID = input("Please enter a student ID:")
#         student_menu(studentID)
#     elif option == 2:
#         system_menu()
#     elif option == 3:
#         print('Are you sure you want to exit the program?')
#         print('1. Yes')
#         print('2. No')
#         option = int(input("Please select a number option:"))
#         while option <1 or option >2:
#             option = int(input("Please select a valid number option:"))
#         if option == 1:
#             quit()
#         elif option == 2:
#             login_menu()

def student_menu(studentID, student_list, program_list, course_list):
    #check with databse
    i = 1
    while i <= len(student_list) - 1:
        student = student_list[i]
        i+=1
        if student.student_id == studentID:
            flag = True
            while flag:
                print('\n\nHello', studentID)
                print('1. Display academic history')
                print('2. Display current enrolment')
                print('3. Display program information')
                print('4. Query course information')
                print('5. Enrol in a current offering')
                print('6. UnEnrol in a current offering')
                print('7. Exit')

                try:
                    option = int(input("Please select a number option:"))
                except:
                    print('Invalid option')
                if option == 1:
                    #display academic history
                    student.display_academic_history()
                elif option == 2:
                    #Display current enrolment
                    student.display_currenet_enrollment()
                elif option == 3:
                    #query program
                    print('\nDisplay all programs information:')
                    for program in program_list[1:]:
                        print(program)
                elif option == 4:
                    #query course
                    search_c = input("Please type in the course code you want to search:").upper()
                    while not search_c:
                        search_c = input("Please type in the course code you want to search:").upper()
                    j = 0
                    while j <= len(course_list) - 2:
                        course = course_list[j]
                        j+=1
                        if course.course_code == search_c:
                            print(course)
                            break
                        if j == len(course_list) - 2:
                            print('Course code cannot be found.')
                            break
                elif option ==5:
                    #enrol
                    enrol_c = input("Please type in the course code you want to enrol:").upper()
                    while not enrol_c:
                        enrol_c = input("Please type in the course code you want to enrol:").upper()
                    j = 0
                    while j <= len(course_list) - 2:
                        course = course_list[j]
                        j+=1
                        if course.course_code == enrol_c:
                            student.enrol(enrol_c, course.prerequisite, course.available_semester)
                            break
                        if j == len(course_list) - 2:
                            print('Course code cannot be found.')
                            break
                    pass
                elif option == 6:
                    #unenrol
                    unenrol_c = input("Please type in the course code you want to unenrol:").upper()
                    while not unenrol_c:
                        unenrol_c = input("Please type in the course code you want to unenrol:").upper()
                    student.unenrol(unenrol_c)
                elif option ==7:
                    #quit to login menu
                    flag = False
                    return
                else:
                    print('Invalid option')
    print('Student ID not found!')
    return    


def system_menu(student_list, program_list, course_list, semester_list):
    #check with databse
    flag = True
    while flag:
        print('\n\nHello admin')
        print('1. Add/Remove/Amend a student')
        print('2. Add/Remove/Amend a course')
        print('3. Add/Remove/Amend a program')
        print('4. Add/Remove/Amend a semester')
        print('5. Query student information including academic history and current enrolment')
        print('6. Manual amendment of the study plan for a student')
        print('7. Validate all student’s study plan')
        print('8. Display student achievements for a course')
        print('9. Grade distrybutions of a course')
        print('10. Exit')

        try:
            option = int(input("Please select a number option:"))
        except:
            print('Invalid option')

        if option == 1:
            #Amend a student
            while True:
                print('\n1. Display all students')
                print('2. Add a student')
                print('3. Amend a student')
                print('4. Exit')

                try:
                    option = int(input("Please select a number option:"))
                except:
                    print('Invalid option')

                if option == 1:
                    for student in student_list[1:]:
                        print(student)
                        student.display_academic_history()
                        student.display_currenet_enrollment()
                        student.display_study_plan()
                elif option == 2:
                    new_name = input("Student name:")
                    new_student_id = input("Student ID:").upper()
                    new_dob = input("Student date of birth:")
                    new_program_code = input("Student program code:").upper()
                    new_status = input("Student program status:")
                    mydict = {}
                    for result in input("Student academic history:").upper().split(' '):
                        id, grade = result.split(':')
                        mydict[id] = grade
                    new_academic_history = mydict
                    new_current_enrollments = input("Student current enrollments:").upper().split(' ')
                    new_study_plan = input("Student study plan:").upper().split(' ')
                    new_student = Student(new_name, new_student_id, new_dob, new_program_code, new_status ,new_academic_history, new_current_enrollments, new_study_plan)
                    student_list.append(new_student)
                    print('New student successfully added')
                elif option == 3:
                    amend_student_id = input("Enter student ID: ").upper()
                    while not amend_student_id:
                        amend_student_id = input("Enter student ID: ").upper()
                    i = 1
                    while i <= len(student_list) -1:
                        student = student_list[i]
                        i+=1
                        if student.student_id == amend_student_id:
                            while True:
                                print('\n1. Remove student')
                                print("2. Change student's name")
                                print("3. Change student's ID")
                                print("4. Change student's date of birth")
                                print("5. Change student's program")
                                print("6. Change student's program status")
                                print("7. Change student's academic grade")
                                print("8. Exit")

                                try:
                                    option = int(input("Please select a number option:"))
                                except:
                                    print('Invalid option')

                                if option == 1:
                                    confirm = input("Type 'yes' to remove course: ").lower()
                                    if confirm == 'yes':
                                        student_list.remove(student)
                                        print('Student successfully removed')
                                elif option == 2:
                                    new_name = input("Please enter a new name:")
                                    while not new_name:
                                        new_name = input("Please enter a new name:")
                                    student.set_name(new_name)
                                    print('Successfully changed')
                                elif option == 3:
                                    new_ID = input("Please enter a new ID:").upper()
                                    while not new_ID:
                                        new_ID = input("Please enter a new ID:").upper()
                                    student.set_student_id(new_ID)
                                    print('Successfully changed')
                                elif option == 4:
                                    new_dob = input("Please enter a new date of birth:")
                                    while not new_dob:
                                        new_dob = input("Please enter a new date of birth:")
                                    student.set_dob(new_dob)
                                    print('Successfully changed')
                                elif option == 5:
                                    new_program = input("Please enter a new program code:").upper()
                                    while not new_program:
                                        new_program = input("Please enter a new program code:").upper()
                                    student.set_program_code(new_program)
                                    print('Successfully changed')
                                elif option == 6:
                                    new_status = input("Please enter a new program status:")
                                    while not new_status:
                                        new_status = input("Please enter a new program status:")
                                    student.set_status(new_status)
                                    print('Successfully changed')
                                elif option == 7:
                                    update_g = input("Please enter the course code of the grade you want to update: ").upper()
                                    try:
                                        print('Course:', update_g, 'Grade:', student.academic_history[update_g])
                                    except:
                                        print('Course not found')
                                    new_grade = input("Please enter the course code of the grade you want to update (HD, D, C, P, N): ").upper()
                                    while new_grade!='HD' and new_grade!='D' and new_grade!='C' and new_grade!='P' and new_grade!='N':
                                        new_grade = input("Please enter the course code of the grade you want to update (HD, D, C, P, N): ").upper()
                                    try:
                                        student.academic_history[update_g] = new_grade
                                        print('Update successful')
                                    except:
                                        print('Error, please try again')
                                    pass
                                elif option == 8:
                                    break
                                else:
                                    print('Invalid option')
                        
                    print('Student ID not found.')            
                elif option == 4:
                    break  
                else:
                    print('Invalid option')  
        elif option == 2:
            #Amend a course
            while True:
                print('\n1. Display all course')
                print('2. Add a course')
                print('3. Amend a course')
                print('4. Exit')

                try:
                    option = int(input("Please select a number option:"))
                except:
                    print('Invalid option')

                if option == 1:
                    for course in course_list[1:]:
                        print(course)
                elif option == 2:
                    new_course_code = input("Course code:").upper()
                    new_title = input("Course title:")
                    new_credit = input("Course credit:")
                    new_prerequisite = input("Course prerequisite:").upper()
                    new_available_semester = input("Course avvailable semester:").split('|')
                    new_course = Course(new_course_code, new_title, new_credit, new_prerequisite, new_available_semester)
                    course_list.append(new_course)
                    print('New course successfully added')
                elif option == 3:
                    amend_course_code = input("Enter course ID: ").upper()
                    while not amend_course_code:
                        amend_course_code = input("Enter course ID: ").upper()
                    i = 1
                    while i <= len(course_list) - 1:
                        course = course_list[i]
                        i+=1
                        if course.course_code == amend_course_code:
                            while True:
                                print('\n1. Remove course')
                                print("2. Change course code")
                                print("3. Change course's title")
                                print("4. Change course's credit")
                                print("5. Change course's prerequisite")
                                print("6. Change course's available semesters")
                                print("7. Exit")

                                try:
                                    option = int(input("Please select a number option:"))
                                except:
                                    print('Invalid option')
            
                                if option == 1:
                                    confirm = input("Type 'yes' to remove course: ").lower()
                                    if confirm == 'yes':
                                        course_list.remove(course)
                                        print('Course successfully removed')
                                        for student in student_list:
                                            for c in student.study_plan:
                                                j = c.split('|')
                                                if j[0] == amend_course_code:
                                                    student.set_status('1')
                                        break
                                elif option == 2:
                                    new_course_code = input("Please enter a new course code:").upper()
                                    while not new_course_code:
                                        new_course_code = input("Please enter a new course:").upper()
                                    course.set_course_code(new_course_code)
                                    print('Successfully changed')
                                elif option == 3:
                                    new_title = input("Please enter a new course title:")
                                    while not new_title:
                                        new_title = input("Please enter a new course title:")
                                    course.set_title(new_title)
                                    print('Successfully changed')
                                elif option == 4:
                                    new_credit = input("Please enter a new course credit")
                                    while not new_credit:
                                        new_credit = input("Please enter a new course credit:")
                                    course.set_credit(new_credit)
                                    print('Successfully changed')
                                elif option == 5:
                                    new_prerequisite = input("Please enter a new course prerequisite:").upper()
                                    while not new_prerequisite:
                                        new_prerequisite = input("Please enter a new course prerequisite:").upper()
                                    course.set_prerequisite(new_prerequisite)
                                    print('Successfully changed')
                                elif option == 6:
                                    new_available_semester = input("Please enter a list of new course available semesters:").upper()
                                    while not new_available_semester:
                                        new_available_semester = input("Please enter a list of new course available semesters:").upper()
                                    new_as = new_available_semester.split('|')
                                    course.set_available_semester(new_as)
                                    print('Successfully changed')
                                elif option == 7:
                                    break
                                else:
                                    print('Invalid option')

                    print('Course code not found.') 
                elif option == 4:
                    break
                else:
                    print('Invalid option')

        elif option ==3:
            #Amend a program
            while True:
                print('\n1. Display all programs')
                print('2. Add a program')
                print('3. Amend a program')
                print('4. Exit')

                try:
                    option = int(input("Please select a number option:"))
                except:
                    print('Invalid option')

                if option == 1:
                    for program in program_list[1:]:
                        print(program)
                elif option == 2:
                    new_program_code = input("Program code:").upper()
                    new_credit = input("Program credit:")
                    new_core_courses = input("Program core courses:").upper().split(' ')
                    new_elective_courses = input("Program elective courses:").upper().split(' ')
                    new_program = Program(new_program_code, new_credit, new_core_courses, new_elective_courses)
                    student_list.append(new_student)
                    print('New program successfully added')
                elif option == 3:
                    amend_program_code = input("Enter program code: ").upper()
                    while not amend_program_code:
                        amend_program_code = input("Enter program code: ").upper()
                    i = 1
                    while i <= len(program_list) -1:
                        program = program_list[i]
                        i+=1
                        if program.program_code == amend_program_code:
                            while True:
                                print('\n1. Remove program')
                                print("2. Change program code")
                                print("3. Change program total credit")
                                print("4. Change program core courses")
                                print("5. Change program elective courses")
                                print("6. Exit")

                                try:
                                    option = int(input("Please select a number option:"))
                                except:
                                    print('Invalid option')

                                if option == 1:
                                    confirm = input("Type 'yes' to remove course: ").lower()
                                    if confirm == 'yes':
                                        program_list.remove(program)
                                        print('Course successfully removed')
                                        for student in student_list:
                                            if student.program_code == amend_program_code:
                                                student.set_status('1')
                                        break
                                elif option == 2:
                                    new_program_code = input("Please enter a new program code:")
                                    while not new_program_code:
                                        new_program_code = input("Please enter a new program code:")
                                    program.set_program_code(new_program_code)
                                    print('Successfully changed')
                                elif option == 3:
                                    new_credit = input("Please enter a new ID:").upper()
                                    while not new_credit:
                                        new_credit = input("Please enter a new ID:").upper()
                                    program.set_credit(new_credit)
                                    print('Successfully changed')
                                elif option == 4:
                                    new_core_courses = input("Please enter a list of new core courses:")
                                    while not new_core_courses:
                                        new_core_courses = input("Please enter a list of new core courses:")
                                    ncc = new_core_courses.split(' ')
                                    program.set_core_courses(ncc)
                                    print('Successfully changed')
                                elif option == 5:
                                    new_elective_courses = input("Please enter a list of new elective courses:")
                                    while not new_elective_courses:
                                        new_elective_courses = input("Please enter a list of new elective courses:")
                                    nec = new_elective_courses.split(' ')
                                    program.set_elective_courses(nec)
                                    print('Successfully changed')
                                elif option == 6:
                                    break
                                else:
                                    print('Invalid option')

                    print('Program code not found.')            
                elif option == 4:
                    break
                else:
                    print('Invalid option')

        elif option == 4:
            #Amend a semester
            while True:
                print('\n1. Display all semester')
                print('2. Add a semester')
                print('3. Amend a semester')
                print('4. Exit')

                try:
                    option = int(input("Please select a number option:"))
                except:
                    print('Invalid option')

                if option == 1:
                    for semester in semester_list[1:]:
                        print(semester)
                        semester.display_course_offerings()
                elif option == 2:
                    new_semester_code = input("Semester: ").upper()
                    match = False
                    for s in semester_list:
                        if s.semester == new_semester_code:
                            print('Semester already exists.')
                            match = True
                    if not match:
                        new_course_offerings = input("Course offerings:(course_name|max_number|student1-student2): ").split(' ')
                        new_semester = Semester(new_semester_code, new_course_offerings)
                        semester_list.append(new_semester)
                        print('New semester successfully added')
                elif option == 3:
                    amend_semester = input("Enter semester: ").upper()
                    while not amend_semester:
                        amend_semester = input("Enter semester: ").upper()
                    i = 1
                    while i <= len(semester_list) -1:
                        semester = semester_list[i]
                        i+=1
                        if semester.semester == amend_semester:
                            while True:
                                print('\n1. Remove semester')
                                print("2. Change semester's ID")
                                print("3. Change semester's courses offerings")
                                print("4. Exit")

                                try:
                                    option = int(input("Please select a number option:"))
                                except:
                                    print('Invalid option')

                                if option == 1:
                                    confirm = input("Type 'yes' to remove course: ").lower()
                                    if confirm == 'yes':
                                        semester_list.remove(semester)
                                        print('Course successfully removed')
                                        break
                                elif option == 2:
                                    new_semester = input("Please enter a new semester:").upper()
                                    while not new_semester:
                                        new_semester = input("Please enter a new semester:").upper()
                                    semester.set_semester(new_semester)
                                    print('Successfully changed')
                                elif option == 3:
                                    new_course_offerings = input("Please enter a list of new courses offerings:")
                                    while not new_course_offerings:
                                        new_course_offerings = input("Please enter a list of new courses offerings:")
                                    nco = new_course_offerings.split(' ')
                                    student.set_student_id(nco)
                                    print('Successfully changed')
                                elif option == 4:
                                    break
                                else:
                                    print('Invalid option')

                    print('Student ID not found.')  

                elif option == 4:
                    break
                else:
                    print('Invalid option')

        elif option == 5:
            #Query student information
            search_s = input("Enter student ID: ").upper()
            while not search_s:
                search_s = input("Enter student ID: ").upper()
            match = False
            for student in student_list[1:]:
                if student.student_id == search_s:
                    print(student)
                    student.display_academic_history()
                    student.display_currenet_enrollment()
                    student.display_study_plan()
                    match = True    
            if not match:
                print('Student not found.')
        elif option == 6:
            #Manual amendment of a study plan 
            search_s = input("Enter student ID: ").upper()
            while not search_s:
                search_s = input("Enter student ID: ").upper()
            match = False
            for student in student_list[1:]:
                if student.student_id == search_s:
                    print(student)
                    student.display_study_plan()
                    new_study_plan = input("Enter student new study plan: ").upper()
                    while not new_study_plan:
                        new_study_plan = input("Enter student new study plan (study_plan|semester|year): ").upper()
                    nsp = new_study_plan.split(' ')
                    student.set_study_plan(nsp)
                    match = True    
            if not match:
                print('Student not found.')
        elif option == 7:
            #Validating a student’s study plan
            print('Students who needs manual amendament on study plan: ')
            match = False
            for student in student_list[1:]:
                if student.status == '1':
                    print(student)
                    match = True
            if not match:
                print("Every student's study plan is valid!")
        elif option == 8:
            #Display student achievements for a course
            achievements =[]
            search_c = input("Enter course code: ").upper()
            while not search_c:
                search_c = input("Enter course code: ").upper()
            match = False
            for student in student_list:
                if search_c in student.academic_history.keys():
                    formatted_str = student.name + ": " + student.academic_history[search_c]
                    achievements.append(formatted_str)
                    match =True
            if not match:
                print('No recorded achievements of searched course.')
            else:
                achievements.sort()
                for i in achievements:
                    print(i)
        elif option == 9:
            result_list=[]
            search_c = input("Enter course code: ").upper()
            while not search_c:
                search_c = input("Enter course code: ").upper()
            match = False
            for student in student_list:
                if search_c in student.academic_history.keys():
                    result_list.append(student.academic_history[search_c])
                    match =True
            if not match:
                print('No recorded achievements of searched course.')
            else:
                d = {'N': 0, 'P': 0, 'C': 0, 'D': 0, 'HD': 0}
                for i in result_list:
                    if d.get(i):
                        d[i] += 1
                    else:
                        d[i] = 1
                dis=[]
                for i in range(int(d['N'])):
                    dis.append('N')
                for i in range(int(d['P'])):
                    dis.append('P')
                for i in range(int(d['C'])):
                    dis.append('C')
                for i in range(int(d['D'])):
                    dis.append('D')
                for i in range(int(d['HD'])):
                    dis.append('HD')
                q2 = len(dis)//2
                q1 = q2//2
                q3 = q1+q2
                print('\nGrade distribution for ', search_c)
                print(d)
                print('25th percentile: ', dis[q1])
                print('50th percentile: ', dis[q2])
                print('75th percentile: ', dis[q3])         
        elif option == 10:
            #quit to login menu
            flag = False 
        else:
            print('Invalid option')


if __name__ == "__main__" :
    pass
    semester_list = []
    student_list = []
    program_list = []
    course_list = []
    
    with open('student.csv') as student_file:
        student_reader =csv.reader(student_file)
        for row in student_reader:
            name = row[0]
            student_id = row[1]
            dob = row[2]
            program_code = row[3]
            status = row[4]
            mydict = {}
            for result in row[5].split(' '):
                id, grade = result.split(':')
                mydict[id] = grade
            academic_history = mydict
            current_enrollments = row[6].split(' ')
            study_plan = row[7].split(' ')
            student = Student(name, student_id, dob, program_code, status ,academic_history, current_enrollments, study_plan)
            student_list.append(student)

    with open('program.csv') as program_file:
        program_reader =csv.reader(program_file)
        for row in program_reader:
            program_code = row[0]
            credit = row[1]
            core_courses = row[2].split(' ')
            elective_courses = row[3].split(' ')
            program = Program(program_code, credit, core_courses, elective_courses)
            program_list.append(program)

    with open('semester.csv') as semester_file:
        semester_reader =csv.reader(semester_file)
        for row in semester_reader:
            semester = row[0]
            course_offerings = row[1].split(' ')
            semester = Semester(semester, course_offerings)
            semester_list.append(semester)
    
    with open('course.csv') as course_file:
        course_reader =csv.reader(course_file)
        for row in course_reader:
            course_code = row[0]
            title = row[1]
            credit = row[2]
            prerequisite = row[3]
            available_semester = row[4].split('|')
            course = Course(course_code, title, credit, prerequisite, available_semester)
            course_list.append(course)


    #login
    flag = True
    while flag:
        print('\n\nWelcom to School Enrollment System')
        print('1. Student login')
        print('2. System login')
        print('3. Exit Program')

        try:
            option = int(input("Please select a number option:"))
        except:
            print('Invalid opion')
        if option == 1:
            studentID = input("Please enter a student ID:").upper()
            student_menu(studentID, student_list, program_list, course_list)
        elif option == 2:
            system_menu(student_list, program_list, course_list, semester_list)
        elif option == 3:
            print('Are you sure you want to exit the program?')
            print('1. Yes')
            print('2. No')
            try:
                option = int(input("Please select a number option:"))
            except:
                print('Invalid option')
            if option == 1:
                flag = False
            elif option == 2:
                pass
            else:
                print('Invalid option')
        else:
            print('Invalid option')


    #menu


