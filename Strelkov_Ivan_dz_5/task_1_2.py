# *1 Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
# *2 (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.

def odd_nums_01(max_num: int):
    """
    Generator odd numbers with yield
    :param max_num:
    :return:
    """
    for num in range(1, max_num + 1):
        if num % 2 == 1:
            yield num


if __name__ == '__main__':
    # gen1 = odd_nums_01(51)
    # for i in range(1, 51):
    #     print(next(gen1))

    max_number = 51
    gen2 = (num for num in range(1, max_number + 1) if num % 2 == 1)
    for i in range(1, 51):
        print(next(gen2))
