import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name:str):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name.lower() not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__number_items += 1
                self.__name_items.append(name.lower())
        except ValueError as e:
            print(e)
        except NameError as e:
            print(e)

    def delete_item_from_check(self, name:str):
        try:    
            if name.lower() not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name.lower())
                self.__number_items -= 1
        except NameError as e:
            print(e)

    def check_amount(self):
        total = []
        for i in range(self.__number_items):
            total.append(self.__item_price[self.__name_items[i]])
        total = sum(total)
        if self.__number_items > 10:
            total -= (total * 10) / 100
        return total
        
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []   
        total = []
        tax = 0
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)
        for i in twenty_percent_tax:
            total.append(self.__item_price[i])
        for i in total:
            tax += i * 0.2
        return tax

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []   
        total = []
        tax = 0
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)
        for i in ten_percent_tax:
            total.append(self.__item_price[i])
        for i in total:
            tax += i * 0.1
        return tax

    def total_tax(self):
        total_sum = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_sum

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if type(telephone_number) is not int:
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
        except ValueError as e:
            return e
        return f'+7{telephone_number}'
    
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = []