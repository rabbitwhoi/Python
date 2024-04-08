
number1 = int(input("Введите 1 число: "))
number2 = int(input("Введите 2 число: "))
number3 = int(input("Введите 3 число: "))

if number1 > number2 and number1 > number3:
    print("Самое большое число: ", number1)
elif number2 > number1 and number2 > number3:
    print("Самое большое число: ", number2)
elif number3 > number1 and number3 > number2:
    print("Самое большое число: ", number3)