import sqlite3
import config
import requests


class Crypto:
    def __init__(self, database, fiat):
        # Подключаемся к бд
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def update_info(self):

        url_usd = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,1027,1831,2,1720,1376,1321,131'
        #parameters = dict.fromkeys(['convert'], fiat)

        parameters_usd = {
         'convert': 'USD'
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.coin_api_token,
        }
        usd =  requests.get(url_usd, headers=headers, params=parameters_usd)
        usd = usd.json()

        usd_1 = usd['data']['1']['quote']['USD']['price']

        usd_2 = usd['data']['2']['quote']['USD']['price']

        usd_131 = usd['data']['131']['quote']['USD']['price']

        usd_1027 = usd['data']['1027']['quote']['USD']['price']

        usd_1321 = usd['data']['1321']['quote']['USD']['price']

        usd_1376 = usd['data']['1376']['quote']['USD']['price']

        usd_1720 = usd['data']['1720']['quote']['USD']['price']

        usd_1831 = usd['data']['1831']['quote']['USD']['price']

        url_eur = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,1027,1831,2,1720,1376,1321,131'

        parameters_eur = {
            'convert': 'EUR'
        }

        eur =  requests.get(url_eur, headers=headers, params=parameters_eur)
        eur = eur.json()

        eur_1 = eur['data']['1']['quote']['EUR']['price']

        eur_2 = eur['data']['2']['quote']['EUR']['price']

        eur_131 = eur['data']['131']['quote']['EUR']['price']

        eur_1027 = eur['data']['1027']['quote']['EUR']['price']

        eur_1321 = eur['data']['1321']['quote']['EUR']['price']

        eur_1376 = eur['data']['1376']['quote']['EUR']['price']

        eur_1720 = eur['data']['1720']['quote']['EUR']['price']

        eur_1831 = eur['data']['1831']['quote']['EUR']['price']

        url_rub = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,1027,1831,2,1720,1376,1321,131'

        parameters_rub = {
            'convert': 'RUB'
        }

        rub = requests.get(url_rub, headers=headers, params=parameters_rub)
        rub = rub.json()

        rub_1 = rub['data']['1']['quote']['RUB']['price']

        rub_2 = rub['data']['2']['quote']['RUB']['price']

        rub_131 = rub['data']['131']['quote']['RUB']['price']

        rub_1027 = rub['data']['1027']['quote']['RUB']['price']

        rub_1321 = rub['data']['1321']['quote']['RUB']['price']

        rub_1376 = rub['data']['1376']['quote']['RUB']['price']

        rub_1720 = rub['data']['1720']['quote']['RUB']['price']

        rub_1831 = rub['data']['1831']['quote']['RUB']['price']

        url_cny = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,1027,1831,2,1720,1376,1321,131'

        parameters_cny = {
            'convert': 'CNY'
        }

        cny = requests.get(url_cny, headers=headers, params=parameters_cny)
        cny = cny.json()

        cny_1 = cny['data']['1']['quote']['CNY']['price']

        cny_2 = cny['data']['2']['quote']['CNY']['price']

        cny_131 = cny['data']['131']['quote']['CNY']['price']

        cny_1027 = cny['data']['1027']['quote']['CNY']['price']

        cny_1321 = cny['data']['1321']['quote']['CNY']['price']

        cny_1376 = cny['data']['1376']['quote']['CNY']['price']

        cny_1720 = cny['data']['1720']['quote']['CNY']['price']

        cny_1831 = cny['data']['1831']['quote']['CNY']['price']



        with self.connection:

            sql_1 = f"""UPDATE crypto SET 
             RUB = {rub_1} ,
             USD = {usd_1},
             EUR = {eur_1},
             CNY = {cny_1}
             WHERE coin_id = 1"""

            sql_2 = f"""UPDATE crypto SET 
             RUB = {rub_2} ,
             USD = {usd_2},
             EUR = {eur_2},
             CNY = {cny_2}
             WHERE coin_id = 2"""

            sql_131 = f"""UPDATE crypto SET 
             RUB = {rub_131} ,
             USD = {usd_131},
             EUR = {eur_131},
             CNY = {cny_131}
             WHERE coin_id = 131"""

            sql_1027 = f"""UPDATE crypto SET 
             RUB = {rub_1027} ,
             USD = {usd_1027},
             EUR = {eur_1027},
             CNY = {cny_1027}
             WHERE coin_id = 1027"""

            sql_1321 = f"""UPDATE crypto SET 
             RUB = {rub_1321} ,
             USD = {usd_1321},
             EUR = {eur_1321},
             CNY = {cny_1321}
             WHERE coin_id = 1321"""

            sql_1376 = f"""UPDATE crypto SET 
             RUB = {rub_1376} ,
             USD = {usd_1376},
             EUR = {eur_1376},
             CNY = {cny_1376}
             WHERE coin_id = 1376"""

            sql_1720 = f"""UPDATE crypto SET 
             RUB = {rub_1720} ,
             USD = {usd_1720},
             EUR = {eur_1720},
             CNY = {cny_1720}
             WHERE coin_id = 1720"""

            sql_1831 = f"""UPDATE crypto SET 
             RUB = {rub_1831} ,
             USD = {usd_1831},
             EUR = {eur_1831},
             CNY = {cny_1831}
             WHERE coin_id = 1831"""

            return self.cursor.execute(sql_1) ,self.cursor.execute(sql_2) , self.cursor.execute(sql_131) ,self.cursor.execute(sql_1027)  ,self.cursor.execute(sql_1321) ,self.cursor.execute(sql_1376) ,self.cursor.execute(sql_1720) ,self.cursor.execute(sql_1831) 
    

    def get_courses(self , fiat):

        with self.connection:

            sql = f'SELECT {fiat} FROM `crypto`'

            return self.cursor.execute(sql).fetchall()
       