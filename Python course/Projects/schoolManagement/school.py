class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.teachers={} #{"sub_name":Teacher object}
        self.classrooms={} #{"class " :classroom object}

    def add_classroom(self,classroom):#classroom object
        self.classrooms[classroom.name]=classroom
    
    def add_teacher(self,sunject,teacher):
        self.teachers[sunject]=teacher
    
    def student_addmission(self,student):
        classname=student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A'
        elif marks>=60 and marks<70:
            return 'A-'
        elif marks>=50 and marks<60:
            return 'B'
        elif marks>=40 and marks<50:
            return 'C'
        elif marks>=33 and marks<40:
            return 'D'
        else:
            return 'F'
        
    
    @staticmethod
    def grade_to_value(grade):
        grade_map ={
            'A+' : 5.00,
            'A'  : 4.00,
            'A-' : 3.50,
            'B'  : 3.00,
            'C'  : 2.00,
            'D'  : 1.00,
            'F'  : 0.00
         }
        
        return grade_map[grade]
    
    @staticmethod

    def value_to_grade(value):
        if value>=4.5 and value<=5.00:
            return 'A+'
        elif value >= 3.5 and value<4.50:
            return 'A'
        elif value>=3.00 and value<3.50:
            return 'A-'
        elif value>=2.5 and value<3.00:
            return 'B'
        elif value>=2.00 and value<=2.50:
            return 'C'
        elif value>=1.00 and value<2.00:
            return 'D'
        else:
            return 'F'
    def __repr__(self) -> str:
        #All classroom
        for key,value in self.classrooms.items():
            print(key)
        #All Students
        print("All student")
        result=''

        for key,value in self.classrooms.item():#shob classroom a gelam
            result += f'--{key.upper()} Classroom Students\n'

            for student in value.students:
                result+=f'{student.name}\n'
        print(result)

        #All Subject

        subject=''
        for key,value in self.classrooms.item():#shob classroom a gelam
            subject += f'--{key.upper()} Classroom Students\n'

            for sub in value.subjects:
                subject+=f'{sub.name}\n'
        print(subject)

        #All Student Results
        print("Student Result")

        for key,value in self.classrooms.items():
            for student in self.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                
                print(student.calculate_final_grade())

            return ''
        

    

