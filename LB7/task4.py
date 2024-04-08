
number = int(input("Введите целое число больше 1: "))

for i in range(2, int(number ** 0.5) + 1):
    if (number % i) == 0:
        print(f"{number} не является простым числом.")
        break
    else:
        print(f"{number} является простым числом.")