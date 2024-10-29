from mySql_DB import MySqlDb



class MoneyMachine:
    CURRENCY = '$'

    COIN_VALUES = {
        'dollar': 1.00,
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }

    def __init__(self):
        db = MySqlDb()
        db.select_execute('profit')
        profit = db.fetchall()
        self.profit = profit[0][0]
        self.money_received = 0
        db.close_cursor()

    def report(self):
        db = MySqlDb()
        db.select_execute('profit')
        profit = db.fetchall()
        print(f'💵Money: {self.CURRENCY}{profit[0][0]}')

    def process_coins(self):

        print('\nPlease insert coins.')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f'How many {coin}?:')) * self.COIN_VALUES[coin]
            if input('Do you continue to add money ?(y/n) :')=='n':
                break

        return self.money_received




    def make_payment(self, cost):
        db = MySqlDb()
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f'\nHere is {self.CURRENCY}{change} in change.')
            db.update_execute_positive('money', cost, 'profit')
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money.Money refunded. ")
            self.money_received = 0
            return False
