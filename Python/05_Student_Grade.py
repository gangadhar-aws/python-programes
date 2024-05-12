

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
  "Hari" : 30,
  "Gangadhar" : 88,
  "Siddharth" : 98,
  "Keerthi " : 97,
}

student_grades = {}
for item in student_scores:
    if student_scores[item] > 80:
        student_grades[item] = "Outstanding A+"
    elif student_scores[item] > 60:
        student_grades[item] = "First Class A"
    elif student_scores[item] > 45:
        student_grades[item] = "Second Class B"
    elif student_scores[item] > 35:
        student_grades[item] = "Third Class C"
    else:
        student_grades[item] = "Failed.."

for item in student_grades:
    print(item,"=",student_grades[item])

