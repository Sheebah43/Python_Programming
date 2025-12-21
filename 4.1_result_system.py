# Maintaining a student result system with sorting and searching
# Add student (10,..., marks)
# Search by 10
# Sort by marks
# Count fail
# Find top 5
# Student Result System

class student_result_system:
    def __init__(self):
        self.students = [] #list of dictionaries

    def add_student(self, roll_no, name, marks):
        self.students.append({"roll_no": roll_no, "name": name, "marks": marks})

    def sort_by_marks(self):
        return sorted(self.students, key=lambda x: x["marks"], reverse=True)

    def count_fail(self, pass_mark=40):
        return sum(1 for student in self.students if student["marks"] < pass_mark)

    def top_n_students(self, n=3):
        return self.sort_by_marks()[:n]


if __name__ == "__main__":
    system = student_result_system()

    system.add_student(10, "abc", 32)
    system.add_student(11, "def", 57)
    system.add_student(12, "ghi", 87)
    system.add_student(13, "jkl", 5)
    system.add_student(14, "mno", 24)
    system.add_student(15, "pqr", 90)


    print("\nSorted by Marks:\n")
    for s in system.sort_by_marks():
        print(s)

    print("Fail Count:", system.count_fail())

    print("\nTop 3 Students:\n")
    for s in system.top_n_students(3):
        print(s)
