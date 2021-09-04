#Data Types
#Strings
#Integers
#Can use underscores to make the whole number more readable
print(123_456_789)
#Float
#Boolean

#Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(5 % 3)
print(10 ** 2)

#Order of operations
#PEMDAS -> Parentheses Exponents Multiply Divide Addition Subtraction
print(3 * 3 + 3 / 3 - 3)

height = input("What is your height in m: ")
weight = input("What is your weight in kg: ")

bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print("Your Body Mass Index is: " + str(bmi_as_int))

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#FAQ: How to round to 2 decimal places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Each person should pay: ${final_amount}")


