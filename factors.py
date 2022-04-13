number = input("Please enter a positive integer: ")
integer = int(number)
print ("The factors of " + number + " are:")
for i in range (1, integer + 1):
    if integer % i == 0:
        print(i)