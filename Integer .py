targetValue = int(input("Enter your target value: "))

number1 = int(input("Enter any number from 1 to 9 :"))
number2 = int(input("Enter any number from 1 to 9 :"))
number3 = int(input("Enter any number from 1 to 9 :"))

sum = 0
for count in range(1,4): 
    sum = number1 + number2 + number3
    if sum == targetValue:
        print(number1 ,number2 ,number3)











