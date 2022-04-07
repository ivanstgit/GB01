# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
# список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()

history_nums = set()
non_unique_nums = {num for num in src if num in history_nums or history_nums.add(num)}
uniq_nums = history_nums - non_unique_nums

print(perf_counter() - start)

result = [el for el in src if el in uniq_nums]
print(result)

#
# src = [el % 2 for el in range(10**8)]
# src.extend([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
#
# uniq_nums = set()
# history_nums = set()
# for num in src:
#     if num not in history_nums:
#         uniq_nums.add(num)
#     else:
#         uniq_nums.discard(num)
#     history_nums.add(num)
#
# print(perf_counter() - start)
#
# result = [el for el in src if el in uniq_nums]
# print(result)
#
#
# uniq_nums.clear()
# history_nums.clear()
# start = perf_counter()
# history_nums = set()
# non_unique_nums = set()
# uniq_nums = set()
# for num in src:
#     if num in history_nums:
#         non_unique_nums.add(num)
#     history_nums.add(num)
# uniq_nums = history_nums - non_unique_nums
#
# print(perf_counter() - start)
# result = [el for el in src if el in uniq_nums]
# print(result)
#
# uniq_nums.clear()
# history_nums.clear()
# non_unique_nums.clear()
# start = perf_counter()
# history_nums = set()
# non_unique_nums = set()
# uniq_nums = set()
#
# non_unique_nums = {num for num in src if num in history_nums or history_nums.add(num)}
# uniq_nums = history_nums - non_unique_nums
#
# print(perf_counter() - start)
# result = [el for el in src if el in uniq_nums]
# print(result)
