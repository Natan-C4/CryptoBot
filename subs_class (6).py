import sqlite3
from crypto_class import Crypto

class Subs:
    def __init__(self, database):
        # Подключаемся к бд
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

# add_subscriber handler
   

    def add_subscriber(self, user_id, crypto_symbol, more, crypto_cost):
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id` , `crypto_symbol`, `more` , `crypto_cost`) VALUES (?,?,?,?) ", (user_id, crypto_symbol, more, crypto_cost))
# remove_subscriptions handler
    def remove_subscriptions(self, user_id):
        with self.connection:
            sql = f""" DELETE FROM `subscriptions` WHERE `user_id` = {user_id}"""
            return self.cursor.execute(sql)
#get all subs 
    def subs_messages(self):
        with self.connection:
            messages = []
            subs_arr =  self.cursor.execute('SELECT * FROM `subscriptions`').fetchall()
            for sub in subs_arr:
                
                user_id = sub[1]
                crypto = sub[2]
                set_cost = sub[4]
                more = sub[3]
                
                sql = f"SELECT USD FROM crypto WHERE symbol = '{crypto}'"
                crypto_cost = self.cursor.execute(sql).fetchall()[0][0]
                mes = f"{crypto} is {more} {set_cost}"
               
                if more == '>':
                    if crypto_cost > set_cost:
                        mes = f"{crypto} is {more} {set_cost}"
                        messages.append([user_id,mes])
                if more == '<':
                    if crypto_cost < set_cost:
                        mes = f"{crypto} is {more} {set_cost}"
                        messages.append([user_id,mes])
                if more == '=':
                    if crypto_cost == set_cost:
                        mes = f"{crypto} is {more} {set_cost}"
                        messages.append([user_id,mes])
            return messages

                
            

    def close(self):
        self.connection.close()
