
string = input("Введите строку: ")

string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")