"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится
   одновременно как в первом списке, так и во втором.
"""


lst_ = [1, 2, 3, 4, 5, 6, 7]
lst_1 = [1, 2, 2, 3]
lst_.extend(lst_1)
print(len(set(lst_)))
