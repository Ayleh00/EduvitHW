squares = [x**2 for x in range(1, 11)]
print("1.", squares)

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_numbers = = {day: i for i, day in enumerate(days, start=1)}
print("\n2.", day_numbers)

libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
unique_tags = {lib.lower() for lib in libs}
print("\n3.", unique_tags)

numbers = [1, 3, 4, 87, 98, 15, 7, 4]
numbers_da = [num for num in numbers if num % 2 == 0]
print("\n4.", numbers_da)

import math
factorials = {i: factorial(i) for i in range(1, 6)}
print("\n5.", factorials)