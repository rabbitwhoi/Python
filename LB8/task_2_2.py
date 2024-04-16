

num = int(input("Введите число: "))

def is_polindrom(num):
    s = str(num)
    if s == s[::-1]:
        return True
    else:
        return False
    
if is_polindrom(num):
    print('Число полиндром')
else:
    print("Число не полиндром")

