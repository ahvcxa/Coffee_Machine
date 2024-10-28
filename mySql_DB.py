import mysql.connector

class MySqlDb:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tor',
            port='3306',
            database='CoffeeMachine'
        )
        self.myCursor = self.mydb.cursor()

    def update_execute_negative(self,what, amount,where='resources'):

        self.myCursor.execute(f'UPDATE {where} SET {what} = {what} - {amount}')
        self.mydb.commit()

    def update_execute_positive(self, what, amount, where='resources'):

        self.myCursor.execute(f'UPDATE {where} SET {what} = {what} + {amount}')
        self.mydb.commit()

    def select_execute(self,where):
        self.myCursor.execute(f'SELECT * FROM {where}')

    def fetchall(self):
        return self.myCursor.fetchall()



    def close_cursor(self):
        self.myCursor.close()
        self.mydb.close()

