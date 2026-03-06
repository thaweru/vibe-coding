# Get student details
name = input("Enter student's name: ")

# Get marks for 3 subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (mark1 + mark2 + mark3) / 3

# Determine result and display output
result = "Pass" if average >= 40 else "Fail"

print(f"\nStudent: {name}")
print(f"Average Mark: {average:.2f}")
print(f"Result: {result}")
