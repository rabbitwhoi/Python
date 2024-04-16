import random 


s = ["Артем", "Людвиг", "Амстердам", "Александр", "Алексей", "Париж", "Тигр", "Красные волосы", "Плавание", "Врач", "Токио", "Елена", "Лондон", "Собака", 
     "Серфинг", "Программист", "Москва", "Максим", "Нью-Йорк", "Лев", "Катание на велосипеде", "Учитель", "Берлин", "Юлия", "Барселона", 
     "Кот", "Пение", "Актер", "Рим", "Джон", "Сан-Франциско", "Зебра", "Фотография", "Инженер", "Ирина", "Чикаго", "Попугай", "Блондинка", "Гитара", "Пилот", "Мадрид", 
     "Сергей", "Дубай", "Слон", "Рисование", "Юрист", "Милан", "Виктория", "Сидней", "Лиса", "Йога", "Архитектор", "Амстердам", "Вадим", "Канкун", "Панда", "Скейтбординг", 
     "Фотограф", "Венеция", "Анна", "Мумбаи", "Кролик", "Бег", "Дизайнер", "Каир", "Марина", "Торонто", "Обезьяна", "Бальные танцы", "Бухгалтер", "Лас-Вегас", "Екатерина", 
     "Шанхай", "Гепард", "Лыжный спорт", "Биолог", "Стамбул", "Дмитрий", "Хельсинки", "Жираф", "Танцы живота", "Стоматолог", "Афины", "Ева"]

def catch_ball():
    if random.random() <= 0.3:
        return True
    else:
        return False
    
def quest1():
    global quest1
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest1 = input("Вопрос: Ваше имя? ")
        print("Ответ: ", quest1)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest1 = random.choice(s)
        print("Ваше имя?")
        print("Ответ: ", quest1)
        print(" ")
def quest2():
    global quest2
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Как зовут компьютер?")
        quest2 = random.choice(s)
        print("Ответ: ", quest2)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest2 = input("Как зовут компьютер?: ")
        print("Ответ: ", quest2)
        print(" ")
def quest3():
    global quest3
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest3 = input("Вопрос: Из какго вы города? ")
        print("Ответ: ", quest3)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest3 = random.choice(s)
        print("Из какго вы города?")
        print("Ответ: ", quest3)
        print(" ")
def quest4():
    global quest4
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Из какаго города компьютер?")
        quest4 = random.choice(s)
        print("Ответ: ", quest4)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest4 = input("Из какго города компьютер?: ")
        print("Ответ: ", quest4)
        print(" ")
def quest5():
    global quest5
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest5 = input("Вопрос: Какое ваше любимое животное? ")
        print("Ответ: ", quest5)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest5 = random.choice(s)
        print("Какое ваше любимое животное?")
        print("Ответ: ", quest5)
        print(" ")
def quest6():
    global quest6
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Какое любимое животное у компьютера?")
        quest6 = random.choice(s)
        print("Ответ: ", quest6)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest6 = input("Какое любимое животное у компьютера?: ")
        print("Ответ: ", quest6)
        print(" ")
def quest7():
    global quest7
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest7 = input("Вопрос: Ваше хобби? ")
        print("Ответ: ", quest7)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest7 = random.choice(s)
        print("Ваше хобби?")
        print("Ответ: ", quest7)
        print(" ")
def quest8():
    global quest8
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Хобби компьютера?")
        quest8 = random.choice(s)
        print("Ответ: ", quest8)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest8 = input("Хобби компьютера?: ")
        print("Ответ: ", quest8)
        print(" ")


def quest9():
    global quest9
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest9 = input("Вопрос: Профессия? ")
        print("Ответ: ", quest9)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest9 = random.choice(s)
        print("Профессия?")
        print("Ответ: ", quest9)
        print(" ")
def quest10():
    global quest10
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Профессия компьютера?")
        quest10 = random.choice(s)
        print("Ответ: ", quest10)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest10 = input("Профессия компьютера?: ")
        print("Ответ: ", quest10)
        print(" ")

def quest11():
    global quest11
    if catch_ball():
        print("Копьютер бросает мяч: Вы поймали!")
        quest11 = input("Вопрос: Где бы вы хотели побывать? ")
        print("Ответ: ", quest11)
        print(" ")
    else:
        print("Копьютер бросает мяч: Вы не поймали!")
        quest11 = random.choice(s)
        print("Где бы вы хотели побывать?")
        print("Ответ: ", quest11)
        print(" ")
def quest12():
    global quest12
    if catch_ball():
        print("Вы бросаете мяч: Компьютре поймал!")
        print("Вопрос: Где хотел побывать компьютер?")
        quest12 = random.choice(s)
        print("Ответ: ", quest12)
        print(" ")
    else:
        print("Вы бросаете мяч: Компьютре не поймал!")
        quest12 = input("Где хотел побывать компьютер?: ")
        print("Ответ: ", quest12)
        print(" ")


quest1()
quest2()
quest3()
quest4()
quest5()
quest6()
quest7()
quest8()
quest9()
quest10()
quest11()
quest12()

print("Рассказ человека: ")
print("Привет! Меня зовет", quest1, "я из города", quest3, ", мое любимое животное", quest5, ", мое хобби это", quest7, ", я по професси", quest9, ", я бы хотел побывать в", quest11)
print(" ")

print("Рассказ компьютера: ")
print("Привет! Меня зовет", quest2, "я из города", quest4, ", мое любимое животное", quest6, ", мое хобби это", quest8, ", я по професси ", quest10, "я бы хотел побывать в", quest12)