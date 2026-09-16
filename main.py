import datetime
from decimal import Decimal

# Холодильник пуст:
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
           ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
} 

def add(items, title, amount, expiration_date=None):

     if isinstance(expiration_date, str):
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()

    # Если продукта ещё нет, создаём для него пустой список партий.
     if title not in items:
        items[title] = []

    # Добавляем новую партию продукта.
     items[title].append({'amount': amount, 'expiration_date': expiration_date,})

#print(goods.keys())
#print(goods.items())


def add_by_note(items, note):
    words = note.split()
     # Проверяем, что строка не пустая.
    if not words:
        return False

    # Последняя часть должна быть датой.
    try:
        expiration_date = datetime.datetime.strptime(
            words[-1], '%Y-%m-%d'
        ).date()
    except ValueError:
        return False

    # До даты должны находиться название и количество.
    if len(words) < 3:
        return False

    try:
        # Количество — предпоследняя часть строки.
        amount = Decimal(words[-2])
    except Exception:
        return False

    # Все части до количества и даты — название продукта.
    title = ' '.join(words[:-2])

    # Передаём items первым аргументом.
    print(title, amount, expiration_date)
    #add(goods, 'Яйца', Decimal('10'), '2023-9-30')
    add(items, title, amount, expiration_date)
    return True
    
#print(goods.keys())

goods = {}

result = add_by_note(goods, 'Яйца 4 2023-07-15')

print(result)
print(goods)
#Оставшуюся часть строки объединить, чтобы получить название продукта: 
# если название состояло из нескольких слов — функция str.split разобьёт его на части.
#Вызвать функцию add(), передав в неё получившиеся данные — название, количество и срок хранения.