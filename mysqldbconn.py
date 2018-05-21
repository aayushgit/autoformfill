#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pymysql


conn = pymysql.connect(host='localhost',
                       database='autoformfill',
                       user='root',
                       password='root')
if conn.is_connected():
    print('Connected to MySQL database')

cursor = conn.cursor()


def insert_record(date, link, headline, content, newsof):
    sql = """INSERT INTO autofill(date,link,headline,content,newsof)
     VALUES(%s,%s,%s,%s,%s)"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        conn.commit()
    except:
        # Rollback in case there is any error
        conn.rollback()


# disconnect from server
conn.close()


def main():
    insert_record('2018/12/3', 'https://sharesansar.com/hello', 'This is my headline', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam quo dignissimos consequatur debitis ducimus dolorum voluptates, error at maiores odit eos reiciendis inventore ex, molestiae quibusdam rerum unde consequuntur doloremque!', 'NEPSE')


if __name__ == '__main__':
    main()
