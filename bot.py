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

    except Exception as e:
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

    except Exception as e:
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

    except Exception as e:
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
    'AgACAgIAAxkBAAMQXx8BA9Pk2XMdKTC25b5zQ6Hd2VcAAkOvMRv_w_lIuaOXNp0mDy-9x36RLgADAQADAgADbQAD1TAGAAEaBA',
    'AgACAgIAAxkBAAMRXx8BJPd39Z1uC6cCiNkzG3E1En0AAkSvMRv_w_lIjpOtnqCQ0coM5OaSLgADAQADAgADbQADPVAEAAEaBA',
    'AgACAgIAAxkBAAMSXx8BOYc_7sdEOULLd16WMAymPh0AAkWvMRv_w_lICO28nMmNwB4KauiSLgADAQADAgADbQADkU8EAAEaBA',
    'AgACAgIAAxkBAAMTXx8BP2bhqhWOkplsUxO1AAGG8q_ZAAJGrzEb_8P5SDad-EqP7QElssvDki4AAwEAAwIAA20AA6TqBAABGgQ',
    'AgACAgIAAxkBAAMUXx8BQ4xLMMSyFxAEfs02skHdJj4AAkevMRv_w_lIGYr3WKGA86pG4xaVLgADAQADAgADbQADJxYCAAEaBA',
    'AgACAgIAAxkBAAMVXx8BS7BfbLYTdqHsDAFvz_XrEaQAAkivMRv_w_lIH-WX5QIHopFkXPiULgADAQADAgADbQADynoCAAEaBA',
    'AgACAgIAAxkBAAMWXx8BUdfjWXr5p3IU6B5bvzVqFWUAAkmvMRv_w_lIjqo7eX4hR1NJhe6SLgADAQADAgADbQADNl0EAAEaBA',
    'AgACAgIAAxkBAAMXXx8BVcOQ7pj2Lvg4MEsAAeB_flqhAAJKrzEb_8P5SGkmOI3FTCfCNKXskS4AAwEAAwIAA20AA9zZBAABGgQ',
    'AgACAgIAAxkBAAMYXx8BW-06aQABcGCv1xC_DCOJfwl4AAJLrzEb_8P5SAPXzlyHEHWVdy2Cki4AAwEAAwIAA20AA8FYBAABGgQ',
    'AgACAgIAAxkBAAMZXx8BYIjBn8X8IIRXHDAG5EBMPWUAAkyvMRv_w_lIIoPd4PHiYUQNmd-TLgADAQADAgADbQADpksDAAEaBA',
    'AgACAgIAAxkBAAMaXx8BZo21AazKZr577BfiCbQwb7AAAk2vMRv_w_lISUxpUw7zZ-Gp4haVLgADAQADAgADbQADrRsCAAEaBA',
    'AgACAgIAAxkBAAMbXx8BaRR-jqYrtPfIPugcTe_tPwgAAk6vMRv_w_lITIayRnNoAvMuobqSLgADAQADAgADbQADyfQEAAEaBA',
    'AgACAgIAAxkBAAMcXx8BduVvth6TFEiuimeZJ8U0mtYAAk-vMRv_w_lI7WCiu8o4boCvTICRLgADAQADAgADbQAD4SkGAAEaBA',
    'AgACAgIAAxkBAAMdXx8BeB2SJ6RxBXl5tla6uxxI1lgAAlCvMRv_w_lIbJ8zppMPI2rpGHSRLgADAQADAgADbQADrTIGAAEaBA',
    'AgACAgIAAxkBAAMeXx8Be3Edo-Nqumn_swABG03Q0CloAAJRrzEb_8P5SA-8sSMcD7c4CfXhkS4AAwEAAwIAA20AAyjVBAABGgQ']
netology_courses = [
    'AgACAgIAAxkBAANXXx8HwxAXtcwH2giThOpQtcIEKYAAAkivMRv_w_lIH-WX5QIHopFkXPiULgADAQADAgADbQADynoCAAEaBA',
    'AgACAgIAAxkBAANYXx8HxkqnayO1UUtFf802Cq_5cIUAAkevMRv_w_lIGYr3WKGA86pG4xaVLgADAQADAgADbQADJxYCAAEaBA',
    'AgACAgIAAxkBAANZXx8IVO744YEyd3PY_EKVpGkzG60AAnmvMRv_w_lIvijxXOhegmbUgNmTLgADAQADAgADbQAD_kMDAAEaBA',
    'AgACAgIAAxkBAANaXx8IWZsY3ehgq6rwW8Dp9IsDZgIAAnqvMRv_w_lIpXOUCUhZ__2OXUmRLgADAQADAgADbQADtnMGAAEaBA',
    'AgACAgIAAxkBAANbXx8IX__5fpAUi76JLquvnUL4LMgAAk-vMRv_w_lI7WCiu8o4boCvTICRLgADAQADAgADbQAD4SkGAAEaBA',
    'AgACAgIAAxkBAANcXx8IZWcuaeuJOTUHY7e1lgQoewUAAnuvMRv_w_lINxEE5-NqHR5oeOuSLgADAQADAgADbQAD5koEAAEaBA',
    'AgACAgIAAxkBAANdXx8IaFQPoEVnvhD81_MWFP1DiyQAAnyvMRv_w_lIkztdBfKvExNRLoKSLgADAQADAgADbQADnlMEAAEaBA',
    'AgACAgIAAxkBAANeXx8Ibr4N7XbF5z80hVz6bYf7iBUAAn2vMRv_w_lILA-2ZBjggPfZBOWRLgADAQADAgADbQAD-94EAAEaBA',
    'AgACAgIAAxkBAANfXx8IcsIhrbxYGyrEFFcRGb5j_SwAAn6vMRv_w_lIhUfp4GicstdIxn6RLgADAQADAgADbQADqTAGAAEaBA',
    'AgACAgIAAxkBAANgXx8IecQB72TpqdNxSCI6k-YknLMAAnmvMRv_w_lIvijxXOhegmbUgNmTLgADAQADAgADbQAD_kMDAAEaBA',
    'AgACAgIAAxkBAANhXx8IgaJ0CsApLHjLBAABaCO-tLghAAJ_rzEb_8P5SBxusnq29XLAJm5MkS4AAwEAAwIAA20AA3VrBgABGgQ',
    'AgACAgIAAxkBAANiXx8IiMintkyApTE0XJsaSMUL5PwAAoCvMRv_w_lI0dA3PvikucSb5OaSLgADAQADAgADbQAD4VQEAAEaBA',
    'AgACAgIAAxkBAANjXx8IlRAVwy0lDuAZxGvpRczeLaQAAoGvMRv_w_lIRZ3zy5SgXUxxg-6SLgADAQADAgADbQADdlMEAAEaBA',
    'AgACAgIAAxkBAANkXx8Im_ygwCzad17KhDSFRwro-qsAAoKvMRv_w_lIqAqHtC8Ql6ph9E2RLgADAQADAgADbQADp24GAAEaBA',
    'AgACAgIAAxkBAANlXx8IoJ6SIjLjR5UX_Rfx2TRF5v4AAoOvMRv_w_lIc1R-shiGEnoJx36RLgADAQADAgADbQADTToGAAEaBA']
otus_courses = ['AgACAgIAAxkBAAN8Xx8LbmV3vq1vrmRq93YMvCAPYwADh68xG__D-UhJ-JF63jBp0OiedZEuAAMBAAMCAANtAAO9MwYAARoE',
                'AgACAgIAAxkBAAN8Xx8LbmV3vq1vrmRq93YMvCAPYwADh68xG__D-UhJ-JF63jBp0OiedZEuAAMBAAMCAANtAAO9MwYAARoE',
                'AgACAgIAAxkBAAN9Xx8LeKxr3wZ4nln4yKtkZKlMISoAApevMRv_w_lIIi5LdR-INP97D-iRLgADAQADAgADbQADueEEAAEaBA',
                'AgACAgIAAxkBAAN-Xx8Lf0gE1ED8CXulvxCQ-uEWaXgAApivMRv_w_lIt3rMUHjMnDe8E96TLgADAQADAgADbQADFUoDAAEaBA',
                'AgACAgIAAxkBAAN_Xx8Ll5xUFliCHESIHNRXmv4ESZUAAjSvMRtNBvBIs_goaq4AAdcu9QlxkS4AAwEAAwIAA20AAwcqBgABGgQ',
                'AgACAgIAAxkBAAOAXx8LqRWGwyY_hSSlD-Nvmunba04AAnCvMRv_w_lI0PebS65BXhJDCCCVLgADAQADAgADbQADYBcCAAEaBA',
                'AgACAgIAAxkBAAOBXx8LrqOqkDnrGkwlBy0GlEKPhjEAAoavMRv_w_lIFDGMaEEuyY2-ouyRLgADAQADAgADbQADld4EAAEaBA',
                'AgACAgIAAxkBAAOCXx8LswYty2HnOcq47z4lH41PtlEAApmvMRv_w_lI_N23N6gKXLoCduuSLgADAQADAgADbQADoVcEAAEaBA',
                'AgACAgIAAxkBAAODXx8LuKtGvMsdSDnmmw4tJzSBevMAAkivMRv_w_lIH-WX5QIHopFkXPiULgADAQADAgADbQADynoCAAEaBA',
                'AgACAgIAAxkBAAOEXx8Lvqn4BjI8qJgfVUihuZGxE_QAApqvMRv_w_lIUX6SFrB7DXsJzMOSLgADAQADAgADbQADK-wEAAEaBA',
                'AgACAgIAAxkBAAOFXx8LwkIXRkHB_ZCmzWpNH_VIdbIAApuvMRv_w_lI1_ssYC6uUATMRMKSLgADAQADAgADbQADde8EAAEaBA',
                'AgACAgIAAxkBAAOGXx8LxuJmFoHAlzXgJYZ3_8a-IfUAApyvMRv_w_lIyC4HDCkadDzupOyRLgADAQADAgADbQADt9sEAAEaBA',
                'AgACAgIAAxkBAAOHXx8LyoqK_kX2X82lnfksnLXUGmUAAp2vMRv_w_lIoHYaYKp1_U7_nnWRLgADAQADAgADbQADvjQGAAEaBA',
                'AgACAgIAAxkBAAOIXx8LzxY47KP_RWwlCAYx6PmrNXMAAp6vMRv_w_lIsb0-2A6A_EmoTBKVLgADAQADAgADbQAD9RoCAAEaBA',
                'AgACAgIAAxkBAAOJXx8L2K-32ck1aHeFODuJjpbNqVQAAjavMRtNBvBItr2YK3czgZcdGnSRLgADAQADAgADbQADoioGAAEaBA']
webformyself_courses = [
    'AgACAgIAAxkBAANGXx8HPXdE9k-ndZ0IAAEkuEVcTUD0AAJtrzEb_8P5SMmb8E04JqnodxXeky4AAwEAAwIAA20AAy5OAwABGgQ',
    'AgACAgIAAxkBAANHXx8HPeyvqNHwi_FCxd1LDitkNScAAm6vMRv_w_lIMwABFaTI566ISwpxkS4AAwEAAwIAA20AA-4sBgABGgQ',
    'AgACAgIAAxkBAANIXx8HPaPm8JuCKrjenSnD24238PcAAm-vMRv_w_lIFLb0XYGDSX-q4-aSLgADAQADAgADbQAD2U8EAAEaBA',
    'AgACAgIAAxkBAANJXx8HPdrMq0nIUX4e2SWp3qBGj1wAAnCvMRv_w_lI0PebS65BXhJDCCCVLgADAQADAgADbQADYBcCAAEaBA',
    'AgACAgIAAxkBAANKXx8HPWWg1p3CDr72HW-Z0DAVZkwAAnGvMRv_w_lIJfcwdFmCGzn618aSLgADAQADAgADbQAD_uMEAAEaBA',
    'AgACAgIAAxkBAANLXx8HPWlJKE4Hao8AAaHol2g7VSNcAAJNrzEb_8P5SElMaVMO82fhqeIWlS4AAwEAAwIAA20AA60bAgABGgQ',
    'AgACAgIAAxkBAANMXx8HPYULCAEQryuxb4ddkCjHMz0AAlGvMRv_w_lID7yxIxwPtzgJ9eGRLgADAQADAgADbQADKNUEAAEaBA',
    'AgACAgIAAxkBAANNXx8HPZO9aeo7Yp4xODVBUbq-jxcAAnOvMRv_w_lIwIDAqxlKb0xos--RLgADAQADAgADbQADItcEAAEaBA',
    'AgACAgIAAxkBAANOXx8HPUb1oaJ9a_2mcprVnad3va0AAnSvMRv_w_lIVYe2WPmearKSAuWRLgADAQADAgADbQADRegEAAEaBA',
    'AgACAgIAAxkBAANPXx8HPeF1y8K-KfOEz4IWVoyZp08AAk-vMRv_w_lI7WCiu8o4boCvTICRLgADAQADAgADbQAD4SkGAAEaBA',
    'AgACAgIAAxkBAANQXx8HPX9bjlKBq1GocuFKi3PZpv4AAnavMRv_w_lI7eCEkBzBo5dGpLqSLgADAQADAgADbQAD5fAEAAEaBA',
    'AgACAgIAAxkBAANRXx8HPbnBu7mu9FP8u5UyzLcIJ44AAnevMRv_w_lIDfn4ZTo1mgABMK-9ki4AAwEAAwIAA20AA3zvBAABGgQ',
    'AgACAgIAAxkBAANSXx8HPSc24RMtcALKrRY1I6x_ogcAAnivMRv_w_lINWuhPG4C9Am9LYKSLgADAQADAgADbQADJFoEAAEaBA',
    'AgACAgIAAxkBAANTXx8HPVT3mbhk7s-1YiS5mw2VVDgAAnivMRv_w_lINWuhPG4C9Am9LYKSLgADAQADAgADbQADJFoEAAEaBA',
    'AgACAgIAAxkBAAN7Xx8K3drXZ1IQQuRpfcZzoMlPWvoAAp6yMRsiU_lISStIB8hYt6OdXfiULgADAQADAgADbQADZ38CAAEaBA']
skillbox_courses = [
    'AgACAgIAAxkBAAMiXx8CPFpSXd1jDyetKAVFk1MR_4AAAlOvMRv_w_lImn7OSeuuMwnYLO6RLgADAQADAgADbQADy9wEAAEaBA',
    'AgACAgIAAxkBAAMjXx8CRd7B0wYVaHTvP4jk2Ow4jcYAAlSvMRv_w_lIOnfdgbBaYKVfaOiSLgADAQADAgADbQADX1YEAAEaBA',
    'AgACAgIAAxkBAAMkXx8DQXmXm1CwjOCXeoBDEPyogk4AAkyvMRv_w_lIIoPd4PHiYUQNmd-TLgADAQADAgADbQADpksDAAEaBA',
    'AgACAgIAAxkBAAMlXx8DSL8oSU4-wX90XSroQW_ULu4AAmGvMRv_w_lIa9utm5ZSCagiorqSLgADAQADAgADbQADivEEAAEaBA',
    'AgACAgIAAxkBAAMmXx8DWVMkvj-diUl7n2WLbQ08UnoAAmKvMRv_w_lIx-tsLFRDuumCvcCSLgADAQADAgADbQADzvcEAAEaBA',
    'AgACAgIAAxkBAAMnXx8DcvbP3VJrLu0Qx22bdD-MmtsAAmOvMRv_w_lIyhM45L0jy7_2XviULgADAQADAgADbQADgH0CAAEaBA',
    'AgACAgIAAxkBAAMoXx8DeGAIGInzXG8zvFOjU5NQR9UAAmSvMRv_w_lIfPF4VRlDhqPCHbmSLgADAQADAgADbQADR_cEAAEaBA',
    'AgACAgIAAxkBAAMpXx8DfGUNwefPL0U_Jn6tHta9k9wAAmWvMRv_w_lI_sWs0HPj5HbJgh6VLgADAQADAgADbQADBxQCAAEaBA',
    'AgACAgIAAxkBAAMqXx8DgzwaqtL3AV0axVj4CL-CbbUAAmavMRv_w_lIVlP5DkwMDBro9uGRLgADAQADAgADbQADGeMEAAEaBA',
    'AgACAgIAAxkBAAMrXx8DiNKqZ4VpUxjtOx2-B7-4s_MAAmevMRv_w_lIEStFFrBinJJ_p4CSLgADAQADAgADbQAD4EoEAAEaBA',
    'AgACAgIAAxkBAAMsXx8DjE8xw1UYCgoAAdAyXXkLSdNLAAJorzEb_8P5SFPyaUUc8S-mbk4SlS4AAwEAAwIAA20AA8sYAgABGgQ',
    'AgACAgIAAxkBAAMtXx8D27kT9pbdAY3nVgWwdjslFkEAAmmvMRv_w_lIuxioUtTJpDvPo-yRLgADAQADAgADbQADIdsEAAEaBA',
    'AgACAgIAAxkBAAMuXx8D4soH0c83ahRapvHk3P5fWJAAAmqvMRv_w_lIU-aTV09CsQ4hGwiSLgADAQADAgADbQADU1cEAAEaBA',
    'AgACAgIAAxkBAAMvXx8D6ONIHVL6yOoIOMP25JShvoYAAmuvMRv_w_lIHXxKfXU371DS1faULgADAQADAgADbQADm38CAAEaBA',
    'AgACAgIAAxkBAAMwXx8D7Iz5FB3wrqE0INpzgI-_tkcAAmyvMRv_w_lIIrccSDzpHxzIm9-TLgADAQADAgADbQADJEsDAAEaBA']
udemy_courses = ['AgACAgIAAxkBAANpXx8JC3qxrXJb1YoyPxykLYymij8AAnmvMRv_w_lIvijxXOhegmbUgNmTLgADAQADAgADbQAD_kMDAAEaBA',
                 'AgACAgIAAxkBAANqXx8JFtAQoh9FxP-VqFVuPggm3YAAAoavMRv_w_lIFDGMaEEuyY2-ouyRLgADAQADAgADbQADld4EAAEaBA',
                 'AgACAgIAAxkBAANrXx8JGDMreZWH0PWIFKtFcG9IEBEAAoevMRv_w_lISfiRet4wadDonnWRLgADAQADAgADbQADvTMGAAEaBA',
                 'AgACAgIAAxkBAANsXx8JHPwi61PVKLT6tCyZPdWoFA8AAomvMRv_w_lIMnDqvPpOesKka0yRLgADAQADAgADbQAD6nEGAAEaBA',
                 'AgACAgIAAxkBAANtXx8JIFVcy-9Qb_0fVUVYRRc7MbcAAoqvMRv_w_lIfNrvSy3BWGRY8emSLgADAQADAgADbQADbVoEAAEaBA',
                 'AgACAgIAAxkBAANuXx8JJW2NuHplRThZVX24RGHUL-sAAouvMRv_w_lIRjT1OYpzRicE2PaULgADAQADAgADbQADpYECAAEaBA',
                 'AgACAgIAAxkBAANvXx8JLLWQPgt-YbSSNqMkR5nNKHAAAoyvMRv_w_lI3l335o99E_7w2PaULgADAQADAgADbQAD74ECAAEaBA',
                 'AgACAgIAAxkBAANwXx8JNzyqCsu6XAPtELwvZptnr4QAAmmvMRv_w_lIuxioUtTJpDvPo-yRLgADAQADAgADbQADIdsEAAEaBA',
                 'AgACAgIAAxkBAANxXx8JRBqku4WjOHNbMzZeQxPUuzQAAo6vMRv_w_lIgwf6zhO0Lfic_RyVLgADAQADAgADbQADHBcCAAEaBA',
                 'AgACAgIAAxkBAANyXx8JSFQpdLWD5v1Y9ORqFBvm_TsAAo-vMRv_w_lIDIb9AAFoATCPzJAhlS4AAwEAAwIAA20AA-kWAgABGgQ',
                 'AgACAgIAAxkBAANzXx8JTIdXXCGSiTW43m_l4rvcxKoAAk6vMRv_w_lITIayRnNoAvMuobqSLgADAQADAgADbQADyfQEAAEaBA',
                 'AgACAgIAAxkBAAN0Xx8JU5yqT6wciUhSAAFoCrOHs9hpAAKQrzEb_8P5SIKVk7wdgpnjEonmkS4AAwEAAwIAA20AA4HcBAABGgQ',
                 'AgACAgIAAxkBAAN1Xx8JXO0LCBGh1DJ3W__QB-NouZ0AApGvMRv_w_lIZoYTD8WOHO0Yse-RLgADAQADAgADbQAD5t4EAAEaBA',
                 'AgACAgIAAxkBAAN2Xx8JXyQHOVhVDsyw3WV3LsHudhIAApKvMRv_w_lI-jca_d5w74JL_RyVLgADAQADAgADbQADkxkCAAEaBA',
                 'AgACAgIAAxkBAAN3Xx8JY9JMQt61viGoaOZ3BR0GRTkAApOvMRv_w_lI96wUAAEfo7x2xtUTlS4AAwEAAwIAA20AA-kXAgABGgQ']
