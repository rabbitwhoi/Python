def reverse_number(n):
    reversed_str = str(n)[::-1]
    if reversed_str == str(n):
        print(f"{n} полидром")
    return int(reversed_str)

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_numbers.append(reverse_number(num))
    return reversed_numbers

numbers = [123, 456, 789, 121, 343, 555]
result = process_numbers(numbers)
print("Reversed numbers:", result)

