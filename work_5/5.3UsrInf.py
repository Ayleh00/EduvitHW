import random
import json
import string

def fake_name(): #Не работает Faker, заменил своей функцией
    first_names = ["Олег", "Игорь", "Анна", "Елена", "Дмитрий", "Светлана", "Алексей", "Мария"]
    last_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Попов", "Новиков"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def fake_email(name=None):
    domains = ["mail.ru", "yandex.ru", "gmail.com", "bk.ru"]
    if not name:
        name = "user" + str(random.randint(1000, 9999))
    email_name = name.lower().replace(" ", "") + str(random.randint(10, 99))
    return f"{email_name}@{random.choice(domains)}"

password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

age = random.randint(1,100)

data = {
    "name": fake_name(),
    "age": age,
    "email": fake_email(),
    "password": password
    }
json_string = json.dumps(data)

with open('user.json', 'w') as f:
    json.dump(data, f)

with open('user.json') as f:
    print(json.load(f))
