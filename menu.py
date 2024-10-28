from mySql_DB import MySqlDb


class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }


class Menu:

    def __init__(self):
        db = MySqlDb()
        db.select_execute('ingredients')
        menu = db.fetchall()
        self.menu = [
            MenuItem(
                name=item[0],
                water=item[1],
                milk=item[2],
                coffee=item[3],
                cost=item[4]
            ) for item in menu
        ]
        db.close_cursor()

    def get_items(self):
        options = ''
        for item in self.menu:
            options += f'\n{item.name} --> ${item.cost}'

        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item

        print('Sorry that item is not available')


