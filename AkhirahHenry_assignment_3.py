student_name = "Akhirah"
current_gpa = 3.5
study_hours = 20
social_points = 47
stress_level = 89

print(f"Welcome, {student_name}!")
print("Your current stats are:")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: B)")

if choice == "A":
    if current_gpa >= 2.5:
        study_hours += 5
        stress_level -= 5
        print("You picked a light load. More time to relax!")
    else:
        study_hours += 2
        print("Light load, but you still need to catch up.")
elif choice == "B":
    study_hours += 10
    stress_level += 10
    print("A standard load, typical but balanced.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 20
        print("Oh...this is gonna be a lot. Good luck!")
    else: 
        print("Heavy load is overwhelming with this current GPA.")
else:
    print("Invalid choice. No changes made.")
