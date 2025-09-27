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

study_options = ["Programming", "Math", "English", "History"]

print("\nChoose a subject to focus on: ")
print(study_options)

subject = input("Your choice: ")

if subject not in study_options:
    print(f"The subject {subject} is not in a part of {study_options}. Lock in!!")

if subject in study_options:
    if subject == "Programming" and current_gpa >= 3.0:
        current_gpa += 0.1
        social_points -= 5
        print("Programming boosted your GPA but no fun for you.")
    elif subject == "Math" or "English":
        current_gpa += 0.05
        print("Nice progression in your core classes.")
    else:
        if not stress_level > 70:
            social_points += 10
            print("History gave you balance and friends, hooray!")
        else:
            print("Too stressed to enjoy studying History.")
else:
    print("Invalid subject choice. Stop wasting time.")

print("\n--- End of Semester Assessment ---")

if type(current_gpa) is float and type(study_hours) is int:
    print("Stats are valid. Proceeding with with final evalutation...")

    if current_gpa >= 3.5:
        if stress_level < 50:
            print("Ending 1: You're an honors grad with a healthy mental state and healthy academic health!")
        else:
            print("Ending 2: You made it out with good grades, that's all that matters. Go treat yourself with some rest or something sweet.")
    elif 2.0 <= current_gpa < 3.5:
        if social_points > 40:
            print("Ending 3: Solid student life and academic balance. Your grades are just like everyone else's!")
        else:
            print("Ending 4: Looks like you were struggling socially, but at least you passed your classes.")
    else:
        print("Ending 5: Academic probation...let's go ahead and rethink about how college works so we can lock in this time.")
else:
    print("Stats are invalid. Simulation Error.")