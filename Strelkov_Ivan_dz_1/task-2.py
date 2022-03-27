# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

cube_list = []

for i in range(1, 1001):
    if i % 2 == 1:
        cube_list.append(i**3)

sum_7 = 0
for value in cube_list:
    frac_val = value
    sum_digits = 0
    while frac_val > 0:
        sum_digits += frac_val % 10
        frac_val = frac_val // 10
    if sum_digits % 7 == 0:
        sum_7 += value
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7: {sum_7}')

sum_add17_7 = 0
for i in range(len(cube_list)):
    cube_list[i] += 17
for value in cube_list:
    frac_val = value
    sum_digits = 0
    while frac_val > 0:
        sum_digits += frac_val % 10
        frac_val = frac_val // 10
    if sum_digits % 7 == 0:
        sum_add17_7 += value
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7 для +17: {sum_add17_7}')

# Решить задачу под пунктом b, не создавая новый список
cube_list.clear()

for i in range(1, 1001):
    if i % 2 == 1:
        cube_list.append(i**3)

sum_7 = 0
sum_add17_7 = 0
for value in cube_list:
    frac_val = value
    sum_digits = 0
    while frac_val > 0:
        sum_digits += frac_val % 10
        frac_val = frac_val // 10
    if sum_digits % 7 == 0:
        sum_7 += value

    new_value = value + 17
    frac_val = new_value
    sum_digits = 0
    while frac_val > 0:
        sum_digits += frac_val % 10
        frac_val = frac_val // 10
    if sum_digits % 7 == 0:
        sum_add17_7 += new_value
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7: {sum_7}; для +17: {sum_add17_7}')
