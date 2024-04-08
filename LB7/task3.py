
number = int(input("Введите число: "))

factorial = number

for i in range(1, number):
    factorial = factorial * i

print(factorial)