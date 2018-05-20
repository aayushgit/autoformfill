from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import mysql.connector


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='autoform fill',
                                       user='root',
                                       password='toor')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


def insert_record(date, link, headline, content, newsof):
    query = "INSERT INTO autofill(date,link,headline,content,newsof) VALUES(%s,%s,%s,%s,%s)"
    args = (date, link, headline, content, newsof)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def main():
    connect()
    insert_record('2018/12/3', 'https://sharesansar.com/hello', 'This is my headline', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam quo dignissimos consequatur debitis ducimus dolorum voluptates, error at maiores odit eos reiciendis inventore ex, molestiae quibusdam rerum unde consequuntur doloremque!', 'NEPSE')


if __name__ == '__main__':
    main()
