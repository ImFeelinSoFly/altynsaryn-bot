# coding=utf-8
import telebot
import const
# import time
# import mysql.connector
# import re
# import shelve

from telebot import types
from telebot.types import LabeledPrice
flag_for_cancel_payment = 0
flag_for_confirmation_of_payment = 0
flag = 0
bot = telebot.TeleBot(const.TOKEN)

"""conn = mysql.connector.connect(user='root', password='idris6397', host='127.0.0.1', database='testshit',
                               auth_plugin='mysql_native_password')
Cursor = conn.cursor(buffered=True)
conn._execute_query('CREATE DATABASE IF NOT EXISTS progbot')

Cursor.execute('''CREATE TABLE IF NOT EXISTS user (id int NOT NULL auto_increment primary key,
    IDIS varchar(100) NOT NULL,
    FullAc bit NOT NULL,
    Name varchar(100) NOT NULL,
    Number varchar(100) )''')

Cursor.execute("SELECT * FROM USER")
rows = Cursor.fetchall()
for j in rows:
    print(j)"""

prices = [LabeledPrice(label='School', amount=500000), LabeledPrice(label='1 course', amount=200000)]
schools = ['geekbrains', 'netology', 'otus', 'webformyself', 'udemy', 'skillbox']
geekbrains_courses = [
    'AgACAgIAAxkBAAICW18PNKQye4ClO8Dh5ALdn9tGKPxsAAL0rTEbtmeBSA1s1pzQezU_uRu5ki4AAwEAAwIAA20AA5VoBAABGgQ',
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
    'AgACAgIAAxkBAAICm18POZgBuSvVOQYs37y4LOiKOsCYAAL8rTEbtmeBSAUHrkl4L_uqeIeVlS4AAwEAAwIAA20AAyeQAQABGgQ',
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
    'AgACAgIAAxkBAAICiF8POJ0K3Sj_YC1RfCXG8zAPQHHYAAIirjEbtmeBSB9jB5vtzFAmK_OQlS4AAwEAAwIAA20AA-CPAQABGgQ',
    'AgACAgIAAxkBAAICiV8POKTzc4nxDBYFXMgevsIC8uSNAAL-rTEbtmeBSIuioEsXyX_iGrC9ki4AAwEAAwIAA20AAyloBAABGgQ',
    'AgACAgIAAxkBAAICil8POKmYuRbIXT28SuwkY4XsFT7kAAIjrjEbtmeBSGoPQk1nt9V43SedlS4AAwEAAwIAA20AA3aPAQABGgQ',
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
    'AgACAgIAAxkBAAICe18PNgzvpoPV1kCeoga8_2RmLzeBAAIYrjEbtmeBSBuZ74MXOcRiqPJNkS4AAwEAAwIAA20AA6TrBQABGgQ',
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
                 'AgACAgIAAxkBAAICrF8POkYBRksmvbBfuQnl6a82A_TJAAI9rjEbtmeBSKGaNilhb8BfrfxtkS4AAwEAAwIAA20AAwetBQABGgQ',
                 'AgACAgIAAxkBAAICqV8POgu76vAugw6kKhjrli26QgNoAAI6rjEbtmeBSKAhxvX5yjYjMHcblS4AAwEAAwIAA20AAweNAQABGgQ',
                 'AgACAgIAAxkBAAICql8POhFXilkcnGHZdizijEdumYodAAI7rjEbtmeBSLAB-vi88XRe41v4lC4AAwEAAwIAA20AA5f7AQABGgQ',
                 'AgACAgIAAxkBAAICq18POhNFToTrYEOckiZMnr06F5AjAAI8rjEbtmeBSNJJPDAlIh0cPwLlkS4AAwEAAwIAA20AA3hVBAABGgQ']


# db = shelve.open('test.txt', writeback=True)
# .close()

