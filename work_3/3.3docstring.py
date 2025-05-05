from typing import List

def function_name(search: str, status: bool, *args: int | str, **kwargs: str) -> List[int] | str:
    """
    Функция function_name обрабатывает аргументы в зависимости от параметров search и status.

    Аргументы:
        search: Обрабатывает "args" или "kwargs".
        status: Если True, добавляет числа из args в список и возвращает этот список, если False, то возвращает строку из args.
        *args: Позиционные аргументы (целые числа или строки).
        **kwargs: Именованные аргументы (строки).

    Возвращает:
        - При search="args" и status=True: список целых чисел из args.
        - При search="args" и status=False: строку с объединением args.
        - При search="kwargs": строку в формате "Key: k, Value: v;".

    Ошибка:
        ValueError: Если search не "args" или не "kwargs".
    """
    if search == "args":
        if status:
            return [i for i in args if isinstance(i, int)]
        else:
            return ''.join(str(i) for i in args)
    elif search == "kwargs":
        return '; '.join(f"Key: {k}, Value: {v};" for k, v in kwargs.items())
    else:
        raise ValueError("Error for search")ffff
