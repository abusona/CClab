def calculate_cgpa(grades, credits):
    total_grade_points = sum(g * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    if total_credits == 0:
        return 0
    return total_grade_points / total_credits

def cgpa_calculator():
    print("CGPA Calculator")
    
    num_subjects = int(input("Enter number of subjects: "))
    
    grades = []
    credits = []
    
    for i in range(num_subjects):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        credit = float(input(f"Enter credit hours for subject {i + 1}: "))
        grades.append(grade)
        credits.append(credit)
    
    cgpa = calculate_cgpa(grades, credits)
    print(f"Your CGPA is: {cgpa:.2f}")

cgpa_calculator()
