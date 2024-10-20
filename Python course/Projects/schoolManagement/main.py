from school  import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school=School("ABC","Dhaka")

#adding classroom
eight=Classroom("Eight")
nine=Classroom("Nine")
ten=Classroom("Ten")


school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#Adding student
rahim=Student("Rahim",eight)
karim=Student("Karim",nine)
fahim=Student("Fahim",ten)
hamim=Student("Hamim",ten)

school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(fahim)
school.student_addmission(hamim)

#Adding teacher

abul=Teacher("Abul Khan")
babul=Teacher("Babul Khan")
kabul=Teacher("kabul khan")

#Adding subject

bangla=Subject("Bangla",abul)
physics=Subject("Physics",babul)
chemistry=Subject("Chemistry",kabul)
biology=Subject("Biology",kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)
ten.add_subject(bangla)

eight.take_semester_final_exam()

print(school)
