from mySql_DB import MySqlDb

class CoffeeMaker:

    def __init__(self):

        db = MySqlDb()
        db.select_execute('resources')
        resources = db.fetchall()
        self.resources = {
            'water': resources[0][0],
            'milk': resources[0][1],
            'coffee': resources[0][2]
        }
        db.close_cursor()

    @staticmethod
    def report():
        db = MySqlDb()
        db.select_execute('resources')
        resources = db.fetchall()

        print(f'💧Water {resources[0][0]} ml')
        print(f'🥛Milk {resources[0][1]} ml')
        print(f'🫘Coffee {resources[0][2]} g')

        db.close_cursor()

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:

            if drink.ingredients[item] > self.resources[item]:
                print(f'Sorry, there is not enough {item}.')
                can_make = False


        return can_make


    def make_coffee(self,order):
        db = MySqlDb()
        for item in order.ingredients:
            db.update_execute_negative(item, order.ingredients[item])
            self.resources[item]-=order.ingredients[item]
        db.close_cursor()

        print(f'Here is your {order.name}☕️. Enjoy!')
        input('Enter the continue...\n\n\n\n\n')
