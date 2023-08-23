class Company:
    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):

        if Company.valid_name(name):
            self.name = name
        else:
            raise ValueError("its not valid name")
        if Company.valid_stocks_num(stocks_num):
            self.stocks_num = stocks_num
        else:
            raise ValueError("its not valid stocks_num")
        if Company.valid_stock_price(stock_price):
            self.stock_price = stock_price
        else:
            raise ValueError("its not valid stock_price")
        if Company.valid_name(comp_type):
            self.comp_type = comp_type
        else:
            raise ValueError("its not valid comp_type")

    def net_worth(self):
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        if Company.valid_name(name):
            self.name = name
            return True
        else:
            return False

    def set_stocks_num(self, stocks_num):
        if Company.valid_stocks_num(stocks_num):
            companys_market_cup = self.stocks_num * self.stock_price
            self.stocks_num = stocks_num
            self.stock_price = companys_market_cup / stocks_num
            return True
        else:
            return False

    def set_stock_price(self, stock_price):
        if Company.valid_stock_price(stock_price):
            old_companys_market_cup = self.stocks_num * self.stock_price
            if stock_price > old_companys_market_cup:
                return False
            else:
                self.stocks_num = int(old_companys_market_cup // stock_price)
                self.stock_price = stock_price
                return True
        return False

    def set_comp_type(self, comp_type):
        if Company.valid_name(comp_type):
            self.comp_type = comp_type
            return True
        else:
            return False

    def update_net_worth(self, net_worth):
        if Company.valid_stock_price(net_worth):
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        new_stocks = self.stocks_num + number
        if Company.valid_stocks_num(new_stocks):
            self.stocks_num = new_stocks
            return True
        else:
            return False

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type == "net value":
            cls._comparison_type = "net value"
            return True
        elif comparison_type == "stock num":
            cls._comparison_type = "stock num"
            return True
        elif comparison_type == "stock price":
            cls._comparison_type = "stock price"
            return True
        return False

    def __str__(self):
        return "(" + str(self.name) + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " + str(self.comp_type) + ", Net Worth: " + str(self.stock_price * self.stocks_num) + ")"

    def __repr__(self):
        return "(" + str(self.name) + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " + str(self.comp_type) + ", Net Worth: " + str(self.stock_price * self.stocks_num) + ")"

    def __lt__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price < other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num < other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price < other.stock_price:
                    return True
        return False

    def __gt__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price > other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num > other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price > other.stock_price:
                    return True
        return False

    def __eq__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price == other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num == other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price == other.stock_price:
                    return True
        return False

    def __ge__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price >= other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num >= other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price >= other.stock_price:
                    return True
        return False

    def __le__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price <= other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num <= other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price <= other.stock_price:
                    return True
        return False

    def __ne__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                if self.stocks_num * self.stock_price != other.stocks_num * other.stock_price:
                    return True
            elif self._comparison_type == "stock num":
                if self.stocks_num != other.stocks_num:
                    return True
            elif self._comparison_type == "stock price":
                if self.stock_price != other.stock_price:
                    return True
        return False

    def __add__(self, other):
        the_market_cap = self.stocks_num * self.stock_price + other.stocks_num * other.stock_price
        new_stock_num = self.stocks_num + other.stocks_num
        new_stock_price = the_market_cap / new_stock_num
        return Company(self.name, new_stock_num, new_stock_price, self.comp_type)

    @staticmethod
    def valid_name(name):
        if type(name) is not str:
            return False
        if not name[0].isupper():
            return False
        elif len(name) < 1:
            return False
        for i in range(len(name)):
            if ord(name[i].upper()) != 32:
                if 65 > ord(name[i].upper()) or ord(name[i].upper()) > 90:
                    return False
            else:
                if name[i] == " ":
                    if name[i - 1] == name[i]:
                        return False
        return True

    @staticmethod
    def valid_stocks_num(stocks_num):
        if type(stocks_num) is int:
            if stocks_num > 0:
                return True
        return False

    @staticmethod
    def valid_stock_price(stock_price):
        if type(stock_price) is int or type(stock_price) is float:
            if stock_price > 0:
                return True
        return False