geekbrains_clouds = [('https://cloud.mail.ru/public/45dt/2sXphnx7S', '', ''),
                     ('https://cloud.mail.ru/public/3Qe2/3VC32qu1D', '', ''),
                     ('https://cloud.mail.ru/public/3mmv/jHRmscBiR', 'v9utq9c78=qv4q3t', ''),
                     ('https://cloud.mail.ru/public/2U2A/1m9nFpAqT', '', ''),
                     ('https://cloud.mail.ru/public/Se6p/5o4mEmQLi', 'WWW.infobit.me@2016', ''),
                     ('https://cloud.mail.ru/public/3x5q/28uLwUjcr', '', ''),
                     ('https://cloud.mail.ru/public/45Ae/eXCyArpUT', '', ''),
                     ('https://mega.nz/#F!f65DySiC!rMkWqMN2G7I-JnRtNADpmg', '',
                      'Если не открывается ссылка, используйте VPN для загрузки'),
                     ('https://cloud.mail.ru/public/3GeF/5P7vWpnWn', '', ''),
                     ('https://cloud.mail.ru/public/3QdZ/3sSxF5QC3', '', ''),
                     ('https://cloud.mail.ru/public/gT3t/5Q3V6Km79', '', ''),
                     ('https://drive.google.com/drive/folders/0B-R36PiAc5SHSUx2WXREUzlrbWs', '', ''),
                     ('https://yadi.sk/d/TOdytdXcUZ7UCQ', '', ''),
                     ('https://yadi.sk/d/ONylu_t6J5DN8g', '', ''),
                     ('https://cloud.mail.ru/public/L5Mn/vujyoaRmk', '', ''),
                     (
                         'https://docs.google.com/document/d/1G4vGhR9JDNN77KBXo62evDYEKnaalJ8WoNMKoFxuQdM/edit?usp=sharing',
                         '', '')]
skillbox_clouds = [('https://cloud.mail.ru/public/2Bj1/5c2pvbnbB', '', ''),
                   ('https://cloud.mail.ru/public/46vF/43wWAnWzd', '', ''),
                   ('https://cloud.mail.ru/public/4wJ8/PMnPcxF8G', '', ''),
                   ('https://yadi.sk/d/DcNTOdb32MWL_w', '', ''),
                   ('https://cloud.mail.ru/public/557t/aAFpcyZoF', '', ''),
                   ('https://cloud.mail.ru/public/4E5L/2gTjSoMQD', '', ''),
                   ('https://cloud.mail.ru/public/34E5/2JQdKzQa5', '', ''),
                   ('https://cloud.mail.ru/public/54YG/3K5B1EDuV', '', ''),
                   ('https://cloud.mail.ru/public/MvKY/AzmKmtbaX', '', ''),
                   ('https://cloud.mail.ru/public/3c4B/4hE4m4svK', '', ''),
                   ('https://yadi.sk/d/JaM2OX52Uka1bQ', '', ''),
                   ('https://mega.nz/#F!PIUhABrA!BbfEl0AfO_h8QkaGlq-31w', '4z9dj_7kE>8d',
                    'Если не открывается ссылка, используйте VPN для загрузки'),
                   (
                       'https://www.obuka.org/course/skillbox-figma-3-0-2019/6468-modul-1-vvedenie-v-figma-obzor-vozmojnostey/?p=1',
                       '', ''),
                   ('https://cloud.mail.ru/public/4XFp/Gw9N6p8bk', '', ''),
                   ('https://cloud.mail.ru/public/59AT/3UGXJwvyA', '', ''),
                   ('https://docs.google.com/document/d/1YICN4AqVNM68Mb3m6ArJO4TunhN2guyRXzcdQKi5VQc/edit?usp=sharing',
                    '', '')]
webformyself_clouds = [('https://cloud.mail.ru/public/5mpi/3jrGzfXTr', '*P06WOAQCYpudFWt38GL', ''),
                       ('https://cloud.mail.ru/public/475o/5nWcfgdq2', '', ''),
                       ('https://cloud.mail.ru/public/4KYu/4c5HnB2s4 ', 'PnURDCcK+umtoqi+X5-r', ''),
                       ('https://cloud.mail.ru/public/5tAG/2WAdLbWFr', '', ''),
                       ('https://cloud.mail.ru/public/4zuC/PGfKq7GKN', '', ''),
                       ('https://cloud.mail.ru/public/5gVF/32QFwdctH', '', ''),
                       ('https://cloud.mail.ru/public/3pbT/3PiqyJJgi', 'boominfo.ru', ''),
                       ('https://cloud.mail.ru/public/3GoN/mKTRHWMN9', 'iG3DgL8gaapAYvdslNbH', ''),
                       ('https://cloud.mail.ru/public/2kNB/3SV1rp3Gv', '', ''),
                       ('https://cloud.mail.ru/public/4C6B/zzwrkibck', '', ''),
                       ('https://drive.google.com/file/d/0ByrBQHjtdyvxalFmT1BqR2hGN2c/view', '', ''),
                       ('https://cloud.mail.ru/public/4Vmb/VKHqoRcxc', '', ''),
                       ('https://cloud.mail.ru/public/3epA/3KDZMqueV', '', ''),
                       ('https://cloud.mail.ru/public/23JP/29QeD7PAY', '', ''),
                       ('https://drive.google.com/uc?id=0B_CgcOGcfxd9c21EQTBZWnZ3alU&export=download', '', ''),
                       (
                           'https://docs.google.com/document/d/1c2AOfLPT0UqkGOv_1YeFe1_1L7oJz1wTRGa4Si-R2LI/edit?usp=sharing',
                           '', '')]
netology_clouds = [('https://yadi.sk/d/0oAsDnYilAuqnQ', 'ASdkzxczmr234', ''),
                   ('https://cloud.mail.ru/public/2UEK/rRLKv5P8N', '', ''),
                   ('https://cloud.mail.ru/public/3iQd/32GvAbcAE', '', ''),
                   ('https://yadi.sk/d/wIX0BbWERd28gA', '', ''),
                   ('https://cloud.mail.ru/public/3Lc6/56YfZZLYx', '', ''),
                   ('https://cloud.mail.ru/public/2rBY/3Fmx8uCrm', '', ''),
                   ('https://cloud.mail.ru/public/26pG/kmvQsxA8n', '', ''),
                   ('https://cloud.mail.ru/public/3mRG/3mpHDQEcN', '', ''),
                   ('https://cloud.mail.ru/public/4H8j/5n2VowXjf', '', ''),
                   ('https://yadi.sk/d/lkEbSYroP-kqjw', 'www.infosklad.org', ''),
                   ('https://cloud.mail.ru/public/4yUD/TxkzXytMJ', '79809puhjgfdgAW', ''),
                   ('https://cloud.mail.ru/public/39hC/35rjs8RnS', '', ''),
                   ('https://cloud.mail.ru/public/5oDw/52mXULe9B', '', ''),
                   ('https://cloud.mail.ru/public/5ndq/2k8ZYKS6s', '', ''),
                   ('https://cloud.mail.ru/public/2AKj/2hRsUiXrD', '', ''),
                   ('https://docs.google.com/document/d/1Gukyj_mhaEM61rGxrmquvT35qQBIGXUFqezQlMF_HtY/edit?usp=sharing',
                    '', '')]
udemy_clouds = [('https://cloud.mail.ru/public/2vnq/KAvTyy5C8', '', ''),
                ('https://cloud.mail.ru/public/2w8u/3cKh8G2P7', '', ''),
                ('https://cloud.mail.ru/public/FKvQ/4yJsfw1c9', '', ''),
                ('https://cloud.mail.ru/public/3Pra/5efk2PAHD', '', ''),
                ('https://cloud.mail.ru/public/529o/56kMg8AR3', '', ''),
                ('https://cloud.mail.ru/public/ktq2/5wL5XFnx4', '', ''),
                ('https://yadi.sk/d/Iu7RlD6Dj7DeYg', '', ''),
                ('https://cloud.mail.ru/public/44RQ/4zREiFxwZ', '', ''),
                ('https://cloud.mail.ru/public/3WWE/2Smgkdpi4', '', ''),
                ('https://cloud.mail.ru/public/2d9S/5jSpt4udg', '', ''),
                ('https://cloud.mail.ru/public/3nRd/4sjwSgRhj', '', ''),
                ('https://cloud.mail.ru/public/2uz2/28CXPLb3k', '', ''),
                ('https://cloud.mail.ru/public/5B9r/3kqX3hdFW', '', ''),
                ('https://cloud.mail.ru/public/4Gd4/4VUWgSRP2', '', ''),
                ('https://cloud.mail.ru/public/3rk5/3KgXzFT4u', '', ''),
                ('https://docs.google.com/document/d/1TOvRB0jVpRa0wTKwYTuMQkqztj6NflMRPoEqlfAgcPU/edit?usp=sharing', '',
                 '')]
otus_clouds = [('https://cloud.mail.ru/public/4k9e/54v2kmjyC', '', ''),
               ('https://cloud.mail.ru/public/2NtN/3ND8GHPFR', '', ''),
               ('https://yadi.sk/d/M_RvXysm1rIgkw', '', ''),
               ('https://drive.google.com/drive/folders/171bFgjO0Z71unomeZPCeBaXXBvfa62u0', '', ''),
               ('https://cloud.mail.ru/public/2Ri5/2hHUUnXQ6', '', ''),
               ('https://cloud.mail.ru/public/4x7k/2qKomB3RH', '', ''),
               ('https://cloud.mail.ru/public/49oi/3pFwx3xmq', '', ''),
               ('https://cloud.mail.ru/public/4SAp/5wDtzx3oX', '', ''),
               ('https://yadi.sk/d/Fd8IDU4HlfDYdA', '', ''),
               ('https://cloud.mail.ru/public/5yYw/MCnGyDru4', '', ''),
               ('https://cloud.mail.ru/public/3zsX/3gqCKQF7v', '', ''),
               ('https://cloud.mail.ru/public/ZgRJ/TcDPj2cXD', '', ''),
               ('https://yadi.sk/d/ZWrxwxTR1YV8rw', 'sharewood.biz', ''),
               ('https://cloud.mail.ru/public/43bu/ceFuRrHHj', '', ''),
               ('https://yadi.sk/d/WTwmF2mKqXWhPA \n https://yadi.sk/d/dE3KNvn5ZWQvvQ', '', ''),
               ('https://docs.google.com/document/d/1_-dcJMf0mxNECIrP33q70-JLf6Cr2GqX_W3BWJ8MH_s/edit?usp=sharing', '',
                '')]


def payment_method(client_id):
    pm = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Банковской картой',
                                       callback_data='pay' + query_with_fetchone('payment_course',
                                                                                 client_id) + ' ' + 'credit card')
    but_2 = types.InlineKeyboardButton(text='Qiwi кошелек', callback_data='pay' + query_with_fetchone('payment_course',
                                                                                                      client_id) + ' ' + 'qiwi wallet')
    but_3 = types.InlineKeyboardButton(text='Kaspi Gold', callback_data='pay' + query_with_fetchone('payment_course',
                                                                                                    client_id) + ' ' + 'kaspi gold')
    but_4 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    pm.add(but_1, but_2, but_3)
    pm.add(but_4)
    return pm


def credit_keyboard( url, client_id):
    ck = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Оплатить ', url=url)
    but_2 = types.InlineKeyboardButton(text='Назад',
                                       callback_data=query_with_fetchone('payment_course', client_id)[3:] + 'rep')
    ck.add(but_1, but_2)
    return ck


