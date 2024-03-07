"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def file_reader(path):
    with open(path) as files:
        csv_reader = csv.reader(files)
        count = 0
        result = []
        for row in csv_reader:
            if count == 0:
                count += 1
            else:
                result.append(row)
                count += 1
    return result


customers_data = file_reader('north_data/customers_data.csv')
employees_data = file_reader('north_data/employees_data.csv')
orders_data = file_reader('north_data/orders_data.csv')

with psycopg2.connect(host='localhost', database='north', user='postgres', password='Wanted13') as conn:
    with conn.cursor() as cur:
        for customer in customers_data:
            cur.execute('INSERT INTO customer VALUES(%s, %s, %s)',
                        (customer[0], customer[1], customer[2]))
        for employee in employees_data:
            cur.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)',
                        (employee[0], employee[1], employee[2], employee[3], employee[4], employee[4]))
        for orders in orders_data:
            cur.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s)',
                        (orders[0], orders[1], orders[2], orders[3], orders[3]))
conn.close()
