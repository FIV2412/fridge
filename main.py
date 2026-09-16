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

#print(result)
#print(goods)

def find(items, needle):
    result = []
    needle = needle.lower()

    for title in items:
        if needle in title.lower():
            result.append(title)

    return result


def get_amount(items, needle):
    total = Decimal('0')

    for title in find(items, needle):
        for batch in items[title]:
            total += batch['amount']

    return total


def get_expired(items, in_advance_days=0):
    result = []

    today = datetime.date.today()
    expiration_limit = today + datetime.timedelta(
        days=in_advance_days
    )

    for title in items:
        total_amount = Decimal('0')

        for batch in items[title]:
            expiration_date = batch['expiration_date']

            if (
                expiration_date is not None
                and expiration_date <= expiration_limit
            ):
                total_amount += batch['amount']

        if total_amount > 0:
            result.append((title, total_amount))

    return result