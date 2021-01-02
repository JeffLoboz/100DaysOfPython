"""" 
DON'T USE len() or sum() functions. Use for loops.

prints the number of inputs entered
print(len(student_heights))

prints sum of all inputs entered
print(sum(student_heights))

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
"""



student_heights = input("Input a list of student heights in centimeters").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)


# Loop through each height in list
total_height = 0
for height in student_heights:
  #total_height = total_height + height
  total_height += height
#print (total_height)

# Loop and add 1 each time loop runs
number_of_students = 0
for students in student_heights:
  number_of_students += 1
#print(number_of_students)

average_height = round(total_height / number_of_students)

print(f"The average height of the class is {average_height}cm")
