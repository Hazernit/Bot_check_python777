import sqlite3

def add_to_database_customer(name, chat_id, subject, deadline, price, order_text, file_path='', file_type=''):
    db = sqlite3.connect(r'C:\Users\dimak\Downloads\Gmail\dima_db.db')
    cursor = db.cursor()
    cursor.execute('insert into customers_table ("name", "chat_id", "subject", "deadline", "price", "order_text", '
                   '"file_path", "file_type") values (?,?,?,?,?,?,?,?)',
                   (name, chat_id, subject, deadline, price, order_text, file_path, file_type))
    db.commit()

def add_to_database_implementer(name, chat_id):
    db = sqlite3.connect(r'C:\Users\dimak\Downloads\Gmail\dima_db.db')
    cursor = db.cursor()
    try:
        cursor.execute('insert into executors_table ("name", "chat_id", "count_of_orders") values(?, ?, ?)',(name, chat_id, 0))
    except:
        pass
    db.commit()

def get_orders_by_price(subject, price):
    db = sqlite3.connect(r'C:\Users\dimak\Downloads\Gmail\dima_db.db')
    cursor = db.cursor()
    answer = ''
    number = []
    a = cursor.execute('select * from customers_table where subject = ? and price >= ? ', (subject, price)).fetchall()
    b = cursor.execute('select chat_id from customers_table where subject = ? and price >= ?',
                       (subject, price)).fetchall()
    for i in range(len(b)):
        number.append(*b[i])
    print(number)
    for i in range(len(a)):
        answer += '🔥 Заказ номер: {} \n👁Имя заказчика: {} \n📚 Предмет: {} \n🕑 Дедлайн: {} \n💰 Ценник: {}\n\n\n'.format(i + 1,a[i][0],a[i][2],a[i][3],a[i][4])
    return answer, number


print(get_orders_by_price('Естественник',700))