# using for loops and built-in python functions eg sum , max , min 

students = [20,30,40,70,90,10,45,78]

print(sum(students))


# using the for loop to sum the items in the list
sum = 0
for student in students:
    sum+= student
print(f"the sum is {sum}")

# using the max built-in funtion
print(max(students))

# using the for loop to go through the whole list and return the max output
max_score = 0
for score in students:
    if score > max_score:
       max_score = score
print(f"{max_score}: Is the maximum score in the list")

# output the minimum score using the built-in fuction min and a for loop with an if statement
# print(min(students))


min_score = students[0] #we cannot set this min_variable to zero because when we start going through the loop
for score in students:
    if score < min_score:
        min_score = score
print(f"{min_score}: Is the minumum score in the list")
