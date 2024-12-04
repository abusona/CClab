def calculate_cgpa():
    
    num_subjects = int(input("Enter the number of subjects: "))
    
    grade_points = []
    
    
    for i in range(num_subjects):
        grade = float(input(f"Enter the grade point for subject {i+1}: "))
        grade_points.append(grade)
    
   
    cgpa = sum(grade_points) / num_subjects
    return cgpa


cgpa = calculate_cgpa()
print(f"Your CGPA is: {cgpa:.2f}")
