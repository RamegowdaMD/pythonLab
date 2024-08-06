import random

numbers = []

for i in range(20):
    numbers.append(random.randint(1, 10000))

print("Random numbers: ", numbers)

print("Odd numbers of length 2 and 4: ", end="")
for number in numbers:
    if number % 2 != 0 and len(str(number)) in [2,4]:
        print(number, end=" ")
