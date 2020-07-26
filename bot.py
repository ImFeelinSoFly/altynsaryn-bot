# coding=utf-8
import telebot
import const
import time
import mysql.connector
from mysql.connector import MySQLConnection, Error
# import re
# import shelve

from telebot import types
from telebot.types import LabeledPrice
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def query_with_fetchone(select, client_id):
    if select == 'client_id':
        query = "SELECT client_id FROM user WHERE client_id = %s"
    elif select == 'payment_course':
        query = "SELECT payment_course FROM user WHERE client_id = %s"
    elif select == 'flag':
        query = "SELECT flag FROM user WHERE client_id = %s"
    elif select == 'flag_for_confirmation_of_payment':
        query = "SELECT flag_for_confirmation_of_payment FROM user WHERE client_id = %s"
    elif select == 'flag_for_cancel_payment':
        query = "SELECT flag_for_cancel_payment FROM user WHERE client_id = %s"
    elif select == 'flag_moderator':
        query = "SELECT flag_moderator FROM user WHERE client_id = %s"
    elif select == 'flag_copyright':
        query = "SELECT flag_copyright FROM user WHERE client_id = %s"
    elif select == 'flag_new_com':
        query = "SELECT flag_new_com FROM user WHERE client_id = %s"
    elif select == 'position_of_pointer':
        query = "SELECT position_of_pointer FROM user WHERE client_id = %s"
    elif select == 'flag_comments':
        query = "SELECT flag_comments FROM user WHERE client_id = %s"
    elif select == 'user':
        query = "SELECT user FROM user WHERE client_id = %s"
    elif select == 'previous_message_id':
        query = "SELECT previous_message_id FROM user WHERE client_id = %s"
    args = (client_id,)
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor(buffered=True)

        cursor.execute(query, args)

        row = cursor.fetchone()

        while row is not None:
            return row[0]

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `testshit`.`user`")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM `testshit`.`user`")

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def update_flag(flag, client_id):
    query = "update `testshit`.`user` \
    SET flag = %s \
    WHERE client_id = %s \
    "
    args = (flag, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def update_payment_course(payment_course, client_id):
    query = "update `testshit`.`user` \
        SET payment_course = %s\
        WHERE client_id = %s\
        "
    args = (payment_course, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def update_previous_message_id(message_id, client_id):
    query = "update `testshit`.`user` \
    SET previous_message_id = %s\
    WHERE client_id = %s\
    "
    args = (message_id, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def update_flag_for_confirmation_of_payment(flag_for_confirmation_of_payment, client_id):
    query = "update `testshit`.`user` \
    SET flag_for_confirmation_of_payment = %s\
    WHERE client_id = %s\
    "
    args = (flag_for_confirmation_of_payment, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_flag_for_cancel_payment(flag_for_cancel_payment, client_id):
    query = "update `testshit`.`user` \
    SET flag_for_cancel_payment = %s\
    WHERE client_id = %s\
    "
    args = (flag_for_cancel_payment, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_flag_moderator(flag_moderator, client_id):
    query = "update `testshit`.`user` \
    SET flag_moderator = %s\
    WHERE client_id = %s\
    "
    args = (flag_moderator, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_flag_new_com(flag_new_com, client_id):
    query = "update `testshit`.`user` \
    SET flag_new_com = %s\
    WHERE client_id = %s\
    "
    args = (flag_new_com, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_flag_copyright(flag_copyright, client_id):
    query = "update `testshit`.`user` \
    SET flag_copyright = %s\
    WHERE client_id = %s\
    "
    args = (flag_copyright, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_position_of_pointer(position_of_pointer, client_id):
    query = "update `testshit`.`user` \
    SET position_of_pointer = %s\
    WHERE client_id = %s\
    "
    args = (position_of_pointer, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def update_flag_comments(flag_comments, client_id):
    query = "update `testshit`.`user` \
    SET flag_comments = %s\
    WHERE client_id = %s\
    "
    args = (flag_comments, client_id)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def insert_user(user_id, message_id, user_name):
    query = "INSERT INTO user (client_id,payment_course,flag,flag_for_confirmation_of_payment,flag_for_cancel_payment,flag_moderator,flag_copyright,flag_new_com,position_of_pointer,flag_comments,user)" \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    query = "INSERT INTO `testshit`.`user` \
(`client_id`,\
`flag`,\
`payment_course`,\
`flag_for_confirmation_of_payment`,\
`flag_for_cancel_payment`,\
`flag_moderator`,\
`flag_copyright`,\
`flag_new_com`,\
`position_of_pointer`,\
`flag_comments`,\
`previous_message_id`,\
`user`)\
VALUES\
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\
"
    args = (user_id, 0, '', 0, 0, 0, 0, 0, 0, 0, message_id, user_name)

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


bot = telebot.TeleBot(const.TOKEN)

mydb = mysql.connector.connect(user='root', password='idris6397', host='127.0.0.1', database='testshit',
                               auth_plugin='mysql_native_password')

Cursor = mydb.cursor(buffered=True)

Cursor.execute('''CREATE TABLE IF NOT EXISTS user (id int NOT NULL auto_increment primary key,
    client_id INT UNSIGNED NOT NULL DEFAULT 0,
    payment_course VARCHAR(100),
    flag TINYINT UNSIGNED NOT NULL DEFAULT 0,
    flag_for_confirmation_of_payment TINYINT UNSIGNED NOT NULL DEFAULT 0,
    flag_for_cancel_payment TINYINT UNSIGNED NOT NULL DEFAULT 0,
    flag_moderator TINYINT UNSIGNED NOT NULL DEFAULT 0,
    flag_copyright TINYINT UNSIGNED NOT NULL DEFAULT 0,
    flag_new_com TINYINT UNSIGNED NOT NULL DEFAULT 0,
    position_of_pointer INT UNSIGNED NOT NULL DEFAULT 0,
    flag_comments TINYINT UNSIGNED NOT NULL DEFAULT 0,
    user VARCHAR(100),
    previous_message_id INT UNSIGNED)''')
mydb.commit()

global content

prices = [LabeledPrice(label='School', amount=500000), LabeledPrice(label='1 course', amount=200000)]
schools = ['geekbrains', 'netology', 'otus', 'webformyself', 'udemy', 'skillbox']
geekbrains_courses = [
    'AgACAgIAAxkBAAIPT18dbBZKehbh_HDqll8WeOrKu6V8AAJCrzEbWwPwSPwdhU8IuctcJyh3kS4AAwEAAwIAA20AA2kiBgABGgQ',
    'AgACAgIAAxkBAAICXF8PNKfQXWJWyjwvS7DYpJrM8i7FAAL1rTEbtmeBSFAFUShtnSCqoQ2XlS4AAwEAAwIAA20AA4GOAQABGgQ',
    'AgACAgIAAxkBAAICXV8PNKnN0XbL13wcrWfgoOPOe2i5AAIBrjEbtmeBSJwvVBAZxx9aw-MWlS4AAwEAAwIAA20AA0mNAQABGgQ',
    'AgACAgIAAxkBAAICXl8PNKuG3VggCrrQxQn6mw8Fkc8_AAICrjEbtmeBSHw4CiQCIjO4r4QelS4AAwEAAwIAA20AA3mSAQABGgQ',
    'AgACAgIAAxkBAAICX18PNK3EEGwWXZkuKU0gDyHOwt-8AAIDrjEbtmeBSBsNr-OFrhYWVYZvkS4AAwEAAwIAA20AA-WrBQABGgQ',
    'AgACAgIAAxkBAAICYF8PNLPBtz3mA92BX0dICtPvBG6jAAL4rTEbtmeBSMe2T-GyIY2EkAHlkS4AAwEAAwIAA20AAwFLBAABGgQ',
    'AgACAgIAAxkBAAICYV8PNLcVhLZ8xmwpVq_xl4yfoRsGAAL5rTEbtmeBSPsHu707SQxmqFsVlS4AAwEAAwIAA20AA5aTAQABGgQ',
    'AgACAgIAAxkBAAICYl8PNLkG1Vcu946p3upq--DWhQd8AAL6rTEbtmeBSMEIuNRf_DiLlX7Zky4AAwEAAwIAA20AA97CAgABGgQ',
    'AgACAgIAAxkBAAICY18PNLvGN5lYgCwL0-HRAuGUvbIIAAL7rTEbtmeBSHZVFDZCG_hLsTF6kS4AAwEAAwIAA20AA22hBQABGgQ',
    'AgACAgIAAxkBAAICZF8PNL1oAAGwz3e1HeOccDSnJZ5FEgAC_K0xG7ZngUgFB65JeC_7qniHlZUuAAMBAAMCAANtAAMnkAEAARoE',
    'AgACAgIAAxkBAAICZV8PNMDtdqL50D2J-Tbqquye3NQZAAIErjEbtmeBSBE72x221gABqP-teJEuAAMBAAMCAANtAANppAUAARoE',
    'AgACAgIAAxkBAAICZl8PNMa6jnpodFTGCkMI8YycgrKkAAL9rTEbtmeBSDhaRPvKfU-AwAgglS4AAwEAAwIAA20AA2GLAQABGgQ',
    'AgACAgIAAxkBAAICZ18PNMhUOOlOULiGV5XiQzgKUxeIAAL-rTEbtmeBSIuioEsXyX_iGrC9ki4AAwEAAwIAA20AAyloBAABGgQ',
    'AgACAgIAAxkBAAICaF8PNMo1sSUfcJrB4_2tU-Rq2xEdAAL_rTEbtmeBSA-4Rg-FWDaNCpnfky4AAwEAAwIAA20AA57CAgABGgQ',
    'AgACAgIAAxkBAAICaV8PNM7H0W0zNJRHp4osBG5aUFBVAAIFrjEbtmeBSA8ZCIzV3cHRuJAhlS4AAwEAAwIAA20AA7eMAQABGgQ']
netology_courses = [
    'AgACAgIAAxkBAAICj18POWIa_dCOW3xtfASdcJxY2gy0AAL4rTEbtmeBSMe2T-GyIY2EkAHlkS4AAwEAAwIAA20AAwFLBAABGgQ',
    'AgACAgIAAxkBAAICkF8POWZw75krya3GWhbEsHvxe7LkAAIDrjEbtmeBSBsNr-OFrhYWVYZvkS4AAwEAAwIAA20AA-WrBQABGgQ',
    'AgACAgIAAxkBAAICkV8POWh017s7dra4xaf8Bf3zRcq-AAInrjEbtmeBSJkWXK9Ip_x0HhHokS4AAwEAAwIAA20AA99OBAABGgQ',
    'AgACAgIAAxkBAAICkl8POWx5tr4sIa1NFZaZFF0o8ZjvAAIorjEbtmeBSIwC2DmP5yHVHn3jkS4AAwEAAwIAA20AAzdUBAABGgQ',
    'AgACAgIAAxkBAAICk18POXLfMv0MFijAZ6nXF46Uj1nsAAL-rTEbtmeBSIuioEsXyX_iGrC9ki4AAwEAAwIAA20AAyloBAABGgQ',
    'AgACAgIAAxkBAAIClF8POXpF43h5QcVUPDHV48G-EDU8AAIprjEbtmeBSPOB0aJZVsW5kMvDki4AAwEAAwIAA20AA7hlBAABGgQ',
    'AgACAgIAAxkBAAIClV8POX1YN8LLA-W5vNwh7LEBftt-AAIqrjEbtmeBSEfVGa74JcYFWRPeky4AAwEAAwIAA20AA668AgABGgQ',
    'AgACAgIAAxkBAAICll8POYORBnhzEnElCjeCMzB5uqAaAAIrrjEbtmeBSECJP9D38ApUS8rDki4AAwEAAwIAA20AA95oBAABGgQ',
    'AgACAgIAAxkBAAICl18POYfIYojJNiebiMxybt--ZIfmAAIsrjEbtmeBSCCtz6Qj95mc7A4Fki4AAwEAAwIAA20AA6fJAwABGgQ',
    'AgACAgIAAxkBAAICmF8POYwj5AiI41U6lFLMRrYQSHnZAAInrjEbtmeBSJkWXK9Ip_x0HhHokS4AAwEAAwIAA20AA99OBAABGgQ',
    'AgACAgIAAxkBAAICmV8POZOyMJKiXF_OSfHS-Sia-sDCAAItrjEbtmeBSIOCKNIQGTSfI3lPkS4AAwEAAwIAA20AA1HoBQABGgQ',
    'AgACAgIAAxkBAAICml8POZcP3eqINcQjZYZ--f7Sn-EeAAIurjEbtmeBSPmVJI8p3KCFVaG6ki4AAwEAAwIAA20AA5FqBAABGgQ',
    'AgACAgIAAxkBAAIPS18da6FP-Uoaw6SPYMgxsUzL-CYyAAJBrzEbWwPwSK-bUsjw2yN5rO0ZlS4AAwEAAwIAA20AA4gEAgABGgQ',
    'AgACAgIAAxkBAAICnF8POZwUUrcvbGH-nFm3cImcISVYAAIvrjEbtmeBSHvK3dsp6Yk6Yv7ski4AAwEAAwIAA20AAx_LAwABGgQ',
    'AgACAgIAAxkBAAICnV8POZ0shlDwjRodrMhIH3HBDzBEAAIwrjEbtmeBSIUROuyjcmSIzXlPkS4AAwEAAwIAA20AA8vpBQABGgQ']
otus_courses = ['AgACAgIAAxkBAAICrV8POtLq6NzkUOMDBGMLs02YjeqSAAIyrjEbtmeBSGfu0jopVvlk0NQTlS4AAwEAAwIAA20AA5CTAQABGgQ',
                'AgACAgIAAxkBAAICrl8POtTHGMT678Mn1uS_-PkBuOUlAAIyrjEbtmeBSGfu0jopVvlk0NQTlS4AAwEAAwIAA20AA5CTAQABGgQ',
                'AgACAgIAAxkBAAICr18POtjaDBtuE4WYCn1qT5p7pZHOAAI_rjEbtmeBSNC5Yv7lPvUMx3vjkS4AAwEAAwIAA20AA4tXBAABGgQ',
                'AgACAgIAAxkBAAICsF8POtrSvkNyBHFjPPpuWkacIy46AAJArjEbtmeBSGBTo5hPR3E6B9QTlS4AAwEAAwIAA20AA3mSAQABGgQ',
                'AgACAgIAAxkBAAICsV8POtydmGybMEbKm9wOqxQ0xYkrAAJBrjEbtmeBSCTBGvftPFwKr6XskS4AAwEAAwIAA20AA9FXBAABGgQ',
                'AgACAgIAAxkBAAICsl8POuDDwcF2Zo1PSrXtEfpUU8vkAAIfrjEbtmeBSDKHvW-aFR6RLZaYlS4AAwEAAwIAA20AA4OQAQABGgQ',
                'AgACAgIAAxkBAAICs18POuMAAdVp8T4YQH_l7UTIzogi0AACMa4xG7ZngUgmGTa1q9dJ4L1845EuAAMBAAMCAANtAAOoYAQAARoE',
                'AgACAgIAAxkBAAICtF8POu23hSLG2cv2AsPuSDcJAYcpAAJCrjEbtmeBSGMOdyUFbStSTGBJkS4AAwEAAwIAA20AA1HuBQABGgQ',
                'AgACAgIAAxkBAAICtV8POvSBwbaKSdefZ__jNq2FgTW_AAL4rTEbtmeBSMe2T-GyIY2EkAHlkS4AAwEAAwIAA20AAwFLBAABGgQ',
                'AgACAgIAAxkBAAICtl8POvbGFVKCaQcHEU6CUPhNIqnxAAJErjEbtmeBSNZnkz-uYpfLRTW_ki4AAwEAAwIAA20AA4JqBAABGgQ',
                'AgACAgIAAxkBAAICt18POvps55qIYS7b_V1y87rH60ESAAJFrjEbtmeBSFe201SiinFicqGblS4AAwEAAwIAA20AAyyOAQABGgQ',
                'AgACAgIAAxkBAAICuF8POv5IBMkRSQXkHoNNLDGZwHzrAAJGrjEbtmeBSKFfOQENzEo429fGki4AAwEAAwIAA20AAx1vBAABGgQ',
                'AgACAgIAAxkBAAICuV8POwABHBlQxtMQSfwnFm1kI4c7zQACR64xG7ZngUjc03hT5K7wnufIfpEuAAMBAAMCAANtAAO6qQUAARoE',
                'AgACAgIAAxkBAAICul8POweWMCemiv_ZKK_dW2f2f_nnAAJIrjEbtmeBSLsWvLBLe-QfRTjxkS4AAwEAAwIAA20AA8RSBAABGgQ',
                'AgACAgIAAxkBAAICu18POwmMRJaI80fsbdnMM1jbm0X3AAJJrjEbtmeBSIJ69n_964c8MP1tkS4AAwEAAwIAA20AA7WrBQABGgQ']
webformyself_courses = [
    'AgACAgIAAxkBAAICf18POEfkKnK-MypP3vPY5tEQ_A0wAAIRrjEbtmeBSJjVetqrXflfULSDki4AAwEAAwIAA20AA-_HAwABGgQ',
    'AgACAgIAAxkBAAICgF8POGDDwDTT6guffYlFPm-Ca9jUAAIdrjEbtmeBSGQkfcOWLmP9YDR6kS4AAwEAAwIAA20AA-CpBQABGgQ',
    'AgACAgIAAxkBAAICgV8POGXWxmy8uO3tGTlje19UHAN6AAIerjEbtmeBSKqza28AAQ09noNcFZUuAAMBAAMCAANtAAPFkAEAARoE',
    'AgACAgIAAxkBAAICgl8POGpkmOe3FONutRDIiF__yucqAAIfrjEbtmeBSDKHvW-aFR6RLZaYlS4AAwEAAwIAA20AA4OQAQABGgQ',
    'AgACAgIAAxkBAAICg18POHRGkmaZHNHkMOU99OLIE1wJAAIgrjEbtmeBSOfCtYnNLnR7BzyFki4AAwEAAwIAA20AAxrFAwABGgQ',
    'AgACAgIAAxkBAAIChF8POHfwHXiH1ZaSeSdN2Xd-5V2tAAIErjEbtmeBSBE72x221gABqP-teJEuAAMBAAMCAANtAANppAUAARoE',
    'AgACAgIAAxkBAAIChV8POHtel_kxbf9GxZlVMqngM-0VAAIFrjEbtmeBSA8ZCIzV3cHRuJAhlS4AAwEAAwIAA20AA7eMAQABGgQ',
    'AgACAgIAAxkBAAICh18POI5thAABlJnBSB6B3ze76Ps5hgACIa4xG7ZngUi2_Ov9_Q1xXEeZfZIuAAMBAAMCAANtAAOe0QMAARoE',
    'AgACAgIAAxkBAAIPxF8decxd-gqWVlSVeY4Ha_BKkPb4AAJnsDEbWwPwSFEGbuAQU0Tr05EhlS4AAwEAAwIAA20AAzcIAgABGgQ',
    'AgACAgIAAxkBAAICiV8POKTzc4nxDBYFXMgevsIC8uSNAAL-rTEbtmeBSIuioEsXyX_iGrC9ki4AAwEAAwIAA20AAyloBAABGgQ',
    'AgACAgIAAxkBAAIP0V8des8H-72PZ-gbYItw4jjZsGCoAAJosDEbWwPwSAuZYIsKlCLKQgTlkS4AAwEAAwIAA20AA9zGBAABGgQ',
    'AgACAgIAAxkBAAICi18POK0J6l-zLIH-aYWusmBGHNF4AAIkrjEbtmeBSE5p7SYhiC8b84VvkS4AAwEAAwIAA20AA_WhBQABGgQ',
    'AgACAgIAAxkBAAICjF8POLGSJK3TDmwG_SwOPscUe8aRAAIlrjEbtmeBSAQW8gLb0oUlA1ASlS4AAwEAAwIAA20AAwGOAQABGgQ',
    'AgACAgIAAxkBAAICjV8POLPYFC06cc-JqYIYoKcLQ09UAAIlrjEbtmeBSAQW8gLb0oUlA1ASlS4AAwEAAwIAA20AAwGOAQABGgQ',
    'AgACAgIAAxkBAAICjl8POLiCUKi8mbzbRx7BM8nBazyNAAImrjEbtmeBSPuv-I2DwgPybyqdlS4AAwEAAwIAA20AA1qQAQABGgQ']
skillbox_courses = [
    'AgACAgIAAxkBAAICcF8PNc4z9MQxvKuCZiPm8tzhLAPnAAIOrjEbtmeBSDHXWTPr8Q7QuqWAki4AAwEAAwIAA20AA32-AwABGgQ',
    'AgACAgIAAxkBAAICcV8PNdcsSNzdca4eytUfETeChcNBAAIPrjEbtmeBSOE-LTWO9a8VjCV3kS4AAwEAAwIAA20AAx2mBQABGgQ',
    'AgACAgIAAxkBAAICcl8PNdzqFJ1t837M2Zp8Wpomra27AAL8rTEbtmeBSAUHrkl4L_uqeIeVlS4AAwEAAwIAA20AAyeQAQABGgQ',
    'AgACAgIAAxkBAAICc18PNeKK0DoF8a5JWqM3_SGvNduJAAIQrjEbtmeBSECRpbGrUndkapWYlS4AAwEAAwIAA20AA6iQAQABGgQ',
    'AgACAgIAAxkBAAICdF8PNe2DkcjFCmqnX9a8yrF8qQABXwACEa4xG7ZngUiY1Xraq135X1C0g5IuAAMBAAMCAANtAAPvxwMAARoE',
    'AgACAgIAAxkBAAICdV8PNe7MSNn6LP8pY5gcD9uGaHAmAAISrjEbtmeBSCauD9vcumoPnIjmkS4AAwEAAwIAA20AA7dLBAABGgQ',
    'AgACAgIAAxkBAAICdl8PNfTn3K1xJAoQM2N7RtB0kvZ6AAITrjEbtmeBSIOoUf5MOcnGThLokS4AAwEAAwIAA20AA4NNBAABGgQ',
    'AgACAgIAAxkBAAICd18PNfrwWkjGOnNsXH8vDDqkVRYhAAIUrjEbtmeBSIV4wPYQ6-2VdKPskS4AAwEAAwIAA20AA4taBAABGgQ',
    'AgACAgIAAxkBAAICeF8PNgKxbvadbKikENw_JqgbIIfEAAIVrjEbtmeBSMEZzSXuPItylmnoki4AAwEAAwIAA20AA1HLAwABGgQ',
    'AgACAgIAAxkBAAICeV8PNgVIUiqKWUAoMj-LUJ-Evgp3AAIWrjEbtmeBSOok8Lsj4lb19Rd0kS4AAwEAAwIAA20AA6iuBQABGgQ',
    'AgACAgIAAxkBAAICel8PNgg4kDrB3vHmYk6-JIRYdfP6AAIXrjEbtmeBSMissJfTxhp8qax4kS4AAwEAAwIAA20AAwipBQABGgQ',
    'AgACAgIAAxkBAAIPdF8dbkqIaJc9KYhYkbMPMcKZTqJ4AAJSrzEbWwPwSMkBjj4FXOIBEMh-kS4AAwEAAwIAA20AA8wmBgABGgQ',
    'AgACAgIAAxkBAAICfF8PNhd6iIdMGeY31cT3byId7UkoAAIarjEbtmeBSL5GCZ3BVZ9JevfhkS4AAwEAAwIAA20AAzBSBAABGgQ',
    'AgACAgIAAxkBAAICfV8PNh35FOjvcXUc779tD8QAAZhmIQACG64xG7ZngUj0qfOMjVaNqWAAAW6RLgADAQADAgADbQADSa0FAAEaBA',
    'AgACAgIAAxkBAAICfl8PNiIbhhSXblueC2Z0CmfZRMomAAIcrjEbtmeBSJTw0nXbgtnGl_jXky4AAwEAAwIAA20AA1HAAgABGgQ']
udemy_courses = ['AgACAgIAAxkBAAICnl8POdyrMZiSOx8okKDqBzG5nW8AAyeuMRu2Z4FImRZcr0in_HQeEeiRLgADAQADAgADbQAD304EAAEaBA',
                 'AgACAgIAAxkBAAICn18POd83F4zmSfxA5rCSZ2MNNWdWAAIxrjEbtmeBSCYZNrWr10ngvXzjkS4AAwEAAwIAA20AA6hgBAABGgQ',
                 'AgACAgIAAxkBAAICoF8POeLEsNwDrYSi0s8VW9Ymljm9AAIyrjEbtmeBSGfu0jopVvlk0NQTlS4AAwEAAwIAA20AA5CTAQABGgQ',
                 'AgACAgIAAxkBAAICoV8POeQlwU0sP1FQUZXumkrVX29sAAIzrjEbtmeBSDloM4zGdgZHUU4SlS4AAwEAAwIAA20AA-6TAQABGgQ',
                 'AgACAgIAAxkBAAICol8POehaASzOnbOant80hDrhqzsvAAI0rjEbtmeBSBevxohco6v8ZIHZky4AAwEAAwIAA20AA1TDAgABGgQ',
                 'AgACAgIAAxkBAAICo18POe4h_1U8g-jQdOtLkDsDZ7XzAAI1rjEbtmeBSFAhm9OZnC6llIZvkS4AAwEAAwIAA20AA3KiBQABGgQ',
                 'AgACAgIAAxkBAAICpF8POfTp-C03iWdGRdUPdjcCAAHUOQACNq4xG7ZngUj4RozMlh0E6Aaw75EuAAMBAAMCAANtAAMFVAQAARoE',
                 'AgACAgIAAxkBAAICpV8POfhFSzoCixiAt26B-mfdRaYeAAI3rjEbtmeBSN_B-rD6Z8TVI4LZky4AAwEAAwIAA20AA-G-AgABGgQ',
                 'AgACAgIAAxkBAAICpl8POf7pAhYGHFeHDO0Ui6EX0wk8AAI4rjEbtmeBSOVou3eRJ7L7OAoglS4AAwEAAwIAA20AA3aMAQABGgQ',
                 'AgACAgIAAxkBAAICp18POgI7mEbCKtehSY9AYQL93vkyAAI5rjEbtmeBSKIgxTkR-F30LcZ-kS4AAwEAAwIAA20AAw2jBQABGgQ',
                 'AgACAgIAAxkBAAICqF8POgaUiDuUlkKyGk05zlnrs0ZUAAL9rTEbtmeBSDhaRPvKfU-AwAgglS4AAwEAAwIAA20AA2GLAQABGgQ',
                 'AgACAgIAAxkBAAIPol8ddnR1Z7rrQ1oj0wmm77CwvWMMAAKQrzEbWwPwSBhUeduQQRvrxJAhlS4AAwEAAwIAA20AA5QJAgABGgQ',
                 'AgACAgIAAxkBAAICqV8POgu76vAugw6kKhjrli26QgNoAAI6rjEbtmeBSKAhxvX5yjYjMHcblS4AAwEAAwIAA20AAweNAQABGgQ',
                 'AgACAgIAAxkBAAICql8POhFXilkcnGHZdizijEdumYodAAI7rjEbtmeBSLAB-vi88XRe41v4lC4AAwEAAwIAA20AA5f7AQABGgQ',
                 'AgACAgIAAxkBAAICq18POhNFToTrYEOckiZMnr06F5AjAAI8rjEbtmeBSNJJPDAlIh0cPwLlkS4AAwEAAwIAA20AA3hVBAABGgQ']


def payment_method(client_id):
    pm = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Банковской картой',
                                       callback_data='pay' + query_with_fetchone('payment_course',
                                                                                 client_id) + 'credit card')
    but_2 = types.InlineKeyboardButton(text='Qiwi кошелек', callback_data='pay' + query_with_fetchone('payment_course',
                                                                                                      client_id) + 'qiwi wallet')
    but_3 = types.InlineKeyboardButton(text='Kaspi Gold', callback_data='pay' + query_with_fetchone('payment_course',
                                                                                                    client_id) + 'kaspi gold')
    but_4 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    pm.add(but_1, but_2, but_3)
    pm.add(but_4)
    return pm


def credit_keyboard(amount, url, client_id):
    ck = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Оплатить ' + str(amount), url=url)
    but_2 = types.InlineKeyboardButton(text='Назад',
                                       callback_data=query_with_fetchone('payment_course', client_id)[3:] + 'rep')
    ck.add(but_1, but_2)
    return ck


def successful_payment(client_id):
    sp = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Подтверждаю',
                                       callback_data='success' + query_with_fetchone('payment_course', client_id)[
                                                                 3:] + str(client_id))
    but_2 = types.InlineKeyboardButton(text='Отказано', callback_data='reject' + " " + str(client_id))
    sp.add(but_1, but_2)
    return sp


def one_course(client_id, url, school):
    oc = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Купить', callback_data=query_with_fetchone('payment_course', client_id))
    but_2 = types.InlineKeyboardButton(text='Сайт курса', url=url)
    but_3 = types.InlineKeyboardButton(text='Назад', switch_inline_query_current_chat=school)
    oc.add(but_1, but_2, but_3)
    return oc


def confirmation():
    con = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Подтвердить', callback_data='confirmed')
    but_2 = types.InlineKeyboardButton(text='Отмена', callback_data='disconf')
    con.add(but_1, but_2)
    return con


def gb_school():
    gb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='geekbrains')
    but_2 = types.InlineKeyboardButton("Buy School's courses",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    gb.add(but_1)
    gb.add(but_2)
    gb.add(but_3)
    return gb


def sb_school():
    sb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='skillbox')
    but_2 = types.InlineKeyboardButton(text="Buy School's courses",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    sb.add(but_1)
    sb.add(but_2)
    sb.add(but_3)
    return sb


def ud_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='udemy')
    but_2 = types.InlineKeyboardButton("Buy School's courses",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def ot_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='otus')
    but_2 = types.InlineKeyboardButton("Buy School's courses",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def wb_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='webformyself')
    but_2 = types.InlineKeyboardButton("Buy School's courses",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def nt_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('List of courses', switch_inline_query_current_chat='netology')
    but_2 = types.InlineKeyboardButton("Buy School's courses",
                                       callback_data='netology16')
    but_3 = types.InlineKeyboardButton('back', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def all_courses():
    ac = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Zaberi Koziri', callback_data='all')
    ac.add(but_1)
    return ac


@bot.inline_handler(lambda query: query.query == 'courses')
def query_text(query):
    global content
    try:
        with open('stats.txt', mode='w') as file:
            content[query_with_fetchone('position_of_pointer', query.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', query.from_user.id)][:-25] + query.query + ' ' + content[
                                                                                            query_with_fetchone(
                                                                                                'position_of_pointer',
                                                                                                query.from_user.id)][
                                                                                        -25:]
            file.writelines(content)
    except:
        pass
    icon_1 = 'https://imagizer.imageshack.com/img923/1812/KajI64.png'
    icon_2 = 'https://imagizer.imageshack.com/img924/7666/5J69S1.png'
    icon_3 = 'https://imagizer.imageshack.com/img924/9480/sBPIE4.png'
    icon_4 = 'https://imagizer.imageshack.com/img922/5692/cNjY8b.png'
    icon_5 = 'https://imagizer.imageshack.com/img924/2395/WwgFJU.png'
    icon_6 = 'https://imagizer.imageshack.com/img923/5373/VDXsBb.png'
    article_1 = types.InlineQueryResultArticle(id=1, input_message_content=types.InputTextMessageContent('geekbrains'),
                                               title='GeekBrains', description='GeekBrains courses', thumb_url=icon_1,
                                               thumb_width=48, thumb_height=48, reply_markup=gb_school())
    article_2 = types.InlineQueryResultArticle(id=4, input_message_content=types.InputTextMessageContent('skillbox'),
                                               title='SkillBox', description='SkillBox courses', thumb_url=icon_2,
                                               thumb_width=48, thumb_height=48, reply_markup=sb_school())
    article_3 = types.InlineQueryResultArticle(id=3,
                                               input_message_content=types.InputTextMessageContent('webformyself'),
                                               title='WebForMyself', description='WebForMyself courses',
                                               thumb_url=icon_3, thumb_width=48, thumb_height=48,
                                               reply_markup=wb_school())
    article_4 = types.InlineQueryResultArticle(id=2, input_message_content=types.InputTextMessageContent('netology'),
                                               title='Netology', description='Netology courses', thumb_url=icon_4,
                                               thumb_width=48, thumb_height=48, reply_markup=nt_school())
    article_5 = types.InlineQueryResultArticle(id=5, input_message_content=types.InputTextMessageContent('udemy'),
                                               title='Udemy', description='Udemy courses', thumb_url=icon_5,
                                               thumb_width=48, thumb_height=48, reply_markup=ud_school())
    article_6 = types.InlineQueryResultArticle(id=6, input_message_content=types.InputTextMessageContent('otus'),
                                               title='OTUS', description='OTUS courses', thumb_url=icon_6,
                                               thumb_width=48, thumb_height=48, reply_markup=ot_school())
    results = [article_1, article_2, article_3, article_4, article_5, article_6]
    bot.answer_inline_query(query.id, results)


@bot.inline_handler(
    lambda query: query.query in ['geekbrains', 'netology', 'otus', 'webformyself', 'udemy', 'skillbox'])
def schools(query):
    global content
    try:
        with open('stats.txt', mode='w') as file:
            content[query_with_fetchone('position_of_pointer', query.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', query.from_user.id)][:-25] + query.query + ' ' + content[
                                                                                            query_with_fetchone(
                                                                                                'position_of_pointer',
                                                                                                query.from_user.id)][
                                                                                        -25:]
            file.writelines(content)
    except:
        pass
    if query.query == 'geekbrains':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('geekbrains1'),
                                                   title='Профессия Разработчик игр',
                                                   description='Стань частью игровой индустрии',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6049/wcpahi.jpg',
                                                   reply_markup=gb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('geekbrains2'),
                                                   title='Профессия Программист Android',
                                                   description='Разрабатывай под 80% рынка мобильных устройств!',
                                                   thumb_url='https://imagizer.imageshack.com/img922/7097/C2sRw9.png',
                                                   reply_markup=gb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('geekbrains3'),
                                                   title='Профессия Frontend-разработчик',
                                                   description='Профессиональная верстка сайтов по современным '
                                                               'стандартам',
                                                   thumb_url='https://imagizer.imageshack.com/img922/5341/CeMvD6.jpg',
                                                   reply_markup=gb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('geekbrains4'),
                                                   title='Курс по Agile-методологиям',
                                                   description='Когда дедлайны горят, заказчик дает новые вводные, '
                                                               'а в продуктах встречаются ошибки, используйте '
                                                               'Agile-метод.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/84/i23qQ7.png',
                                                   reply_markup=gb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('geekbrains5'),
                                                   title='Профессия Веб-разработчик',
                                                   description='Создай свой фейсбук!С музыкой и нормальным интерфейсом',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6565/dLJYLy.jpg',
                                                   reply_markup=gb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('geekbrains6'),
                                                   title='Профессиональная Backend-разработка',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса backend-разработки ',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3277/V3opMS.png',
                                                   reply_markup=gb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('geekbrains7'),
                                                   title='Создание сайтов и приложений. Методы повышения конверсии',
                                                   description='Создавай действительно продающие структуры сайтов',
                                                   thumb_url='https://imagizer.imageshack.com/img923/558/XMlivo.jpg',
                                                   reply_markup=gb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('geekbrains8'),
                                                   title='Факультет Python-разработки',
                                                   description='Онлайн-университет от @mail.ru Group',
                                                   thumb_url='https://imagizer.imageshack.com/img924/9392/UCl3tF.jpg',
                                                   reply_markup=gb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('geekbrains9'),
                                                   title='Системный администратор',
                                                   description='Незаменимый специалист в любой компании',
                                                   thumb_url='https://imagizer.imageshack.com/img923/8554/aScFbP.jpg',
                                                   reply_markup=gb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent('geekbrains10'),
                                                    title='Дизайнер интерфейсов',
                                                    description='Факультет Дизайна интерфейсов (UX/UI)',
                                                    thumb_url='https://imagizer.imageshack.com/img922/3497/cs4Eto.jpg',
                                                    reply_markup=gb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent('geekbrains11'),
                                                    title='1С-Битрикс: Управление сайтом',
                                                    description='Всё необходимое для запуска и ведения бизнеса:CMS',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7259/47VpVE.jpg',
                                                    reply_markup=gb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent('geekbrains12'),
                                                    title='Школа Программирования. Java 0, 1, 2.',
                                                    description='Написано однажды - работает везде',
                                                    thumb_url='https://imagizer.imageshack.com/img922/1973/CfOxaX.png',
                                                    reply_markup=gb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent('geekbrains13'),
                                                    title='Базы данных для профессионалов и язык SQL',
                                                    description='Проектирование БД и запросы SQL',
                                                    thumb_url='https://imagizer.imageshack.com/img923/4985/1Rw1BR.png',
                                                    reply_markup=gb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent('geekbrains14'),
                                                    title='Анатомия блокчейна',
                                                    description='На пике технического прогресса',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7537/Mn107B.jpg',
                                                    reply_markup=gb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent('geekbrains15'),
                                                    title='Node.js Серверное программирование на JavaScript',
                                                    description='Создавай веб-сервисы с помощью популярного '
                                                                'фреймворка Express.js',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9976/xpE4KK.png',
                                                    reply_markup=gb_school())
        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'skillbox':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('skillbox1'),
                                                   title='Дизайн мобильных приложений',
                                                   description='За 8 месяцев научитесь создавать дизайн под '
                                                               'разные мобильные платформы',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6688/YLaF26.png',
                                                   reply_markup=sb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('skillbox2'),
                                                   title='Управление digital-проектами',
                                                   description='За четыре месяца вы освоите все этапы работы над '
                                                               'проектом',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8969/lY3YcD.jpg',
                                                   reply_markup=sb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('skillbox3'),
                                                   title='UX-дизайн, UX-аналитика, UI-анимация',
                                                   description='Погрузитесь в самую популярную профессию за 4 месяца.',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6160/6tQ5Ir.jpg',
                                                   reply_markup=sb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('skillbox4'),
                                                   title='Cinema 4D для веб-дизайна',
                                                   description="Сможете создавать графику для рекламы, кино или ТV",
                                                   thumb_url='https://imagizer.imageshack.com/img924/6632/KbRFFr.png',
                                                   reply_markup=sb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('skillbox5'),
                                                   title='Веб-дизайн с Нуля до Про',
                                                   description='Вы научитесь создавать дизайн сайтов и приложений',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5687/7dqETn.jpg',
                                                   reply_markup=sb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('skillbox6'),
                                                   title='UI анимация. Стань motion-дизайнером за 16 недель',
                                                   description='Научитесь превращать статичный дизайн в динамичные '
                                                               'креативные интерфейсы.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/4631/YSnodB.png',
                                                   reply_markup=sb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('skillbox7'),
                                                   title='Сквозная аналитика',
                                                   description='Вы научитесь выжимать максимум из рекламы, '
                                                               'принимать решения на основе точных данных',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3386/Gx1DUN.jpg',
                                                   reply_markup=sb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('skillbox8'),
                                                   title='Как открыть и развивать свою веб-студию',
                                                   description='Запустите digital-агентство всего за 3,5 месяца.',
                                                   thumb_url='https://imagizer.imageshack.com/img923/7425/83nbUl.jpg',
                                                   reply_markup=sb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('skillbox9'),
                                                   title='Рекламная Графика',
                                                   description='Курс от создателей самых сочных рекламных иллюстраций '
                                                               'на российском рынке',
                                                   thumb_url='https://imagizer.imageshack.com/img924/6655/mN1T6z.jpg',
                                                   reply_markup=sb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent('skillbox10'),
                                                    title='Excel c 0 до PRO',
                                                    description='Научитесь составлять сложные отчёты и строить '
                                                                'прогнозы',
                                                    thumb_url='https://imagizer.imageshack.com/img922/4359/2s9kaf.jpg',
                                                    reply_markup=sb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent('skillbox11'),
                                                    title='Adobe After Effects с 0 до PRO',
                                                    description='На курсе вы освоите самый популярный в мире '
                                                                'инструмент для работы с анимацией',
                                                    thumb_url='https://imagizer.imageshack.com/img924/5734/F1r8Hv.jpg',
                                                    reply_markup=sb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent('skillbox12'),
                                                    title='Профессия С#-разработчик',
                                                    description='130 часов обучения — и вы научитесь писать программы, разрабатывать веб-сервисы и игры на языке от Microsoft, в команде и индивидуально',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9595/7FhQEE.jpg',
                                                    reply_markup=sb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent('skillbox13'),
                                                    title='Онлайн-курс Figma 3.0',
                                                    description='Вы освоите популярный сервис для разработки '
                                                                'интерфейсов Figma',
                                                    thumb_url='https://imagizer.imageshack.com/img924/26/BWxykA.png',
                                                    reply_markup=sb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent('skillbox14'),
                                                    title='Практический интенсивный курс SMM менеджер',
                                                    description='Вы научитесь создавать '
                                                                'вовлекающий контент, общаться с аудиторией и '
                                                                'запускать рекламу',
                                                    thumb_url='https://imagizer.imageshack.com/img922/4848/hQENuo.png',
                                                    reply_markup=sb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent('skillbox15'),
                                                    title='Профессия интернет-маркетолог от А до Я',
                                                    description='Вы с нуля научитесь выстраивать стратегию '
                                                                'продвижения бизнеса',
                                                    thumb_url='https://imagizer.imageshack.com/img922/2634/WjKwAG.png',
                                                    reply_markup=sb_school())
        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'udemy':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('udemy1'),
                                                   title='ITtensive - Базовый Python',
                                                   description='Изучите с нуля самый востребованный язык '
                                                               'программирования',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3961/F5dFaz.png',
                                                   reply_markup=ud_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('udemy2'),
                                                   title='Продвинутые навыки Python: станьте лучшим разработчиком '
                                                         'Python!',
                                                   description='В этом курсе вы узнаете много встроенных функций и '
                                                               'овладеете их преимуществами.',
                                                   thumb_url='https://imagizer.imageshack.com/img923/5372/T4pET7.jpg',
                                                   reply_markup=ud_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('udemy3'),
                                                   title='iOS программирование на Swift',
                                                   description='Практический курс по созданию iOS приложения на языке '
                                                               'Swift в среде Xcode и публикации его в AppStore',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ud_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('udemy4'),
                                                   title='Kotlin. От А до Я',
                                                   description='Узнай за что Kotlin так полюбили в Google!',
                                                   thumb_url='https://imagizer.imageshack.com/img922/2655/hDxlt6.png',
                                                   reply_markup=ud_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('udemy5'),
                                                   title='React Native 2020. Мобильная разработка на JavaScript',
                                                   description="Научись создавать крутейшие мобильные приложения для "
                                                               "Android и iOS на JavaScript + React JS",
                                                   thumb_url='https://imagizer.imageshack.com/img922/1056/o81JjI.jpg',
                                                   reply_markup=ud_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('udemy6'),
                                                   title='Android разработка с нуля до профессионала',
                                                   description='Android, основы Java, Kotlin. Создай 21 приложение, '
                                                               'включая Firebase real-time чат и приложение заказа '
                                                               'такси!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/2665/oM9XRj.png',
                                                   reply_markup=ud_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('udemy7'),
                                                   title='PHP v.7+ и MySQL с нуля',
                                                   description='Начните с основ и создайте полноценную CMS!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/3152/jplVFA.png',
                                                   reply_markup=ud_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('udemy8'),
                                                   title='Программирование на C#: от новичка до специалиста',
                                                   description='Изучите C# и платформу .NET, включая .NET Core и '
                                                               'начните практиковать объектно-ориентированное '
                                                               'программирование',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8886/0dJ95T.png',
                                                   reply_markup=ud_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('udemy9'),
                                                   title='Программирование игр для детей на Scratch для начинающих',
                                                   description='Научитесь основам программирования и созданию '
                                                               'увлекательных компьютерных игр в интересном формате с '
                                                               'помощью Scratch',
                                                   thumb_url='https://imagizer.imageshack.com/img922/4049/X4LqGg.png',
                                                   reply_markup=ud_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent('udemy10'),
                                                    title='Создание Telegram ботов с помощью JavaScript: Полное '
                                                          'руководство ',
                                                    description='Создайте чат-ботов Telegram с Node.js, используя '
                                                                'современный Telegraf Framework',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8400/OS8IYK.jpg',
                                                    reply_markup=ud_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent('udemy11'),
                                                    title='Продвинутые алгоритмы в Java',
                                                    description='Лучший курс по Java',
                                                    thumb_url='https://imagizer.imageshack.com/img922/906/L3oGTD.png',
                                                    reply_markup=ud_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent('udemy12'),
                                                    title='Аналитика и Data Science для менеджеров и гуманитариев',
                                                    description='Профкурс по аналитике для социально-экономических '
                                                                'направлений. Современные методы поиска скрытых '
                                                                'закономерностей',
                                                    thumb_url='https://imagizer.imageshack.com/img923/1600/1N4TKz.png',
                                                    reply_markup=ud_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent('udemy13'),
                                                    title='Основы программирования',
                                                    description='Основные понятия, алгоритмы и блок-схемы',
                                                    thumb_url='https://imagizer.imageshack.com/img922/3774/f554V8.png',
                                                    reply_markup=ud_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent('udemy14'),
                                                    title='Машинное обучение: кластеризация и классификация на Python',
                                                    description="Выигрываем соревнование Kaggle с kNN, SVM, "
                                                                "логистической регрессией, случайным лесом, XGBoost, "
                                                                "CatBoost и LightGBM",
                                                    thumb_url='https://imagizer.imageshack.com/img924/1604/6VOBKY.jpg',
                                                    reply_markup=ud_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent('udemy15'),
                                                    title='Изучаем Linux и командную строку. Линукс шаг за шагом',
                                                    description='Администрирование Linux, используюя командную строку '
                                                                'bash',
                                                    thumb_url='https://imagizer.imageshack.com/img924/1100/XYrY6t.png',
                                                    reply_markup=ud_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'netology':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('netology1'),
                                                   title='PHP/SQL: back-end разработка и базы данных',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса backend-разработки ',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8519/rNEsyy.png',
                                                   reply_markup=nt_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('netology2'),
                                                   title='Веб-дизайн: Эффективный сайт от идеи до реализации',
                                                   description='Пройдите все этапы разработки дизайна продукта с нуля',
                                                   thumb_url='https://imagizer.imageshack.com/img923/4756/FTRedT.jpg',
                                                   reply_markup=nt_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('netology3'),
                                                   title='Python для работы с данными',
                                                   description="Освойте ключевой инструмент в мире аналитики и "
                                                               "машинного обучения",
                                                   thumb_url='https://imagizer.imageshack.com/img923/7515/w2ceS4.png',
                                                   reply_markup=nt_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('netology4'),
                                                   title='Аналитик данных',
                                                   description='Научим с нуля собирать, анализировать и презентовать '
                                                               'данные',
                                                   thumb_url='https://imagizer.imageshack.com/img922/9082/J0RDQG.jpg',
                                                   reply_markup=nt_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('netology5'),
                                                   title='SQL и получение данных',
                                                   description='Научим получать данные для анализа без помощи '
                                                               'разработчиков',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6286/mE6xiK.png',
                                                   reply_markup=nt_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('netology6'),
                                                   title='Power BI: анализ и визуализация данных без программирования',
                                                   description='инструмент бизнес-анализа, позволяющий анализировать '
                                                               '«живые» данные и создавать визуальные отчёты',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6430/OkjPfV.png',
                                                   reply_markup=nt_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('netology7'),
                                                   title='BIG DATA с нуля',
                                                   description='Научитесь работать с большими данными,Перейдите на '
                                                               'новый уровень в профессии',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6725/Y8rzwz.jpg',
                                                   reply_markup=nt_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('netology8'),
                                                   title='Таргетированная реклам',
                                                   description='Курс одобрен компаниями ВКонтакте и myTarget',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8099/kJAshb.jpg',
                                                   reply_markup=nt_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('netology9'),
                                                   title='Геймдизайн',
                                                   description='Превращайте идеи в успешные игровые проекты',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6162/fTVCcG.jpg',
                                                   reply_markup=nt_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent('netology10'),
                                                    title='Python: программирование на каждый день',
                                                    description='Python — самый простой язык для старта',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7515/w2ceS4.png',
                                                    reply_markup=nt_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent('netology11'),
                                                    title='Веб-аналитика: что нужно знать интернет-специалисту',
                                                    description='Прокачаете знания в Google Analytics, '
                                                                'Яндекс.Метрике, Google Tag Manager, Optimize, '
                                                                'Google Data Studio и Excel',
                                                    thumb_url='https://imagizer.imageshack.com/img923/2681/KyyMhJ.png',
                                                    reply_markup=nt_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent('netology12'),
                                                    title='Анализ статистики сайта с помощью Яндекс.Метрики',
                                                    description='Для отслеживания поведение посетителей на сайте, '
                                                                'оценки отдачи от рекламных кампаний',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7376/AKFeM9.jpg',
                                                    reply_markup=nt_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent('netology13'),
                                                    title='Математика для анализа данных',
                                                    description='Если специалист не разбирается в этих направлениях — гипотезы и выводы будут неточными',
                                                    thumb_url='https://imagizer.imageshack.com/img924/6558/aWldIr.png',
                                                    reply_markup=nt_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent('netology14'),
                                                    title='Основы поисковой оптимизации (SEO)',
                                                    description='Как использовать факторы ранжирования и работать с '
                                                                'разными типами пользовательских запросов',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8043/IcXiRk.png',
                                                    reply_markup=nt_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent('netology15'),
                                                    title='Исследуйте в R',
                                                    description='Прокачайтесь до уровня middle в прогнозировании и '
                                                                'визуализации в R-Studio',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8065/1ES0y7.jpg',
                                                    reply_markup=nt_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'otus':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('otus1'),
                                                   title='iOS-разработчик. Базовый курс',
                                                   description=' Все что нужно чтобы '
                                                               'претендовать на должность iOS-разработчика уровня '
                                                               'junior+',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ot_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('otus2'),
                                                   title='iOS Разработчик. Продвинутый курс v 2.0',
                                                   description="Вся мощь Swift 5.2 для развития профессиональных "
                                                               "навыков уровня Middle/Senior iOS Developer",
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ot_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('otus3'),
                                                   title='Разработчик Golang',
                                                   description='При переходе на Go люди зачастую сталкиваются с '
                                                               'различными неудобствами, вызванными непохожестью Go '
                                                               'на другие языки программирования.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/6091/eGiQd7.png',
                                                   reply_markup=ot_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('otus4'),
                                                   title='Framework Laravel',
                                                   description='Веб-фреймворк, который сделает вашу работу '
                                                               'интереснее, проще и быстрее',
                                                   thumb_url='https://imagizer.imageshack.com/img922/635/Psn8zD.png',
                                                   reply_markup=ot_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('otus5'),
                                                   title='Облачные сервисы',
                                                   description='Именно такие специалисты являются самыми '
                                                               'востребованными и высокооплачиваемыми в крупных '
                                                               'мировых проектах: Google, Amazon, Microsoft, Yandex, '
                                                               'Сбербанк и др.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/2545/AP0Y2X.png',
                                                   reply_markup=ot_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('otus6'),
                                                   title='Подготовительный курс по JavaScript разработке',
                                                   description='Подготовка к курсам "Fullstack разработчик '
                                                               'Javascript", "React.js-разработчик" и '
                                                               '"Node.js-разработчик"',
                                                   thumb_url='https://imagizer.imageshack.com/img923/1618/5C7tcM.png',
                                                   reply_markup=ot_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('otus7'),
                                                   title='Разработчик Python',
                                                   description="Best Practice по решению прикладных задач и освоению "
                                                               "инструментов, применяемых программистом при "
                                                               "разработке инфраструктурных решений, веб-приложений, "
                                                               "систем контроля качества и аналитических систем",
                                                   thumb_url='https://imagizer.imageshack.com/img923/5372/T4pET7.jpg',
                                                   reply_markup=ot_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('otus8'),
                                                   title='Data Engineer',
                                                   description='Ученый может открыть новую звезду, но не может ее '
                                                               'создать. Ему придется просить инженера сделать это за'
                                                               ' него.–Гордон Линдсей Глегг',
                                                   thumb_url='https://imagizer.imageshack.com/img924/1946/u1kjso.png',
                                                   reply_markup=ot_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('otus9'),
                                                   title='Backend разработчик на PHP',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса разработки на PHP',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8519/rNEsyy.png',
                                                   reply_markup=ot_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent('otus10'),
                                                    title='С++ для начинающих программистов',
                                                    description='Курс по разработке на C++ для начинающих программистов',
                                                    thumb_url='https://imagizer.imageshack.com/img924/5227/UQUaCm.jpg',
                                                    reply_markup=ot_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent('otus11'),
                                                    title='Архитектура и шаблоны проектирования ',
                                                    description='изучить основные паттерны проектирования и научиться '
                                                                'применять их, находить им замену в сложных ситуация '
                                                                'и научиться мыслить, как архитектор программного '
                                                                'обеспечения',
                                                    thumb_url='https://imagizer.imageshack.com/img924/6048/vhXoet.png',
                                                    reply_markup=ot_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent('otus12'),
                                                    title='Пентест. Практика тестирования на проникновение',
                                                    description='Пентестер выявляет уязвимости информационной системы '
                                                                'и дает заказчику рекомендации по их устранению',
                                                    thumb_url='https://imagizer.imageshack.com/img922/2896/9w3dE2.png',
                                                    reply_markup=ot_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent('otus13'),
                                                    title='MS SQL Server разработчик',
                                                    description='Во время курса будем подробно разбирать язык '
                                                                'запросов и внутренние процессы СУБД, происходящие на '
                                                                'всех этапах работы с запросом.',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9613/K0j4q3.jpg',
                                                    reply_markup=ot_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent('otus14'),
                                                    title='Реляционные СУБД',
                                                    description='Курс включает в себя все основные и популярные БД, '
                                                                'которые могут пригодиться разработчику: PostgreSQL, '
                                                                'MySQL, Redis, MongoDB, Cassandra и т.д.',
                                                    thumb_url='https://imagizer.imageshack.com/img922/7028/PuKrke.png',
                                                    reply_markup=ot_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent('otus15'),
                                                    title='Python QA Engineer',
                                                    description='Как решаются задачи автоматизации тестирования на '
                                                                'реальных проектах с использованием языка Python.',
                                                    thumb_url='https://imagizer.imageshack.com/img922/3263/upmrEN.png',
                                                    reply_markup=ot_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'webformyself':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent('webformyself1'),
                                                   title='Веб-дизайнер профессионал',
                                                   description='Создавайте востребованные макеты быстро,легко и... '
                                                               'дорого',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3433/nlxsIn.jpg',
                                                   reply_markup=wb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent('webformyself2'),
                                                   title='Фриланс - Мастер',
                                                   description='Мощный видеокурс от Webformyself о том, '
                                                               'как добиваться успеха, работая удаленно',
                                                   thumb_url='https://imagizer.imageshack.com/img922/658/oOjZm0.png',
                                                   reply_markup=wb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent('webformyself3'),
                                                   title='Верстка-Мастер',
                                                   description='ОТ ТЕОРИИ ДО ВЕРСТКИ ПОПУЛЯРНЫХ ШАБЛОНОВ',
                                                   thumb_url='https://imagizer.imageshack.com/img923/2302/ehsKgx.jpg',
                                                   reply_markup=wb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent('webformyself4'),
                                                   title='JavaScript. Полное руководство для современной веб-разработки',
                                                   description='Изучите самый популярный язык разработки и станьте '
                                                               'высокооплачиваемым профи',
                                                   thumb_url='https://imagizer.imageshack.com/img923/5725/YEk2bu.png',
                                                   reply_markup=wb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent('webformyself5'),
                                                   title='PHP-Мастер. От теории до собственной CMS интернет-магазина',
                                                   description='Абсолютное большинство всех сайтов в интернете '
                                                               'написаны на PHP.',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8404/5etgXb.jpg',
                                                   reply_markup=wb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent('webformyself6'),
                                                   title='1-С Битрикс. Практика создания веб-проектов',
                                                   description="Новый фундаментальный курс поможет вам в считанные "
                                                               "недели овладеть профессиональной разработкой на CMS "
                                                               "1C-Битрикс с нуля.",
                                                   thumb_url='https://imagizer.imageshack.com/img924/4378/TRcSpV.jpg',
                                                   reply_markup=wb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent('webformyself7'),
                                                   title='FullStack-Мастер: Разработка CRM-системы на Node.js, '
                                                         'Express, Angular 6',
                                                   description='Впервые в одном видеокурсе раскрыт полный пошаговый '
                                                               'алгоритм FullStack JavaScript-разработки!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5864/QVWdgz.png',
                                                   reply_markup=wb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent('webformyself8'),
                                                   title='ReactJS с Нуля до Профи',
                                                   description='Овладейте Frontend-разработкой на стеке React.js',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8393/RUvgWb.jpg',
                                                   reply_markup=wb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent('webformyself9'),
                                                   title='Курс по CSS3 ',
                                                   description='Простота использования, ускорение процесса разработки '
                                                               'и оформления web страниц, уменьшение количества кода, '
                                                               'практически 100% кроссбраузерность',
                                                   thumb_url='https://imagizer.imageshack.com/img924/2403/uuq2Tn.jpg',
                                                   reply_markup=wb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself10'),
                                                    title='Курс по базе данных MySQL',
                                                    description='Посвящен изучению языка запросов SQL и работе с '
                                                                'сервером MySQL.',
                                                    thumb_url='https://imagizer.imageshack.com/img923/1227/cGGBNH.png',
                                                    reply_markup=wb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself11'),
                                                    title='Cоздание каталога товаров с помощью PHP, MySQL и jQuery',
                                                    description='Написанный в курсе движок, можно будет использовать '
                                                                'как для каталога, так и для любого другого сайта: '
                                                                'визитка, интернет-магазин, корпоративный сайт, блог.',
                                                    thumb_url='https://imagizer.imageshack.com/img923/3650/B59cvX.jpg',
                                                    reply_markup=wb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself12'),
                                                    title='Библиотека JQuery UI',
                                                    description='Научимся создавать элементы пользовательского '
                                                                'интерфейса, используя библиотеку jQuery UI',
                                                    thumb_url='https://imagizer.imageshack.com/img922/6707/QGdV0V.png',
                                                    reply_markup=wb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself13'),
                                                    title='WordPress-Мастер. Разработка тем для WordPress с нуля',
                                                    description='Вам станет подвластна CMS №1 в мире по популярности',
                                                    thumb_url='https://imagizer.imageshack.com/img924/273/rEutMJ.jpg',
                                                    reply_markup=wb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself14'),
                                                    title='Создание интернет-магазина на CMS WordPress',
                                                    description='Если Вы задались целью создать несложный '
                                                                'интернет-магазин, тогда обратите внимание на данный '
                                                                'курс',
                                                    thumb_url='https://imagizer.imageshack.com/img924/273/rEutMJ.jpg',
                                                    reply_markup=wb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'webformyself15'),
                                                    title='Angular 4 с Нуля до Профи',
                                                    description='Мы начнем с самых основ и закончим созданием с нуля '
                                                                'полностью рабочего реактивного приложения, '
                                                                'где вы увидите все шаги по его созданию.',
                                                    thumb_url='https://imagizer.imageshack.com/img924/6950/L9ZLXC.jpg',
                                                    reply_markup=wb_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    print(call.data)
    global content
    try:
        with open('stats.txt', mode='w') as file:
            content[query_with_fetchone('position_of_pointer', call.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', call.from_user.id)][:-25] + call.data + ' ' + content[
                                                                                         query_with_fetchone(
                                                                                             'position_of_pointer',
                                                                                             call.from_user.id)][
                                                                                     -25:]
            file.writelines(content)
    except:
        pass
    if 'success' in call.data:
        chat_id = ''.join([i for i in call.data[-13:] if i.isdigit()])
        bot.send_message(909435473,
                         text='Заказ под номером  ' + chat_id + ' подтвержден от @' + query_with_fetchone('user',
                                                                                                          chat_id))
        bot.send_message(chat_id,
                         text='Спасибо за покупку!\nВот ваш заказ:\nhttps://cloud.mail.ru/public/7BRK/JuvmnLWdU')
    elif 'pay' in call.data:
        if not query_with_fetchone('flag_for_confirmation_of_payment', call.from_user.id):
            bot.send_message(call.from_user.id,
                             text='После совершения покупки нажмите кнопку ниже, чтобы получить товар',
                             reply_markup=confirmation())
        update_flag_for_confirmation_of_payment(1, call.from_user.id)
        update_payment_course(call.data, call.from_user.id)
        if '16' in call.data:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('5000',
                                                                   'https://oplata.qiwi.com/form?invoiceUid=12252f8a-cf6d-4417-9243-4b137f68fdfd',
                                                                   call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('5000',
                                                                   'https://oplata.qiwi.com/form?invoiceUid=12252f8a-cf6d-4417-9243-4b137f68fdfd',
                                                                   call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('5000', 'https://github.com/', call.from_user.id))
        elif 'all' in call.data:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.from_user.id))
        elif call.data[3:7] in ['geek', 'neto', 'otus', 'webf', 'udem', 'skil']:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.from_user.id))
    elif call.data == 'confirmed':
        bot.send_message(chat_id=909435473,
                         text=query_with_fetchone('payment_course', call.from_user.id) + ' @' + query_with_fetchone(
                             'user', call.from_user.id) + '\n' + str(call.from_user.id),
                         reply_markup=successful_payment(call.from_user.id))
        bot.delete_message(call.from_user.id, call.message.message_id)
        bot.send_message(call.from_user.id, text='Ваш заказ принят, ожидайте подтверждения')
        update_flag_for_confirmation_of_payment(0, call.from_user.id)
    elif call.data == 'disconf':
        bot.delete_message(call.from_user.id, call.message.message_id)
        update_flag_for_confirmation_of_payment(0, call.from_user.id)
    elif call.data == 'moderator':
        if not query_with_fetchone('flag_moderator', call.from_user.id):
            update_flag_moderator(1, call.from_user.id)
            bot.send_message(chat_id=call.from_user.id, text='По всем вопросам пишите:\n@official_aldarkose')
    elif call.data == 'copyright':
        if not query_with_fetchone("flag_copyright", call.from_user.id):
            update_flag_copyright(1, call.from_user.id)
            bot.send_message(chat_id=call.from_user.id,
                             text='Если вы обладатель курса, то можете оставить жалобу здесь:\n@AltynsarynCopyrightBot')
    elif call.data == 'new_com':
        if not query_with_fetchone("flag_new_com", call.from_user.id):
            update_flag_new_com(1, call.from_user.id)
            bot.send_message(call.from_user.id, text='Вы можете написать отзыв здесь:\n@AlynsarynCommentsBot')
    elif call.data == 'comments':
        if not query_with_fetchone('flag_comments', call.from_user.id):
            update_flag_comments(1, call.from_user.id)
            bot.send_message(call.from_user.id,
                             text='Здесь вы можете посмотреть отзывы здесь:\nhttps://t.me/joinchat/AAAAAFR7paS_hiUvmuspfw')
    elif call.data == 'cancel':
        bot.delete_message(call.from_user.id, call.message.message_id)
        update_flag_for_cancel_payment(0, call.from_user.id)
        update_flag(0, call.from_user.id)
    elif 'pay' not in call.data and (
            not query_with_fetchone('flag_for_cancel_payment', call.from_user.id) or 'rep' in call.data):
        if not query_with_fetchone("flag", call.from_user.id):
            update_flag(1, call.from_user.id)
            update_flag_for_cancel_payment(1, call.from_user.id)
            if call.message:
                update_payment_course(call.data[:18], call.from_user.id)
                bot.send_message(chat_id=call.from_user.id,
                                 text="Выберите способ оплаты:", reply_markup=payment_method(call.from_user.id))
            else:
                update_payment_course(call.data[:18], call.from_user.id)
                bot.send_message(chat_id=call.from_user.id, text="Выберите способ оплаты:",
                                 reply_markup=payment_method(call.from_user.id))
        else:
            if call.message:
                update_payment_course(call.data[:18], call.from_user.id)
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text="Выберите способ оплаты:", reply_markup=payment_method(call.from_user.id))
            else:
                update_payment_course(call.data[:18], call.from_user.id)
                bot.send_message(chat_id=call.from_user.id, text="Выберите способ оплаты:",
                                 reply_markup=payment_method(call.from_user.id))


@bot.message_handler(commands=['start'])
def startpg(message):
    global content
    update_position_of_pointer(0, message.from_user.id)
    if message.from_user.last_name and message.from_user.username:
        user = message.from_user.username + ' ' + message.from_user.first_name + ' ' + message.from_user.last_name
    elif message.from_user.last_name:
        user = 'NoUsermane' + message.from_user.last_name + ' ' + message.from_user.first_name
    elif message.from_user.username:
        user = message.from_user.username + ' ' + message.from_user.first_name
    else:
        user = 'NoUsermane' + message.from_user.first_name
    if not query_with_fetchone('client_id', message.from_user.id):
        insert_user(message.from_user.id, message.message_id, user)
    try:
        with open('stats.txt', mode='r') as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w') as file:
            if content:
                for i in range(len(content)):
                    t = time.strftime('%c', time.gmtime(time.time()))
                    if str(message.from_user.id) in content[i]:
                        update_position_of_pointer(i, message.from_user.id)
                        break
                if (content[query_with_fetchone('position_of_pointer', message.from_user.id)][-21:-18] != t[-20:-17] and
                    content[query_with_fetchone('position_of_pointer', message.from_user.id)][-17:-15] == t[-16:-14]) or \
                        content[query_with_fetchone('position_of_pointer', message.from_user.id)][-17:-15] != t[
                                                                                                              -16:-14]:
                    content[query_with_fetchone('position_of_pointer', message.from_user.id)] = content[
                                                                                                    query_with_fetchone(
                                                                                                        'position_of_pointer',
                                                                                                        message.from_user.id)][
                                                                                                :-1] + ' ' + t + \
                                                                                                content[
                                                                                                    query_with_fetchone(
                                                                                                        'position_of_pointer',
                                                                                                        message.from_user.id)][
                                                                                                    -1]
                elif str(message.from_user.id) not in content[
                    query_with_fetchone('position_of_pointer', message.from_user.id)]:
                    content.append(
                        str(message.from_user.id) + ' ' + time.strftime('%c', time.gmtime(time.time())) + '\n')
                    update_position_of_pointer(len(content) - 1, message.from_user.id)
                file.writelines(content)
            else:
                file.write(str(message.from_user.id) + ' ' + time.strftime('%c', time.gmtime(time.time())) + '\n')
    except:
        with open('stats.txt', mode='w') as file:
            file.seek(0)
            content = [str(message.from_user.id) + ' ' + time.strftime('%c', time.gmtime(time.time())) + '\n']
            file.writelines(content)
    try:
        with open('stats.txt', mode='w') as file:
            content[query_with_fetchone('position_of_pointer', message.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', message.from_user.id)][:-25] + message.text + ' ' + content[
                                                                                               query_with_fetchone(
                                                                                                   'position_of_pointer',
                                                                                                   message.from_user.id)][
                                                                                           -25:]
            file.writelines(content)
    except:
        pass
    if message.from_user.id == 442051731:
        bot.send_message(message.from_user.id, text='Присоединился Gold Administrator')
    main_keyboard = types.ReplyKeyboardMarkup(True, False)
    main_keyboard.row('Все 999 курса за 100кзт')
    bot.send_message(message.from_user.id, 'Привет {name}!'.format(name=message.chat.first_name),
                     reply_markup=main_keyboard)
    main_menu = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Список курсов', switch_inline_query_current_chat='courses')
    but_2 = types.InlineKeyboardButton(text='Связавться с модератором', callback_data='moderator')
    but_3 = types.InlineKeyboardButton(text='Правообладателям', callback_data='copyright')
    but_4 = types.InlineKeyboardButton(text='Оставить отзыв', callback_data='new_com')
    but_5 = types.InlineKeyboardButton(text='Отзывы', callback_data='comments')
    main_menu.add(but_1)
    main_menu.add(but_2)
    main_menu.add(but_3)
    main_menu.add(but_4, but_5)
    bot.send_message(message.from_user.id,
                     'Я бот, который продает курсы по программированию !\n', reply_markup=main_menu)
    update_previous_message_id(message.message_id + 3, message.from_user.id)
    update_flag_for_confirmation_of_payment(0, message.from_user.id)
    update_flag_moderator(0, message.from_user.id)
    update_flag_copyright(0, message.from_user.id)
    update_flag_new_com(0, message.from_user.id)
    update_flag_comments(0, message.from_user.id)
    update_payment_course('', message.from_user.id)


@bot.message_handler(content_types=['text'])
def essential(message):
    global content
    try:
        with open('stats.txt', mode='w') as file:
            content[query_with_fetchone('position_of_pointer', message.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', message.from_user.id)][:-25] + message.text + ' ' + content[
                                                                                               query_with_fetchone(
                                                                                                   'position_of_pointer',
                                                                                                   message.from_user.id)][
                                                                                           -25:]
            file.writelines(content)
    except:
        pass
    photo = 0
    update_flag_for_cancel_payment(0, message.from_user.id)
    update_flag(0, message.from_user.id)
    update_flag_for_confirmation_of_payment(0, message.from_user.id)
    update_flag_moderator(0, message.from_user.id)
    update_flag_copyright(0, message.from_user.id)
    update_flag_new_com(0, message.from_user.id)
    update_flag_comments(0, message.from_user.id)
    update_payment_course(message.text, message.from_user.id)
    school = ''.join([i for i in message.text if not i.isdigit()])
    url = 'https://www.geeksforgeeks.org/python-ways-to-remove-numeric-digits-from-given-string/'
    print(query_with_fetchone('previous_message_id', message.from_user.id))
    try:
        i = 0
        while query_with_fetchone('previous_message_id', message.from_user.id) + i < message.message_id:
            print(query_with_fetchone('previous_message_id', message.from_user.id))
            bot.delete_message(message.from_user.id,
                               query_with_fetchone('previous_message_id', message.from_user.id) + i)
            i += 1
        update_previous_message_id(message.message_id, message.from_user.id)
    except:
        update_previous_message_id(message.message_id, message.from_user.id)
    if message.text == 'Все 999 курса за 100кзт':
        bot.send_photo(message.from_user.id,
                       photo='AgACAgIAAxkBAAIORV8dRTR-QS2LbL9pvCXhBcZ_mdKdAAInrzEbWwPwSJzKGpKODmu4jWkYlS4AAwEAAwIAA20AAzMAAQIAARoE',
                       caption='Dai deneg', reply_markup=all_courses())
    elif message.text == 'geekbrains1':
        text = '<strong>[GeekBrains] Профессия Разработчик игр</strong>\n \n<strong>Описание:</strong>\nЭта профессия позволяет исполнить мечту увлеченного геймера: сделать игру, в которой не будет недостатков. Разработчик игр создает концепцию и прототип игры, выбирает средства для реализации проекта.\n \n<strong>Вы научитесь:</strong>\n🎮Git\n🎮Основы C#\n🎮Unity и C#\n🎮Архитектура и шаблоны проектирования\n \n🤢Цена курса: ̶7̶2̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶2̶1̶ ̶9̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/game_developer'
        photo = geekbrains_courses[0]
    elif message.text == 'geekbrains2':
        text = '<strong>[GeekBrains] Профессия Программист Android</strong>\n \n<strong>Описание:</strong>\nРазработка под Android — это создание игр и полезных приложений под 80% мобильных устройств. Android — открытая и свободная система, настроенная к модернизации и адаптации, она позволяет реализовать самые смелые фантазии программиста.\n \n<strong>Вы научитесь:</strong>\n🤖Git. Базовый курс\n🤖Java Core. \n🤖Android. \n🤖Android. Популярные библиотеки.\n🤖Базы данных.\n \n🤢Цена курса:  ̶8̶4̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶9̶2̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/android_developer'
        photo = geekbrains_courses[1]
    elif message.text == 'geekbrain7':
        text = '<strong>[GeekBrains] Создание сайтов и приложений. Методы повышения конверсии</strong>\n \n<strong>Описание:</strong>\nЭтот курс даст вам доступ к мощным маркетинговым инструментам. Вы узнаете, что действительно важно, а что необязательно, а порой даже вредно. \nАкцент сделан на начинающих специалистов, поэтому информация представлена максимально просто.\n \n<strong>Вы научитесь:</strong>\n🌊Создавать действительно продающие структуры сайтов;\n🌊Повышать эффективность сайта в несколько раз;\n🌊Обыгрывать конкурентов в интернет маркетинге благодаря анализу;\n🌊Подготавливать проект для создания мобильной версии продукта;\n🌊Проводить качественный аудит сайта;\n \n🤢Цена курса:  ̶1̶1̶ ̶3̶7̶0̶₽ ̶/̶ ̶6̶6̶ ̶6̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/100'
        photo = geekbrains_courses[6]
    elif message.text == 'geekbrains3':
        text = '<strong>[GeekBrains] Профессия Frontend-разработчик</strong>\n \n<strong>Описание:</strong>\nFrontend-разработчик создаёт интерфейсы, с которыми будут взаимодействовать пользователи, верстает сайты по современным стандартам, виртуозно владеет JavaScript, HTML, CSS.\n \n<strong>Вы научитесь:</strong>\n🧨Основы HTML/CSS и PHP.\n🧨HTML/CSS.\n🧨JavaScript.\n🧨Основы баз данных.\n🧨ReactJS.\n \n🤢Цена курса: ̶1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶₽ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶₸̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://geekbrains.ru/professions/frontend_developer'
        photo = geekbrains_courses[2]
    elif message.text == 'geekbrains5':
        text = '<strong>[GeekBrains] Профессия Веб-разработчик</strong>\n \n<strong>Описание:</strong>\nВеб-разработчики создают и обслуживают сайты, порталы. Они верстают пользовательские интерфейсы веб-ресурсов, проектируют серверную часть, которая обеспечивает работу всех функций и хранение данных.\n \n<strong>Вы научитесь:</strong>\n✨HTML/CSS.\n✨Основы работы с Git\n✨HTML5 и CSS3.\n✨JavaScript.\n✨Проектирование БД и запросы SQL\n✨PHP. \n✨Laravel. Глубокое погружение\n \n🤢Цена курса:  ̶9̶6̶ ̶0̶0̶0̶₽ ̶/̶ ̶5̶6̶2̶ ̶5̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸  \n'
        url = 'http://geekbrains.ru/professions/web_developer'
        photo = geekbrains_courses[4]
    elif message.text == 'geekbrains8':
        text = '<strong>[GeekBrains] Факультет Python-разработки</strong>\n \n<strong>Описание:</strong>\nСтаньте программистом Python и изучите один из самых востребованных навыков современной разработки!\n \n<strong>Вы научитесь:</strong>\n🔥Backend-разработка\n🔥Frontend и Backend интернет-магазина\n🔥Сетевой чат\n🔥Архитектура и шаблоны проектирования на Python\n🔥Компьютерные сети\n🔥Продвинутый курс Javascript\n \n🤢Цена курса: 1̶8̶0̶ ̶0̶0̶0̶₽ ̶/̶ ̶1̶ ̶0̶5̶4̶ ̶8̶0̶0̶₸\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/geek_university/python'
        photo = geekbrains_courses[7]
    elif message.text == 'geekbrains9':
        text = '<strong>[GeekBrains] Системный администратор </strong>\n \n<strong>Описание:</strong>\nСистемный администратор обеспечивает бесперебойное функционирование компьютерной техники и программного обеспечения в организации. Он занимается поддержкой серверов, проектирует и администрирует локальную сеть, выдаёт пользователям доступ к сайтам.\n \n<strong>Вы научитесь:</strong>\n🛡Проектирование БД и запросы SQL\n🛡Классика computer science\n🛡Практика администрирования ОС Linux на компьютере\n🛡Операционные системы\n🛡Безопасность компьютерных сетей\n🛡Основные сервисы на Linux для предприятия\n \n🤢Цена курса:  ̶7̶0̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶1̶0̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/sys_admin'
        photo = geekbrains_courses[8]
    elif message.text == 'geekbrains10':
        text = '<strong>[GeekBrains] Дизайнер интерфейсов </strong>\n \n<strong>Описание:</strong>\nДизайнер UX/UI проектирует взаимодействие пользователя с сайтом, приложением или сервисом и создает визуальные элементы, систему и прототип интуитивно понятного интерфейса.\n \n<strong>Вы научитесь:</strong>\n✨Основы Adobe Illustrator\n✨Figma\n✨Базовые знания. Дизайн\n✨Адаптивный дизайн\n✨Adobe After Effects\n \n🤢Цена курса:   ̶8̶5̶ ̶5̶0̶0̶ ̶₽̶ ̶/̶ ̶4̶9̶3̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://geekbrains.ru/geek_university/interface-design'
        photo = geekbrains_courses[9]
    elif message.text == 'geekbrains11':
        text = '<strong>[GeekBrains] 1С-Битрикс: Управление сайтом</strong>\n \n<strong>Описание:</strong>\nКурс предназначен для тех разработчиков, кто собирается работать с CMS 1C-Битрикс и хочет узнать подробнее о ее функционале и настройках.\n \n<strong>Вы научитесь:</strong>\n💣Выбирать правильные редакции и решения для своего веб-проекта на CMS Битрикс;\n💣Устанавливать и запускать сайт на CMS Битрикс.\n💣Проектировать бизнес-логику своих веб-приложений, создавать структуру и навигацию.\n💣Интегрировать HTML-верстку в проект.\n💣Работать с компонентами CMS Битрикс и расширять их базовые возможности.\n💣Настраивать информационные блоки и выводить динамическую информацию на сайте.\n \n🤢Цена курса: ̶9̶ ̶9̶0̶0̶₽ ̶/̶ ̶5̶8̶ ̶0̶0̶0̶₸̶\n🤑Наша цена:  390₽ / 1990₸\n'
        url = 'http://geekbrains.ru/courses/26'
        photo = geekbrains_courses[10]
    elif message.text == 'geekbrains6':
        text = '<strong>[GeekBrains] </strong><strong>Yii2 </strong><strong>Профессиональная Backend-разработка</strong>\n \n<strong>Описание:</strong>\nYii2 framework - oдин из самых популярных и востребованных фреймворков на PHP. Знание любого фреймворка качественно увеличивает востребованность php-программиста на рынке труда, и его оклад.\n \n<strong>Вы научитесь:</strong>\n🌊Настраивать веб-сервер и разворачивать приложение;\n🌊Проектировать БД и работать с моделями и формами Yii;\n🌊Работать с генератором кода;\n🌊Управлять кэшированием;\n🌊Использовать расширения и особенности фреймворка;\n \n🤢Цена курса: 1̶5̶ ̶0̶0̶0̶₽ ̶/̶ ̶8̶7̶ ̶9̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/35'
        photo = geekbrains_courses[5]
    elif message.text == 'geekbrains12':
        text = '<strong>[GeekBrains] Школа Программирования. Java 0, 1, 2.</strong>\n \n<strong>Описание:</strong>\nНа Java пишут игры, мобильные и десктопные приложения, enterprise-проекты, серверные проекты в сфере финансовых услуг, инструменты для обработки Big Data.\nИз-за широкой сферы применения и кроссплатформенности языка программирования Java-разработчики крайне востребованы в IT-компаниях.\n \n<strong>Вы научитесь:</strong>\n🔥Java SE 8 и выше\n🔥Основы работы с Git\n🔥Проектирование БД и запросы SQL\n🔥Алгоритмы Java. \n🔥HTML/CSS.\n🔥Создание веб-приложений на Java\n \n🤢Цена курса:   ̶6̶6̶ ̶0̶0̶0̶₽ ̶/̶ ̶3̶8̶6̶ ̶7̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/java_developer'
        photo = geekbrains_courses[11]
    elif message.text == 'geekbrains13':
        text = '<strong>[GeekBrains] Базы данных для профессионалов и язык SQL</strong>\n \n<strong>Описание:</strong>\nНи одно современное веб-приложение, и не только веб, не обходится без долговременного хранилища данных. И для многих приложений таким решением становится MySQL. Зарекомендовавшая себя на многих популярных и больших проектах, эта СУБД развивается и является одним из основных решений для организации баз данных.\n \n<strong>Вы научитесь:</strong>\n💾Проектировать БД для наиболее эффективного их построения\n💾Создавать БД по созданным проектам\n💾Строить простые и сложные запросы на выборки данных\n💾Анализировать производительность запросов и оптимизировать их\n💾Писать транзакции\n💾Администрировать БД\n \n🤢Цена курса:   ̶1̶5̶ ̶0̶0̶0̶₽ ̶/̶ ̶8̶7̶ ̶9̶0̶0̶₸\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/1181'
        photo = geekbrains_courses[12]
    elif message.text == 'geekbrains14':
        text = '<strong>[GeekBrains] Анатомия блокчейна</strong>\n \n<strong>Описание:</strong>\nРазбираться в криптовалютах. Вы поймете, в чем их смысл, сможете читать официальную документацию проекта (whitepaper), оценивать идеи, понимать описания криптопротоколов.\nПонимать, как построены сервисы, обеспечивающие безопасность коммуникаций между участниками. Вы сможете оценить техническое выполнение проекта и оригинальность замысла.\n \n<strong>Вы научитесь:</strong>\n💸Введение в криптографию\n💸Блокчейн\n💸Практическая работа с криптовалютой, кошельками и биржами.\n💸Использование блокчейн для проведения ICO.\n \n🤢Цена курса:   ̶2̶0̶ ̶0̶0̶0̶₽̶ ̶/̶ ̶1̶1̶7̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://geekbrains.ru/blockchain'
        photo = geekbrains_courses[13]
    elif message.text == 'geekbrains4':
        text = '<strong>[GeekBrains] Курс по Agile-методологиям</strong>\n \n<strong>Описание:</strong>\nКогда дедлайны горят, заказчик дает новые вводные, а в продуктах встречаются ошибки, используйте Agile-метод. С помощью гибкого подхода вы будете отслеживать развитие проекта на всех этапах, оценивать риски и расставлять приоритеты.\n \n<strong>Вы научитесь:</strong>\n🌟Примените полученные знания для практической работы Agile-команде\n🌟Научитесь оценивать задачи и свои возможности\n🌟Научитесь оптимизировать рабочие процессы и и нагрузку\n \n🤢Цена курса:   ̶9̶ ̶9̶0̶0̶₽̶ ̶/̶ ̶5̶8̶ ̶0̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://intensives.geekbrains.ru/agile'
        photo = geekbrains_courses[3]
    elif message.text == 'geekbrains15':
        text = '<strong> [GeekBrains] Node.js Серверное программирование на JavaScript</strong>\n \n<strong>Описание:</strong>\nЭволюция JavaScript с каждым годом дает возможность для веб-разработчиков создавать большое количество новых технологий и инновационных приложений. Один из наиболее интересных и популярных инструментов для создания легко масштабируемых сетевых приложений является Node.js – это серверная реализация языка программирования JavaScript, основанная на движке V8.\n \n<strong>Вы научитесь:</strong>\n☁️Создавать консольные утилиты на Node.js;\n☁️Создавать веб-сервисы с помощью популярного фреймворка Express.js;\n☁️Применять шаблонизаторы для разделения кода и оформления интерфейса в проекте;\n☁️Создавать и использовать различные REST API;\n☁️Использовать в программе веб-сокеты с помощью socket.io\n \n🤢Цена курса:    ̶1̶5̶ ̶0̶0̶0̶₽̶ ̶/̶ ̶8̶6̶ ̶7̶0̶0̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/11'
        photo = geekbrains_courses[14]
    elif message.text == 'netology1':
        text = '<b> [Нетология] PHP/SQL: back-end разработка и базы данных\n\nОписание:</b> \nПод PHP работает 80% сайтов, в том числе Facebook, «ВКонтакте» и «Википедия». В преподавательском составе "Нетологии" состоят только опытные и бывалые разработчики, которые проведут вас в мир программирования и сделают востребованным специалистом!\n<b>Вы научитесь:</b>\n🔥работать со строками, массивами и объектами;\n🔥устанавливать и настраивать веб-сервера;\n🔥создавать классы и объекты в ООП;\n🔥управлять таблицами и базами данных в MySQL.\n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ₽̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 390 ₽ / 1990 ₸'
        url = 'https://it-events.com/events/6470'
        photo = netology_courses[0]
    elif message.text == 'netology2':
        text = '<b>[Нетология]Веб-дизайн: Эффективный сайт от идеи до реализации\n\nОписание:</b>\n Пользователи курса «Веб дизайн. Обучение с нуля» узнают о таких понятиях и инструментах интернет-разработки, как:\n🌟разработка дизайн-макета;\n🌟тестирование и взаимодействие с пользователями;\n🌟векторные и растровые изображения;\n🌟основы работы с цветом;\n🌟веб-типографика;\n🌟подготовка портфолио;\n🌟презентация проекта клиенту.\n\n🤢Цена курса:  ̶3̶4̶ ̶0̶0̶0̶ ₽ ̶/̶̶̶ ̶2̶0̶2̶ ̶0̶0̶0̶ ₸̶̶̶\n🤑Наша цена: 390 ₽ / 1990 ₸'
        url = 'https://netology.ru/programs/web-design'
        photo = netology_courses[1]
    elif message.text == 'netology3':
        text = '<b>[Нетология] Python для работы с данными\n\nОписание:</b>\nPython — простой и универсальный инструмент для решения любых аналитических задач.\n👨‍💻Автоматизируйте свою рутинную работу с помощью Python\n🦾Обрабатывайте большие объемы информации без администрирования и баз данных\n🤖Освойте ключевой инструмент в мире аналитики и машинного обучения\n<b>Ключевые навыки</b>\n⚡️Работа с сырыми данными и их подготовка для анализа\n⚡️Работа с аналитическими библиотеками numpy, scipy и pandas\n⚡️Визуализация данных с помощью библиотек seaborn, plotly, matplotlib\n⚡️Статистический анализ данных\n⚡️Применение математических моделей\n⚡️Выбор и создание фич\n\n🤢Цена курса:  ̶4̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶7̶0̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390 ₽ / 1990 ₸ '
        photo = netology_courses[2]
    elif message.text == 'netology4':
        text = '<b>[Нетология] Профессия Аналитик данных\n\nОписание:</b>\nНаучим с нуля собирать, анализировать и презентовать данные.Получите востребованную профессию с зарплатой от 400 000 ₸. (по данным hh.kz)\n<b>Ключевые навыки:</b>\n🌟Сбор и подготовка данных для анализа\n🌟Визуализация данных\n🌟Сбор и понимание бизнес-требований заказчика\n🌟Подготовка ad-hoc исследований и аналитики\n🌟Тестирование гипотез\n🌟Умение писать сложные запросы на SQL\n🌟Python для анализа данных\n🌟Знание основ работы с Hadoop\n\n🤢Цена курса:  ̶1̶0̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶5̶8̶5̶ ̶5̶0̶0̶ ̶₸\n🤑Наша цена: 390 ₽ / 1990 ₸ '
        photo = netology_courses[3]
    elif message.text == 'netology5':
        text = ' <strong>[Нетология] SQL и получение данных</strong>\n\n<strong>Описание: </strong>\n<strong>Программа обучения SQL</strong> — первый шаг в профессиональном росте дата саентистов и аналитиков данных в сильных командах и проектах. Без владения SQL невозможно будет вырасти выше уровня junior.\n \n<strong>Возможности после обучения:</strong>\n🌊Овладеете языком запросов SQL\nПознакомитесь с разнообразным окружением БД: git, виртуальные машины, linux\n🌊Углубите знания SQL\nПерейдёте от исполнения запросов к написанию функций\n🌊Найдёте общий язык с разработчиками\nУлучшите понимание процессов инжиниринга данных\n \n🤢Цена курса:  ̶2̶3̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶1̶4̶3̶ ̶4̶0̶0̶ ̶₸̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/sql-lessons#/'
        photo = netology_courses[4]
    elif message.text == 'netology6':
        text = '<strong>[Нетология] Power BI: анализ и визуализация данных без программирования</strong>\n \n<strong>Описание:</strong>\nBI-платформы — инструмент бизнес-анализа, позволяющий анализировать «живые» данные и создавать визуальные отчёты без привлечения ИТ-специалистов\n \n<strong>Ключевые навыки:</strong>\n🔥Подготовка исходных данных для анализа\n🔥Построение моделей данных из разных неструктурированных источников: таблиц, сайтов и баз данных\n🔥Преобразование сложных данных в простые для восприятия и ценные для бизнеса сведения\n🔥Подготовка интерактивных отчётов и дашбордов для совместной работы\n🔥Написание кастомных формул на языке запросов DAX\n🔥Визуализация результатов анализа\n🔥Анализ динамики изменений на дашбордах\n \n🤢Цена курса:  ̶2̶8̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶1̶6̶8̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/power-bi#/'
        photo = netology_courses[5]
    elif message.text == 'netology7':
        text = '<strong>[Нетология] BIG DATA с нуля</strong>\n\n<strong>Описание:</strong>\n Big data - инструменты, подходы и методы обработки огромных объёмов данных.;\n<strong>Вы получите:</strong>\n🔥Сбор и подготовка данных для анализа\n🔥Понимание бизнес-требований заказчика и организация эффективной команды\n🔥Преобразование неструктурированных данных в простые для восприятия и ценные для бизнеса сведения\n🔥Построение моделей данных из разных неструктурированных источников: таблиц, сайтов и баз данных\n🔥Определение и выбор оптимальной архитектуры для Big Data проекта\n🔥Определение результатов обработки и инсайтов в данных и улучшение качества принятия решений на их основе\n\n🤢Цена курса: ̶3̶2̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶1̶9̶7̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/programs/big-data#/presentation'
        photo = netology_courses[6]
    elif message.text == 'netology8':
        text = ' <strong>[Нетология] Таргетированная реклама</strong>\n\n<strong>Описание:</strong>\nНаучим работать с рекламой в социальных сетях. Курс одобрен компаниями ВКонтакте и myTarget.\n<strong>Ключевые навыки:</strong>\n🌟Анализ и сегментация целевой аудитории\n🌟Разработка стратегии таргетированной рекламы\n🌟Настройка рекламных кампаний в кабинетах Facebook/Instagram, ВКонтакте, myTarget\n🌟Создание креативов и текстов для рекламных кампаний\n🌟Работа с системами аналитики: Google Analytics, Яндекс.Метрика\n🌟Работа с парсерами, пикселями ремаркетинга/ретаргетинга\n🌟Анализ и оптимизация рекламных кампаний\n🌟Планирование бюджета рекламных кампаний\n🌟Поиск клиентов и отчётность\n \n🤢Цена курса:  ̶4̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶9̶9̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/target-smm#/'
        photo = netology_courses[7]
    elif message.text == 'netology9':
        text = ' <strong>[Нетология] Геймдизайн</strong>\n<strong>Описание:</strong>\n\nГеймдизайнер знает, как с нуля создать игровой продукт. Он умеет грамотно формулировать задачи для команды, понимает маркетинг игр и способен убедить инвестора в успешности проекта. Освойте новую профессию — и создавайте по-настоящему успешные, захватывающие игры.\n\n<strong>Чему вы научитесь на курсе:</strong>\n🎮Создавать сюжет и композицию игры, строить дизайн игрового пространства, карты уровней и карты маршрутов\n🎮Прототипировать игры и создавать шаблоны игровых интерфейсов для UI-дизайнеров\n🎮Собирать и анализировать игровую статистику, а также участвовать в разработке стратегии продвижения игры\n\n🤢Цена курса:  ̶4̶5̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶7̶5̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 390 ₽ / 1990 ₸ '
        url = 'https://netology.ru/programs/gamedesign#/'
        photo = netology_courses[8]
    elif message.text == 'netology10':
        text = '<strong>[Нетология] Python: программирование на каждый день</strong>\n\n<strong>Описание:</strong>\nPython входит в топ-10 самых востребованных языков программирования (по данным Stack Overflow). Он открывает путь в топовые IT-компании: Google, Pixar, Youtube, Instagram, Nasa, Intel, Pinterest используют именно его.\n \n<strong>Программа курса:</strong>\n👨‍💻Вычислительные задачи на Python\n👨‍💻Работа с файловой системой\n👨‍💻Работа с внешним API\n👨‍💻Краткое введение в анализ данных\n👨‍💻Подводные камни разработки на Python\n \n🤢Цена курса:  ̶7̶9̶ ̶9̶9̶0̶ ̶₽ ̶/̶ ̶4̶7̶9̶ ̶9̶4̶0̶ ̶₸̶ ̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/python#/'
        photo = netology_courses[9]
    elif message.text == 'netology11':
        text = '<strong>[Нетология] Веб-аналитика: что нужно знать интернет-специалисту</strong>\n\n<strong>Описание:</strong>\nНаучитесь управлять маркетингом при помощи данных и использовать их для роста бизнеса и увеличения прибыли\n \n<strong>Ключевые навыки</strong>\n🌊Настройка отслеживания в аккаунтах Google Analytics и Яндекс. Метрики\n🌊Использование Google Tag Manager для разметки сайта\n🌊Создание отчётов, сводок и оповещений в Google Analytics и Яндекс. Метрике\n🌊Анализ эффективности сайта, продаж на сайте и источников трафика\n🌊Проведение А/В тестов для повышения конверсии сайта\n🌊Использование Excel\n🌊Использование Google Data Studio для визуализации данных\n \n🤢Цена курса:  ̶3̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶9̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'http://netology.ru/programs/ws-web-analytics'
        photo = netology_courses[10]
    elif message.text == 'netology12':
        text = '<strong>[Нетология] Анализ статистики сайта с помощью Яндекс.Метрики</strong>\n\n<strong>Описание:</strong>\nКурс по Яндекс Метрике создан для тех, кто хочет отслеживать поведение посетителей на сайте, оценивать отдачу от рекламных кампаний, а также наблюдать в реальном времени за изменением KPI вашего интернет-проекта.\n \n<strong>Содержание курса:</strong>\n💥Принципы работы Яндекс.Метрики\n💥Краткий обзор отчетов Яндекс.Метрики\n💥Создание аккаунта Яндекс.Метрики\n💥Дополнительные настройки счетчика\n💥Настройка целей Яндекс.Метрики\n💥Приемы работы с отчетами Яндекс Метрики\n \n🤢Цена курса:  ̶3̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶9̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://metrika.yandex.ru/welcome?utm_medium=search&utm_source=google&utm_campaign=8146429199&utm_content=397582312057&utm_term=%2B%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%2B%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B0&gclid=Cj0KCQjw0rr4BRCtARIsAB0_48NI8Uk7BgxMRex52HNUvuCAF6cCE7HFz8BrRe3hTEqpVo9u28YH5E8aAmNWEALw_wcB'
        photo = netology_courses[11]
    elif message.text == 'netology13':
        text = ' <strong>[Нетология] Математика для анализа данных</strong>\n \n<strong>Описание:</strong>\nЧтобы увидеть в больших объёмах данных закономерности, аналитик опирается на линейную алгебру, математический анализ и теорию вероятности. Если специалист не разбирается в этих направлениях — гипотезы и выводы будут неточными. Это как запустить ракету в космос, не зная траекторию полёта.\n \n<strong>Кому подойдёт курс:</strong>\n🤓Аналитикам данных\nПознакомитесь с основными математическими концепциями и заложите теоретический фундамент, чтобы лучше разбираться в статистике и правильно интерпретировать данные.\n🤓Специалистам по Data Science\nНачнёте глубже разбираться в алгоритмах машинного обучения. Поймёте, какие принципы лежат в основе разных алгоритмов, чтобы выбирать правильные инструменты.\n \n🤢Цена курса:  ̶1̶7̶ ̶̶̶0̶0̶0̶ ̶₽ ̶̶̶/̶̶̶ ̶̶̶9̶9̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶ ̶\n🤑Наша цена: 390 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/mathematics-for-data-science'
        photo = netology_courses[12]
    elif message.text == 'netology14':
        text = '<strong>[Нетология] Основы поисковой оптимизации (SEO)</strong>\n \n<strong>Описание:</strong> \nКурс по основам поисковой оптимизации (SEO) — источник и теоретических, и практических знаний. Вы освоите принципы работы поисковых систем, поймете, как использовать факторы ранжирования и работать с разными типами пользовательских запросов.\n \n<strong>Ключевые навыки:</strong>\n💫Знание основных факторов ранжирования в поисковых системах и умение эти знания применять на практике\n💫Умение на базовом уровне визуально разбираться в коде и находить ошибки, допущенные при html-верстке документов\n💫Формирование семантического ядра вручную и с помощью софта и распределение запросов по страницам\n💫Умение находить технические ошибки на сайте\n💫Проведение работ по контентной оптимизации\n \n🤢Цена курса:  ̶7̶9̶0̶ ̶₽ ̶̶̶/̶̶̶ ̶̶̶4̶5̶0̶0̶ ̶₸̶̶̶\n🤑Наша цена: 390 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/courses/osnovy-poiskovoy-optimizatsii-seo'
        photo = netology_courses[13]
    elif message.text == 'netology15':
        text = '<strong>[Нетология] Исследуйте в R (2020)</strong>\n\n<strong>Описание:</strong>\nМы живём в эпоху цифровизации, когда каждый процесс можно автоматизировать и упростить свою работу. На языке R можно написать код, который освободит вам время для новых проектов.\n \n<strong>Возможности после обучения:</strong>\n🦾Собирать данные из большинства аналитических систем\n🦾Преобразовывать R-скрипты для переработки получаемых данных в зависимости от задач\n🦾Анализировать рутинные процессы с помощью скриптов и показывать результаты на графиках\n \n🤢Цена курса:  ̶2̶7̶ ̶0̶0̶0̶ ̶̶̶̶̶̶̶₽ ̶/̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶6̶2̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 390 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/programs/r-analysis#/presentation'
        photo = netology_courses[14]
    elif message.text == 'skillbox1':
        text = ' <strong>[SkillBox] Дизайн мобильных приложений</strong>\n \n<strong>Описание:</strong>\nВы научитесь создавать интерфейсы для мобильных платформ и эффектно презентовать свои работы. Сможете начать карьеру дизайнера в IT-компании или зарабатывать на фрилансе.\n \n<strong>Вы научитесь:</strong>\n🔥Работать с дизайнерским софтом\n🔥Проектировать приложения\n🔥Тестировать гипотезы\n🔥Адаптировать дизайн\n🔥Анимировать интерфейсы\n🔥Презентовать проекты\n \n🤢Цена курса:  ̶8̶0̶ ̶0̶0̶0̶₽̶ ̶̶̶ ̶/̶̶̶̶̶̶̶ ̶̶̶4̶6̶3̶ ̶0̶0̶0̶₸̶ ̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/app-design-pro/'
        photo = skillbox_courses[0]
    elif message.text == 'skillbox2':
        text = '<strong>[SkillBox] Управление digital-проектами</strong>\n \n<strong>Описание:</strong>\nЗа четыре месяца вы освоите все этапы работы над проектом — от планирования до запуска — и сможете стать руководителем digital-проектов с зарплатой от 90 000 рублей.\n \n<strong>Вы научитесь:</strong>\n🌟Вести переговоры\n🌟Быстро запускать проекты\n🌟Управлять изменениями\n🌟Контролировать команду\n🌟Считать деньги\n🌟Понимать техническую часть проекта\n \n🤢Цена курса:  ̶6̶5̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶7̶6̶ ̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/sibirix/'
        photo = skillbox_courses[1]
    elif message.text == 'skillbox4':
        text = '<strong>[SkillBox] Cinema 4D для веб-дизайна</strong>\n \n<strong>Описание:</strong>\nВы с нуля освоите Cinema 4D, научитесь моделировать объекты и работать со светом, анимацией и физикой.\n \n<strong>Вы научитесь:</strong>\n💣Работать в Cinema 4D\n💣Моделировать 3D-объекты\n💣Рендерить объекты\n💣Создавать анимацию в один клик\n💣Использовать продвинутые возможности софта\n\n🤢Цена курса:  ̶2̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶1̶5̶ ̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/cinema4d/'
        photo = skillbox_courses[3]
    elif message.text == 'skillbox3':
        text = '<strong>[SkillBox] Три дизайн-курса в одном - UX-дизайн, UX-аналитика, UI-анимация</strong>\n \n<strong>Описание:</strong>\nВы узнаете, как проводить UX-исследования и проектировать удобные интерфейсы. Научитесь создавать сайты и приложения, которые точно понравятся пользователям.\n \n<strong>Вы научитесь:</strong>\n🔥Проектировать интерфейсы на основе поведения пользователей\n🔥Решать проблемы пользователей\n🔥Создавать дизайн-системы\n🔥Проводить пользовательские исследования\n🔥Проектировать интерфейсы мобильных приложений\n🔥Работать с текстом в интерфейсе\n🔥Создавать дизайн на основе данных\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶4̶7̶ ̶3̶5̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/aic/'
        photo = skillbox_courses[2]
    elif message.text == 'skillbox5':
        text = ' <strong>[SkillBox] Веб-дизайн с Нуля до Про </strong>\n \n<strong>Описание:</strong>\nВы научитесь создавать дизайн сайтов и приложений, работать с реальными заказчиками и презентовать свои проекты. \n \n<strong>Вы научитесь:</strong>\n✨Создавать интерфейсы\n✨Делать адаптивные макеты\n✨Работать с типографикой\n✨Делать анимации и иконки\n✨Проектировать пользовательский опыт\n✨Работать с клиентами\n \n🤢Цена курса:  ̶1̶0̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶7̶8̶ ̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/webdesign/'
        photo = skillbox_courses[4]
    elif message.text == 'skillbox7':
        text = '<strong>[SkillBox] Сквозная аналитика </strong>\n \n<strong>Описание:</strong>\nВы научитесь настраивать аналитику для всех каналов продвижения, чтобы выжимать максимум из рекламы, принимать решения на основе точных данных и не терять деньги.\n \n<strong>Вы научитесь:</strong>\n🌟Отслеживать путь клиента в воронке продаж\n🌟Создавать системы сквозной аналитики\n🌟Оценивать эффективность рекламы\n🌟Собирать статистику по всем каналам сразу\n🌟Анализировать данные\n🌟Создавать наглядные отчёты\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n\n\n'
        url = 'https://skillbox.ru/end-to-end/'
        photo = skillbox_courses[6]
    elif message.text == 'skillbox8':
        text = ' <strong>[SkillBox]</strong><strong>Как открыть и развивать свою веб-студию </strong>\n \n<strong>Описание:</strong>\nНастоящий бриллиант среди курсов от SkillBox - что по содержанию, что по стоимости. Сладкая мечта всех дизайнеров - открыть собственную прибыльную веб-студию - и мы поможем ее осуществить!\n \n<strong>Вы научитесь:</strong>\n🔥Запускать бизнес с нуля\n🔥Развивать личный бренд\n🔥Выстраивать стратегию развития\n🔥Находить заказы для студии\n🔥Организовывать работу команды\n🔥Эффективно управлять веб-студией\n🔥Работать с необходимыми юридическими и финансовыми отчетностями\n🔥Выстраивать долгосрочные отношения с клиентами\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skill-box.ru/studio/'
        photo = skillbox_courses[7]
    elif message.text == 'skillbox6':
        text = '<strong> [SkillBox] UI анимация. Стань motion-дизайнером за 16 недель </strong>\n \n<strong>Описание:</strong>\nВы научитесь создавать анимации в After Effects и Atomic и превращать статичный дизайн в динамичные креативные интерфейсы.\n \n<strong>Вы научитесь:</strong>\n💣Работать в After Effects, Principle и Atomic\n💣Анимировать интерфейсы\n💣Анимировать статичные концепции\n💣Создавать видеобаннеры\n💣Презентовать проекты\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/motion/'
        photo = skillbox_courses[5]
    elif message.text == 'skillbox9':
        text = ' <strong>[SkillBox] Рекламная Графика </strong>\n \n<strong>Описание:</strong>\nКурс от создателей самых сочных рекламных иллюстраций на российском рынке\n \n<strong>Вы научитесь:</strong>\n🧨Профессиональная ретушь\n🧨Создание фотореалистичных иллюстраций\n🧨Работа в технике matte-painting\n🧨Организация фотосессий\n🧨Постобработка визуализаций в Photoshop\n🧨Создание скетчей\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶4̶7̶ ̶3̶5̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/cpeople/'
        photo = skillbox_courses[8]
    elif message.text == 'skillbox10':
        text = '<strong>[SkillBox] Excel c 0 до PRO </strong>\n \n<strong>Описание:</strong>\nНаучитесь составлять сложные отчёты и строить прогнозы, сможете автоматизировать свою работу с помощью скриптов и макросов — тем самым освободите время для других задач.\n \n<strong>Вы научитесь:</strong>\n⚡️Быстро делать сложные расчёты\n⚡️Наглядно представлять данные\n⚡️Строить прогнозы\n⚡️Работать с внешними источниками данных\n⚡️Создавать макросы и скрипты\n⚡️Работать с инструментами фильтрации\n \n🤢Цена курса: ̶ ̶4̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶3̶1̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/excel/'
        photo = skillbox_courses[9]
    elif message.text == 'skillbox11':
        text = '<strong>[SkillBox]</strong><strong>Adobe After Effects с 0 до PRO</strong>\n \n<strong>Описание:</strong>\nВы научитесь работать с анимацией, освоите возможности After Effects на профессиональном уровне и сделаете первые проекты для портфолио — сможете расширить навыки в дизайне или начать карьеру в киноиндустрии.\n \n<strong>Вы научитесь:</strong>\n✨Работать в Adobe After Effects\n✨Создавать анимации\n✨Создавать эффекты\n✨Разрабатывать 3D-сцены\n✨Редактировать и стабилизировать видео\n✨Настраивать параметры рендера\n \n🤢Цена курса:  ̶2̶5̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶1̶4̶4̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://course.skillbox.ru/after-effects'
        photo = skillbox_courses[10]
    elif message.text == 'skillbox12':
        text = '<strong> [Skillbox] Профессия С# разработчик </strong>\n \n<strong>Описание:</strong>\n130 часов обучения — и вы научитесь писать программы, разрабатывать веб-сервисы и игры на языке от Microsoft, в команде и индивидуально.\n \n<strong>Вы научитесь:</strong>\n💣Программировать на C#\n💣Разбираться в технологиях ADO.NET и Entity Framework Code First\n💣Разрабатывать собственное Windows-приложение\n💣Использовать ООП, LINQ, коллекции, исключения и делегаты\n💣Разрабатывать собственную файловую базу данных\n💣Работать с платформой .NET Framework и средой разработки Visual Studio\n \n🤢Цена курса:  ̶1̶3̶0̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶7̶5̶2̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/profession-c-sharp/'
        photo = skillbox_courses[11]
    elif message.text == 'skillbox13':
        text = '<strong>[SkillBox]</strong><strong>Онлайн-курс Figma 3.0</strong>\n \n<strong>Описание:</strong>\nВы освоите популярный сервис для разработки интерфейсов Figma. Сможете создавать дизайн-проекты, делать прототипы и использовать этот инструмент для командной работы. Станете более востребованным дизайнером в Digital.\n \n<strong>Вы научитесь:</strong>\n🔥Уверенно работать в Figma\n🔥Выстраивать рабочий процесс\n🔥Создавать прототипы\n🔥Организовывать дизайн-проекты\n🔥Делать анимацию\n \n🤢Цена курса:  ̶2̶0̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶1̶1̶5̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/figma/'
        photo = skillbox_courses[12]
    elif message.text == 'skillbox14':
        text = ' <strong>[SkillBox] Практический интенсивный курс SMM менеджер</strong>\n \n<strong>Описание:</strong>\nВы научитесь продвигать бизнес в соцсетях, создавать вовлекающий контент, общаться с аудиторией и запускать рекламу. Курс подойдет как новичкам, которые никогда не занимались SMM, так и руководителям бизнеса.\n \n<strong>Вы научитесь:</strong>\n🌟Определять целевую аудиторию\n🌟Выбирать инструменты продвижения\n🌟Запускать таргетированную рекламу\n🌟Создавать контент\n🌟Работать с аудиторией\n🌟Анализировать метрики\n \n🤢Цена курса:  ̶7̶2̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶4̶1̶6̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/smm/'
        photo = skillbox_courses[13]
    elif message.text == 'skillbox15':
        text = '<strong>[SkillBox] Большой курс "Профессия интернет-маркетолог от А до Я"</strong>\n \n<strong>Описание:</strong>\nЗа полгода вы с нуля научитесь выстраивать стратегию продвижения бизнеса и настраивать разные виды рекламы в интернете.\n \n<strong>Вы научитесь:</strong>\n🧨Продвигать бизнес в социальных сетях: от описания профиля до контент-плана\n🧨Определять подходящие каналы маркетинга и оценивать потенциал трафика в проектах\n🧨Запускать контекстную и таргетированную рекламу\n🧨Создавать классические лендинги на Tilda и делать сайты-анкеты\n🧨Планировать рекламные кампании\n🧨Анализировать продукт, целевую аудиторию и конкурентов\n🧨Продвигать себя как специалиста в соцсетях\n \n🤢Цена курса:  ̶7̶2̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶4̶1̶6̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/internet-marketolog/'
        photo = skillbox_courses[14]
    elif message.text == 'udemy1':
        text = '<strong>[Udemy] Центр digital-профессий ITtensive - Базовый Python</strong>\n \n<strong>Описание:</strong>\nНа этом курсе вы освоите программирование на языке Python и научитесь работать с данными для самостоятельно анализа. \n \n<strong>Вы научитесь:</strong>\n🧨Основы работы с Python\n🧨Jupyter Notebook\n🧨Переменные, типы и базовые операции\n🧨Циклы for и while, управляющие конструкции\n🧨Срезы и диапазоны строк\n🧨Одномерные и многомерные списки\n🧨Базовые статистические методы\n🧨Словари, кортежи и отображения\n🧨Работа с файлами\n🧨Модули numpy и matplotlib\n \n🤢Цена курса:  ̶3̶5̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶2̶0̶ ̶5̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-python-basic/'
        photo = udemy_courses[0]
    elif message.text == 'udemy2':
        text = '<strong>[Udemy] Продвинутые навыки Python: станьте лучшим разработчиком Python!</strong>\n \n<strong>Описание:</strong>\nВ этом курсе вы узнаете много встроенных функций, чтобы стать лучшим разработчиком Python. Вы также узнаете, как реализовать лучшие практики и некоторые модульные тесты.\n \n<strong>Вы научитесь:</strong>\n🔥Полезные встроенные функции, которые иногда игнорируются в Python\n🔥Понять, как некоторые вещи работают внутри Python\n🔥Лучшие практики\n🔥Модульное тестирование\n \n🤢Цена курса:  ̶1̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶8̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/advanced-python-skills-become-a-better-python-developer/'
        photo = udemy_courses[1]
    elif message.text == 'udemy3':
        text = '<strong>[Udemy] iOS программирование на Swift. Уровень 1.</strong>\n \n<strong>Описание:</strong>\nВ данном курсе мы спроектируем, разработаем и опубликуем в AppStore полностью рабочее приложение Конвертер валют.\n \n<strong>Вы научитесь:</strong>\n🌊Сможете создавать свои iOS приложения\n🌊Научитесь работать в Xcode (среда разработки iOS приложений)\n🌊Освоите основы программирования на языке Swift\n🌊Научитесь оформлять приложения в AppStore\n🌊Публиковать приложения в AppStore\n \n🤢Цена курса:  ̶̶̶6̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶3̶7̶ ̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ios-swift-programming/'
        photo = udemy_courses[2]
    elif message.text == 'udemy4':
        text = '<strong>[Udemy] Kotlin. От А до Я </strong>\n \n<strong>Описание:</strong>\nС помощью данного курса вы сможете изучить синтаксис, возможности языка Kotlin и начать применять его в проектах и в изучении Android разработки.\n \n<strong>Вы научитесь:</strong>\n🔥Научитесь программировать на Kotlin.\n \n🤢Цена курса:  ̶̶̶8̶6̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶5̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/kotlin-from-a-to-z/'
        photo = udemy_courses[3]
    elif message.text == 'udemy5':
        text = '<strong>[Udemy] React Native 2020. Мобильная разработка на JavaScript</strong>\n \n<strong>Описание:</strong>\nВ рамках данного курса вы создадите 2 мобильных приложения, на которых изучите функционал React Native\n \n<strong>Вы научитесь:</strong>\n🔥Создавать мобильные приложения под iOS и Android на языке JavaScript\n🔥Создадите несколько приложений в течении курса\n🔥React Native на практике\n🔥Получите много опыта и Best Practices в React\n \n🤢Цена курса:  ̶9̶ ̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶ ̶9̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/react-native-complete-guide/'
        photo = udemy_courses[4]
    elif message.text == 'udemy6':
        text = '<strong>[Udemy] Android разработка с нуля до профессионала</strong>\n \n<strong>Описание:</strong>\nЭтот курс подойдет для всех желающих - как для тех, кто хочет стать профессионалом в разработке Андроид приложений, так и для тех, кто просто хочет заниматься этим в качестве хобби и зарабатывать хорошие деньги на этом - никакого опыта программирования не требуется.\n \n<strong>Вы научитесь:</strong>\n🔥Разрабатывать XML разметку и UI андроид приложений\n🔥Основы Java, и также более продвинутые темы, включая ООП\n🔥Работать с аудио, видео и изображениями\n🔥Элементы Material Design, как RecyclerView, CardView и другие \n🔥Сохранять различные виды данных разными способами\n🔥Использовать библиотеки Volley, Glide, Picasso\n🔥Создавать приложения-мессенджеры при помощи Firebase - такие как Viber, WhatsApp, Telegram\n🔥Создавать практически любое андроид приложение, включая игры\n\n🤢Цена курса:  ̶9̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶9̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/android-kak-po-notam-a'
        photo = udemy_courses[5]
    elif message.text == 'udemy7':
        text = '<strong>[Udemy] PHP v.7+ и MySQL с нуля</strong>\n \n<strong>Описание:</strong>\nКурс создан для тех, кто пока еще не знаком с языком программирования PHP и позволит начать с самых азов. \n \n<strong>Вы научитесь:</strong>\nПолный курс по PHP +  MySQL и взаимодействие с данной СУБД через расширение MySQLi PHP\n \n🤢Цена курса:  ̶9̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶9̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/php-v7-mysql/'
        photo = udemy_courses[6]
    elif message.text == 'udemy8':
        text = '<strong>[Udemy] Программирование на C#: от новичка до специалиста</strong>\n \n<strong>Описание:</strong>\nКороче говоря, если вы только начинаете своё путешествие в мир программирования, C# станет отличным выбором в качестве вашего первого языка программирования.\n \n<strong>Вы научитесь:</strong>\n🔥Как устроена платформа .NET и .NET Core\n🔥Основные типы данных в C#\n🔥Управление потоком исполнения программы: циклы, условия\n🔥Массивы и коллекции: Array, List, Dictionary, Stack, Queue\n🔥Классы и структуры: отличия в контексте управления памятью\n🔥ООП в C#: наследование, полиморфизм, инкапсуляция\n🔥ООП в С#: интерфейсы, абстрактные классы, модификатора доступа\n🔥Методы: params, out, ref, static, overloading, optional parameters\n🔥Основы процесса отладки\n🔥Управление памятью: сборка мусора, boxing\\unboxing\n🔥Перечисления\n🔥Обобщения\n🔥Написание простых программ и игр на C# таких как "крестики-нолики"\n\n🤢Цена курса: ̶̶̶7̶1̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶4̶1̶ ̶4̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/csharp-ru/'
        photo = udemy_courses[7]
    elif message.text == 'udemy9':
        text = '<strong>[Udemy] Программирование игр для детей на Scratch для начинающих</strong>\n \n<strong>Описание:</strong>\nНаучитесь основам программирования и созданию увлекательных компьютерных игр в интересном формате с помощью Scratch.\n \n<strong>Вы научитесь:</strong>\n🧨Разрабатывать компьютерные игры;\n🧨Создавать программы различного назначения;\n🧨Понимать принципы программирования, которые помогут при дальнейшем его изучении;\n🧨Использовать структурный подход;\n🧨Пользоваться сеткой координат и градусной мерой углов;\n \n🤢Цена курса:  ̶4̶3̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶2̶4̶ ̶8̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/programming-for-kids-in-scratch-for-beginners/'
        photo = udemy_courses[8]
    elif message.text == 'udemy10':
        text = ' <strong>[Udemy] Создание Telegram ботов с помощью JavaScript: Полное руководство </strong>\n \n<strong>Описание:</strong>\nПолный, легкий и быстрый в освоении курс. Создайте чат-ботов Telegram с Node.js, используя Telegraf Framework.\n \n<strong>Вы научитесь:</strong>\n🧨Этот курс призван предоставить вам полный набор знаний о том, как создавать удивительные боты Telegram.\n \n🤢Цена курса:  ̶̶̶2̶8̶6̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶6̶ ̶5̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/build-telegram-bots-with-javascript-the-complete-guide/'
        photo = udemy_courses[9]
    elif message.text == 'udemy11':
        text = '<strong>[Udemy] Продвинутые алгоритмы в Java </strong>\n \n<strong>Описание:</strong>\nЗная основы Java, вы захотите приступить к выяснению алгоритмов и структур данных. При правильном их использовании ваш код будет работать быстрее, использовать меньше памяти и быть более стабильным.\n \n<strong>Вы научитесь:</strong>\n🔥Лучше решать проблемы, используя лучшие реализации и принимая правильные решения с помощью своего кода\n \n🤢Цена курса:  ̶̶̶3̶2̶2̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶8̶ ̶6̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/java-best/'
        photo = udemy_courses[10]
    elif message.text == 'udemy12':
        text = '<strong>[Udemy] Аналитика и Data Science для менеджеров и гуманитариев</strong>\n \n<strong>Описание:</strong>\nКурс очень постепенно от простого к сложному погружает профессионалов из не-технических наук в захватывающий цифровой мир статистики и вероятностей – и поможет легко в нем ориентироваться, пользоваться и не бояться\n \n<strong>Вы научитесь:</strong>\n🌟Совмещать бизнес- и проф-интуицию с анализом данных, строить гипотезы и проверять их\n🌟Собирать, структурировать и обрабатывать данные\n🌟Современные методы статистического анализа на практике и реальных данных\n🌟Легко находить и видеть скрытые закономерности в данных\n🌟Анализировать большие объемы (массивы) данных\n \n🤢Цена курса:  ̶8̶̶̶6̶0̶̶̶0̶̶̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶0̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/analytics-and-data-science/'
        photo = udemy_courses[11]
    elif message.text == 'udemy13':
        text = '<strong>[Udemy] Основы программирования</strong>\n\n<strong>Описание:</strong>\nНа этом курсе вы освоите базовые понятия и термины программирования как профессии и научитесь создавать программы.\n \n<strong>Вы научитесь:</strong>\n⚡️Алгоритмы\n⚡️Блок-схемы\n⚡️Основные определения программирования\n \n🤢Цена курса:  ̶̶̶1̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶8̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-programmer-basic/'
        photo = udemy_courses[12]
    elif message.text == 'udemy14':
        text = '<strong>[Udemy] Машинное обучение: кластеризация и классификация на Python</strong>\n \n<strong>Описание:</strong>\nМы разберем прикладные подходы к кластеризации и классификации данных с помощью машинного обучения для страхового скоринга Prudential в соревновании на Kaggle вплоть до формирования конечного результата\n \n<strong>Вы научитесь:</strong>\n💣EDA: исследовательский анализ данных\n💣Точность, полнота, F1 и каппа метрики\n💣Простая кластеризация данных\n💣Логистическая регрессия: простая и многоуровневая\n💣Метод ближайших соседей: kNN\n💣Наивный Байес\n💣Метод опорных векторов: SVM\n💣Решающие деревья м случайный лес\n💣XGBoost и градиентный бустинг\n💣CatBoost и LightGBM\n💣Ансамбль голосования и стекинга\n \n🤢Цена курса:  ̶̶̶7̶1̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶4̶1̶ ̶4̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-python-machine-learning-classification/'
        photo = udemy_courses[13]
    elif message.text == 'udemy15':
        text = '<strong>[Udemy] Изучаем Linux и командную строку. Линукс шаг за шагом </strong>\n \n<strong>Описание:</strong>\nЭтот курс познакомит вас с некоторыми наиболее важными функциями интерпретатора bash и как администрировать Linux, используя командную строку bash.\n \n<strong>Вы научитесь:</strong>\n⚡️Вы узнаете о некоторых наиболее важных функциях интерпретатора bash\n⚡️Вы сможете использовать основные команды Linux\n⚡️Вы научитесь получать информацию о системе\n⚡️Многое другое\n \n🤢Цена курса:  ̶9̶ ̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶ ̶9̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/linux-eg/'
        photo = udemy_courses[14]
    elif message.text == 'webformyself1':
        text = '<strong>[WebForMySelf] Веб-дизайнер профессионал</strong>\n\n<strong>Описание:</strong>\nЕсли Вас привлекает возможность вести небольшой, но доходный интернет-бизнес из любой точки планеты и жить насыщенной, интересной жизнью — фриланс в сфере веб-дизайна вполне может Вам подойти.\n\n<strong>Вы научитесь:</strong>\n🌟Научитесь проектировать дизайны сайтов.\n🌟Создавайте востребованные макеты быстро, легко и… дорого.\n🌟Быстрый старт во фрилансе без вложений.\n🌟Фокус на веб-дизайне: только самое главное.\n\n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ̶₽̶ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/wdprofi/'
        photo = webformyself_courses[0]
    elif message.text == 'webformyself2':
        text = ' <strong>[WebForMySelf] Фриланс - Мастер. Как продавать свои услуги онлайн</strong>\n \n<strong>Описание:</strong>\nИменно для людей, желающих освоить тонкое ремесло удаленного заработка издательством WebForMyself был разработан комплексный видеокурс «Фриланс-Мастер. Как продавать свои услуги онлайн».\n \n<strong>Вы научитесь:</strong>\n🔥5 модулей полезных и практических знаний\n🔥Мотивация\n🔥Теория\n🔥Практика\n🔥Курс не устареет в ближайшие 5 лет или больше\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶̶̶₽ ̶̶̶/̶̶̶̶̶̶̶ ̶̶̶4̶6̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 390₽ / 1990₸ \n\n\n'
        url = 'https://webformyself.com/fmaster/'
        photo = webformyself_courses[1]
    elif message.text == 'webformyself3':
        text = '<strong>[WebForMySelf] Верстка-Мастер</strong>\n \n<strong>Описание:</strong>\nВ нашем курсе макеты верстаются как раз-таки с использованием современных подходов. При верстке вы будете применять технологию Flex, препроцессор SasS и сборщик Gulp. Верстку сделаете кроссбраузерной и адаптивной под любые устройства. \n\n<strong>В курсе показана верстка макетов двух наиболее востребованных типов сайтов:\n 🧨</strong>Landing Page и интернет-магазина\n🧨Показано, как быстро верстать сайты, применяя новейшие технологии верстки: Flex, препроцессор SasS и сборщик Gulp\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n\n\n'
        url = 'https://webformyself.com/verstka/?7d19a8f7'
        photo = webformyself_courses[2]
    elif message.text == 'webformyself4':
        text = '<strong>[WebForMySelf] JavaScript. Полное руководство для современной веб-разработки</strong>\n \n<strong>Описание:</strong>\nВ курсе показана разработка с нуля 2-х полноценных веб-приложений, реализованных в форме условной веб-игры и блога. В курсе нет ничего лишнего, только те знания, которые действительно нужны для практической разработки в 2019 году.\n \n<strong>Вы научитесь:</strong>\n🌟Разработка простого веб-приложения на JavaScript в форме игры\n🌟Создание веб-приложения в форме блога на чистом JavaScript (без использования сторонних библиотек)\n🌟В результате успешного прохождения видеокурса вы напишите полноценное веб-приложение на чистом JavaScript без использования сторонних библиотек.\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/javascript/'
        photo = webformyself_courses[6]
    elif message.text == 'webformyself5':
        text = ' <strong>[WebForMySelf] PHP-Мастер. От теории до собственной CMS интернет-магазина</strong>\n \n<strong>Описание:</strong>\nВ этом видеокурсе показано не только создание движка для интернет-магазина, но еще и создание фреймворка, на котором и пишется CMS.\nВ курсе разрабатывается РНР-фреймворк, который вы сможете в дальнейшем использовать многократно, сокращая время разработки.\n \n<strong>Вы научитесь:</strong>\n💣Изучается теория\n💣Пишется php фреймворк\n💣Создаётся cms интернет-магазина\n💣Мастер веб-разработки на PHP\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/phpmaster/?spush=bWFrc2ltYXN6QHlhaG9vLmNvbQ==#price'
        photo = webformyself_courses[4]
    elif message.text == 'webformyself6':
        text = ' <strong>[WebForMySelf] 1-С Битрикс. Практика создания веб-проектов</strong>\n \n<strong>Описание:</strong>\nНовый фундаментальный курс поможет вам в считанные недели овладеть профессиональной разработкой на CMS 1C-Битрикс с нуля.\n \n<strong>Вы научитесь:</strong>\n✨Создание сайта интернет-магазина\n✨Создание сайта моды\n \n🤢Цена курса: ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/bitrix/'
        photo = webformyself_courses[5]
    elif message.text == 'webformyself7':
        text = ' <strong>[WebForMySelf] FullStack-Мастер: Разработка CRM-системы на Node.js, Express, Angular 6</strong>\n \n<strong>Описание:</strong>\nДанный курс наглядно показывает разработку СRМ-системы, где собраны разнообразные элементы, на которых показывается их реализация.\n \n<strong>Вы научитесь:</strong>\n🧨Пагинация\n🧨Аналитика данных с графиками\n🧨Реализация Material Design с Materialize CSS\n🧨Работа с датами через пикеры\n🧨Фильтрация данных\n🧨Загрузка картинок\n🧨Работа с асинхронными событиями\n \n🤢Цена курса:  ̶1̶2̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶7̶5̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/fsnode/'
        photo = webformyself_courses[6]
    elif message.text == 'webformyself8':
        text = '<strong> [WebForMySelf] ReactJS с Нуля до Профи</strong>\n \n<strong>Описание:</strong>\nДаже полный новичок в сайтостроении сможет разобраться с курсом и освоить Frontend-разработку на стеке React.js. Пожалуй, самый быстрый, простой и легкий способ подняться по карьерной лестнице профессионального Frontend-разработчика\n \n<strong>Вы научитесь:</strong>\n🔥Фундаментальная теория\n🔥Море практики\n🔥Актуальная технология\n🔥Примеры из реальной жизни\n🔥Доступ к материалам курса 24/7\n \n🤢Цена курса:  ̶9̶8̶7̶0̶ ̶₽ ̶/̶ ̶5̶7̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/reactjs/'
        photo = webformyself_courses[7]
    elif message.text == 'webformyself9':
        text = '<strong>[WebForMySelf] Курс по CSS3 </strong>\n \n<strong>Описание:</strong>\nОсновными преимуществами CSS3 являются простота использования, ускорение процесса разработки и оформления web страниц, уменьшение количества кода, практически 100% кроссбраузерность, при этом множество свойств уже можно использовать без префиксов.\n \n<strong>Вы научитесь:</strong>\n⚡️Работа с фоном\n⚡️Закругленные углы и рамки\n⚡️Прозрачность фона, картинки, текста, фото\n⚡️Установка теней для элемента и текста\n⚡️Радиальные градиенты\n \n🤢Цена курса:  ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/htmlcss-premium/css3premium/'
        photo = webformyself_courses[8]
    elif message.text == 'webformyself10':
        text = '<strong>[WebForMySelf] Курс по базе данных MySQL</strong>\n \n<strong>Описание:</strong>\nКурс рассчитан как на новичков, так и на специалистов, уже имеющих опыт работы с SQL. Здесь Вы найдете освещение как теоретических вопросов (например, теория реляционных баз данных, нормализация данных), так и множество практических задач.\n \n<strong>Вы научитесь:</strong>\n🧨Типы данных в MySQL\n🧨Операторы в MySQL\n🧨Нормализация БД и объединение таблиц\n🧨Вложенные запросы и объединение таблиц\n🧨Работа с БД из PHP\n \n🤢Цена курса: ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/php-premium/mysqlpremium/'
        photo = webformyself_courses[9]
    elif message.text == 'webformyself11':
        text = ' <strong>[WebForMySelf] Cоздание каталога товаров с помощью PHP, MySQL и jQuery</strong>\n \n<strong>Описание:</strong>\nЭто огромный по объему курс, в котором не просто решается какая-то конкретная задача, но в котором практически в режиме онлайн мы будем создавать собственный движок с нуля. Написанный в курсе по созданию каталога товаров с помощью PHP, MySQL и jQuery движок, можно будет использовать как для каталога, так и для любого другого сайта: визитка, интернет-магазин, корпоративный сайт, блог.\n \n<strong>Вы научитесь:</strong>\n🌟Постраничной навигации\n🌟MVC\n🌟Создадите комментарии\n🌟Авторизация, восстановление пароля, регистрация\n🌟Темы, поиск, каталог\n \n🤢Цена курса:  ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/php-premium/catalogpremium/'
        photo = webformyself_courses[10]
    elif message.text == 'webformyself12':
        text = '<strong> [WebForMySelf] Библиотека JQuery UI (User Interface) </strong>\n \n<strong>Описание:</strong>\nВ данном курсе мы с Вами будем учиться создавать элементы пользовательского интерфейса, используя библиотеку jQuery UI.Потому как библиотека jQuery UI – это часть глобального проекта под названием jQuery, которая в значительной степени расширяет стандартный функционал указанной библиотеки.\n \n<strong>Вы научитесь:</strong>\n🌪Использовать практически все виджеты из библиотеки jQuery\n🌪Использовать инструменты Selectable и Resizable\n🌪Создавать собственные виджеты\n🌪Использовать инструменты Draggable и Droppable\n🌪Использовать Effects\n \n🤢Цена курса: 1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/javascript-premium/jqueryui-premium/'
        photo = webformyself_courses[11]
    elif message.text == 'webformyself13':
        text = '<strong>[WebForMySelf] WordPress-Мастер. Разработка тем для WordPress с нуля</strong>\n \n<strong>Описание:</strong>\nВ курсе будут использованы все современные методы создания тем для WordPress. В частности, мы познакомимся и используем популярную стартовую тему Underscores, благодаря которой разработка тем значительно ускоряется. Использование фреймворком для WordPress при создании тем на сегодняшний день фактически стало стандартом.\n \n<strong>Вы научитесь:</strong>\n🌪Как делать сайты на WordPress практически любой сложности с любым дизайном\n🌪Как делать сайты на WordPress, которые устраивают именно вас\n🌪Как делать сайты на WordPress, которые удовлетворят всем требованиям даже наиболее предвзятых заказчиков\n🌪Как делать сайты на WordPress, за которые заказчик готов заплатить действительно хорошие деньги\n \n🤢Цена курса: ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/wordpress/'
        photo = webformyself_courses[12]
    elif message.text == 'webformyself14':
        text = '<strong>[WebForMySelf] Создание интернет-магазина на CMS WordPress</strong>\n \n<strong>Описание:</strong>\nВ курсе по созданию интернет-магазина на CMS WordPress мы будем работать с плагином WP–Shop. Также, кроме работы непосредственно с плагином, мы затронем вопрос создания темы для WordPress.\n \n<strong>Вы научитесь:</strong>\n✨Верстка макета\n✨Установка макета на WordPress\n✨Установка шаблона на WordPress\n \n🤢Цена курса: 1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/wordpress-premium/wpshoppremium/'
        photo = webformyself_courses[13]
    elif message.text == 'webformyself15':
        text = '<strong>[WebForMySelf] Angular 4 с Нуля до Профи</strong>\n \n<strong>Описание:</strong>\nМы начнем с самых основ и закончим созданием с нуля полностью рабочего реактивного приложения, где вы увидите все шаги по его созданию.\nПрактике предшествует 12 теоретических блоков, где максимально подробно разобраны и систематизированы в виде пошаговой целостной системы все тонкости фреймворка на различных примерах.\n \n<strong>Вы научитесь:</strong>\n🔥Компоненты\n🔥Роуты\n🔥Ленивая загрузка\n🔥Защищенные роуты\n🔥Валидация форм\n🔥Шаблонный подход (вход в систему)\n🔥Реактивный подход (регистрация, асинхронные валидаторы для проверки email)\n \n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ̶₽̶ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://webformyself.com/angular4/'
        photo = webformyself_courses[14]
    elif message.text == 'otus1':
        text = '<strong>[OTUS] iOS-разработчик. Базовый курс.</strong>\n \n<strong>Описание:</strong>\nКурс фундаментальный: вы сможете разрабатывать самые разнообразные iOS-приложения: интернет-магазины, банковские приложения, фото-редакторы, всевозможные помощники, приложения для фитнеса и прочие услуги.\n \n<strong>Вы научитесь:</strong>\n🔥Создавать IOS-приложения на языке Swift\n🔥Использовать новые фреймворки SwiftUI и Combine\n🔥Применять принципы SOLID в разработке\n🔥Покрывать свой код тестами с помощью TDD\n🔥Работать с сетью на примере API VK\n🔥Использовать Instruments\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/basic-ios/?int_source=courses_catalog&int_term=programming'
        photo = otus_courses[0]
    elif message.text == 'otus2':
        text = '<strong>[OTUS] iOS Разработчик. Продвинутый курс v 2.0</strong>\n \n<strong>Описание:</strong>\nПрограмма создана специально для iOS Developers с опытом работы в сфере разработки мобильных iOS-приложений от 1 года и более.\nОбучение построено исключительно на кейсах из практики разработки приложений в production. Мы будем решать сложные и хардкорные задачи с уровнем качества топовых приложений\n \n<strong>Вы научитесь:</strong>\n💣Применять GCD и решать проблемы многозадачности\n💣Работать с протоколами Sequence и Collection\n💣Использовать в проектах структуры данных, Generic Type, Associated Types и техники Type Erasure, PATs (Protocol with Associated Types)\n💣Грамотно работать с различными способами хранения данных (Core Data, Realm, Keychain, Cache)\n💣Применять Dependency Injection (DI) и модуляризации приложений для более комфортной командной разработки и покрытия тестами\n💣На практике изучите все плюсы и минусы известных методологий, подходов и парадигм (Protocol Oriented Programming, ООП, Reactive Programming)\n \n🤢Цена курса:  ̶7̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶0̶5̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸\n'
        url = 'https://otus.ru/lessons/advanced-ios/'
        photo = otus_courses[1]
    elif message.text == 'otus3':
        text = '<strong>[OTUS] Разработчик Golang</strong>\n \n<strong>Описание:</strong>\nВ этом курсе мы хотели бы объяснить, что такое Go-way, рассказать про идиомы языка и помочь избежать типичных ошибок. Программа курса позволит погрузиться в разработку на Go для решения практических задач, углубления знаний в языке и сопутствующем технологическом стеке\n\n<strong>Вы научитесь:</strong>\n⚡️Писать production-ready код, многопоточные и конкурентные программы;\n⚡️Понимать синтаксис и внутреннее устройство языка Go;\n⚡️Понимать особенности сетевого программирования;\n⚡️Уметь создавать микросервисы с помощью Go;\n⚡️Разворачивать микросервисы с помощью docker.\n \n🤢Цена курса:  ̶8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-golang/'
        photo = otus_courses[2]
    elif message.text == 'otus4':
        text = '<strong> [OTUS] Framework Laravel</strong>\n \n<strong>Описание:</strong>\nРазработчики, обладающие навыками профессиональной работы с PHP-фреймворком Laravel, — сегодня одни из самых востребованных и малочисленных специалистов в сфере IT. Работать с ним удобно и приятно любому, кто освоит все его возможности.\n \n<strong>После обучения студенты смогут:</strong>\n🧨Использовать в проектах Laravel\n🧨Обеспечивать безопасность приложения\n🧨Тестировать и разворачивать полученный код\n🧨Выполнять анализ работы логики и делать выводы\n🧨Использовать встроенные инструменты фреймворка\n \n🤢Цена курса:  ̶5̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶8̶9̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n\n\n'
        url = 'https://otus.ru/lessons/laravel/?int_source=courses_catalog&int_term=programming'
        photo = otus_courses[3]
    elif message.text == 'otus5':
        text = '<strong> [OTUS] Облачные сервисы</strong>\n \n<strong>Описание:</strong>\nЗнания в области Agile разработки и сопровождения архитектуры облачных решений становятся обязательным требованием к IT-специалистам. Именно такие специалисты являются самыми востребованными и высокооплачиваемыми в крупных мировых проектах: Google, Amazon, Microsoft, Yandex, Сбербанк и др.\n \n<strong>Вы научитесь:</strong>\n☁️Well‑Architected Framework (фреймворк правильной облачной архитектуры)\n☁️Cloud Architecture Patterns (архитектурные шаблоны решений)\n☁️Cloud Adoption Framework (фреймворк миграции приложений в облако)\n☁️Agile DevOps методология и CloudReady организация (пример реальной CloudReady организации на 150 человек)\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/solutionarchitect/?int_source=courses_catalog&int_term=operations'
        photo = otus_courses[4]
    elif message.text == 'otus6':
        text = '<strong>[OTUS] Подготовительный курс по JavaScript разработке</strong>\n \n<strong>Описание:</strong>\nВсе основные возможности Javascript\nДомашние задания и их разбор\nПодготовка к курсам "Fullstack разработчик Javascript", "React.js-разработчик" и "Node.js-разработчик"\n \n<strong>Вы научитесь:</strong>\n🌟Объекты и массивы\n🌟Работа с DOM\n🌟Встроенные инструменты\n \n🤢Цена курса:  ̶1̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶8̶6̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/online/online-js/'
        photo = otus_courses[5]
    elif message.text == 'otus7':
        text = '<strong>[OTUS] Разработчик Python</strong>\n \n<strong>Описание:</strong>\nПрофессиональный онлайн-курс для тех, кто уже имеет опыт программирования на Python и хочет повысить свой уровень за счет новых знаний и навыков из различных областей разработки. Если вы уверенно чувствуете себя с Python, помните C, имеете представление о сетевом взаимодействии и реляционных СУБД, умеете обращаться с Linux, Git и прочими стандартными инструментами девелопера — курс для вас.\n \n<strong>Вы научитесь:</strong>\n🐍Как писать простой и идиоматичный код, за который не будет мучительно стыдно?\n🐍Как тестировать и поддерживать код на Python?\n🐍Как написать приложение, которое не умрёт под нагрузкой?\n \n🤢Цена курса:  ̶9̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶5̶2̶0̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-python/'
        photo = otus_courses[6]
    elif message.text == 'otus8':
        text = '<strong>[OTUS] Data Engineer</strong>\n \n<strong>Описание:</strong>\nКурс адресован разработчикам, администраторам СУБД и всем, кто стремится повысить профессиональный уровень, освоить новые инструменты и заниматься интересными задачами в сфере работы с данными.\n \n<strong>После обучения Data Engineering вы станете востребованным специалистом, который:</strong>\n🔥Разворачивает, налаживает и оптимизирует инструменты обработки данных\n🔥Адаптирует датасеты для дальнейшей работы и аналитики\n🔥Создает сервисы, которые используют результаты обработки больших объемов данных\n🔥Отвечает за архитектуру данных в компании\n\n\n🤢Цена курса: 8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/data-engineer/'
        photo = otus_courses[7]
    elif message.text == 'otus9':
        text = '<strong>[OTUS] Backend разработчик на PHP</strong>\n \n<strong>Описание:</strong>\nДля реализации больших и долгосрочных проектов современному PHP-разработчику необходимо заботиться об архитектуре кода, применять паттерны проектирования, писать код в соответствии с принципами SOLID и поддерживать высокий code coverage своих unit-тестов.\n \n<strong>Вы научитесь:</strong>\n💣Глубокое знакомство с библиотеками PHP и особенностями языка\n💣Навыки проектирования приложений, работы с базами и файлами, веб-фронтендом\n💣Привычку к хорошему и чистому коду\n💣Владение тактиками по созданию высоконагруженных систем\n \n🤢Цена курса: ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-php/'
        photo = otus_courses[8]
    elif message.text == 'otus10':
        text = '<strong>[OTUS] С++ для начинающих программистов</strong>\n<strong>Описание:</strong>\nКурс по разработке на C++ для начинающих программистов\nЗанятия в формате видео и проверочные тесты\nВсе необходимые знания и навыки для курса "Разработчик С++"\n<strong>Вы научитесь:</strong>\n🌟Классы и алгоритмы\n🌟Шаблоны классов и функций\n🌟Многопоточность\n🌟Исключения\n🌟Работа с сетью\n🤢Цена курса: ̶1̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶8̶6̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/online/online-cpp/'
        photo = otus_courses[9]
    elif message.text == 'otus11':
        text = '<strong>[OTUS] Архитектура и шаблоны проектирования </strong>\n \n<strong>Описание:</strong>\nКурс для разработчиков, которые хотят изучить основные паттерны проектирования и научиться применять их, находить им замену в сложных ситуациях и научиться мыслить как архитектор программного обеспечения.\n \n<strong>Вы научитесь:</strong>\n🔥Формирует представление об архитектуре приложения.\n🔥Даёт представление об основных шаблонах проектирования.\n🔥Даёт навыки построения архитектуры\n🔥Предлагает закрепление материалы через практические работы\n \n🤢Цена курса:  ̶4̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶1̶ ̶4̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/patterns/'
        photo = otus_courses[10]
    elif message.text == 'otus12':
        text = '<strong>[OTUS] Пентест. Практика тестирования на проникновение</strong>\n \n<strong>Описание:</strong>\nПентест — это процесс санкционированного взлома информационных систем по просьбе заказчика, в ходе которого пентестер (аудитор) выявляет уязвимости информационной системы и дает заказчику рекомендации по их устранению.\n \n<strong>Вы научитесь:</strong>\n🧨Основным этапам проведения тестирования на проникновение\n🧨Использованию современных инструментов для проведения анализа защищенности информационной системы или приложения\n🧨Классификации уязвимостей и методам их исправления\n🧨Навыкам программирования для автоматизации рутинных задач\n \n🤢Цена курса: ̶5̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶8̶9̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/pentest/process/'
        photo = otus_courses[11]
    elif message.text == 'otus13':
        text = '<strong>[OTUS] MS SQL Server разработчик</strong>\n \n<strong>Описание:</strong>\nКурс позволит понять детали процессов и получить чёткое представление, что делает тот или иной код, где могут возникнуть потенциальные проблемы, как их можно разрешить.\n \n<strong>Вы научитесь:</strong>\n🌟Разрабатывать на SQL\n🌟Проектировать БД и понимать все нюансы;\n🌟Анализировать и оптимизировать производительности запросов;\n🌟Писать сложные хранимые процедуры, функции и триггеры;\n🌟Читать план запроса.\n \n🤢Цена курса: ̶8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/ms-sql-server-razrabotchik/'
        photo = otus_courses[12]
    elif message.text == 'otus14':
        text = '<strong> [OTUS] Реляционные СУБД</strong>\n \n<strong>Описание:</strong>\nПолный курс по работе с базами данных реляционными и нереляционными.\nКурс включает в себя все основные и популярные БД, которые могут пригодиться разработчику: PostgreSQL, MySQL, Redis, MongoDB, Cassandra и т.д.\n \n<strong>Вы научитесь:</strong>\n🔥Научитесь проектировать базы данных и создавать оптимальную структуру их хранения;\n🔥Будете различать основные СУБД (PostgreSQL, MySQL, Redis, MongoDB, Cassandra и т.д );\n🔥Освоите синтаксис и особенности работы SQL, DDL, DML;\n🔥Сможете оптимизировать медленные запросы.\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/subd/'
        photo = otus_courses[13]
    elif message.text == 'otus15':
        text = '<strong>[OTUS] Python QA Engineer</strong>\n \n<strong>Описание:</strong>\nКурс позволит узнать, как решаются задачи автоматизации тестирования на реальных проектах с использованием языка Python. Освоив данный курс, вы получите навыки решения основных задач в области автоматизации тестирования веб-приложений.\n \n<strong>Вы научитесь:</strong>\n🔥Изучение всех видов тестирования: API, UI, бекенд, безопасности, чтобы быть максимально универсальным специалистом\n🔥Постоянная практика и решение кейсов, чтобы можно было рассказать на собеседовании о том, что делал, а не о том, что прочитал на хабре\n🔥Изучение инструментов диагностики работы сети и ОС Linux для определения причины возникновения багов\n \n🤢Цена курса:  ̶5̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶1̶8̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 390₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/avtomatizaciya-web-testirovaniya/?int_source=courses_catalog&int_term=testing'
        photo = otus_courses[14]
    if photo:
        print(url)
        bot.send_photo(message.from_user.id, photo=photo, caption=text,
                       reply_markup=one_course(message.from_user.id, url, school),
                       parse_mode='html')


bot.polling(none_stop=True, timeout=200)
