nu1 = [1, 2, 3]
nu2 = [4, 5, 6]

result = list(map(lambda x, y : x + y, nu1, nu2))

print('Addition of 2 lists...')
print(result)

num = [1, 2, 3, 4, 5, 6]
def sq(n):
    return n * n

square = list(map(sq, num))
print('Square of numbers in new list...')
print(square)