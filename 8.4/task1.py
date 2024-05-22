# Подключите библиотеку random и дайте ей краткое имя
from random import choice

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    answer = choice(answers)
    return answer

print(how_are_you())