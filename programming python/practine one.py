#For those who are not yet asleep and getting ready tom here's a practice problem. 
# Ask for a number of students, then for each student ask for:
# Name
# 3 subject grades
# Compute the average for each student, print the result, and display who got the highest average.
# I'll give a harder one tomorrow morning If you want.

# Ask for number of students
num_students = int(input("Enter number of students: "))

# Initialize variables to track the highest average
highest_avg = 0
top_student = ""

# Loop through each student
for i in range(num_students):
    print(f"\nStudent {i + 1}:")
    name = input("Enter name: ")
    
    # Get 3 subject grades
    grade1 = float(input("Enter grade for subject 1: "))
    grade2 = float(input("Enter grade for subject 2: "))
    grade3 = float(input("Enter grade for subject 3: "))
    
    # Compute average
    average = (grade1 + grade2 + grade3) / 3
    
    # Print student average
    print(f"{name}'s average is: {average}")
    
    # Check if this student has the highest average
    if average > highest_avg:
        highest_avg = average
        top_student = name

# Display top student
print(f"\nHighest average is {highest_avg}, achieved by {top_student}.")

# Ask if the user wants to repeat
again = input("\nDo you want to run the program again? (yes/no): ")
if again != "yes":
   print("Goodbye!")
   break
