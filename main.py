import tools as t
import random

# ex 1
ar = [random.randint(0, 10000) for _ in range(5000)]

# insert sort
for top in range(1, len(ar)):
    i = top
    while i > 0 and ar[i - 1] > ar[i]:
        ar[i], ar[i - 1] = ar[i - 1], ar[i]
        i -= 1

# show array
for x in range(len(ar)):
    print(f'{x} => {ar[x]}', end='\t' if (x + 1) % 5 != 0 else '\n')

index = 4987
print('Linear: ', t.linear_search(ar, ar[index]))
print('Binary: ', t.binary_search(ar, ar[index]))


# ex 2
print()
print('Direct: ', t.direct_search(t.main_string, t.substring))
print('KMP: ', t.kmp_search(t.main_string, t.substring))

# ex 3
print()
t.bm_search(t.main_string, t.substring)

