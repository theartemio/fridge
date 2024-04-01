from decimal import Decimal
from datetime import datetime, date, timedelta

goods = {}

def add(items, title, amount, expiration_date=None):
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date() if expiration_date else None
    if title not in items:
        items[title] = [{'amount': Decimal(amount), 'expiration_date': expiration_date}]
    else:
        list.append(items[title], {'amount': Decimal(amount), 'expiration_date': expiration_date})

def add_by_note(items, note):
    note = str.split(note, ' ')
    expiration_date = note.pop() if '-' in note[-1] else None
    amount = note.pop()
    title = str.join(' ', note)
    add(items, title, amount, expiration_date)
    
def find(items, needle):
    results = [item for item in items.keys() if needle.lower() in item.lower()]
    return results

def amount(items, needle):
    found_items = find(items, needle) # Ищем нужные элементы по строке
    quantity = Decimal(0)
    for found_item in found_items: # Просматриваем все найденные продукты, подходящие по строке поиска
        amounts = [batch['amount'] for batch in items[found_item]] # Список количеств для продукта в данной итерации
        quantity += sum(amounts)
    return quantity    

def expire(items, in_advance_days=0):
    desired_date = date.today() + timedelta(days=in_advance_days) # Прибавляем дни
    expired_list = []
    for item in items.keys():
        amount = 0
        for batch in items[item]:
            if batch['expiration_date'] and batch['expiration_date'] <= desired_date:
                amount += batch['amount']
        if amount:
            expired_list.append((item, amount))
            
    return expired_list        
