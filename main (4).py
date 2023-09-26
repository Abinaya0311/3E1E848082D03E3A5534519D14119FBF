class Student:
  
  def __init__(self, name,rool_number, cgpa):
    self.name = name
    self.rool_number = rool_number
    self.cgpa = cgpa


def sort_students(student_list):  
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, 
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:
students = [
   Student("abi", "A123", 7.8),
   Student("abinaya", "A124", 8.9),
   Student("abi", "A125", 9.1),
   Student("abinaya", "A126", 9.9),
]


sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                             student.rool_number,
                                                     student.cgpa))