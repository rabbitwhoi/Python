
string = input("Введите строку: ")


string = string.lower()

vowels_count = 0
consonants_count = 0


vowels = "ауоыиэяюёе"

for char in string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print("Количество гласных букв:", vowels_count)
print("Количество согласных букв:", consonants_count)
