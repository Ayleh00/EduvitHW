def plus(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Нужны числа")
    return x + y

def minus(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Нужны числа")
    return x - y

def multiply(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Нужны числа")
    return x * y

def divide(x, y, mode):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Нужны числа")
    if y == 0:
        raise ZeroDivisionError("Нельзя делить на 0")
    if mode == "1":
        return x / y
    elif mode == "2":
        return x // y
    elif mode == "3":
        return x % y
    else:
        raise ValueError("Режим деления: 1, 2 или 3")

def power(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Нужны числа")
    if x == 0 and y < 0:
        raise ValueError("0 нельзя возводить в отрицательную степень")
    return x ** y

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Нужно целое число")
    if n < 0:
        raise ValueError("Факториал только для положительных")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def average(nums):
    return sum(nums) / len(nums)

def show_menu():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Среднее арифметическое")
    print("--------------------")

commands = {
    1: plus,
    2: minus,
    3: multiply,
    4: divide,
    5: power,
    6: factorial,
    7: average
}
    
show_menu()
    
while True:
    try:
        cmd = input("Операция: ")
        if cmd.lower() in ('exit', 'quit', 'выход'):
            print("Калькулятор закрыт")
            break

        cmd = int(cmd)
        if cmd not in commands:
            print("Нет такой операции!")
            continue
            
        if cmd in (1, 2, 3, 5):
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            res = commands[cmd](a, b)
        elif cmd == 4:
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            t = input("Тип деления (1/2/3): ")
            res = commands[cmd](a, b, t)
        elif cmd == 6:
            n = int(input("Число: "))
            res = commands[cmd](n)
        elif cmd == 7:
            nums = list(map(float, input("Числа через пробел: ").split()))
            res = commands[cmd](nums)
            
        print(f">>> {res}")
        print("--------------------")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
    except ZeroDivisionError as e:
        print(f"Мат Ошибка: {e}")
    except Exception as e:
        print(f"Unexp Ошибка: {e}")
