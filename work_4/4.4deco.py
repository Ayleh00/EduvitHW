def deco(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Площадь прямоугольника: {result}")
        return result
    return wrapper

@deco
def calculate_area(length, width):
    return length * width

calculate_area(5, 10)