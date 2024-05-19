import requests
import csv

class MyProject:


    @staticmethod
    def tradeorge_exchange(market, balance):
        url = f"https://tradeogre.com/api/v1/ticker/{market}-USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            sell_price = float(data['bid'])
            total = sell_price * balance
            print("Price: ", sell_price) 
            print("Total: ", total)         
            return total
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")


    @staticmethod
    def xeggex_exchange(market, balance):
        url = f"https://api.xeggex.com/api/v2/market/getorderbookbysymbol/{market}_USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            sell_price = float(data['bids'][0]['price'])
            total = sell_price * balance
            print("Price: ", sell_price)
            print("Total: ", total)
            return total
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")


    @staticmethod
    def gate_exchange(market, balance):
        url = f"https://api.gateio.ws/api/v4/spot/tickers?currency_pair={market}_USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = float(data[0]['highest_bid'])
            total = price * balance
            print("Price: ", price)
            print("Total: ", total)
            return total
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")


    @staticmethod
    def mexc_exchange(market, balance):
        url = f"https://api.mexc.com/api/v3/depth?symbol={market}USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            sell_price = float(data['bids'][0][0])
            total = sell_price * balance
            print("Price: ", sell_price)
            print("Total: ", total)
            return total
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")


    @staticmethod
    def driver_code():
        total_bal = 0
        file_path = 'data.csv'
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                market = row[0]
                balance = float(row[1])
                exchange = row[-1]

                if exchange == "tradeorge":
                    print(market, exchange)
                    t1 = MyProject.tradeorge_exchange(market, balance)
                    total_bal += t1
                elif exchange == "xeggex":
                    print(market, exchange)
                    t2 = MyProject.xeggex_exchange(market, balance) 
                    total_bal += t2               
                elif exchange == "gate":
                    print(market, exchange)
                    t3 = MyProject.gate_exchange(market, balance)
                    total_bal += t3
                elif exchange == "mexc":
                    print(market, exchange)
                    t4 = MyProject.mexc_exchange(market, balance)
                    total_bal += t4
                else:
                    print(market, exchange)
                    print("Exchange Not added")
        return total_bal

bal = MyProject.driver_code()
print("Total Balance: ",bal)