def sucful_payment(client_id):
    sp = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Подтверждаю',
                                       callback_data='suc' + query_with_fetchone('payment_course', client_id)[
                                                             3:] + ' ' + str(client_id))
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
    but_1 = types.InlineKeyboardButton('Список курсов', switch_inline_query_current_chat='GeekBrains')
    but_2 = types.InlineKeyboardButton("Купить все от GeekBrains",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
    gb.add(but_1)
    gb.add(but_2)
    gb.add(but_3)
    return gb


def sb_school():
    sb = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('Список курсов', switch_inline_query_current_chat='SkillBox')
    but_2 = types.InlineKeyboardButton(text="Купить все от SkillBox",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
    sb.add(but_1)
    sb.add(but_2)
    sb.add(but_3)
    return sb


def ud_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('Список курсов ', switch_inline_query_current_chat='Udemy')
    but_2 = types.InlineKeyboardButton("Купить все от Udemy",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def ot_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('Список курсов', switch_inline_query_current_chat='OTUS')
    but_2 = types.InlineKeyboardButton("Купить все от OTUS",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def wb_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('Список курсов', switch_inline_query_current_chat='WebForMySelf')
    but_2 = types.InlineKeyboardButton("Купить все от WebForMySelf",
                                       callback_data=but_1.switch_inline_query_current_chat + '16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
    ud.add(but_1)
    ud.add(but_2)
    ud.add(but_3)
    return ud


def nt_school():
    ud = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('Список курсов', switch_inline_query_current_chat='Netology')
    but_2 = types.InlineKeyboardButton("Купить все от Netology",
                                       callback_data='Netology16')
    but_3 = types.InlineKeyboardButton('Назад', switch_inline_query_current_chat='courses')
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
        print('try inline query')
        with open('stats.txt', mode='r', encoding="utf-8") as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            try:
                content[query_with_fetchone('position_of_pointer', query.from_user.id)] = content[query_with_fetchone(
                    'position_of_pointer', query.from_user.id)][:-25] + query.query + ' ' + content[
                                                                                                query_with_fetchone(
                                                                                                    'position_of_pointer',
                                                                                                    query.from_user.id)][
                                                                                            -25:]
            except:
                pass
            file.writelines(content)
    except:
        pass
    icon_1 = 'https://imagizer.imageshack.com/img923/4231/SRsEFv.jpg'
    icon_2 = 'https://imagizer.imageshack.com/img922/6510/0WjfGC.jpg'
    icon_3 = 'https://imagizer.imageshack.com/img924/9480/sBPIE4.png'
    icon_4 = 'https://imagizer.imageshack.com/img923/2944/TDZF3m.jpg'
    icon_5 = 'https://imagizer.imageshack.com/img924/2395/WwgFJU.png'
    icon_6 = 'https://imagizer.imageshack.com/img922/5809/yX5oKr.jpg'
    article_1 = types.InlineQueryResultArticle(id=1, input_message_content=types.InputTextMessageContent(
        '🧠 GeekBrains - образовательный портал IT-профессий'),
                                               title='GeekBrains', description='GeekBrains courses', thumb_url=icon_1,
                                               thumb_width=48, thumb_height=48, reply_markup=gb_school())
    article_2 = types.InlineQueryResultArticle(id=4, input_message_content=types.InputTextMessageContent(
        '📚 SkillBox - онлайн-образование от практиков своего дела'),
                                               title='SkillBox', description='SkillBox courses', thumb_url=icon_2,
                                               thumb_width=48, thumb_height=48, reply_markup=sb_school())
    article_3 = types.InlineQueryResultArticle(id=3,
                                               input_message_content=types.InputTextMessageContent(
                                                   '💻 WebForMySelf - лидер в сфере веб-разработки и сайтостроения'),
                                               title='WebForMyself', description='WebForMyself courses',
                                               thumb_url=icon_3, thumb_width=48, thumb_height=48,
                                               reply_markup=wb_school())
    article_4 = types.InlineQueryResultArticle(id=2, input_message_content=types.InputTextMessageContent(
        '🏛 Netology - онлайн-университет и источник экспертных знаний'),
                                               title='Netology', description='Netology courses', thumb_url=icon_4,
                                               thumb_width=48, thumb_height=48, reply_markup=nt_school())
    article_5 = types.InlineQueryResultArticle(id=5, input_message_content=types.InputTextMessageContent(
        '👨‍💻 Udemy - лучшая образовательная онлайн-платформа'),
                                               title='Udemy', description='Udemy courses', thumb_url=icon_5,
                                               thumb_width=48, thumb_height=48, reply_markup=ud_school())
    article_6 = types.InlineQueryResultArticle(id=6, input_message_content=types.InputTextMessageContent(
        '👨‍🎓 OTUS - цифровые навыки от ведущих экспертов'),
                                               title='OTUS', description='OTUS courses', thumb_url=icon_6,
                                               thumb_width=48, thumb_height=48, reply_markup=ot_school())
    results = [article_1, article_2, article_3, article_4, article_5, article_6]
    bot.answer_inline_query(query.id, results)


@bot.inline_handler(
    lambda query: query.query in ['GeekBrains', 'Netology', 'OTUS', 'WebForMySelf', 'Udemy', 'SkillBox'])
def schools(query):
    global content
    try:
        print('try inline')
        with open('stats.txt', mode='r', encoding="utf-8") as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            try:
                content[query_with_fetchone('position_of_pointer', query.from_user.id)] = content[query_with_fetchone(
                    'position_of_pointer', query.from_user.id)][:-25] + query.text + ' ' + content[
                                                                                                   query_with_fetchone(
                                                                                                       'position_of_pointer',
                                                                                                       query.from_user.id)][
                                                                                               -25:]
            except:
                pass
            file.writelines(content)
    except Exception as e:
        print(e)
        pass
    if query.query == 'GeekBrains':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣1️⃣'),
                                                   title='Профессия Разработчик игр',
                                                   description='Стань частью игровой индустрии',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6049/wcpahi.jpg',
                                                   reply_markup=gb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣2️⃣'),
                                                   title='Профессия Программист Android',
                                                   description='Разрабатывай под 80% рынка мобильных устройств!',
                                                   thumb_url='https://imagizer.imageshack.com/img922/7097/C2sRw9.png',
                                                   reply_markup=gb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣3️⃣'),
                                                   title='Профессия Frontend-разработчик',
                                                   description='Профессиональная верстка сайтов по современным '
                                                               'стандартам',
                                                   thumb_url='https://imagizer.imageshack.com/img922/5341/CeMvD6.jpg',
                                                   reply_markup=gb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣4️⃣'),
                                                   title='Курс по Agile-методологиям',
                                                   description='Когда дедлайны горят, заказчик дает новые вводные, '
                                                               'а в продуктах встречаются ошибки, используйте '
                                                               'Agile-метод.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/84/i23qQ7.png',
                                                   reply_markup=gb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣5️⃣'),
                                                   title='Профессия Веб-разработчик',
                                                   description='Создай свой фейсбук!С музыкой и нормальным интерфейсом',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6565/dLJYLy.jpg',
                                                   reply_markup=gb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣6️⃣'),
                                                   title='Профессиональная Backend-разработка',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса backend-разработки ',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3277/V3opMS.png',
                                                   reply_markup=gb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣7️⃣'),
                                                   title='Создание сайтов и приложений. Методы повышения конверсии',
                                                   description='Создавай действительно продающие структуры сайтов',
                                                   thumb_url='https://imagizer.imageshack.com/img923/558/XMlivo.jpg',
                                                   reply_markup=gb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣8️⃣'),
                                                   title='Факультет Python-разработки',
                                                   description='Онлайн-университет от @mail.ru Group',
                                                   thumb_url='https://imagizer.imageshack.com/img924/9392/UCl3tF.jpg',
                                                   reply_markup=gb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'GeekBrains🧠0️⃣9️⃣'),
                                                   title='Системный администратор',
                                                   description='Незаменимый специалист в любой компании',
                                                   thumb_url='https://imagizer.imageshack.com/img923/8554/aScFbP.jpg',
                                                   reply_markup=gb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣0️⃣'),
                                                    title='Дизайнер интерфейсов',
                                                    description='Факультет Дизайна интерфейсов (UX/UI)',
                                                    thumb_url='https://imagizer.imageshack.com/img922/3497/cs4Eto.jpg',
                                                    reply_markup=gb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣1️⃣'),
                                                    title='1С-Битрикс: Управление сайтом',
                                                    description='Всё необходимое для запуска и ведения бизнеса:CMS',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7259/47VpVE.jpg',
                                                    reply_markup=gb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣2️⃣'),
                                                    title='Школа Программирования. Java 0, 1, 2.',
                                                    description='Написано однажды - работает везде',
                                                    thumb_url='https://imagizer.imageshack.com/img922/1973/CfOxaX.png',
                                                    reply_markup=gb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣3️⃣'),
                                                    title='Базы данных для профессионалов и язык SQL',
                                                    description='Проектирование БД и запросы SQL',
                                                    thumb_url='https://imagizer.imageshack.com/img923/4985/1Rw1BR.png',
                                                    reply_markup=gb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣4️⃣'),
                                                    title='Анатомия блокчейна',
                                                    description='На пике технического прогресса',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7537/Mn107B.jpg',
                                                    reply_markup=gb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'GeekBrains🧠1️⃣5️⃣'),
                                                    title='Node.js Серверное программирование на JavaScript',
                                                    description='Создавай веб-сервисы с помощью популярного '
                                                                'фреймворка Express.js',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9976/xpE4KK.png',
                                                    reply_markup=gb_school())
        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'SkillBox':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣1️⃣'),
                                                   title='Дизайн мобильных приложений',
                                                   description='За 8 месяцев научитесь создавать дизайн под '
                                                               'разные мобильные платформы',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6688/YLaF26.png',
                                                   reply_markup=sb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣2️⃣'),
                                                   title='Управление digital-проектами',
                                                   description='За четыре месяца вы освоите все этапы работы над '
                                                               'проектом',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8969/lY3YcD.jpg',
                                                   reply_markup=sb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣3️⃣'),
                                                   title='UX-дизайн, UX-аналитика, UI-анимация',
                                                   description='Погрузитесь в самую популярную профессию за 4 месяца.',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6160/6tQ5Ir.jpg',
                                                   reply_markup=sb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣4️⃣'),
                                                   title='Cinema 4D для веб-дизайна',
                                                   description="Сможете создавать графику для рекламы, кино или ТV",
                                                   thumb_url='https://imagizer.imageshack.com/img924/6632/KbRFFr.png',
                                                   reply_markup=sb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣5️⃣'),
                                                   title='Таргетированная реклама Вконтакте',
                                                   description='Учат всему:от того, как писать статьи и оформлять группу;до основ парсинга и рассылок',
                                                   thumb_url='https://imagizer.imageshack.com/img923/4493/UDlNK4.jpg',
                                                   reply_markup=sb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣6️⃣'),
                                                   title='UI анимация. Стань motion-дизайнером за 16 недель',
                                                   description='Научитесь превращать статичный дизайн в динамичные '
                                                               'креативные интерфейсы.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/4631/YSnodB.png',
                                                   reply_markup=sb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣7️⃣'),
                                                   title='Сквозная аналитика',
                                                   description='Вы научитесь выжимать максимум из рекламы, '
                                                               'принимать решения на основе точных данных',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3386/Gx1DUN.jpg',
                                                   reply_markup=sb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣8️⃣'),
                                                   title='Как открыть и развивать свою веб-студию',
                                                   description='Запустите digital-агентство всего за 3,5 месяца.',
                                                   thumb_url='https://imagizer.imageshack.com/img923/7425/83nbUl.jpg',
                                                   reply_markup=sb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'SkillBox📚0️⃣9️⃣'),
                                                   title='Рекламная Графика',
                                                   description='Курс от создателей самых сочных рекламных иллюстраций '
                                                               'на российском рынке',
                                                   thumb_url='https://imagizer.imageshack.com/img924/6655/mN1T6z.jpg',
                                                   reply_markup=sb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣0️⃣'),
                                                    title='Excel c 0 до PRO',
                                                    description='Научитесь составлять сложные отчёты и строить '
                                                                'прогнозы',
                                                    thumb_url='https://imagizer.imageshack.com/img922/4359/2s9kaf.jpg',
                                                    reply_markup=sb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣1️⃣'),
                                                    title='Adobe After Effects с 0 до PRO',
                                                    description='На курсе вы освоите самый популярный в мире '
                                                                'инструмент для работы с анимацией',
                                                    thumb_url='https://imagizer.imageshack.com/img924/5734/F1r8Hv.jpg',
                                                    reply_markup=sb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣2️⃣'),
                                                    title='Профессия С#-разработчик',
                                                    description='130 часов обучения — и вы научитесь писать программы, разрабатывать веб-сервисы и игры на языке от Microsoft, в команде и индивидуально',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9595/7FhQEE.jpg',
                                                    reply_markup=sb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣3️⃣'),
                                                    title='Онлайн-курс Figma 3.0',
                                                    description='Вы освоите популярный сервис для разработки '
                                                                'интерфейсов Figma',
                                                    thumb_url='https://imagizer.imageshack.com/img924/26/BWxykA.png',
                                                    reply_markup=sb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣4️⃣'),
                                                    title='Практический интенсивный курс SMM менеджер',
                                                    description='Вы научитесь создавать '
                                                                'вовлекающий контент, общаться с аудиторией и '
                                                                'запускать рекламу',
                                                    thumb_url='https://imagizer.imageshack.com/img922/4848/hQENuo.png',
                                                    reply_markup=sb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'SkillBox📚1️⃣5️⃣'),
                                                    title='Профессия интернет-маркетолог от А до Я',
                                                    description='Вы с нуля научитесь выстраивать стратегию '
                                                                'продвижения бизнеса',
                                                    thumb_url='https://imagizer.imageshack.com/img922/2634/WjKwAG.png',
                                                    reply_markup=sb_school())
        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'Udemy':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣1️⃣'),
                                                   title='ITtensive - Базовый Python',
                                                   description='Изучите с нуля самый востребованный язык '
                                                               'программирования',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3961/F5dFaz.png',
                                                   reply_markup=ud_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣2️⃣'),
                                                   title='Продвинутые навыки Python: станьте лучшим разработчиком '
                                                         'Python!',
                                                   description='В этом курсе вы узнаете много встроенных функций и '
                                                               'овладеете их преимуществами.',
                                                   thumb_url='https://imagizer.imageshack.com/img923/5372/T4pET7.jpg',
                                                   reply_markup=ud_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣3️⃣'),
                                                   title='iOS программирование на Swift',
                                                   description='Практический курс по созданию iOS приложения на языке '
                                                               'Swift в среде Xcode и публикации его в AppStore',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ud_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣4️⃣'),
                                                   title='Kotlin. От А до Я',
                                                   description='Узнай за что Kotlin так полюбили в Google!',
                                                   thumb_url='https://imagizer.imageshack.com/img922/2655/hDxlt6.png',
                                                   reply_markup=ud_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣5️⃣'),
                                                   title='React Native 2020. Мобильная разработка на JavaScript',
                                                   description="Научись создавать крутейшие мобильные приложения для "
                                                               "Android и iOS на JavaScript + React JS",
                                                   thumb_url='https://imagizer.imageshack.com/img922/1056/o81JjI.jpg',
                                                   reply_markup=ud_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣6️⃣'),
                                                   title='Android разработка с нуля до профессионала',
                                                   description='Android, основы Java, Kotlin. Создай 21 приложение, '
                                                               'включая Firebase real-time чат и приложение заказа '
                                                               'такси!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/2665/oM9XRj.png',
                                                   reply_markup=ud_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣7️⃣'),
                                                   title='PHP v.7+ и MySQL с нуля',
                                                   description='Начните с основ и создайте полноценную CMS!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/3152/jplVFA.png',
                                                   reply_markup=ud_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣8️⃣'),
                                                   title='Программирование на C#: от новичка до специалиста',
                                                   description='Изучите C# и платформу .NET, включая .NET Core и '
                                                               'начните практиковать объектно-ориентированное '
                                                               'программирование',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8886/0dJ95T.png',
                                                   reply_markup=ud_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Udemy👨‍💻0️⃣9️⃣'),
                                                   title='Программирование игр для детей на Scratch для начинающих',
                                                   description='Научитесь основам программирования и созданию '
                                                               'увлекательных компьютерных игр в интересном формате с '
                                                               'помощью Scratch',
                                                   thumb_url='https://imagizer.imageshack.com/img922/4049/X4LqGg.png',
                                                   reply_markup=ud_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣0️⃣'),
                                                    title='Создание Telegram ботов с помощью JavaScript: Полное '
                                                          'руководство ',
                                                    description='Создайте чат-ботов Telegram с Node.js, используя '
                                                                'современный Telegraf Framework',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8400/OS8IYK.jpg',
                                                    reply_markup=ud_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣1️⃣'),
                                                    title='Продвинутые алгоритмы в Java',
                                                    description='Лучший курс по Java',
                                                    thumb_url='https://imagizer.imageshack.com/img922/906/L3oGTD.png',
                                                    reply_markup=ud_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣2️⃣'),
                                                    title='Аналитика и Data Science для менеджеров и гуманитариев',
                                                    description='Профкурс по аналитике для социально-экономических '
                                                                'направлений. Современные методы поиска скрытых '
                                                                'закономерностей',
                                                    thumb_url='https://imagizer.imageshack.com/img923/1600/1N4TKz.png',
                                                    reply_markup=ud_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣3️⃣'),
                                                    title='Основы программирования',
                                                    description='Основные понятия, алгоритмы и блок-схемы',
                                                    thumb_url='https://imagizer.imageshack.com/img922/3774/f554V8.png',
                                                    reply_markup=ud_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣4️⃣'),
                                                    title='Машинное обучение: кластеризация и классификация на Python',
                                                    description="Выигрываем соревнование Kaggle с kNN, SVM, "
                                                                "логистической регрессией, случайным лесом, XGBoost, "
                                                                "CatBoost и LightGBM",
                                                    thumb_url='https://imagizer.imageshack.com/img924/1604/6VOBKY.jpg',
                                                    reply_markup=ud_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Udemy👨‍💻1️⃣5️⃣'),
                                                    title='Изучаем Linux и командную строку. Линукс шаг за шагом',
                                                    description='Администрирование Linux, используюя командную строку '
                                                                'bash',
                                                    thumb_url='https://imagizer.imageshack.com/img924/1100/XYrY6t.png',
                                                    reply_markup=ud_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'Netology':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣1️⃣'),
                                                   title='PHP/SQL: back-end разработка и базы данных',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса backend-разработки ',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8519/rNEsyy.png',
                                                   reply_markup=nt_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣2️⃣'),
                                                   title='Веб-дизайн: Эффективный сайт от идеи до реализации',
                                                   description='Пройдите все этапы разработки дизайна продукта с нуля',
                                                   thumb_url='https://imagizer.imageshack.com/img923/4756/FTRedT.jpg',
                                                   reply_markup=nt_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣3️⃣'),
                                                   title='Python для работы с данными',
                                                   description="Освойте ключевой инструмент в мире аналитики и "
                                                               "машинного обучения",
                                                   thumb_url='https://imagizer.imageshack.com/img923/7515/w2ceS4.png',
                                                   reply_markup=nt_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣4️⃣'),
                                                   title='Аналитик данных',
                                                   description='Научим с нуля собирать, анализировать и презентовать '
                                                               'данные',
                                                   thumb_url='https://imagizer.imageshack.com/img922/9082/J0RDQG.jpg',
                                                   reply_markup=nt_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣5️⃣'),
                                                   title='SQL и получение данных',
                                                   description='Научим получать данные для анализа без помощи '
                                                               'разработчиков',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6286/mE6xiK.png',
                                                   reply_markup=nt_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣6️⃣'),
                                                   title='Power BI: анализ и визуализация данных без программирования',
                                                   description='инструмент бизнес-анализа, позволяющий анализировать '
                                                               '«живые» данные и создавать визуальные отчёты',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6430/OkjPfV.png',
                                                   reply_markup=nt_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣7️⃣'),
                                                   title='BIG DATA с нуля',
                                                   description='Научитесь работать с большими данными,Перейдите на '
                                                               'новый уровень в профессии',
                                                   thumb_url='https://imagizer.imageshack.com/img922/6725/Y8rzwz.jpg',
                                                   reply_markup=nt_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣8️⃣'),
                                                   title='Таргетированная реклам',
                                                   description='Курс одобрен компаниями ВКонтакте и myTarget',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8099/kJAshb.jpg',
                                                   reply_markup=nt_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'Netology🏛0️⃣9️⃣'),
                                                   title='Геймдизайн',
                                                   description='Превращайте идеи в успешные игровые проекты',
                                                   thumb_url='https://imagizer.imageshack.com/img923/6162/fTVCcG.jpg',
                                                   reply_markup=nt_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Netology🏛1️⃣0️⃣'),
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
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Netology🏛1️⃣2️⃣'),
                                                    title='Анализ статистики сайта с помощью Яндекс.Метрики',
                                                    description='Для отслеживания поведение посетителей на сайте, '
                                                                'оценки отдачи от рекламных кампаний',
                                                    thumb_url='https://imagizer.imageshack.com/img923/7376/AKFeM9.jpg',
                                                    reply_markup=nt_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Netology🏛1️⃣3️⃣'),
                                                    title='Математика для анализа данных',
                                                    description='Если специалист не разбирается в этих направлениях — гипотезы и выводы будут неточными',
                                                    thumb_url='https://imagizer.imageshack.com/img924/6558/aWldIr.png',
                                                    reply_markup=nt_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Netology🏛1️⃣4️⃣'),
                                                    title='Основы поисковой оптимизации (SEO)',
                                                    description='Как использовать факторы ранжирования и работать с '
                                                                'разными типами пользовательских запросов',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8043/IcXiRk.png',
                                                    reply_markup=nt_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'Netology🏛1️⃣5️⃣'),
                                                    title='Исследуйте в R',
                                                    description='Прокачайтесь до уровня middle в прогнозировании и '
                                                                'визуализации в R-Studio',
                                                    thumb_url='https://imagizer.imageshack.com/img923/8065/1ES0y7.jpg',
                                                    reply_markup=nt_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'OTUS':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣1️⃣'),
                                                   title='iOS-разработчик. Базовый курс',
                                                   description=' Все что нужно чтобы '
                                                               'претендовать на должность iOS-разработчика уровня '
                                                               'junior+',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ot_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣2️⃣'),
                                                   title='iOS Разработчик. Продвинутый курс v 2.0',
                                                   description="Вся мощь Swift 5.2 для развития профессиональных "
                                                               "навыков уровня Middle/Senior iOS Developer",
                                                   thumb_url='https://imagizer.imageshack.com/img924/5301/Btm9Ln.jpg',
                                                   reply_markup=ot_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣3️⃣'),
                                                   title='Разработчик Golang',
                                                   description='При переходе на Go люди зачастую сталкиваются с '
                                                               'различными неудобствами, вызванными непохожестью Go '
                                                               'на другие языки программирования.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/6091/eGiQd7.png',
                                                   reply_markup=ot_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣4️⃣'),
                                                   title='Framework Laravel',
                                                   description='Веб-фреймворк, который сделает вашу работу '
                                                               'интереснее, проще и быстрее',
                                                   thumb_url='https://imagizer.imageshack.com/img922/635/Psn8zD.png',
                                                   reply_markup=ot_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣5️⃣'),
                                                   title='Разработчик BigData',
                                                   description='Цель прохождения курса — освоение алгоритмов машинного обучения и логических методов, позволяющих находить ценную информацию в крупных массивах данных и эффективно внедрять эту информацию для решения реальных бизнес-задач.',
                                                   thumb_url='https://imagizer.imageshack.com/img924/9905/WdlnRg.jpg',
                                                   reply_markup=ot_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣6️⃣'),
                                                   title='Подготовительный курс по JavaScript разработке',
                                                   description='Подготовка к курсам "Fullstack разработчик '
                                                               'Javascript", "React.js-разработчик" и '
                                                               '"Node.js-разработчик"',
                                                   thumb_url='https://imagizer.imageshack.com/img923/1618/5C7tcM.png',
                                                   reply_markup=ot_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣7️⃣'),
                                                   title='Разработчик Python',
                                                   description="Best Practice по решению прикладных задач и освоению "
                                                               "инструментов, применяемых программистом при "
                                                               "разработке инфраструктурных решений, веб-приложений, "
                                                               "систем контроля качества и аналитических систем",
                                                   thumb_url='https://imagizer.imageshack.com/img923/5372/T4pET7.jpg',
                                                   reply_markup=ot_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣8️⃣'),
                                                   title='Data Engineer',
                                                   description='Ученый может открыть новую звезду, но не может ее '
                                                               'создать. Ему придется просить инженера сделать это за'
                                                               ' него.–Гордон Линдсей Глегг',
                                                   thumb_url='https://imagizer.imageshack.com/img924/1946/u1kjso.png',
                                                   reply_markup=ot_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'OTUS👨‍🎓0️⃣9️⃣'),
                                                   title='Backend разработчик на PHP',
                                                   description='Современные инструменты и лучшие практики для '
                                                               'глубокого понимания процесса разработки на PHP',
                                                   thumb_url='https://imagizer.imageshack.com/img924/8519/rNEsyy.png',
                                                   reply_markup=ot_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣0️⃣'),
                                                    title='С++ для начинающих программистов',
                                                    description='Курс по разработке на C++ для начинающих программистов',
                                                    thumb_url='https://imagizer.imageshack.com/img924/5227/UQUaCm.jpg',
                                                    reply_markup=ot_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣1️⃣'),
                                                    title='Архитектура и шаблоны проектирования ',
                                                    description='изучить основные паттерны проектирования и научиться '
                                                                'применять их, находить им замену в сложных ситуация '
                                                                'и научиться мыслить, как архитектор программного '
                                                                'обеспечения',
                                                    thumb_url='https://imagizer.imageshack.com/img924/6048/vhXoet.png',
                                                    reply_markup=ot_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣2️⃣'),
                                                    title='Пентест. Практика тестирования на проникновение',
                                                    description='Пентестер выявляет уязвимости информационной системы '
                                                                'и дает заказчику рекомендации по их устранению',
                                                    thumb_url='https://imagizer.imageshack.com/img922/2896/9w3dE2.png',
                                                    reply_markup=ot_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣3️⃣'),
                                                    title='MS SQL Server разработчик',
                                                    description='Во время курса будем подробно разбирать язык '
                                                                'запросов и внутренние процессы СУБД, происходящие на '
                                                                'всех этапах работы с запросом.',
                                                    thumb_url='https://imagizer.imageshack.com/img922/9613/K0j4q3.jpg',
                                                    reply_markup=ot_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣4️⃣'),
                                                    title='Реляционные СУБД',
                                                    description='Курс включает в себя все основные и популярные БД, '
                                                                'которые могут пригодиться разработчику: PostgreSQL, '
                                                                'MySQL, Redis, MongoDB, Cassandra и т.д.',
                                                    thumb_url='https://imagizer.imageshack.com/img922/7028/PuKrke.png',
                                                    reply_markup=ot_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'OTUS👨‍🎓1️⃣5️⃣'),
                                                    title='Fullstack разработчик JavaScript',
                                                    description='Практический курс для web-разработчиков по продвинутым возможностям JS и его фреймворков',
                                                    thumb_url='https://imagizer.imageshack.com/img923/2756/m1jdik.png',
                                                    reply_markup=ot_school())

        results = [article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9,
                   article_10, article_11, article_12, article_13, article_14, article_15]
        bot.answer_inline_query(query.id, results)
    elif query.query == 'WebForMySelf':
        article_1 = types.InlineQueryResultArticle(id=1,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣1️⃣'),
                                                   title='Веб-дизайнер профессионал',
                                                   description='Создавайте востребованные макеты быстро,легко и... '
                                                               'дорого',
                                                   thumb_url='https://imagizer.imageshack.com/img922/3433/nlxsIn.jpg',
                                                   reply_markup=wb_school())
        article_2 = types.InlineQueryResultArticle(id=2,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣2️⃣'),
                                                   title='Фриланс - Мастер',
                                                   description='Мощный видеокурс от Webformyself о том, '
                                                               'как добиваться успеха, работая удаленно',
                                                   thumb_url='https://imagizer.imageshack.com/img922/658/oOjZm0.png',
                                                   reply_markup=wb_school())
        article_3 = types.InlineQueryResultArticle(id=3,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣3️⃣'),
                                                   title='Верстка-Мастер',
                                                   description='ОТ ТЕОРИИ ДО ВЕРСТКИ ПОПУЛЯРНЫХ ШАБЛОНОВ',
                                                   thumb_url='https://imagizer.imageshack.com/img923/2302/ehsKgx.jpg',
                                                   reply_markup=wb_school())
        article_4 = types.InlineQueryResultArticle(id=4,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣4️⃣'),
                                                   title='JavaScript. Полное руководство для современной веб-разработки',
                                                   description='Изучите самый популярный язык разработки и станьте '
                                                               'высокооплачиваемым профи',
                                                   thumb_url='https://imagizer.imageshack.com/img923/5725/YEk2bu.png',
                                                   reply_markup=wb_school())
        article_5 = types.InlineQueryResultArticle(id=5,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣4️⃣'),
                                                   title='PHP-Мастер. От теории до собственной CMS интернет-магазина',
                                                   description='Абсолютное большинство всех сайтов в интернете '
                                                               'написаны на PHP.',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8404/5etgXb.jpg',
                                                   reply_markup=wb_school())
        article_6 = types.InlineQueryResultArticle(id=6,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣6️⃣'),
                                                   title='1-С Битрикс. Практика создания веб-проектов',
                                                   description="Новый фундаментальный курс поможет вам в считанные "
                                                               "недели овладеть профессиональной разработкой на CMS "
                                                               "1C-Битрикс с нуля.",
                                                   thumb_url='https://imagizer.imageshack.com/img924/4378/TRcSpV.jpg',
                                                   reply_markup=wb_school())
        article_7 = types.InlineQueryResultArticle(id=7,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣7️⃣'),
                                                   title='FullStack-Мастер: Разработка CRM-системы на Node.js, '
                                                         'Express, Angular 6',
                                                   description='Впервые в одном видеокурсе раскрыт полный пошаговый '
                                                               'алгоритм FullStack JavaScript-разработки!',
                                                   thumb_url='https://imagizer.imageshack.com/img924/5864/QVWdgz.png',
                                                   reply_markup=wb_school())
        article_8 = types.InlineQueryResultArticle(id=8,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣8️⃣'),
                                                   title='ReactJS с Нуля до Профи',
                                                   description='Овладейте Frontend-разработкой на стеке React.js',
                                                   thumb_url='https://imagizer.imageshack.com/img922/8393/RUvgWb.jpg',
                                                   reply_markup=wb_school())
        article_9 = types.InlineQueryResultArticle(id=9,
                                                   input_message_content=types.InputTextMessageContent(
                                                       'WebForMySelf💻 0️⃣9️⃣'),
                                                   title='Курс по CSS3 ',
                                                   description='Простота использования, ускорение процесса разработки '
                                                               'и оформления web страниц, уменьшение количества кода, '
                                                               'практически 100% кроссбраузерность',
                                                   thumb_url='https://imagizer.imageshack.com/img924/2403/uuq2Tn.jpg',
                                                   reply_markup=wb_school())
        article_10 = types.InlineQueryResultArticle(id=10,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣0️⃣'),
                                                    title='Курс по базе данных MySQL',
                                                    description='Посвящен изучению языка запросов SQL и работе с '
                                                                'сервером MySQL.',
                                                    thumb_url='https://imagizer.imageshack.com/img923/1227/cGGBNH.png',
                                                    reply_markup=wb_school())
        article_11 = types.InlineQueryResultArticle(id=11,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣1️⃣'),
                                                    title='Cоздание каталога товаров с помощью PHP, MySQL и jQuery',
                                                    description='Написанный в курсе движок, можно будет использовать '
                                                                'как для каталога, так и для любого другого сайта: '
                                                                'визитка, интернет-магазин, корпоративный сайт, блог.',
                                                    thumb_url='https://imagizer.imageshack.com/img923/3650/B59cvX.jpg',
                                                    reply_markup=wb_school())
        article_12 = types.InlineQueryResultArticle(id=12,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣2️⃣'),
                                                    title='Библиотека JQuery UI',
                                                    description='Научимся создавать элементы пользовательского '
                                                                'интерфейса, используя библиотеку jQuery UI',
                                                    thumb_url='https://imagizer.imageshack.com/img922/6707/QGdV0V.png',
                                                    reply_markup=wb_school())
        article_13 = types.InlineQueryResultArticle(id=13,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣3️⃣'),
                                                    title='WordPress-Мастер. Разработка тем для WordPress с нуля',
                                                    description='Вам станет подвластна CMS №1 в мире по популярности',
                                                    thumb_url='https://imagizer.imageshack.com/img924/273/rEutMJ.jpg',
                                                    reply_markup=wb_school())
        article_14 = types.InlineQueryResultArticle(id=14,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣4️⃣'),
                                                    title='Создание интернет-магазина на CMS WordPress',
                                                    description='Если Вы задались целью создать несложный '
                                                                'интернет-магазин, тогда обратите внимание на данный '
                                                                'курс',
                                                    thumb_url='https://imagizer.imageshack.com/img924/273/rEutMJ.jpg',
                                                    reply_markup=wb_school())
        article_15 = types.InlineQueryResultArticle(id=15,
                                                    input_message_content=types.InputTextMessageContent(
                                                        'WebForMySelf💻 1️⃣5️⃣'),
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
        print('try callback')
        with open('stats.txt', mode='r', encoding="utf-8") as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            content[query_with_fetchone('position_of_pointer', call.from_user.id)] = content[query_with_fetchone(
                'position_of_pointer', call.from_user.id)][:-25] + call.data + ' ' + content[
                                                                                         query_with_fetchone(
                                                                                             'position_of_pointer',
                                                                                             call.from_user.id)][
                                                                                     -25:]
            file.writelines(content)
    except Exception as e:
        print(e)
        file.writelines(content)
        pass
    if 'suc' in call.data:
        try:
            if 'webformyself' in call.data.split()[0].casefold():
                school = webformyself_clouds
            elif 'otus' in call.data.split()[0].casefold():
                school = otus_clouds
            elif 'skillbox' in call.data.split()[0].casefold():
                school = skillbox_clouds
            elif 'udemy' in call.data.split()[0].casefold():
                school = udemy_clouds
            elif 'netology' in call.data.split()[0].casefold():
                school = netology_clouds
            elif 'geekbrains' in call.data.split()[0].casefold():
                school = geekbrains_clouds
            i = 0
            if '0️⃣1️⃣' in call.data.split()[0]:
                i = 0
            elif '0️⃣2️⃣' in call.data.split()[0]:
                i = 1
            elif '0️⃣3️⃣' in call.data.split()[0]:
                i = 2
            elif '0️⃣4️⃣' in call.data.split()[0]:
                i = 3
            elif '0️⃣5️⃣' in call.data.split()[0]:
                i = 4
            elif '0️⃣6️⃣' in call.data.split()[0]:
                i = 5
            elif '0️⃣7️⃣' in call.data.split()[0]:
                i = 6
            elif '0️⃣8️⃣' in call.data.split()[0]:
                i = 7
            elif '0️⃣9️⃣' in call.data.split()[0]:
                i = 8
            elif '1️⃣0️⃣' in call.data.split()[0]:
                i = 9
            elif '1️⃣1️⃣' in call.data.split()[0]:
                i = 10
            elif '1️⃣2️⃣' in call.data.split()[0]:
                i = 11
            elif '1️⃣3️⃣' in call.data.split()[0]:
                i = 12
            elif '1️⃣4️⃣' in call.data.split()[0]:
                i = 13
            elif '1️⃣5️⃣' in call.data.split()[0]:
                i = 14
            elif '16' in call.data.split()[0]:
                i = 15
            if 'all' not in call.data.split()[0]:
                url = school[i]
                if url[1]:
                    url = url[0] + 'Пароль:\n' + url[1] + '\n' + url[2]
                else:
                    url = url[0] + '\n' + url[2]
            else:
                url = 'https://docs.google.com/document/d/1YICN4AqVNM68Mb3m6ArJO4TunhN2guyRXzcdQKi5VQc/edit?usp=sharing'
            chat_id = ''.join([i for i in call.data[-13:] if i.isdigit()])
            bot.send_message(909435473,
                             text='Заказ под номером  ' + chat_id + ' подтвержден от @' + query_with_fetchone('user',
                                                                                                              chat_id))
            bot.send_message(chat_id,
                             text='Спасибо за покупку!\nВот ваш заказ:\n{}'.format(url))
        except Error as e:
            print(e)
            pass
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
                                      text='Вы выбрали оплату банковской картой:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=044ce148-f081-4494-83ff-bcecdc52df0a',
                                                                   call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=044ce148-f081-4494-83ff-bcecdc52df0a',
                                                                   call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold\nПереведите 4 990₸ / 888₽ на карту: \n              5169 4971 7975 8408\n',
                                      reply_markup=credit_keyboard('https://kaspi.kz/Transfers/Landing/g2g', call.from_user.id))
        elif 'all' in call.data:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=d09b3089-d352-4762-b56d-784b0a7898c4', call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=d09b3089-d352-4762-b56d-784b0a7898c4', call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold\nПереведите 9 990₸ / 1 699₽ на карту: \n            5169 4971 7975 8408',
                                      reply_markup=credit_keyboard('https://kaspi.kz/Transfers/Landing/g2g', call.from_user.id))
        elif call.data[3:7] in ['Geek', 'Neto', 'OTUS', 'WebF', 'Udem', 'Skil']:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=ce06c974-a2ec-4a97-af55-91f064d3e3f8', call.from_user.id))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\n',
                                      reply_markup=credit_keyboard('https://oplata.qiwi.com/form?invoiceUid=ce06c974-a2ec-4a97-af55-91f064d3e3f8', call.from_user.id))
            else:
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold\nПереведите 1 990₸ / 333₽ на карту: \n              5169 4971 7975 8408',
                                      reply_markup=credit_keyboard('https://kaspi.kz/Transfers/Landing/g2g', call.from_user.id))
    elif call.data == 'confirmed':
        try:
            bot.send_message(chat_id=909435473,
                             text=query_with_fetchone('payment_course', call.from_user.id) + ' @' + query_with_fetchone(
                                 'user', call.from_user.id) + '\n' + str(call.from_user.id),
                             reply_markup=sucful_payment(call.from_user.id))
            bot.delete_message(call.from_user.id, call.message.message_id)
            bot.send_message(call.from_user.id, text='Ваш заказ принят, ожидайте подтверждения')
            update_flag_for_confirmation_of_payment(0, call.from_user.id)
        except Error as e:
            print(e)
            pass
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
                update_payment_course(call.data[:21], call.from_user.id)
                bot.send_message(chat_id=call.from_user.id,
                                 text="Выберите способ оплаты:", reply_markup=payment_method(call.from_user.id))
            else:
                update_payment_course(call.data[:21], call.from_user.id)
                bot.send_message(chat_id=call.from_user.id, text="Выберите способ оплаты:",
                                 reply_markup=payment_method(call.from_user.id))
        else:
            if call.message:
                update_payment_course(call.data[:21], call.from_user.id)
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                      text="Выберите способ оплаты:", reply_markup=payment_method(call.from_user.id))
            else:
                update_payment_course(call.data[:21], call.from_user.id)
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
        print('try start 1')
        with open('stats.txt', mode='r', encoding="utf-8") as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            if content:
                try:
                    for i in range(len(content)):
                        t = time.strftime('%c', time.gmtime(time.time()))
                        if str(message.from_user.id) in content[i]:
                            update_position_of_pointer(i, message.from_user.id)
                            break
                    if (content[query_with_fetchone('position_of_pointer', message.from_user.id)][-21:-18] != t[
                                                                                                              -20:-17] and
                        content[query_with_fetchone('position_of_pointer', message.from_user.id)][-17:-15] == t[
                                                                                                              -16:-14]) or \
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
                except:
                    pass
                file.writelines(content)
            else:
                file.write(str(message.from_user.id) + ' ' + time.strftime('%c', time.gmtime(time.time())) + '\n')
    except Exception as e:
        print(e)
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            file.seek(0)
            content = [str(message.from_user.id) + ' ' + time.strftime('%c', time.gmtime(time.time())) + '\n']
    try:
        print('try start 2')
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            try:
                content[query_with_fetchone('position_of_pointer', message.from_user.id)] = content[query_with_fetchone(
                    'position_of_pointer', message.from_user.id)][:-25] + message.text + ' ' + content[
                                                                                                   query_with_fetchone(
                                                                                                       'position_of_pointer',
                                                                                                       message.from_user.id)][
                                                                                               -25:]
                file.writelines(content)
            except:
                file.writelines(content)
                pass
    except Exception as e:
        print(e)
        pass
    main_keyboard = types.ReplyKeyboardMarkup(True, False)
    main_keyboard.row('Все 90 курсов за 9 990₸ / 1 699₽')
    bot.send_photo(message.from_user.id,
                   caption='<em><strong>Привет {name}!</strong></em> 👋\n\nИ даа-да, я тот самый Алдар-Косе из сказок, что пылятся на ваших полках.\n\n <em>P.S Явно не тот, что из мультиков. Но сейчас не об этом...</em>\n'.format(
                       name=message.chat.first_name),
                   reply_markup=main_keyboard,
                   photo='AgACAgIAAxkBAAOUXx8Pv-iXlU6c1JGK29OpN0xcOToAAqKvMRv_w_lIh6sY3NELGiO37-mSLgADAQADAgADbQAD5lYEAAEaBA',
                   parse_mode='html')
    main_menu = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Онлайн-университы', switch_inline_query_current_chat='courses')
    but_2 = types.InlineKeyboardButton(text='Связаваться с модератором', callback_data='moderator')
    but_3 = types.InlineKeyboardButton(text='Для правообладателей', callback_data='copyright')
    but_4 = types.InlineKeyboardButton(text='Отзывы', callback_data='comments')
    but_5 = types.InlineKeyboardButton(text='Оставить отзыв', callback_data='new_com')
    main_menu.add(but_1)
    main_menu.add(but_2)
    main_menu.add(but_3)
    main_menu.add(but_4, but_5)
    bot.send_message(message.from_user.id,
                     'Настали тяжелые времена и нужно приносить пользу своему народу, не долго думая я решил начать раздавать курсы по <u>высокооплачиваемым онлайн-профессиям</u>.\n\n<strong>Вашему вниманию представлены 90 топовых курсов от 6 лучших онлайн-университетов СНГ за смешные деньги.</strong>\n',
                     reply_markup=main_menu,
                     parse_mode='html')
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
        print('try messages')
        with open('stats.txt', mode='r', encoding="utf-8") as file:
            file.seek(0)
            content = file.readlines()
        with open('stats.txt', mode='w', encoding="utf-8") as file:
            try:
                content[query_with_fetchone('position_of_pointer', message.from_user.id)] = content[query_with_fetchone(
                    'position_of_pointer', message.from_user.id)][:-25] + message.text + ' ' + content[
                                                                                                   query_with_fetchone(
                                                                                                       'position_of_pointer',
                                                                                                       message.from_user.id)][
                                                                                               -25:]
            except:
                pass
            file.writelines(content)
    except Exception as e:
        print(e)
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
    school = ''.join([i for i in message.text if i.isalpha()])
    url = 'https://www.geeksforgeeks.org/python-ways-to-remove-numeric-digits-from-given-string/'
    try:
        i = 0
        while query_with_fetchone('previous_message_id', message.from_user.id) + i < message.message_id:
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
    elif message.text == 'GeekBrains🧠0️⃣1️⃣':
        text = '<strong>[GeekBrains] Профессия Разработчик игр</strong>\n \n<strong>Описание:</strong>\nЭта профессия позволяет исполнить мечту увлеченного геймера: сделать игру, в которой не будет недостатков. Разработчик игр создает концепцию и прототип игры, выбирает средства для реализации проекта.\n \n<strong>Вы научитесь:</strong>\n🎮Git\n🎮Основы C#\n🎮Unity и C#\n🎮Архитектура и шаблоны проектирования\n \n🤢Цена курса: ̶7̶2̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶2̶1̶ ̶9̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/game_developer'
        photo = geekbrains_courses[0]
    elif message.text == 'GeekBrains🧠0️⃣2️⃣':
        text = '<strong>[GeekBrains] Профессия Программист Android</strong>\n \n<strong>Описание:</strong>\nРазработка под Android — это создание игр и полезных приложений под 80% мобильных устройств. Android — открытая и свободная система, настроенная к модернизации и адаптации, она позволяет реализовать самые смелые фантазии программиста.\n \n<strong>Вы научитесь:</strong>\n🤖Git. Базовый курс\n🤖Java Core. \n🤖Android. \n🤖Android. Популярные библиотеки.\n🤖Базы данных.\n \n🤢Цена курса:  ̶8̶4̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶9̶2̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/android_developer'
        photo = geekbrains_courses[1]
    elif message.text == 'GeekBrains🧠0️⃣7️⃣':
        text = '<strong>[GeekBrains] Создание сайтов и приложений. Методы повышения конверсии</strong>\n \n<strong>Описание:</strong>\nЭтот курс даст вам доступ к мощным маркетинговым инструментам. Вы узнаете, что действительно важно, а что необязательно, а порой даже вредно. \nАкцент сделан на начинающих специалистов, поэтому информация представлена максимально просто.\n \n<strong>Вы научитесь:</strong>\n🌊Создавать действительно продающие структуры сайтов;\n🌊Повышать эффективность сайта в несколько раз;\n🌊Обыгрывать конкурентов в интернет маркетинге благодаря анализу;\n🌊Подготавливать проект для создания мобильной версии продукта;\n🌊Проводить качественный аудит сайта;\n \n🤢Цена курса:  ̶1̶1̶ ̶3̶7̶0̶₽ ̶/̶ ̶6̶6̶ ̶6̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/100'
        photo = geekbrains_courses[6]
    elif message.text == 'GeekBrains🧠0️⃣3️⃣':
        text = '<strong>[GeekBrains] Профессия Frontend-разработчик</strong>\n \n<strong>Описание:</strong>\nFrontend-разработчик создаёт интерфейсы, с которыми будут взаимодействовать пользователи, верстает сайты по современным стандартам, виртуозно владеет JavaScript, HTML, CSS.\n \n<strong>Вы научитесь:</strong>\n🧨Основы HTML/CSS и PHP.\n🧨HTML/CSS.\n🧨JavaScript.\n🧨Основы баз данных.\n🧨ReactJS.\n \n🤢Цена курса: ̶1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶₽ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://geekbrains.ru/professions/frontend_developer'
        photo = geekbrains_courses[2]
    elif message.text == 'GeekBrains🧠0️⃣5️⃣':
        text = '<strong>[GeekBrains] Профессия Веб-разработчик</strong>\n \n<strong>Описание:</strong>\nВеб-разработчики создают и обслуживают сайты, порталы. Они верстают пользовательские интерфейсы веб-ресурсов, проектируют серверную часть, которая обеспечивает работу всех функций и хранение данных.\n \n<strong>Вы научитесь:</strong>\n✨HTML/CSS.\n✨Основы работы с Git\n✨HTML5 и CSS3.\n✨JavaScript.\n✨Проектирование БД и запросы SQL\n✨PHP. \n✨Laravel. Глубокое погружение\n \n🤢Цена курса:  ̶9̶6̶ ̶0̶0̶0̶₽ ̶/̶ ̶5̶6̶2̶ ̶5̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸  \n'
        url = 'http://geekbrains.ru/professions/web_developer'
        photo = geekbrains_courses[4]
    elif message.text == 'GeekBrains🧠0️⃣8️⃣':
        text = '<strong>[GeekBrains] Факультет Python-разработки</strong>\n \n<strong>Описание:</strong>\nСтаньте программистом Python и изучите один из самых востребованных навыков современной разработки!\n \n<strong>Вы научитесь:</strong>\n🔥Backend-разработка\n🔥Frontend и Backend интернет-магазина\n🔥Сетевой чат\n🔥Архитектура и шаблоны проектирования на Python\n🔥Компьютерные сети\n🔥Продвинутый курс Javascript\n \n🤢Цена курса: 1̶8̶0̶ ̶0̶0̶0̶₽ ̶/̶ ̶1̶ ̶0̶5̶4̶ ̶8̶0̶0̶₸\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/geek_university/python'
        photo = geekbrains_courses[7]
    elif message.text == 'GeekBrains🧠0️⃣9️⃣':
        text = '<strong>[GeekBrains] Системный администратор </strong>\n \n<strong>Описание:</strong>\nСистемный администратор обеспечивает бесперебойное функционирование компьютерной техники и программного обеспечения в организации. Он занимается поддержкой серверов, проектирует и администрирует локальную сеть, выдаёт пользователям доступ к сайтам.\n \n<strong>Вы научитесь:</strong>\n🛡Проектирование БД и запросы SQL\n🛡Классика computer science\n🛡Практика администрирования ОС Linux на компьютере\n🛡Операционные системы\n🛡Безопасность компьютерных сетей\n🛡Основные сервисы на Linux для предприятия\n \n🤢Цена курса:  ̶7̶0̶ ̶0̶0̶0̶₽ ̶/̶ ̶4̶1̶0̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/sys_admin'
        photo = geekbrains_courses[8]
    elif message.text == 'GeekBrains🧠1️⃣0️⃣':
        text = '<strong>[GeekBrains] Дизайнер интерфейсов </strong>\n \n<strong>Описание:</strong>\nДизайнер UX/UI проектирует взаимодействие пользователя с сайтом, приложением или сервисом и создает визуальные элементы, систему и прототип интуитивно понятного интерфейса.\n \n<strong>Вы научитесь:</strong>\n✨Основы Adobe Illustrator\n✨Figma\n✨Базовые знания. Дизайн\n✨Адаптивный дизайн\n✨Adobe After Effects\n \n🤢Цена курса:   ̶8̶5̶ ̶5̶0̶0̶ ̶₽̶ ̶/̶ ̶4̶9̶3̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://geekbrains.ru/geek_university/interface-design'
        photo = geekbrains_courses[9]
    elif message.text == 'GeekBrains🧠1️⃣1️⃣':
        text = '<strong>[GeekBrains] 1С-Битрикс: Управление сайтом</strong>\n \n<strong>Описание:</strong>\nКурс предназначен для тех разработчиков, кто собирается работать с CMS 1C-Битрикс и хочет узнать подробнее о ее функционале и настройках.\n \n<strong>Вы научитесь:</strong>\n💣Выбирать правильные редакции и решения для своего веб-проекта на CMS Битрикс;\n💣Устанавливать и запускать сайт на CMS Битрикс.\n💣Проектировать бизнес-логику своих веб-приложений, создавать структуру и навигацию.\n💣Интегрировать HTML-верстку в проект.\n💣Работать с компонентами CMS Битрикс и расширять их базовые возможности.\n💣Настраивать информационные блоки и выводить динамическую информацию на сайте.\n \n🤢Цена курса: ̶9̶ ̶9̶0̶0̶₽ ̶/̶ ̶5̶8̶ ̶0̶0̶0̶₸̶\n🤑Наша цена:  333₽ / 1990₸\n'
        url = 'http://geekbrains.ru/courses/26'
        photo = geekbrains_courses[10]
    elif message.text == 'GeekBrains🧠0️⃣6️⃣':
        text = '<strong>[GeekBrains] </strong><strong>Yii2 </strong><strong>Профессиональная Backend-разработка</strong>\n \n<strong>Описание:</strong>\nYii2 framework - oдин из самых популярных и востребованных фреймворков на PHP. Знание любого фреймворка качественно увеличивает востребованность php-программиста на рынке труда, и его оклад.\n \n<strong>Вы научитесь:</strong>\n🌊Настраивать веб-сервер и разворачивать приложение;\n🌊Проектировать БД и работать с моделями и формами Yii;\n🌊Работать с генератором кода;\n🌊Управлять кэшированием;\n🌊Использовать расширения и особенности фреймворка;\n \n🤢Цена курса: 1̶5̶ ̶0̶0̶0̶₽ ̶/̶ ̶8̶7̶ ̶9̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/35'
        photo = geekbrains_courses[5]
    elif message.text == 'GeekBrains🧠1️⃣2️⃣':
        text = '<strong>[GeekBrains] Школа Программирования. Java 0, 1, 2.</strong>\n \n<strong>Описание:</strong>\nНа Java пишут игры, мобильные и десктопные приложения, enterprise-проекты, серверные проекты в сфере финансовых услуг, инструменты для обработки Big Data.\nИз-за широкой сферы применения и кроссплатформенности языка программирования Java-разработчики крайне востребованы в IT-компаниях.\n \n<strong>Вы научитесь:</strong>\n🔥Java SE 8 и выше\n🔥Основы работы с Git\n🔥Проектирование БД и запросы SQL\n🔥Алгоритмы Java. \n🔥HTML/CSS.\n🔥Создание веб-приложений на Java\n \n🤢Цена курса:   ̶6̶6̶ ̶0̶0̶0̶₽ ̶/̶ ̶3̶8̶6̶ ̶7̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/professions/java_developer'
        photo = geekbrains_courses[11]
    elif message.text == 'GeekBrains🧠1️⃣3️⃣':
        text = '<strong>[GeekBrains] Базы данных для профессионалов и язык SQL</strong>\n \n<strong>Описание:</strong>\nНи одно современное веб-приложение, и не только веб, не обходится без долговременного хранилища данных. И для многих приложений таким решением становится MySQL. Зарекомендовавшая себя на многих популярных и больших проектах, эта СУБД развивается и является одним из основных решений для организации баз данных.\n \n<strong>Вы научитесь:</strong>\n💾Проектировать БД для наиболее эффективного их построения\n💾Создавать БД по созданным проектам\n💾Строить простые и сложные запросы на выборки данных\n💾Анализировать производительность запросов и оптимизировать их\n💾Писать транзакции\n💾Администрировать БД\n \n🤢Цена курса:   ̶1̶5̶ ̶0̶0̶0̶₽ ̶/̶ ̶8̶7̶ ̶9̶0̶0̶₸\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/1181'
        photo = geekbrains_courses[12]
    elif message.text == 'GeekBrains🧠1️⃣4️⃣':
        text = '<strong>[GeekBrains] Анатомия блокчейна</strong>\n \n<strong>Описание:</strong>\nРазбираться в криптовалютах. Вы поймете, в чем их смысл, сможете читать официальную документацию проекта (whitepaper), оценивать идеи, понимать описания криптопротоколов.\nПонимать, как построены сервисы, обеспечивающие безопасность коммуникаций между участниками. Вы сможете оценить техническое выполнение проекта и оригинальность замысла.\n \n<strong>Вы научитесь:</strong>\n💸Введение в криптографию\n💸Блокчейн\n💸Практическая работа с криптовалютой, кошельками и биржами.\n💸Использование блокчейн для проведения ICO.\n \n🤢Цена курса:   ̶2̶0̶ ̶0̶0̶0̶₽̶ ̶/̶ ̶1̶1̶7̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://geekbrains.ru/blockchain'
        photo = geekbrains_courses[13]
    elif message.text == 'GeekBrains🧠0️⃣4️⃣':
        text = '<strong>[GeekBrains] Курс по Agile-методологиям</strong>\n \n<strong>Описание:</strong>\nКогда дедлайны горят, заказчик дает новые вводные, а в продуктах встречаются ошибки, используйте Agile-метод. С помощью гибкого подхода вы будете отслеживать развитие проекта на всех этапах, оценивать риски и расставлять приоритеты.\n \n<strong>Вы научитесь:</strong>\n🌟Примените полученные знания для практической работы Agile-команде\n🌟Научитесь оценивать задачи и свои возможности\n🌟Научитесь оптимизировать рабочие процессы и и нагрузку\n \n🤢Цена курса:   ̶9̶ ̶9̶0̶0̶₽̶ ̶/̶ ̶5̶8̶ ̶0̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://intensives.geekbrains.ru/agile'
        photo = geekbrains_courses[3]
    elif message.text == 'GeekBrains🧠1️⃣5️⃣':
        text = '<strong> [GeekBrains] Node.js Серверное программирование на JavaScript</strong>\n \n<strong>Описание:</strong>\nЭволюция JavaScript с каждым годом дает возможность для веб-разработчиков создавать большое количество новых технологий и инновационных приложений. Один из наиболее интересных и популярных инструментов для создания легко масштабируемых сетевых приложений является Node.js – это серверная реализация языка программирования JavaScript, основанная на движке V8.\n \n<strong>Вы научитесь:</strong>\n☁️Создавать консольные утилиты на Node.js;\n☁️Создавать веб-сервисы с помощью популярного фреймворка Express.js;\n☁️Применять шаблонизаторы для разделения кода и оформления интерфейса в проекте;\n☁️Создавать и использовать различные REST API;\n☁️Использовать в программе веб-сокеты с помощью socket.io\n \n🤢Цена курса:    ̶1̶5̶ ̶0̶0̶0̶₽̶ ̶/̶ ̶8̶6̶ ̶7̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://geekbrains.ru/courses/11'
        photo = geekbrains_courses[14]
    elif message.text == 'Netology🏛0️⃣1️⃣':
        text = '<b> [Нетология] PHP/SQL: back-end разработка и базы данных\n\nОписание:</b> \nПод PHP работает 80% сайтов, в том числе Facebook, «ВКонтакте» и «Википедия». В преподавательском составе "Нетологии" состоят только опытные и бывалые разработчики, которые проведут вас в мир программирования и сделают востребованным специалистом!\n<b>Вы научитесь:</b>\n🔥работать со строками, массивами и объектами;\n🔥устанавливать и настраивать веб-сервера;\n🔥создавать классы и объекты в ООП;\n🔥управлять таблицами и базами данных в MySQL.\n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ₽̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 333 ₽ / 1990 ₸'
        url = 'https://it-events.com/events/6470'
        photo = netology_courses[0]
    elif message.text == 'Netology🏛0️⃣2️⃣':
        text = '<b>[Нетология]Веб-дизайн: Эффективный сайт от идеи до реализации\n\nОписание:</b>\n Пользователи курса «Веб дизайн. Обучение с нуля» узнают о таких понятиях и инструментах интернет-разработки, как:\n🌟разработка дизайн-макета;\n🌟тестирование и взаимодействие с пользователями;\n🌟векторные и растровые изображения;\n🌟основы работы с цветом;\n🌟веб-типографика;\n🌟подготовка портфолио;\n🌟презентация проекта клиенту.\n\n🤢Цена курса:  ̶3̶4̶ ̶0̶0̶0̶ ₽ ̶/̶̶̶ ̶2̶0̶2̶ ̶0̶0̶0̶ ₸̶̶̶\n🤑Наша цена: 333 ₽ / 1990 ₸'
        url = 'https://netology.ru/programs/web-design'
        photo = netology_courses[1]
    elif message.text == 'Netology🏛0️⃣3️⃣':
        text = '<b>[Нетология] Python для работы с данными\n\nОписание:</b>\nPython — простой и универсальный инструмент для решения любых аналитических задач.\n👨‍💻Автоматизируйте свою рутинную работу с помощью Python\n🦾Обрабатывайте большие объемы информации без администрирования и баз данных\n🤖Освойте ключевой инструмент в мире аналитики и машинного обучения\n<b>Ключевые навыки</b>\n⚡️Работа с сырыми данными и их подготовка для анализа\n⚡️Работа с аналитическими библиотеками numpy, scipy и pandas\n⚡️Визуализация данных с помощью библиотек seaborn, plotly, matplotlib\n⚡️Статистический анализ данных\n⚡️Применение математических моделей\n⚡️Выбор и создание фич\n\n🤢Цена курса:  ̶4̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶7̶0̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333 ₽ / 1990 ₸ '
        photo = netology_courses[2]
    elif message.text == 'Netology🏛0️⃣4️⃣':
        text = '<b>[Нетология] Профессия Аналитик данных\n\nОписание:</b>\nНаучим с нуля собирать, анализировать и презентовать данные.Получите востребованную профессию с зарплатой от 400 000 ₸. (по данным hh.kz)\n<b>Ключевые навыки:</b>\n🌟Сбор и подготовка данных для анализа\n🌟Визуализация данных\n🌟Сбор и понимание бизнес-требований заказчика\n🌟Подготовка ad-hoc исследований и аналитики\n🌟Тестирование гипотез\n🌟Умение писать сложные запросы на SQL\n🌟Python для анализа данных\n🌟Знание основ работы с Hadoop\n\n🤢Цена курса:  ̶1̶0̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶5̶8̶5̶ ̶5̶0̶0̶ ̶₸\n🤑Наша цена: 333 ₽ / 1990 ₸ '
        photo = netology_courses[3]
    elif message.text == 'Netology🏛0️⃣5️⃣':
        text = ' <strong>[Нетология] SQL и получение данных</strong>\n\n<strong>Описание: </strong>\n<strong>Программа обучения SQL</strong> — первый шаг в профессиональном росте дата саентистов и аналитиков данных в сильных командах и проектах. Без владения SQL невозможно будет вырасти выше уровня junior.\n \n<strong>Возможности после обучения:</strong>\n🌊Овладеете языком запросов SQL\nПознакомитесь с разнообразным окружением БД: git, виртуальные машины, linux\n🌊Углубите знания SQL\nПерейдёте от исполнения запросов к написанию функций\n🌊Найдёте общий язык с разработчиками\nУлучшите понимание процессов инжиниринга данных\n \n🤢Цена курса:  ̶2̶3̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶1̶4̶3̶ ̶4̶0̶0̶ ̶₸̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/sql-lessons#/'
        photo = netology_courses[4]
    elif message.text == 'Netology🏛0️⃣6️⃣':
        text = '<strong>[Нетология] Power BI: анализ и визуализация данных без программирования</strong>\n \n<strong>Описание:</strong>\nBI-платформы — инструмент бизнес-анализа, позволяющий анализировать «живые» данные и создавать визуальные отчёты без привлечения ИТ-специалистов\n \n<strong>Ключевые навыки:</strong>\n🔥Подготовка исходных данных для анализа\n🔥Построение моделей данных из разных неструктурированных источников: таблиц, сайтов и баз данных\n🔥Преобразование сложных данных в простые для восприятия и ценные для бизнеса сведения\n🔥Подготовка интерактивных отчётов и дашбордов для совместной работы\n🔥Написание кастомных формул на языке запросов DAX\n🔥Визуализация результатов анализа\n🔥Анализ динамики изменений на дашбордах\n \n🤢Цена курса:  ̶2̶8̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶1̶6̶8̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/power-bi#/'
        photo = netology_courses[5]
    elif message.text == 'Netology🏛0️⃣7️⃣':
        text = '<strong>[Нетология] BIG DATA с нуля</strong>\n\n<strong>Описание:</strong>\n Big data - инструменты, подходы и методы обработки огромных объёмов данных.;\n<strong>Вы получите:</strong>\n🔥Сбор и подготовка данных для анализа\n🔥Понимание бизнес-требований заказчика и организация эффективной команды\n🔥Преобразование неструктурированных данных в простые для восприятия и ценные для бизнеса сведения\n🔥Построение моделей данных из разных неструктурированных источников: таблиц, сайтов и баз данных\n🔥Определение и выбор оптимальной архитектуры для Big Data проекта\n🔥Определение результатов обработки и инсайтов в данных и улучшение качества принятия решений на их основе\n\n🤢Цена курса: ̶3̶2̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶1̶9̶7̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/programs/big-data#/presentation'
        photo = netology_courses[6]
    elif message.text == 'Netology🏛0️⃣8️⃣':
        text = ' <strong>[Нетология] Таргетированная реклама</strong>\n\n<strong>Описание:</strong>\nНаучим работать с рекламой в социальных сетях. Курс одобрен компаниями ВКонтакте и myTarget.\n<strong>Ключевые навыки:</strong>\n🌟Анализ и сегментация целевой аудитории\n🌟Разработка стратегии таргетированной рекламы\n🌟Настройка рекламных кампаний в кабинетах Facebook/Instagram, ВКонтакте, myTarget\n🌟Создание креативов и текстов для рекламных кампаний\n🌟Работа с системами аналитики: Google Analytics, Яндекс.Метрика\n🌟Работа с парсерами, пикселями ремаркетинга/ретаргетинга\n🌟Анализ и оптимизация рекламных кампаний\n🌟Планирование бюджета рекламных кампаний\n🌟Поиск клиентов и отчётность\n \n🤢Цена курса:  ̶4̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶9̶9̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/target-smm#/'
        photo = netology_courses[7]
    elif message.text == 'Netology🏛0️⃣9️⃣':
        text = ' <strong>[Нетология] Геймдизайн</strong>\n<strong>Описание:</strong>\n\nГеймдизайнер знает, как с нуля создать игровой продукт. Он умеет грамотно формулировать задачи для команды, понимает маркетинг игр и способен убедить инвестора в успешности проекта. Освойте новую профессию — и создавайте по-настоящему успешные, захватывающие игры.\n\n<strong>Чему вы научитесь на курсе:</strong>\n🎮Создавать сюжет и композицию игры, строить дизайн игрового пространства, карты уровней и карты маршрутов\n🎮Прототипировать игры и создавать шаблоны игровых интерфейсов для UI-дизайнеров\n🎮Собирать и анализировать игровую статистику, а также участвовать в разработке стратегии продвижения игры\n\n🤢Цена курса:  ̶4̶5̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶7̶5̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 333 ₽ / 1990 ₸ '
        url = 'https://netology.ru/programs/gamedesign#/'
        photo = netology_courses[8]
    elif message.text == 'Netology🏛1️⃣0️⃣':
        text = '<strong>[Нетология] Python: программирование на каждый день</strong>\n\n<strong>Описание:</strong>\nPython входит в топ-10 самых востребованных языков программирования (по данным Stack Overflow). Он открывает путь в топовые IT-компании: Google, Pixar, Youtube, Instagram, Nasa, Intel, Pinterest используют именно его.\n \n<strong>Программа курса:</strong>\n👨‍💻Вычислительные задачи на Python\n👨‍💻Работа с файловой системой\n👨‍💻Работа с внешним API\n👨‍💻Краткое введение в анализ данных\n👨‍💻Подводные камни разработки на Python\n \n🤢Цена курса:  ̶7̶9̶ ̶9̶9̶0̶ ̶₽ ̶/̶ ̶4̶7̶9̶ ̶9̶4̶0̶ ̶₸̶ ̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/python#/'
        photo = netology_courses[9]
    elif message.text == 'Netology🏛1️⃣1️⃣':
        text = '<strong>[Нетология] Веб-аналитика: что нужно знать интернет-специалисту</strong>\n\n<strong>Описание:</strong>\nНаучитесь управлять маркетингом при помощи данных и использовать их для роста бизнеса и увеличения прибыли\n \n<strong>Ключевые навыки</strong>\n🌊Настройка отслеживания в аккаунтах Google Analytics и Яндекс. Метрики\n🌊Использование Google Tag Manager для разметки сайта\n🌊Создание отчётов, сводок и оповещений в Google Analytics и Яндекс. Метрике\n🌊Анализ эффективности сайта, продаж на сайте и источников трафика\n🌊Проведение А/В тестов для повышения конверсии сайта\n🌊Использование Excel\n🌊Использование Google Data Studio для визуализации данных\n \n🤢Цена курса:  ̶3̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶9̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'http://netology.ru/programs/ws-web-analytics'
        photo = netology_courses[10]
    elif message.text == 'Netology🏛1️⃣2️⃣':
        text = '<strong>[Нетология] Анализ статистики сайта с помощью Яндекс.Метрики</strong>\n\n<strong>Описание:</strong>\nКурс по Яндекс Метрике создан для тех, кто хочет отслеживать поведение посетителей на сайте, оценивать отдачу от рекламных кампаний, а также наблюдать в реальном времени за изменением KPI вашего интернет-проекта.\n \n<strong>Содержание курса:</strong>\n💥Принципы работы Яндекс.Метрики\n💥Краткий обзор отчетов Яндекс.Метрики\n💥Создание аккаунта Яндекс.Метрики\n💥Дополнительные настройки счетчика\n💥Настройка целей Яндекс.Метрики\n💥Приемы работы с отчетами Яндекс Метрики\n \n🤢Цена курса:  ̶3̶9̶ ̶9̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶9̶ ̶4̶0̶0̶ ̶₸̶ ̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://metrika.yandex.ru/welcome?utm_medium=search&utm_source=google&utm_campaign=8146429199&utm_content=397582312057&utm_term=%2B%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%2B%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B0&gclid=Cj0KCQjw0rr4BRCtARIsAB0_48NI8Uk7BgxMRex52HNUvuCAF6cCE7HFz8BrRe3hTEqpVo9u28YH5E8aAmNWEALw_wcB'
        photo = netology_courses[11]
    elif message.text == 'Netology🏛1️⃣3️⃣':
        text = ' <strong>[Нетология] Математика для анализа данных</strong>\n \n<strong>Описание:</strong>\nЧтобы увидеть в больших объёмах данных закономерности, аналитик опирается на линейную алгебру, математический анализ и теорию вероятности. Если специалист не разбирается в этих направлениях — гипотезы и выводы будут неточными. Это как запустить ракету в космос, не зная траекторию полёта.\n \n<strong>Кому подойдёт курс:</strong>\n🤓Аналитикам данных\nПознакомитесь с основными математическими концепциями и заложите теоретический фундамент, чтобы лучше разбираться в статистике и правильно интерпретировать данные.\n🤓Специалистам по Data Science\nНачнёте глубже разбираться в алгоритмах машинного обучения. Поймёте, какие принципы лежат в основе разных алгоритмов, чтобы выбирать правильные инструменты.\n \n🤢Цена курса:  ̶1̶7̶ ̶̶̶0̶0̶0̶ ̶₽ ̶̶̶/̶̶̶ ̶̶̶9̶9̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶ ̶\n🤑Наша цена: 333 ₽ / 1990 ₸ \n'
        url = 'https://netology.ru/programs/mathematics-for-data-science'
        photo = netology_courses[12]
    elif message.text == 'Netology🏛1️⃣4️⃣':
        text = '<strong>[Нетология] Основы поисковой оптимизации (SEO)</strong>\n \n<strong>Описание:</strong> \nКурс по основам поисковой оптимизации (SEO) — источник и теоретических, и практических знаний. Вы освоите принципы работы поисковых систем, поймете, как использовать факторы ранжирования и работать с разными типами пользовательских запросов.\n \n<strong>Ключевые навыки:</strong>\n💫Знание основных факторов ранжирования в поисковых системах и умение эти знания применять на практике\n💫Умение на базовом уровне визуально разбираться в коде и находить ошибки, допущенные при html-верстке документов\n💫Формирование семантического ядра вручную и с помощью софта и распределение запросов по страницам\n💫Умение находить технические ошибки на сайте\n💫Проведение работ по контентной оптимизации\n \n🤢Цена курса:  ̶7̶9̶0̶ ̶₽ ̶̶̶/̶̶̶ ̶̶̶4̶5̶0̶0̶ ̶₸̶̶̶\n🤑Наша цена: 333 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/courses/osnovy-poiskovoy-optimizatsii-seo'
        photo = netology_courses[13]
    elif message.text == 'Netology🏛1️⃣5️⃣':
        text = '<strong>[Нетология] Исследуйте в R (2020)</strong>\n\n<strong>Описание:</strong>\nМы живём в эпоху цифровизации, когда каждый процесс можно автоматизировать и упростить свою работу. На языке R можно написать код, который освободит вам время для новых проектов.\n \n<strong>Возможности после обучения:</strong>\n🦾Собирать данные из большинства аналитических систем\n🦾Преобразовывать R-скрипты для переработки получаемых данных в зависимости от задач\n🦾Анализировать рутинные процессы с помощью скриптов и показывать результаты на графиках\n \n🤢Цена курса:  ̶2̶7̶ ̶0̶0̶0̶ ̶̶̶̶̶̶̶₽ ̶/̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶6̶2̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 333 ₽ / 1990 ₸\n'
        url = 'https://netology.ru/programs/r-analysis#/presentation'
        photo = netology_courses[14]
    elif message.text == 'SkillBox📚0️⃣1️⃣':
        text = ' <strong>[SkillBox] Дизайн мобильных приложений</strong>\n \n<strong>Описание:</strong>\nВы научитесь создавать интерфейсы для мобильных платформ и эффектно презентовать свои работы. Сможете начать карьеру дизайнера в IT-компании или зарабатывать на фрилансе.\n \n<strong>Вы научитесь:</strong>\n🔥Работать с дизайнерским софтом\n🔥Проектировать приложения\n🔥Тестировать гипотезы\n🔥Адаптировать дизайн\n🔥Анимировать интерфейсы\n🔥Презентовать проекты\n \n🤢Цена курса:  ̶8̶0̶ ̶0̶0̶0̶₽̶ ̶̶̶ ̶/̶̶̶̶̶̶̶ ̶̶̶4̶6̶3̶ ̶0̶0̶0̶₸̶ ̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/app-design-pro/'
        photo = skillbox_courses[0]
    elif message.text == 'SkillBox📚0️⃣2️⃣':
        text = '<strong>[SkillBox] Управление digital-проектами</strong>\n \n<strong>Описание:</strong>\nЗа четыре месяца вы освоите все этапы работы над проектом — от планирования до запуска — и сможете стать руководителем digital-проектов с зарплатой от 90 000 рублей.\n \n<strong>Вы научитесь:</strong>\n🌟Вести переговоры\n🌟Быстро запускать проекты\n🌟Управлять изменениями\n🌟Контролировать команду\n🌟Считать деньги\n🌟Понимать техническую часть проекта\n \n🤢Цена курса:  ̶6̶5̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶7̶6̶ ̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/sibirix/'
        photo = skillbox_courses[1]
    elif message.text == 'SkillBox📚0️⃣4️⃣':
        text = '<strong>[SkillBox] Cinema 4D для веб-дизайна</strong>\n \n<strong>Описание:</strong>\nВы с нуля освоите Cinema 4D, научитесь моделировать объекты и работать со светом, анимацией и физикой.\n \n<strong>Вы научитесь:</strong>\n💣Работать в Cinema 4D\n💣Моделировать 3D-объекты\n💣Рендерить объекты\n💣Создавать анимацию в один клик\n💣Использовать продвинутые возможности софта\n\n🤢Цена курса:  ̶2̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶1̶5̶ ̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/cinema4d/'
        photo = skillbox_courses[3]
    elif message.text == 'SkillBox📚0️⃣3️⃣':
        text = '<strong>[SkillBox] Три дизайн-курса в одном - UX-дизайн, UX-аналитика, UI-анимация</strong>\n \n<strong>Описание:</strong>\nВы узнаете, как проводить UX-исследования и проектировать удобные интерфейсы. Научитесь создавать сайты и приложения, которые точно понравятся пользователям.\n \n<strong>Вы научитесь:</strong>\n🔥Проектировать интерфейсы на основе поведения пользователей\n🔥Решать проблемы пользователей\n🔥Создавать дизайн-системы\n🔥Проводить пользовательские исследования\n🔥Проектировать интерфейсы мобильных приложений\n🔥Работать с текстом в интерфейсе\n🔥Создавать дизайн на основе данных\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶4̶7̶ ̶3̶5̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/aic/'
        photo = skillbox_courses[2]
    elif message.text == 'SkillBox📚0️⃣5️⃣':
        text = '<strong>[Skillbox] Таргетированная реклама Вконтакте</strong>\n\n<strong>Описание:</strong>\nКурс проводится совместно с «Церебро» и HiConversion и одобрен командой «ВКонтакте». В программе девять блоков: от введения в таргетинг до форматов отчетности. Студентов учат анализировать рынок и аудиторию, разрабатывать контент-стратегию, использовать все возможности «Церебро Таргет», разбираться в форматах рекламы, работать с отчетами и воронкой продаж.\n\n<strong>Учат всему:</strong>\n🌠от того, как писать статьи и оформлять группу;\n🌠до основ парсинга и рассылок;\n\n🤢Цена курса: ̶3̶0̶ ̶0̶0̶0̶₽̶ ̶ ̶/̶ ̶1̶7̶3̶ ̶2̶0̶0̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/targetvk/'
        photo = skillbox_courses[4]
    elif message.text == 'SkillBox📚0️⃣7️⃣':
        text = '<strong>[SkillBox] Сквозная аналитика </strong>\n \n<strong>Описание:</strong>\nВы научитесь настраивать аналитику для всех каналов продвижения, чтобы выжимать максимум из рекламы, принимать решения на основе точных данных и не терять деньги.\n \n<strong>Вы научитесь:</strong>\n🌟Отслеживать путь клиента в воронке продаж\n🌟Создавать системы сквозной аналитики\n🌟Оценивать эффективность рекламы\n🌟Собирать статистику по всем каналам сразу\n🌟Анализировать данные\n🌟Создавать наглядные отчёты\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n\n\n'
        url = 'https://skillbox.ru/end-to-end/'
        photo = skillbox_courses[6]
    elif message.text == 'SkillBox📚0️⃣8️⃣':
        text = ' <strong>[SkillBox]</strong><strong>Как открыть и развивать свою веб-студию </strong>\n \n<strong>Описание:</strong>\nНастоящий бриллиант среди курсов от SkillBox - что по содержанию, что по стоимости. Сладкая мечта всех дизайнеров - открыть собственную прибыльную веб-студию - и мы поможем ее осуществить!\n \n<strong>Вы научитесь:</strong>\n🔥Запускать бизнес с нуля\n🔥Развивать личный бренд\n🔥Выстраивать стратегию развития\n🔥Находить заказы для студии\n🔥Организовывать работу команды\n🔥Эффективно управлять веб-студией\n🔥Работать с необходимыми юридическими и финансовыми отчетностями\n🔥Выстраивать долгосрочные отношения с клиентами\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skill-box.ru/studio/'
        photo = skillbox_courses[7]
    elif message.text == 'SkillBox📚0️⃣6️⃣':
        text = '<strong> [SkillBox] UI анимация. Стань motion-дизайнером за 16 недель </strong>\n \n<strong>Описание:</strong>\nВы научитесь создавать анимации в After Effects и Atomic и превращать статичный дизайн в динамичные креативные интерфейсы.\n \n<strong>Вы научитесь:</strong>\n💣Работать в After Effects, Principle и Atomic\n💣Анимировать интерфейсы\n💣Анимировать статичные концепции\n💣Создавать видеобаннеры\n💣Презентовать проекты\n \n🤢Цена курса:  ̶5̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶̶̶8̶̶̶9̶̶̶ ̶̶̶5̶̶̶0̶̶̶0̶̶̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/motion/'
        photo = skillbox_courses[5]
    elif message.text == 'SkillBox📚0️⃣9️⃣':
        text = ' <strong>[SkillBox] Рекламная Графика </strong>\n \n<strong>Описание:</strong>\nКурс от создателей самых сочных рекламных иллюстраций на российском рынке\n \n<strong>Вы научитесь:</strong>\n🧨Профессиональная ретушь\n🧨Создание фотореалистичных иллюстраций\n🧨Работа в технике matte-painting\n🧨Организация фотосессий\n🧨Постобработка визуализаций в Photoshop\n🧨Создание скетчей\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶3̶4̶7̶ ̶3̶5̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/cpeople/'
        photo = skillbox_courses[8]
    elif message.text == 'SkillBox📚1️⃣0️⃣':
        text = '<strong>[SkillBox] Excel c 0 до PRO </strong>\n \n<strong>Описание:</strong>\nНаучитесь составлять сложные отчёты и строить прогнозы, сможете автоматизировать свою работу с помощью скриптов и макросов — тем самым освободите время для других задач.\n \n<strong>Вы научитесь:</strong>\n⚡️Быстро делать сложные расчёты\n⚡️Наглядно представлять данные\n⚡️Строить прогнозы\n⚡️Работать с внешними источниками данных\n⚡️Создавать макросы и скрипты\n⚡️Работать с инструментами фильтрации\n \n🤢Цена курса: ̶ ̶4̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶2̶3̶1̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/excel/'
        photo = skillbox_courses[9]
    elif message.text == 'SkillBox📚1️⃣1️⃣':
        text = '<strong>[SkillBox]</strong><strong>Adobe After Effects с 0 до PRO</strong>\n \n<strong>Описание:</strong>\nВы научитесь работать с анимацией, освоите возможности After Effects на профессиональном уровне и сделаете первые проекты для портфолио — сможете расширить навыки в дизайне или начать карьеру в киноиндустрии.\n \n<strong>Вы научитесь:</strong>\n✨Работать в Adobe After Effects\n✨Создавать анимации\n✨Создавать эффекты\n✨Разрабатывать 3D-сцены\n✨Редактировать и стабилизировать видео\n✨Настраивать параметры рендера\n \n🤢Цена курса:  ̶2̶5̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶1̶4̶4̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://course.skillbox.ru/after-effects'
        photo = skillbox_courses[10]
    elif message.text == 'SkillBox📚1️⃣2️⃣':
        text = '<strong> [Skillbox] Профессия С# разработчик </strong>\n \n<strong>Описание:</strong>\n130 часов обучения — и вы научитесь писать программы, разрабатывать веб-сервисы и игры на языке от Microsoft, в команде и индивидуально.\n \n<strong>Вы научитесь:</strong>\n💣Программировать на C#\n💣Разбираться в технологиях ADO.NET и Entity Framework Code First\n💣Разрабатывать собственное Windows-приложение\n💣Использовать ООП, LINQ, коллекции, исключения и делегаты\n💣Разрабатывать собственную файловую базу данных\n💣Работать с платформой .NET Framework и средой разработки Visual Studio\n \n🤢Цена курса:  ̶1̶3̶0̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶7̶5̶2̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/profession-c-sharp/'
        photo = skillbox_courses[11]
    elif message.text == 'SkillBox📚1️⃣3️⃣':
        text = '<strong>[SkillBox]</strong><strong>Онлайн-курс Figma 3.0</strong>\n \n<strong>Описание:</strong>\nВы освоите популярный сервис для разработки интерфейсов Figma. Сможете создавать дизайн-проекты, делать прототипы и использовать этот инструмент для командной работы. Станете более востребованным дизайнером в Digital.\n \n<strong>Вы научитесь:</strong>\n🔥Уверенно работать в Figma\n🔥Выстраивать рабочий процесс\n🔥Создавать прототипы\n🔥Организовывать дизайн-проекты\n🔥Делать анимацию\n \n🤢Цена курса:  ̶2̶0̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶1̶1̶5̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/figma/'
        photo = skillbox_courses[12]
    elif message.text == 'SkillBox📚1️⃣4️⃣':
        text = ' <strong>[SkillBox] Практический интенсивный курс SMM менеджер</strong>\n \n<strong>Описание:</strong>\nВы научитесь продвигать бизнес в соцсетях, создавать вовлекающий контент, общаться с аудиторией и запускать рекламу. Курс подойдет как новичкам, которые никогда не занимались SMM, так и руководителям бизнеса.\n \n<strong>Вы научитесь:</strong>\n🌟Определять целевую аудиторию\n🌟Выбирать инструменты продвижения\n🌟Запускать таргетированную рекламу\n🌟Создавать контент\n🌟Работать с аудиторией\n🌟Анализировать метрики\n \n🤢Цена курса:  ̶7̶2̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶4̶1̶6̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/smm/'
        photo = skillbox_courses[13]
    elif message.text == 'SkillBox📚1️⃣5️⃣':
        text = '<strong>[SkillBox] Большой курс "Профессия интернет-маркетолог от А до Я"</strong>\n \n<strong>Описание:</strong>\nЗа полгода вы с нуля научитесь выстраивать стратегию продвижения бизнеса и настраивать разные виды рекламы в интернете.\n \n<strong>Вы научитесь:</strong>\n🧨Продвигать бизнес в социальных сетях: от описания профиля до контент-плана\n🧨Определять подходящие каналы маркетинга и оценивать потенциал трафика в проектах\n🧨Запускать контекстную и таргетированную рекламу\n🧨Создавать классические лендинги на Tilda и делать сайты-анкеты\n🧨Планировать рекламные кампании\n🧨Анализировать продукт, целевую аудиторию и конкурентов\n🧨Продвигать себя как специалиста в соцсетях\n \n🤢Цена курса:  ̶7̶2̶ ̶0̶0̶0̶₽̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶4̶1̶6̶ ̶5̶0̶0̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://skillbox.ru/course/internet-marketolog/'
        photo = skillbox_courses[14]
    elif message.text == 'Udemy👨‍💻0️⃣1️⃣':
        text = '<strong>[Udemy] Центр digital-профессий ITtensive - Базовый Python</strong>\n \n<strong>Описание:</strong>\nНа этом курсе вы освоите программирование на языке Python и научитесь работать с данными для самостоятельно анализа. \n \n<strong>Вы научитесь:</strong>\n🧨Основы работы с Python\n🧨Jupyter Notebook\n🧨Переменные, типы и базовые операции\n🧨Циклы for и while, управляющие конструкции\n🧨Срезы и диапазоны строк\n🧨Одномерные и многомерные списки\n🧨Базовые статистические методы\n🧨Словари, кортежи и отображения\n🧨Работа с файлами\n🧨Модули numpy и matplotlib\n \n🤢Цена курса:  ̶3̶5̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶2̶0̶ ̶5̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-python-basic/'
        photo = udemy_courses[0]
    elif message.text == 'Udemy👨‍💻0️⃣2️⃣':
        text = '<strong>[Udemy] Продвинутые навыки Python: станьте лучшим разработчиком Python!</strong>\n \n<strong>Описание:</strong>\nВ этом курсе вы узнаете много встроенных функций, чтобы стать лучшим разработчиком Python. Вы также узнаете, как реализовать лучшие практики и некоторые модульные тесты.\n \n<strong>Вы научитесь:</strong>\n🔥Полезные встроенные функции, которые иногда игнорируются в Python\n🔥Понять, как некоторые вещи работают внутри Python\n🔥Лучшие практики\n🔥Модульное тестирование\n \n🤢Цена курса:  ̶1̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶8̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/advanced-python-skills-become-a-better-python-developer/'
        photo = udemy_courses[1]
    elif message.text == 'Udemy👨‍💻0️⃣3️⃣':
        text = '<strong>[Udemy] iOS программирование на Swift. Уровень 1.</strong>\n \n<strong>Описание:</strong>\nВ данном курсе мы спроектируем, разработаем и опубликуем в AppStore полностью рабочее приложение Конвертер валют.\n \n<strong>Вы научитесь:</strong>\n🌊Сможете создавать свои iOS приложения\n🌊Научитесь работать в Xcode (среда разработки iOS приложений)\n🌊Освоите основы программирования на языке Swift\n🌊Научитесь оформлять приложения в AppStore\n🌊Публиковать приложения в AppStore\n \n🤢Цена курса:  ̶̶̶6̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶3̶7̶ ̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ios-swift-programming/'
        photo = udemy_courses[2]
    elif message.text == 'Udemy👨‍💻0️⃣4️⃣':
        text = '<strong>[Udemy] Kotlin. От А до Я </strong>\n \n<strong>Описание:</strong>\nС помощью данного курса вы сможете изучить синтаксис, возможности языка Kotlin и начать применять его в проектах и в изучении Android разработки.\n \n<strong>Вы научитесь:</strong>\n🔥Научитесь программировать на Kotlin.\n \n🤢Цена курса:  ̶̶̶8̶6̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶5̶0̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/kotlin-from-a-to-z/'
        photo = udemy_courses[3]
    elif message.text == 'Udemy👨‍💻0️⃣5️⃣':
        text = '<strong>[Udemy] React Native 2020. Мобильная разработка на JavaScript</strong>\n \n<strong>Описание:</strong>\nВ рамках данного курса вы создадите 2 мобильных приложения, на которых изучите функционал React Native\n \n<strong>Вы научитесь:</strong>\n🔥Создавать мобильные приложения под iOS и Android на языке JavaScript\n🔥Создадите несколько приложений в течении курса\n🔥React Native на практике\n🔥Получите много опыта и Best Practices в React\n \n🤢Цена курса:  ̶9̶ ̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶ ̶9̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/react-native-complete-guide/'
        photo = udemy_courses[4]
    elif message.text == 'Udemy👨‍💻0️⃣6️⃣':
        text = '<strong>[Udemy] Android разработка с нуля до профессионала</strong>\n \n<strong>Описание:</strong>\nЭтот курс подойдет для всех желающих - как для тех, кто хочет стать профессионалом в разработке Андроид приложений, так и для тех, кто просто хочет заниматься этим в качестве хобби и зарабатывать хорошие деньги на этом - никакого опыта программирования не требуется.\n \n<strong>Вы научитесь:</strong>\n🔥Разрабатывать XML разметку и UI андроид приложений\n🔥Основы Java, и также более продвинутые темы, включая ООП\n🔥Работать с аудио, видео и изображениями\n🔥Элементы Material Design, как RecyclerView, CardView и другие \n🔥Сохранять различные виды данных разными способами\n🔥Использовать библиотеки Volley, Glide, Picasso\n🔥Создавать приложения-мессенджеры при помощи Firebase - такие как Viber, WhatsApp, Telegram\n🔥Создавать практически любое андроид приложение, включая игры\n\n🤢Цена курса:  ̶9̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶9̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/android-kak-po-notam-a'
        photo = udemy_courses[5]
    elif message.text == 'Udemy👨‍💻0️⃣7️⃣':
        text = '<strong>[Udemy] PHP v.7+ и MySQL с нуля</strong>\n \n<strong>Описание:</strong>\nКурс создан для тех, кто пока еще не знаком с языком программирования PHP и позволит начать с самых азов. \n \n<strong>Вы научитесь:</strong>\nПолный курс по PHP +  MySQL и взаимодействие с данной СУБД через расширение MySQLi PHP\n \n🤢Цена курса:  ̶9̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶9̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/php-v7-mysql/'
        photo = udemy_courses[6]
    elif message.text == 'Udemy👨‍💻0️⃣8️⃣':
        text = '<strong>[Udemy] Программирование на C#: от новичка до специалиста</strong>\n \n<strong>Описание:</strong>\nКороче говоря, если вы только начинаете своё путешествие в мир программирования, C# станет отличным выбором в качестве вашего первого языка программирования.\n \n<strong>Вы научитесь:</strong>\n🔥Как устроена платформа .NET и .NET Core\n🔥Основные типы данных в C#\n🔥Управление потоком исполнения программы: циклы, условия\n🔥Массивы и коллекции: Array, List, Dictionary, Stack, Queue\n🔥Классы и структуры: отличия в контексте управления памятью\n🔥ООП в C#: наследование, полиморфизм, инкапсуляция\n🔥ООП в С#: интерфейсы, абстрактные классы, модификатора доступа\n🔥Методы: params, out, ref, static, overloading, optional parameters\n🔥Основы процесса отладки\n🔥Управление памятью: сборка мусора, boxing\\unboxing\n🔥Перечисления\n🔥Обобщения\n🔥Написание простых программ и игр на C# таких как "крестики-нолики"\n\n🤢Цена курса: ̶̶̶7̶1̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶4̶1̶ ̶4̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/csharp-ru/'
        photo = udemy_courses[7]
    elif message.text == 'Udemy👨‍💻0️⃣9️⃣':
        text = '<strong>[Udemy] Программирование игр для детей на Scratch для начинающих</strong>\n \n<strong>Описание:</strong>\nНаучитесь основам программирования и созданию увлекательных компьютерных игр в интересном формате с помощью Scratch.\n \n<strong>Вы научитесь:</strong>\n🧨Разрабатывать компьютерные игры;\n🧨Создавать программы различного назначения;\n🧨Понимать принципы программирования, которые помогут при дальнейшем его изучении;\n🧨Использовать структурный подход;\n🧨Пользоваться сеткой координат и градусной мерой углов;\n \n🤢Цена курса:  ̶4̶3̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶2̶4̶ ̶8̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/programming-for-kids-in-scratch-for-beginners/'
        photo = udemy_courses[8]
    elif message.text == 'Udemy👨‍💻1️⃣0️⃣':
        text = ' <strong>[Udemy] Создание Telegram ботов с помощью JavaScript: Полное руководство </strong>\n \n<strong>Описание:</strong>\nПолный, легкий и быстрый в освоении курс. Создайте чат-ботов Telegram с Node.js, используя Telegraf Framework.\n \n<strong>Вы научитесь:</strong>\n🧨Этот курс призван предоставить вам полный набор знаний о том, как создавать удивительные боты Telegram.\n \n🤢Цена курса:  ̶̶̶2̶8̶6̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶6̶ ̶5̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/build-telegram-bots-with-javascript-the-complete-guide/'
        photo = udemy_courses[9]
    elif message.text == 'Udemy👨‍💻1️⃣1️⃣':
        text = '<strong>[Udemy] Продвинутые алгоритмы в Java </strong>\n \n<strong>Описание:</strong>\nЗная основы Java, вы захотите приступить к выяснению алгоритмов и структур данных. При правильном их использовании ваш код будет работать быстрее, использовать меньше памяти и быть более стабильным.\n \n<strong>Вы научитесь:</strong>\n🔥Лучше решать проблемы, используя лучшие реализации и принимая правильные решения с помощью своего кода\n \n🤢Цена курса:  ̶̶̶3̶2̶2̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶1̶8̶ ̶6̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/java-best/'
        photo = udemy_courses[10]
    elif message.text == 'Udemy👨‍💻1️⃣2️⃣':
        text = '<strong>[Udemy] Аналитика и Data Science для менеджеров и гуманитариев</strong>\n \n<strong>Описание:</strong>\nКурс очень постепенно от простого к сложному погружает профессионалов из не-технических наук в захватывающий цифровой мир статистики и вероятностей – и поможет легко в нем ориентироваться, пользоваться и не бояться\n \n<strong>Вы научитесь:</strong>\n🌟Совмещать бизнес- и проф-интуицию с анализом данных, строить гипотезы и проверять их\n🌟Собирать, структурировать и обрабатывать данные\n🌟Современные методы статистического анализа на практике и реальных данных\n🌟Легко находить и видеть скрытые закономерности в данных\n🌟Анализировать большие объемы (массивы) данных\n \n🤢Цена курса:  ̶8̶̶̶6̶0̶̶̶0̶̶̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶0̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/analytics-and-data-science/'
        photo = udemy_courses[11]
    elif message.text == 'Udemy👨‍💻1️⃣3️⃣':
        text = '<strong>[Udemy] Основы программирования</strong>\n\n<strong>Описание:</strong>\nНа этом курсе вы освоите базовые понятия и термины программирования как профессии и научитесь создавать программы.\n \n<strong>Вы научитесь:</strong>\n⚡️Алгоритмы\n⚡️Блок-схемы\n⚡️Основные определения программирования\n \n🤢Цена курса:  ̶̶̶1̶4̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶8̶2̶0̶0̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-programmer-basic/'
        photo = udemy_courses[12]
    elif message.text == 'Udemy👨‍💻1️⃣4️⃣':
        text = '<strong>[Udemy] Машинное обучение: кластеризация и классификация на Python</strong>\n \n<strong>Описание:</strong>\nМы разберем прикладные подходы к кластеризации и классификации данных с помощью машинного обучения для страхового скоринга Prudential в соревновании на Kaggle вплоть до формирования конечного результата\n \n<strong>Вы научитесь:</strong>\n💣EDA: исследовательский анализ данных\n💣Точность, полнота, F1 и каппа метрики\n💣Простая кластеризация данных\n💣Логистическая регрессия: простая и многоуровневая\n💣Метод ближайших соседей: kNN\n💣Наивный Байес\n💣Метод опорных векторов: SVM\n💣Решающие деревья м случайный лес\n💣XGBoost и градиентный бустинг\n💣CatBoost и LightGBM\n💣Ансамбль голосования и стекинга\n \n🤢Цена курса:  ̶̶̶7̶1̶0̶0̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶4̶1̶ ̶4̶0̶̶̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/ittensive-python-machine-learning-classification/'
        photo = udemy_courses[13]
    elif message.text == 'Udemy👨‍💻1️⃣5️⃣':
        text = '<strong>[Udemy] Изучаем Linux и командную строку. Линукс шаг за шагом </strong>\n \n<strong>Описание:</strong>\nЭтот курс познакомит вас с некоторыми наиболее важными функциями интерпретатора bash и как администрировать Linux, используя командную строку bash.\n \n<strong>Вы научитесь:</strong>\n⚡️Вы узнаете о некоторых наиболее важных функциях интерпретатора bash\n⚡️Вы сможете использовать основные команды Linux\n⚡️Вы научитесь получать информацию о системе\n⚡️Многое другое\n \n🤢Цена курса:  ̶9̶ ̶6̶7̶5̶₽̶̶̶ ̶̶̶̶̶̶̶ ̶̶̶/̶̶̶̶̶̶̶̶̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶5̶5̶ ̶9̶0̶̶̶0̶̶̶₸̶̶̶ ̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://www.udemy.com/course/linux-eg/'
        photo = udemy_courses[14]
    elif message.text == 'WebForMySelf💻 0️⃣1️⃣':
        text = '<strong>[WebForMySelf] Веб-дизайнер профессионал</strong>\n\n<strong>Описание:</strong>\nЕсли Вас привлекает возможность вести небольшой, но доходный интернет-бизнес из любой точки планеты и жить насыщенной, интересной жизнью — фриланс в сфере веб-дизайна вполне может Вам подойти.\n\n<strong>Вы научитесь:</strong>\n🌟Научитесь проектировать дизайны сайтов.\n🌟Создавайте востребованные макеты быстро, легко и… дорого.\n🌟Быстрый старт во фрилансе без вложений.\n🌟Фокус на веб-дизайне: только самое главное.\n\n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ̶₽̶ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/wdprofi/'
        photo = webformyself_courses[0]
    elif message.text == 'WebForMySelf💻 0️⃣2️⃣':
        text = ' <strong>[WebForMySelf] Фриланс - Мастер. Как продавать свои услуги онлайн</strong>\n \n<strong>Описание:</strong>\nИменно для людей, желающих освоить тонкое ремесло удаленного заработка издательством WebForMyself был разработан комплексный видеокурс «Фриланс-Мастер. Как продавать свои услуги онлайн».\n \n<strong>Вы научитесь:</strong>\n🔥5 модулей полезных и практических знаний\n🔥Мотивация\n🔥Теория\n🔥Практика\n🔥Курс не устареет в ближайшие 5 лет или больше\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶̶̶₽ ̶̶̶/̶̶̶̶̶̶̶ ̶̶̶4̶6̶ ̶0̶0̶0̶ ̶̶̶₸̶̶̶̶̶̶̶\n🤑Наша цена: 333₽ / 1990₸ \n\n\n'
        url = 'https://webformyself.com/fmaster/'
        photo = webformyself_courses[1]
    elif message.text == 'WebForMySelf💻 0️⃣3️⃣':
        text = '<strong>[WebForMySelf] Верстка-Мастер</strong>\n \n<strong>Описание:</strong>\nВ нашем курсе макеты верстаются как раз-таки с использованием современных подходов. При верстке вы будете применять технологию Flex, препроцессор SasS и сборщик Gulp. Верстку сделаете кроссбраузерной и адаптивной под любые устройства. \n\n<strong>В курсе показана верстка макетов двух наиболее востребованных типов сайтов:\n 🧨</strong>Landing Page и интернет-магазина\n🧨Показано, как быстро верстать сайты, применяя новейшие технологии верстки: Flex, препроцессор SasS и сборщик Gulp\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n\n\n'
        url = 'https://webformyself.com/verstka/?7d19a8f7'
        photo = webformyself_courses[2]
    elif message.text == 'WebForMySelf💻 0️⃣4️⃣':
        text = '<strong>[WebForMySelf] JavaScript. Полное руководство для современной веб-разработки</strong>\n \n<strong>Описание:</strong>\nВ курсе показана разработка с нуля 2-х полноценных веб-приложений, реализованных в форме условной веб-игры и блога. В курсе нет ничего лишнего, только те знания, которые действительно нужны для практической разработки в 2019 году.\n \n<strong>Вы научитесь:</strong>\n🌟Разработка простого веб-приложения на JavaScript в форме игры\n🌟Создание веб-приложения в форме блога на чистом JavaScript (без использования сторонних библиотек)\n🌟В результате успешного прохождения видеокурса вы напишите полноценное веб-приложение на чистом JavaScript без использования сторонних библиотек.\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/javascript/'
        photo = webformyself_courses[6]
    elif message.text == 'WebForMySelf💻 0️⃣4️⃣':
        text = ' <strong>[WebForMySelf] PHP-Мастер. От теории до собственной CMS интернет-магазина</strong>\n \n<strong>Описание:</strong>\nВ этом видеокурсе показано не только создание движка для интернет-магазина, но еще и создание фреймворка, на котором и пишется CMS.\nВ курсе разрабатывается РНР-фреймворк, который вы сможете в дальнейшем использовать многократно, сокращая время разработки.\n \n<strong>Вы научитесь:</strong>\n💣Изучается теория\n💣Пишется php фреймворк\n💣Создаётся cms интернет-магазина\n💣Мастер веб-разработки на PHP\n \n🤢Цена курса:  ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/phpmaster/?spush=bWFrc2ltYXN6QHlhaG9vLmNvbQ==#price'
        photo = webformyself_courses[4]
    elif message.text == 'WebForMySelf💻 0️⃣6️⃣':
        text = ' <strong>[WebForMySelf] 1-С Битрикс. Практика создания веб-проектов</strong>\n \n<strong>Описание:</strong>\nНовый фундаментальный курс поможет вам в считанные недели овладеть профессиональной разработкой на CMS 1C-Битрикс с нуля.\n \n<strong>Вы научитесь:</strong>\n✨Создание сайта интернет-магазина\n✨Создание сайта моды\n \n🤢Цена курса: ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/bitrix/'
        photo = webformyself_courses[5]
    elif message.text == 'WebForMySelf💻 0️⃣7️⃣':
        text = ' <strong>[WebForMySelf] FullStack-Мастер: Разработка CRM-системы на Node.js, Express, Angular 6</strong>\n \n<strong>Описание:</strong>\nДанный курс наглядно показывает разработку СRМ-системы, где собраны разнообразные элементы, на которых показывается их реализация.\n \n<strong>Вы научитесь:</strong>\n🧨Пагинация\n🧨Аналитика данных с графиками\n🧨Реализация Material Design с Materialize CSS\n🧨Работа с датами через пикеры\n🧨Фильтрация данных\n🧨Загрузка картинок\n🧨Работа с асинхронными событиями\n \n🤢Цена курса:  ̶1̶2̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶7̶5̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/fsnode/'
        photo = webformyself_courses[6]
    elif message.text == 'WebForMySelf💻 0️⃣8️⃣':
        text = '<strong> [WebForMySelf] ReactJS с Нуля до Профи</strong>\n \n<strong>Описание:</strong>\nДаже полный новичок в сайтостроении сможет разобраться с курсом и освоить Frontend-разработку на стеке React.js. Пожалуй, самый быстрый, простой и легкий способ подняться по карьерной лестнице профессионального Frontend-разработчика\n \n<strong>Вы научитесь:</strong>\n🔥Фундаментальная теория\n🔥Море практики\n🔥Актуальная технология\n🔥Примеры из реальной жизни\n🔥Доступ к материалам курса 24/7\n \n🤢Цена курса:  ̶9̶8̶7̶0̶ ̶₽ ̶/̶ ̶5̶7̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/reactjs/'
        photo = webformyself_courses[7]
    elif message.text == 'WebForMySelf💻 0️⃣9️⃣':
        text = '<strong>[WebForMySelf] Курс по CSS3 </strong>\n \n<strong>Описание:</strong>\nОсновными преимуществами CSS3 являются простота использования, ускорение процесса разработки и оформления web страниц, уменьшение количества кода, практически 100% кроссбраузерность, при этом множество свойств уже можно использовать без префиксов.\n \n<strong>Вы научитесь:</strong>\n⚡️Работа с фоном\n⚡️Закругленные углы и рамки\n⚡️Прозрачность фона, картинки, текста, фото\n⚡️Установка теней для элемента и текста\n⚡️Радиальные градиенты\n \n🤢Цена курса:  ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/htmlcss-premium/css3premium/'
        photo = webformyself_courses[8]
    elif message.text == 'WebForMySelf💻 1️⃣0️⃣':
        text = '<strong>[WebForMySelf] Курс по базе данных MySQL</strong>\n \n<strong>Описание:</strong>\nКурс рассчитан как на новичков, так и на специалистов, уже имеющих опыт работы с SQL. Здесь Вы найдете освещение как теоретических вопросов (например, теория реляционных баз данных, нормализация данных), так и множество практических задач.\n \n<strong>Вы научитесь:</strong>\n🧨Типы данных в MySQL\n🧨Операторы в MySQL\n🧨Нормализация БД и объединение таблиц\n🧨Вложенные запросы и объединение таблиц\n🧨Работа с БД из PHP\n \n🤢Цена курса: ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/php-premium/mysqlpremium/'
        photo = webformyself_courses[9]
    elif message.text == 'WebForMySelf💻 1️⃣1️⃣':
        text = ' <strong>[WebForMySelf] Cоздание каталога товаров с помощью PHP, MySQL и jQuery</strong>\n \n<strong>Описание:</strong>\nЭто огромный по объему курс, в котором не просто решается какая-то конкретная задача, но в котором практически в режиме онлайн мы будем создавать собственный движок с нуля. Написанный в курсе по созданию каталога товаров с помощью PHP, MySQL и jQuery движок, можно будет использовать как для каталога, так и для любого другого сайта: визитка, интернет-магазин, корпоративный сайт, блог.\n \n<strong>Вы научитесь:</strong>\n🌟Постраничной навигации\n🌟MVC\n🌟Создадите комментарии\n🌟Авторизация, восстановление пароля, регистрация\n🌟Темы, поиск, каталог\n \n🤢Цена курса:  ̶1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/php-premium/catalogpremium/'
        photo = webformyself_courses[10]
    elif message.text == 'WebForMySelf💻 1️⃣2️⃣':
        text = '<strong> [WebForMySelf] Библиотека JQuery UI (User Interface) </strong>\n \n<strong>Описание:</strong>\nВ данном курсе мы с Вами будем учиться создавать элементы пользовательского интерфейса, используя библиотеку jQuery UI.Потому как библиотека jQuery UI – это часть глобального проекта под названием jQuery, которая в значительной степени расширяет стандартный функционал указанной библиотеки.\n \n<strong>Вы научитесь:</strong>\n🌪Использовать практически все виджеты из библиотеки jQuery\n🌪Использовать инструменты Selectable и Resizable\n🌪Создавать собственные виджеты\n🌪Использовать инструменты Draggable и Droppable\n🌪Использовать Effects\n \n🤢Цена курса: 1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/javascript-premium/jqueryui-premium/'
        photo = webformyself_courses[11]
    elif message.text == 'WebForMySelf💻 1️⃣3️⃣':
        text = '<strong>[WebForMySelf] WordPress-Мастер. Разработка тем для WordPress с нуля</strong>\n \n<strong>Описание:</strong>\nВ курсе будут использованы все современные методы создания тем для WordPress. В частности, мы познакомимся и используем популярную стартовую тему Underscores, благодаря которой разработка тем значительно ускоряется. Использование фреймворком для WordPress при создании тем на сегодняшний день фактически стало стандартом.\n \n<strong>Вы научитесь:</strong>\n🌪Как делать сайты на WordPress практически любой сложности с любым дизайном\n🌪Как делать сайты на WordPress, которые устраивают именно вас\n🌪Как делать сайты на WordPress, которые удовлетворят всем требованиям даже наиболее предвзятых заказчиков\n🌪Как делать сайты на WordPress, за которые заказчик готов заплатить действительно хорошие деньги\n \n🤢Цена курса: ̶7̶ ̶9̶7̶0̶ ̶₽ ̶/̶ ̶4̶6̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/wordpress/'
        photo = webformyself_courses[12]
    elif message.text == 'WebForMySelf💻 1️⃣4️⃣':
        text = '<strong>[WebForMySelf] Создание интернет-магазина на CMS WordPress</strong>\n \n<strong>Описание:</strong>\nВ курсе по созданию интернет-магазина на CMS WordPress мы будем работать с плагином WP–Shop. Также, кроме работы непосредственно с плагином, мы затронем вопрос создания темы для WordPress.\n \n<strong>Вы научитесь:</strong>\n✨Верстка макета\n✨Установка макета на WordPress\n✨Установка шаблона на WordPress\n \n🤢Цена курса: 1̶1̶ ̶8̶2̶0̶ ̶₽ ̶/̶ ̶6̶8̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/category/premium/wordpress-premium/wpshoppremium/'
        photo = webformyself_courses[13]
    elif message.text == 'WebForMySelf💻 1️⃣5️⃣':
        text = '<strong>[WebForMySelf] Angular 4 с Нуля до Профи</strong>\n \n<strong>Описание:</strong>\nМы начнем с самых основ и закончим созданием с нуля полностью рабочего реактивного приложения, где вы увидите все шаги по его созданию.\nПрактике предшествует 12 теоретических блоков, где максимально подробно разобраны и систематизированы в виде пошаговой целостной системы все тонкости фреймворка на различных примерах.\n \n<strong>Вы научитесь:</strong>\n🔥Компоненты\n🔥Роуты\n🔥Ленивая загрузка\n🔥Защищенные роуты\n🔥Валидация форм\n🔥Шаблонный подход (вход в систему)\n🔥Реактивный подход (регистрация, асинхронные валидаторы для проверки email)\n \n🤢Цена курса: 1̶̶̶8̶̶̶ ̶̶̶9̶̶̶0̶̶̶0̶̶̶ ̶₽̶ ̶/̶̶̶ ̶1̶̶̶1̶̶̶3̶̶̶4̶̶̶0̶̶̶0̶̶̶ ̶₸̶̶̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://webformyself.com/angular4/'
        photo = webformyself_courses[14]
    elif message.text == 'OTUS👨‍🎓0️⃣1️⃣':
        text = '<strong>[OTUS] iOS-разработчик. Базовый курс.</strong>\n \n<strong>Описание:</strong>\nКурс фундаментальный: вы сможете разрабатывать самые разнообразные iOS-приложения: интернет-магазины, банковские приложения, фото-редакторы, всевозможные помощники, приложения для фитнеса и прочие услуги.\n \n<strong>Вы научитесь:</strong>\n🔥Создавать IOS-приложения на языке Swift\n🔥Использовать новые фреймворки SwiftUI и Combine\n🔥Применять принципы SOLID в разработке\n🔥Покрывать свой код тестами с помощью TDD\n🔥Работать с сетью на примере API VK\n🔥Использовать Instruments\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/basic-ios/?int_source=courses_catalog&int_term=programming'
        photo = otus_courses[0]
    elif message.text == 'OTUS👨‍🎓0️⃣2️⃣':
        text = '<strong>[OTUS] iOS Разработчик. Продвинутый курс v 2.0</strong>\n \n<strong>Описание:</strong>\nПрограмма создана специально для iOS Developers с опытом работы в сфере разработки мобильных iOS-приложений от 1 года и более.\nОбучение построено исключительно на кейсах из практики разработки приложений в production. Мы будем решать сложные и хардкорные задачи с уровнем качества топовых приложений\n \n<strong>Вы научитесь:</strong>\n💣Применять GCD и решать проблемы многозадачности\n💣Работать с протоколами Sequence и Collection\n💣Использовать в проектах структуры данных, Generic Type, Associated Types и техники Type Erasure, PATs (Protocol with Associated Types)\n \n🤢Цена курса:  ̶7̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶0̶5̶ ̶0̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://otus.ru/lessons/advanced-ios/'
        photo = otus_courses[1]
    elif message.text == 'OTUS👨‍🎓0️⃣3️⃣':
        text = '<strong>[OTUS] Разработчик Golang</strong>\n \n<strong>Описание:</strong>\nВ этом курсе мы хотели бы объяснить, что такое Go-way, рассказать про идиомы языка и помочь избежать типичных ошибок. Программа курса позволит погрузиться в разработку на Go для решения практических задач, углубления знаний в языке и сопутствующем технологическом стеке\n\n<strong>Вы научитесь:</strong>\n⚡️Писать production-ready код, многопоточные и конкурентные программы;\n⚡️Понимать синтаксис и внутреннее устройство языка Go;\n⚡️Понимать особенности сетевого программирования;\n⚡️Уметь создавать микросервисы с помощью Go;\n⚡️Разворачивать микросервисы с помощью docker.\n \n🤢Цена курса:  ̶8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-golang/'
        photo = otus_courses[2]
    elif message.text == 'OTUS👨‍🎓0️⃣4️⃣':
        text = '<strong> [OTUS] Framework Laravel</strong>\n \n<strong>Описание:</strong>\nРазработчики, обладающие навыками профессиональной работы с PHP-фреймворком Laravel, — сегодня одни из самых востребованных и малочисленных специалистов в сфере IT. Работать с ним удобно и приятно любому, кто освоит все его возможности.\n \n<strong>После обучения студенты смогут:</strong>\n🧨Использовать в проектах Laravel\n🧨Обеспечивать безопасность приложения\n🧨Тестировать и разворачивать полученный код\n🧨Выполнять анализ работы логики и делать выводы\n🧨Использовать встроенные инструменты фреймворка\n \n🤢Цена курса:  ̶5̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶8̶9̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n\n\n'
        url = 'https://otus.ru/lessons/laravel/?int_source=courses_catalog&int_term=programming'
        photo = otus_courses[3]
    elif message.text == 'OTUS👨‍🎓0️⃣5️⃣':
        text = '<strong> [OTUS] Разработчик BigData</strong>\n\n<strong>Описание:</strong>\nЦель прохождения курса — освоение алгоритмов машинного обучения и логических методов, позволяющих находить ценную информацию в крупных массивах данных и эффективно внедрять эту информацию для решения реальных бизнес-задач.\n\n<strong>Вы научитесь:</strong>\n👨‍💻Использовать методы машинного обучения в практически полезных приложениях и исследованиях;\n👨‍💻Выбирать подходящие алгоритмы и метрики;\n👨‍💻Проводить статистические исследования и интерпретировать их результаты;\n👨‍💻Проектировать архитектуру нейросетей и обучать их;\n👨‍💻Самостоятельно реализовывать весь процесс: от поиска полезной информации в массивах данных до построения схемы обработки данных в боевом окружении.\n\n🤢Цена курса: ̶̶̶4̶̶̶0̶̶̶ ̶̶̶0̶̶̶0̶̶̶0̶̶̶₽̶ ̶̶̶/̶̶̶ ̶̶̶2̶̶̶3̶̶̶1̶̶̶ ̶̶̶4̶̶̶0̶̶̶0̶̶̶₸̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://otus.ru/events/bigdata/70/'
        photo = otus_courses[4]
    elif message.text == 'OTUS👨‍🎓0️⃣6️⃣':
        text = '<strong>[OTUS] Подготовительный курс по JavaScript разработке</strong>\n \n<strong>Описание:</strong>\nВсе основные возможности Javascript\nДомашние задания и их разбор\nПодготовка к курсам "Fullstack разработчик Javascript", "React.js-разработчик" и "Node.js-разработчик"\n \n<strong>Вы научитесь:</strong>\n🌟Объекты и массивы\n🌟Работа с DOM\n🌟Встроенные инструменты\n \n🤢Цена курса:  ̶1̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶8̶6̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/online/online-js/'
        photo = otus_courses[5]
    elif message.text == 'OTUS👨‍🎓0️⃣7️⃣':
        text = '<strong>[OTUS] Разработчик Python</strong>\n \n<strong>Описание:</strong>\nПрофессиональный онлайн-курс для тех, кто уже имеет опыт программирования на Python и хочет повысить свой уровень за счет новых знаний и навыков из различных областей разработки. Если вы уверенно чувствуете себя с Python, помните C, имеете представление о сетевом взаимодействии и реляционных СУБД, умеете обращаться с Linux, Git и прочими стандартными инструментами девелопера — курс для вас.\n \n<strong>Вы научитесь:</strong>\n🐍Как писать простой и идиоматичный код, за который не будет мучительно стыдно?\n🐍Как тестировать и поддерживать код на Python?\n🐍Как написать приложение, которое не умрёт под нагрузкой?\n \n🤢Цена курса:  ̶9̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶5̶2̶0̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-python/'
        photo = otus_courses[6]
    elif message.text == 'OTUS👨‍🎓0️⃣8️⃣':
        text = '<strong>[OTUS] Data Engineer</strong>\n \n<strong>Описание:</strong>\nКурс адресован разработчикам, администраторам СУБД и всем, кто стремится повысить профессиональный уровень, освоить новые инструменты и заниматься интересными задачами в сфере работы с данными.\n \n<strong>После обучения Data Engineering вы станете востребованным специалистом, который:</strong>\n🔥Разворачивает, налаживает и оптимизирует инструменты обработки данных\n🔥Адаптирует датасеты для дальнейшей работы и аналитики\n🔥Создает сервисы, которые используют результаты обработки больших объемов данных\n🔥Отвечает за архитектуру данных в компании\n\n\n🤢Цена курса: 8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/data-engineer/'
        photo = otus_courses[7]
    elif message.text == 'OTUS👨‍🎓0️⃣9️⃣':
        text = '<strong>[OTUS] Backend разработчик на PHP</strong>\n \n<strong>Описание:</strong>\nДля реализации больших и долгосрочных проектов современному PHP-разработчику необходимо заботиться об архитектуре кода, применять паттерны проектирования, писать код в соответствии с принципами SOLID и поддерживать высокий code coverage своих unit-тестов.\n \n<strong>Вы научитесь:</strong>\n💣Глубокое знакомство с библиотеками PHP и особенностями языка\n💣Навыки проектирования приложений, работы с базами и файлами, веб-фронтендом\n💣Привычку к хорошему и чистому коду\n💣Владение тактиками по созданию высоконагруженных систем\n \n🤢Цена курса: ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/razrabotchik-php/'
        photo = otus_courses[8]
    elif message.text == 'OTUS👨‍🎓1️⃣0️⃣':
        text = '<strong>[OTUS] С++ для начинающих программистов</strong>\n\n<strong>Описание:</strong>\nКурс по разработке на C++ для начинающих программистов\nЗанятия в формате видео и проверочные тесты\nВсе необходимые знания и навыки для курса "Разработчик С++"\n\n<strong>Вы научитесь:</strong>\n🌟Классы и алгоритмы\n🌟Шаблоны классов и функций\n🌟Многопоточность\n🌟Исключения\n🌟Работа с сетью\n\n🤢Цена курса: ̶1̶5̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶8̶6̶ ̶8̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/online/online-cpp/'
        photo = otus_courses[9]
    elif message.text == 'OTUS👨‍🎓1️⃣1️⃣':
        text = '<strong>[OTUS] Архитектура и шаблоны проектирования </strong>\n \n<strong>Описание:</strong>\nКурс для разработчиков, которые хотят изучить основные паттерны проектирования и научиться применять их, находить им замену в сложных ситуациях и научиться мыслить как архитектор программного обеспечения.\n \n<strong>Вы научитесь:</strong>\n🔥Формирует представление об архитектуре приложения.\n🔥Даёт представление об основных шаблонах проектирования.\n🔥Даёт навыки построения архитектуры\n🔥Предлагает закрепление материалы через практические работы\n \n🤢Цена курса:  ̶4̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶3̶1̶ ̶4̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/patterns/'
        photo = otus_courses[10]
    elif message.text == 'OTUS👨‍🎓1️⃣2️⃣':
        text = '<strong>[OTUS] Пентест. Практика тестирования на проникновение</strong>\n \n<strong>Описание:</strong>\nПентест — это процесс санкционированного взлома информационных систем по просьбе заказчика, в ходе которого пентестер (аудитор) выявляет уязвимости информационной системы и дает заказчику рекомендации по их устранению.\n \n<strong>Вы научитесь:</strong>\n🧨Основным этапам проведения тестирования на проникновение\n🧨Использованию современных инструментов для проведения анализа защищенности информационной системы или приложения\n🧨Классификации уязвимостей и методам их исправления\n🧨Навыкам программирования для автоматизации рутинных задач\n \n🤢Цена курса: ̶5̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶2̶8̶9̶ ̶3̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/pentest/process/'
        photo = otus_courses[11]
    elif message.text == 'OTUS👨‍🎓1️⃣3️⃣':
        text = '<strong>[OTUS] MS SQL Server разработчик</strong>\n \n<strong>Описание:</strong>\nКурс позволит понять детали процессов и получить чёткое представление, что делает тот или иной код, где могут возникнуть потенциальные проблемы, как их можно разрешить.\n \n<strong>Вы научитесь:</strong>\n🌟Разрабатывать на SQL\n🌟Проектировать БД и понимать все нюансы;\n🌟Анализировать и оптимизировать производительности запросов;\n🌟Писать сложные хранимые процедуры, функции и триггеры;\n🌟Читать план запроса.\n \n🤢Цена курса: ̶8̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶4̶6̶2̶ ̶9̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/ms-sql-server-razrabotchik/'
        photo = otus_courses[12]
    elif message.text == 'OTUS👨‍🎓1️⃣4️⃣':
        text = '<strong> [OTUS] Реляционные СУБД</strong>\n \n<strong>Описание:</strong>\nПолный курс по работе с базами данных реляционными и нереляционными.\nКурс включает в себя все основные и популярные БД, которые могут пригодиться разработчику: PostgreSQL, MySQL, Redis, MongoDB, Cassandra и т.д.\n \n<strong>Вы научитесь:</strong>\n🔥Научитесь проектировать базы данных и создавать оптимальную структуру их хранения;\n🔥Будете различать основные СУБД (PostgreSQL, MySQL, Redis, MongoDB, Cassandra и т.д );\n🔥Освоите синтаксис и особенности работы SQL, DDL, DML;\n🔥Сможете оптимизировать медленные запросы.\n \n🤢Цена курса:  ̶6̶0̶ ̶0̶0̶0̶ ̶₽ ̶/̶ ̶3̶4̶7̶ ̶2̶0̶0̶ ̶₸̶\n🤑Наша цена: 333₽ / 1990₸ \n'
        url = 'https://otus.ru/lessons/subd/'
        photo = otus_courses[13]
    elif message.text == 'OTUS👨‍🎓1️⃣5️⃣':
        text = '<strong> [OTUS] Fullstack разработчик JavaScript</strong>\n \n<strong>Описание:</strong>\nПрактический курс для web-разработчиков по продвинутым возможностям JS и его фреймворков\n \n<strong>Вы научитесь:</strong>\n🔥Полный ландшафт современных технологий Node.js / React / Angular / Vue / Svelte / TypeScript / Web Components\n🔥Углубитесь во внутренние алгоритмы и логику работы фреймворков и рассмотрите спецификации\n🔥Домашние задания в формате мини-assignment, как на собеседованиях в российских и европейских компаниях\n \n🤢Цена курса:  ̶̶̶̶̶̶̶4̶0̶ ̶̶̶̶̶̶̶0̶̶̶̶̶̶̶0̶̶̶̶̶̶̶0̶̶̶̶̶̶̶₽̶̶̶ ̶̶̶̶̶̶̶/̶̶̶̶̶̶̶ ̶̶̶̶̶̶̶2̶3̶0̶ ̶0̶0̶0̶₸̶̶̶\n🤑Наша цена: 333₽ / 1990₸\n'
        url = 'https://otus.ru/lessons/javascript/'
        photo = otus_courses[14]
    if photo:
        bot.send_photo(message.from_user.id, photo=photo, caption=text,
                       reply_markup=one_course(message.from_user.id, url, school),
                       parse_mode='html')


bot.polling(none_stop=True, timeout=200)
