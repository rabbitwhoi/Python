def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    
    return f"Вы прослушали {len(listened)} песен. Минут потрачено: {int(sum(listened) / 60)}"
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))