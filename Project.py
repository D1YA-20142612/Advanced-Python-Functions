n = int(input("Enter a number: "))

odd_numbers_under = [x for x in range(n) if x % 2 != 0]

odd_numbers_list = [2 * x + 1 for x in range(n)]

print("Odd numbers under input:", odd_numbers_under)
print("Another list of odd numbers:", odd_numbers_list)



fruits = ["apple", "banana", "cherry", "mango", "orange"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("New list of updated values:", updated_fruits)