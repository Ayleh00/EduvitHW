import string

def check_palindrome(s: str) -> bool:
    normalized = s.lower().replace(" ", "")
    cleaned = ''.join([ch for ch in normalized if ch not in string.punctuation])
    return cleaned == cleaned[::-1]


assert check_mirror_string("А роза упала на лапу Азора") == True
assert check_mirror_string("Аргентина манит негра!") == True 
assert check_mirror_string("987656789") == True
assert check_mirror_string("Я иду с мечем судия") == True
assert check_mirror_string("Не палиндром") == False