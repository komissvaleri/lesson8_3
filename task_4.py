# 4. Определить, какое число в массиве встречается чаще всего.

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

print(f'Чаще всего встречается число {r[max_index]}, количесвто повторов - {r.count(max_index)} ')

