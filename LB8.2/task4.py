DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        frirnds = DATABASE.keys()
        frirnds_string = ", ".join(frirnds)
        return 'Твои друзья: ' + frirnds_string

    elif query == 'Где все мои друзья?':
        geo = set(DATABASE.values())
        geo_string = ", ".join(geo)
        return 'Твои друзья в городах: ' + geo_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))