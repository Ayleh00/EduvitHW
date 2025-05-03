from typing import List, Union, Any

def function_name(
    search: str,
    status: bool,
    *args: Union[int, str],
    **kwargs: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search (str): Определяет режим обработки:
            - "args" - обработка позиционных аргументов
            - "kwargs" - обработка именованных аргументов
        status (bool): Флаг, определяющий способ обработки (только для search="args")
        *args (Union[int, str]): Позиционные аргументы (целые числа или строки)
        **kwargs (Any): Именованные аргументы произвольного типа

    Возвращает:
        Union[List[int], str]:
            - Если search="args" и status=True: список целых чисел из args
            - Если search="args" и status=False: строку с конкатенацией всех args
            - Если search="kwargs": строку с описанием всех пар ключ-значение

    Исключения:
        ValueError: Если параметр search имеет недопустимое значение

    Примеры использования:
        >>> function_name("args", True, 1, 2, "three")
        [1, 2]
        >>> function_name("args", False, 1, 2, "three")
        "123three"
        >>> function_name("kwargs", False, name="John", age=25)
        "Key: name, Value: John; Key: age, Value: 25; "
    """
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            return ''.join(str(i) for i in args)
    elif search == "kwargs":
        return '; '.join(f"Key: {k}, Value: {v}" for k, v in kwargs.items()) + ('; ' if kwargs else '')
    else:
        raise ValueError("Invalid search parameter. Expected 'args' or 'kwargs'")