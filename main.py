import datetime
from decimal import Decimal

# Холодильник пуст:
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
} 

def add(items, title, amount, expiration_date=None):
    pass  # Код, который добавляет продукты в словарь goods.
    #имя_словаря[новый_ключ] = значение

    goods['Вода']={'amount(Decimal('10'), '2023-9-30')'}
# Добавляем продукт с названием 'Яйца', количество - 10 шт.
#add(goods, 'Яйца', Decimal('10'), '2023-9-30')

# Словарь goods должен стать таким:

# {
#     'Яйца': [
#         {'amount': Decimal('10'), 'expiration_date': datetime.date(2023, 9, 30)}
#     ]
# }
add(goods, 'Яйца', Decimal('10'), '2023-9-30')

print(goods.keys())
print(goods.items())
