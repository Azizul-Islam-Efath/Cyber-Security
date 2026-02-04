# Student Marks Analyzer

marks = [78, 45, 32, 90, 56, 41, 67, 38]

# Total students
total_students = len(marks)

# Average mark
average = sum(marks) / total_students

# Highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Count passed students (marks >= 40)
passed_students = 0
for mark in marks:
    if mark >= 40:
        passed_students += 1

# Display results
print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Number of Passed Students:", passed_students)
