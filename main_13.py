# Program to check palindrome number

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")