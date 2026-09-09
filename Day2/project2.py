print("-" * 30)
print("Welcome to the tip Calculator")
print("-" * 30)

#type casted the input so that it can prevent the  user from inputing wrong types
total= float(input("Whats the total amount of bill in Ksh:\n"))
tip = int(input("How much tip would you like to give in %:\n"))
people_no = int(input("How many people would be splitting this bill?:\n"))

# the calculation behind the final generated splitted bill
split_bill = round((total + (total * tip/100))/people_no, 2)

# used the f-string to combine the split_bill variable and the string  
print (f"The bill for each is: Ksh {split_bill}")