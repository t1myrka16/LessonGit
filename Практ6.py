import math

nums = []

for i in range(10):
    try:
        x = int(input(f"nums[{i}] = "))
        nums.append(x)
    except ValueError:
        print("Ошибка: неправильно набранное число")

# 1
print("Список:", *(nums))

# 2
pos_sum = sum(x for x in nums if x > 0)
print("Сумма положительных:", pos_sum if pos_sum > 0 else 0)

# 3
print("Количество чётных:", len([x for x in nums if x % 2 == 0]))

# 4
mv = max(nums)
print("Максимум:", mv, "Индекс:", nums.index(mv))

# 5
for i in range(len(nums) - 1, -1, -1):
    print(nums[i], end=" ")
print("Реверс:", )

# 6
nums_6 = [x for x in nums if x >= 0]
print("Список без отрицательных чисел:", nums_6)

# 7
print("Сдвиг вправо:", [nums[-1]] + nums[:-1] if nums else [])

# 8
temp = [x for x in nums if x != 0]
res8 = "YES" if all((temp[i] > 0) != (temp[i+1] > 0) for i in range(len(temp)-1)) and len(temp) > 1 else "NO"
print(res8)

# 9
avg = sum(nums) / len(nums)
print("Ближайшее к среднему:", min(nums, key=lambda x: abs(x - avg)))

# 10
print("Сортировка по последней цифре:", sorted(nums, key=lambda x: abs(x) % 10))

# 11
unq = []
for x in nums:
    if x not in unq: unq.append(x)
print("Уникальные элементы:", unq)

# 12
for i in range(len(nums) - 1):
    if nums[i] * nums[i+1] > 0:
        print("Соседи одного знака:", f"i:{i},{i+1} v:{nums[i]},{nums[i+1]}")

# 13
lm = []
for i in range(len(nums)):
    if (i == 0 or nums[i] < nums[i-1]) and (i == len(nums)-1 or nums[i] < nums[i+1]):
        lm.append(nums[i])
print("Локальные минимумы:", lm)

# 14
ml = cl = 1
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        cl += 1
        ml = max(ml, cl)
    else:
        cl = 1
print("Длиннейшая возрастающая подпоследовательность:", ml)

# 15
def qs(a, k):
    p = a[len(a)//2]
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    h = [x for x in a if x > p]
    if k < len(l): return qs(l, k)
    if k < len(l) + len(m): return m[0]
    return qs(h, k - len(l) - len(m))

print("Медиана без сортировки:" )
print(qs(nums, len(nums)//2))