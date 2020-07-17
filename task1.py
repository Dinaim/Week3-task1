# Написать генератор списка, который итерируется по функции range от 1 до 100
# и фильтрует по четным числам.
# Пример:
# [1, 2, 3, 4, 5, 6]
# [2, 4, 6]
# Требование:
# Использовать list comprehension


nums = list(range(1, 101))
nums2 = [num for num in nums if num%2 == 0 and num>0]
print(nums2)