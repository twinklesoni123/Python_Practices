# Program to find the smallest of n numbers

n = int(input("Enter how many numbers: "))

smallest = None

for i in range(n):
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num

print("Smallest number is:", smallest)