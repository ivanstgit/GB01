# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [elem for elem, prev in zip(src[1:], src) if elem > prev]

print(result)


# from time import perf_counter
# result.clear()
# start = perf_counter()
# gen1 = (elem for elem in src)
# dummy = next(gen1)
# gen2 = (elem for elem in src)
# result = [elem for elem in gen1 if elem > next(gen2)]
# print(perf_counter() - start)
# print(result)
# zip & slice are more effective
