def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


# Input
n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculation
average = calculate_average(marks)
grade = assign_grade(average)

# Output
print("Average Marks:", average)
print("Grade:", grade)

