def multiply_list(nums: list[int], multiplier: int = 2) -> list[int]:
    return [num * multiplier for num in nums]

lambda_multiply = lambda nums, multiplier=2: list(map(lambda x: x * multiplier, nums))

input_nums = input("Введите список чисел через пробел: ").split()
numbers = [int(x) for x in input_nums]
    
multiplier_input = input("Введите множитель (по умолчанию 2): ")
multiplier = int(multiplier_input) if multiplier_input else 2
    
print("Результат (функция):", multiply_list(numbers, multiplier))
print("Результат (лямбда-функция):", lambda_multiply(numbers, multiplier))
