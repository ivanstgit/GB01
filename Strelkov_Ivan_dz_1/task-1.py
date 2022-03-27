# 1. Реализовать вывод информации о промежутке времени в
# зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# init
duration_list = []
duration_list_max = 1
duration = 1

# user input
while duration > 0 and len(duration_list) < duration_list_max:
    duration = int(input("Type duration (0 to calculate): "))
    if duration > 0:
        duration_list.append(duration)
    elif duration < 0:
        print('Отрицательное число!')

# calc & print
for duration in duration_list:
    result_string = str(duration) + '= '
    duration_seconds = duration % 60
    duration = duration // 60
    duration_minutes = duration % 60
    duration = duration // 60
    duration_hours = duration % 24
    duration_days = duration // 24

    if duration_days > 0:
        result_string += str(duration_days) + ' дн '
    if duration_hours > 0:
        result_string += str(duration_hours) + ' час '
    if duration_minutes > 0:
        result_string += str(duration_minutes) + ' мин '
    if duration_seconds > 0:
        result_string += str(duration_seconds) + ' сек '
    print(result_string)
