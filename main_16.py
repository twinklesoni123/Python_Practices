# Program to find the largest of n numbers

n = int(input("Enter how many numbers: "))

largest = None

for i in range(n):
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num

print("Largest number is:", largest)