def payment_method():
    pm = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text='Банковской картой', callback_data='pay' + payment_course + 'credit card')
    but_2 = types.InlineKeyboardButton(text='Qiwi кошелек', callback_data='pay' + payment_course + 'qiwi wallet')
    but_3 = types.InlineKeyboardButton(text='Kaspi Gold', callback_data='pay' + payment_course + 'kaspi gold')
    but_4 = types.InlineKeyboardButton(text='Отмена',callback_data='cancel')
    pm.add(but_1, but_2, but_3)
    pm.add(but_4)
    return pm


def credit_keyboard(amount, url, payment_course):
    ck = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Оплатить ' + str(amount), url=url, callback_data='money')
    but_2 = types.InlineKeyboardButton(text='Назад', callback_data=payment_course[3:])
    ck.add(but_1, but_2)
    return ck


def successful_payment(user_id):
    sp = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Подтверждаю',
                                       callback_data='success' + payment_course[3:] + ' ' + str(user_id))
    but_2 = types.InlineKeyboardButton(text='Отказано', callback_data='reject' + " " + str(user_id))
    sp.add(but_1, but_2)
    return sp


def one_course(payment_course, url, school):
    oc = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text='Купить', callback_data=payment_course)
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


@bot.inline_handler(lambda query: query.query == 'courses')
def query_text(query):
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
    """global previous_query_message
    previous_query_message = query.inline_query_id
    bot.send_message(chat_id=chat_id, text=previous_query_message)"""
    results = [article_1, article_2, article_3, article_4, article_5, article_6]
    bot.answer_inline_query(query.id, results)


@bot.inline_handler(
    lambda query: query.query in ['geekbrains', 'netology', 'otus', 'webformyself', 'udemy', 'skillbox'])
def schools(query):
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
                                                    title='Тренды SMM',
                                                    description='Это полноценный маркетинг, а не только продвижение '
                                                                'через различные социальные платформы',
                                                    thumb_url='https://imagizer.imageshack.com/img923/3730/oM6Vfo.jpg',
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
                                                    title='UX-дизайнер: основы профессии и тренды',
                                                    description='Проанализируете пользовательские сценарии',
                                                    thumb_url='https://imagizer.imageshack.com/img923/1329/rm6tyt.jpg',
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
                                                   thumb_url='https://imagizer.imageshack.com/img922/656/fWuCv0.png',
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
    global payment_course, flag, user, flag_for_confirmation_of_payment, flag_for_cancel_payment
    if 'success' in call.data:
        chat_id = ''.join([i for i in call.data[-13:] if i.isdigit()])
        bot.send_message(909435473, text='Заказ под номером  ' + chat_id + ' подтвержден от ' + user)
        bot.send_message(chat_id,
                         text='Спасибо за покупку!\nВот ваш заказ:\nhttps://cloud.mail.ru/public/7BRK/JuvmnLWdU')
    elif 'pay' in call.data:
        if call.from_user.last_name and call.from_user.username:
            user = call.from_user.first_name + ' ' + call.from_user.last_name + ' ' + call.from_user.username
        elif call.from_user.last_name:
            user = call.from_user.first_name + ' ' + call.from_user.last_name
        else:
            user = call.from_user.first_name
        if not flag_for_confirmation_of_payment:
            bot.send_message(call.from_user.id,
                             text='После совершения покупки нажмите кнопку ниже, чтобы получить товар',
                             reply_markup=confirmation())
        flag_for_confirmation_of_payment = 1
        payment_course = call.data
        if '16' in call.data:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('5000',
                                                                   'https://oplata.qiwi.com/form?invoiceUid=12252f8a-cf6d-4417-9243-4b137f68fdfd',
                                                                   payment_course))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('5000',
                                                                   'https://oplata.qiwi.com/form?invoiceUid=12252f8a-cf6d-4417-9243-4b137f68fdfd',
                                                                   payment_course))
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('5000', 'https://github.com/', payment_course))
        elif 'all' in call.data:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.data))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.data))
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('9990', 'https://github.com/', call.data))
        elif call.data[3:7] in ['geek', 'neto', 'otus', 'webf', 'udem', 'skil']:
            if 'card' == call.data[-4:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату банковской картой:\nПерейдите по ссылке и следуйте инструкции чтобы '
                                           'оплатить\nhttps://secure.tap2pay.me/products/6PsHzmg9/telegram',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.data))
            elif 'wallet' == call.data[-6:]:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Qiwi кошелек:\nПереведите 5000 на номер 4353454535234',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.data))
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали оплату через Kaspi Gold:\nПереведите 5000 на карту 424242424244242424424',
                                      reply_markup=credit_keyboard('2000', 'https://github.com/', call.data))
    elif call.data == 'confirmed':
        bot.send_message(chat_id=909435473, text=payment_course + '\n' + str(call.from_user.id),
                         reply_markup=successful_payment(call.from_user.id))
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text='Ваш заказ принят, ожидайте подтверждения')
    elif call.data == 'disconf':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        flag_for_confirmation_of_payment = 0
    elif call.data == 'moderator':
        bot.send_message(chat_id=call.from_user.id, text='По всем вопросам пишите:\n@official_aldarkose')
    elif call.data == 'copyright':
        bot.send_message(chat_id=call.from_user.id,
                         text='Если вы обладатель курса, то можете оставить жалобу здесь:\n@AltynsarynCopyrightBot')
    elif call.data == 'new_com':
        bot.send_message(call.from_user.id, text='Вы можете написать отзыв здесь:\n@AlynsarynCommentsBot')
    elif call.data == 'comments':
        bot.send_message(call.from_user.id, text='Здесь вы можете посмотреть отзывы здесь:\nLink')
    elif call.data == 'cancel':
        bot.delete_message(call.from_user.id,call.message.message_id)
        flag_for_cancel_payment = 0
    elif 'pay' not in call.data and not flag_for_cancel_payment:
        if not flag:
            flag = 1
            flag_for_cancel_payment = 1
            if call.message:
                payment_course = call.data[:18]
                bot.send_message(chat_id=call.message.chat.id,
                                 text="Выберите способ оплаты:", reply_markup=payment_method())
            else:
                payment_course = call.data[:18]
                bot.send_message(chat_id=call.from_user.id, text="Выберите способ оплаты:",
                                 reply_markup=payment_method())
        else:
            if call.message:
                payment_course = call.data[:18]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Выберите способ оплаты:", reply_markup=payment_method())
            else:
                payment_course = call.data[:18]
                bot.send_message(chat_id=call.from_user.id, text="Выберите способ оплаты:",
                                 reply_markup=payment_method())


