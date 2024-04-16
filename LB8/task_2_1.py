

num = int(input("Введите число: "))

def reverse_number(num):
    string = str(num)
    reversed_string = string[::-1]
    return int(reversed_string)


reversed_num = reverse_number(num)
print("Перевернутое число:", reversed_num)