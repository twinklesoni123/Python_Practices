# Program to find sum of odd numbers up to n

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n + 1, 2):
    sum += i

print("Sum of odd numbers up to", n, "is:", sum)