@bot.message_handler(commands=['start'])
def startpg(message):
    if message.chat.id == 442051731:
        bot.send_message(message.chat.id, text='Присоединился Gold Administrator')
    main_keyboard = types.ReplyKeyboardMarkup(True, False)
    main_keyboard.row('Поддержать проект')
    main_keyboard.row('Все 999 курса за 100кзт')
    bot.send_message(message.chat.id, 'Привет {name}!'.format(name=message.chat.first_name), reply_markup=main_keyboard)
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
    bot.send_message(message.chat.id,
                     'Я бот, который продает курсы по программированию !\n', reply_markup=main_menu)
    global previous_message_id, chat_id, payment_course
    previous_message_id = message.message_id + 3
    chat_id = message.chat.id
    payment_course = ''


@bot.message_handler(content_types=['text'])
def essential(message):
    global payment_course, flag
    photo = 0
    flag = 0
    payment_course = message.text
    global previous_message_id, chat_id
    chat_id = message.chat.id
    school = ''.join([i for i in message.text if not i.isdigit()])
    url = 'https://www.geeksforgeeks.org/python-ways-to-remove-numeric-digits-from-given-string/'
    try:
        i = 0
        while previous_message_id + i < message.message_id:
            bot.delete_message(message.chat.id, previous_message_id + i)
            i += 1
        previous_message_id = message.message_id
    except:
        previous_message_id = message.message_id
    if message.text == 'Все 999 курса за 100кзт':
        bot.send_message(message.chat.id, text='Nurzhik krossovok')
    elif message.text == 'geekbrains1':
        text = 'text1'
        photo = geekbrains_courses[0]
    elif message.text == 'geekbrains2':
        text = ''
        photo = geekbrains_courses[1]
    elif message.text == 'geekbrains3':
        text = ''
        photo = geekbrains_courses[2]
    elif message.text == 'geekbrains4':
        text = ''
        photo = geekbrains_courses[3]
    elif message.text == 'geekbrains5':
        text = ''
        photo = geekbrains_courses[4]
    elif message.text == 'geekbrains6':
        text = ''
        photo = geekbrains_courses[5]
    elif message.text == 'geekbrains7':
        text = ''
        photo = geekbrains_courses[6]
    elif message.text == 'geekbrains8':
        text = ''
        photo = geekbrains_courses[7]
    elif message.text == 'geekbrains9':
        text = ''
        photo = geekbrains_courses[8]
    elif message.text == 'geekbrains10':
        text = ''
        photo = geekbrains_courses[9]
    elif message.text == 'geekbrains11':
        text = ''
        photo = geekbrains_courses[10]
    elif message.text == 'geekbrains12':
        text = ''
        photo = geekbrains_courses[11]
    elif message.text == 'geekbrains13':
        text = ''
        photo = geekbrains_courses[12]
    elif message.text == 'geekbrains14':
        text = ''
        photo = geekbrains_courses[13]
    elif message.text == 'geekbrains15':
        text = ''
        photo = geekbrains_courses[14]
    elif message.text == 'netology1':
        text = ''
        photo = netology_courses[0]
    elif message.text == 'netology2':
        text = ''
        photo = netology_courses[1]
    elif message.text == 'netology3':
        text = ''
        photo = netology_courses[2]
    elif message.text == 'netology4':
        text = ''
        photo = netology_courses[3]
    elif message.text == 'netology5':
        text = ''
        photo = netology_courses[4]
    elif message.text == 'netology6':
        text = ''
        photo = netology_courses[5]
    elif message.text == 'netology7':
        text = ''
        photo = netology_courses[6]
    elif message.text == 'netology8':
        text = ''
        photo = netology_courses[7]
    elif message.text == 'netology9':
        text = ''
        photo = netology_courses[8]
    elif message.text == 'netology10':
        text = ''
        photo = netology_courses[9]
    elif message.text == 'netology11':
        text = ''
        photo = netology_courses[10]
    elif message.text == 'netology12':
        text = ''
        photo = netology_courses[11]
    elif message.text == 'netology13':
        text = ''
        photo = netology_courses[12]
    elif message.text == 'netology14':
        text = ''
        photo = netology_courses[13]
    elif message.text == 'netology15':
        text = ''
        photo = netology_courses[14]
    elif message.text == 'skillbox1':
        text = ''
        photo = skillbox_courses[0]
    elif message.text == 'skillbox2':
        text = ''
        photo = skillbox_courses[1]
    elif message.text == 'skillbox3':
        text = ''
        photo = skillbox_courses[2]
    elif message.text == 'skillbox4':
        text = ''
        photo = skillbox_courses[3]
    elif message.text == 'skillbox5':
        text = ''
        photo = skillbox_courses[4]
    elif message.text == 'skillbox6':
        text = ''
        photo = skillbox_courses[5]
    elif message.text == 'skillbox7':
        text = ''
        photo = skillbox_courses[6]
    elif message.text == 'skillbox8':
        text = ''
        photo = skillbox_courses[7]
    elif message.text == 'skillbox9':
        text = ''
        photo = skillbox_courses[8]
    elif message.text == 'skillbox10':
        text = ''
        photo = skillbox_courses[9]
    elif message.text == 'skillbox11':
        text = ''
        photo = skillbox_courses[10]
    elif message.text == 'skillbox12':
        text = ''
        photo = skillbox_courses[11]
    elif message.text == 'skillbox13':
        text = ''
        photo = skillbox_courses[12]
    elif message.text == 'skillbox14':
        text = ''
        photo = skillbox_courses[13]
    elif message.text == 'skillbox15':
        text = ''
        photo = skillbox_courses[14]
    elif message.text == 'udemy1':
        text = ''
        photo = udemy_courses[0]
    elif message.text == 'udemy2':
        text = ''
        photo = udemy_courses[1]
    elif message.text == 'udemy3':
        text = ''
        photo = udemy_courses[2]
    elif message.text == 'udemy4':
        text = ''
        photo = udemy_courses[3]
    elif message.text == 'udemy5':
        text = ''
        photo = udemy_courses[4]
    elif message.text == 'udemy6':
        text = ''
        photo = udemy_courses[5]
    elif message.text == 'udemy7':
        text = ''
        photo = udemy_courses[6]
    elif message.text == 'udemy8':
        text = ''
        photo = udemy_courses[7]
    elif message.text == 'udemy9':
        text = ''
        photo = udemy_courses[8]
    elif message.text == 'udemy10':
        text = ''
        photo = udemy_courses[9]
    elif message.text == 'udemy11':
        text = ''
        photo = udemy_courses[10]
    elif message.text == 'udemy12':
        text = ''
        photo = udemy_courses[11]
    elif message.text == 'udemy13':
        text = ''
        photo = udemy_courses[12]
    elif message.text == 'udemy14':
        text = ''
        photo = udemy_courses[13]
    elif message.text == 'udemy15':
        text = ''
        photo = udemy_courses[14]
    elif message.text == 'webformyself1':
        text = ''
        photo = webformyself_courses[0]
    elif message.text == 'webformyself2':
        text = ''
        photo = webformyself_courses[1]
    elif message.text == 'webformyself3':
        text = ''
        photo = webformyself_courses[2]
    elif message.text == 'webformyself4':
        text = ''
        photo = webformyself_courses[6]
    elif message.text == 'webformyself5':
        text = ''
        photo = webformyself_courses[4]
    elif message.text == 'webformyself6':
        text = ''
        photo = webformyself_courses[5]
    elif message.text == 'webformyself7':
        text = ''
        photo = webformyself_courses[6]
    elif message.text == 'webformyself8':
        text = ''
        photo = webformyself_courses[7]
    elif message.text == 'webformyself9':
        text = ''
        photo = webformyself_courses[8]
    elif message.text == 'webformyself10':
        text = ''
        photo = webformyself_courses[9]
    elif message.text == 'webformyself11':
        text = ''
        photo = webformyself_courses[10]
    elif message.text == 'webformyself12':
        text = ''
        photo = webformyself_courses[11]
    elif message.text == 'webformyself13':
        text = ''
        photo = webformyself_courses[12]
    elif message.text == 'webformyself14':
        text = ''
        photo = webformyself_courses[13]
    elif message.text == 'webformyself15':
        text = ''
        photo = webformyself_courses[14]
    elif message.text == 'otus1':
        text = ''
        photo = otus_courses[0]
    elif message.text == 'otus2':
        text = ''
        photo = otus_courses[1]
    elif message.text == 'otus3':
        text = ''
        photo = otus_courses[2]
    elif message.text == 'otus4':
        text = ''
        photo = otus_courses[3]
    elif message.text == 'otus5':
        text = ''
        photo = otus_courses[4]
    elif message.text == 'otus6':
        text = ''
        photo = otus_courses[5]
    elif message.text == 'otus7':
        text = ''
        photo = otus_courses[6]
    elif message.text == 'otus8':
        text = ''
        photo = otus_courses[7]
    elif message.text == 'otus9':
        text = ''
        photo = otus_courses[8]
    elif message.text == 'otus10':
        text = ''
        photo = otus_courses[9]
    elif message.text == 'otus11':
        text = ''
        photo = otus_courses[10]
    elif message.text == 'otus12':
        text = ''
        photo = otus_courses[11]
    elif message.text == 'otus13':
        text = ''
        photo = otus_courses[12]
    elif message.text == 'otus14':
        text = ''
        photo = otus_courses[13]
    elif message.text == 'otus15':
        text = ''
        photo = otus_courses[14]

    if photo:
        bot.send_photo(message.chat.id, photo=photo, caption=text, reply_markup=one_course(payment_course, url, school))


bot.polling(none_stop=True,timeout=123)
