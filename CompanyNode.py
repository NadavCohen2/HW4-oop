from Company import Company
import copy


class CompanyNode(Company):
    def __init__(self, name, stocks_num, stock_price, comp_type):
        super().__init__(name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return copy.deepcopy(self.__parent)

    def get_children(self):
        return copy.deepcopy(self.__children)

    def is_leaf(self):
        if len(self.__children) == 0:
            return True
        return False

    def add_child(self, child):
        if isinstance(child, Company):
            if super()._comparison_type == "total sum":
                child_companys_market_cup = child.stocks_num * child.stock_price
                for i in self.__children:
                    child_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                if child_companys_market_cup <= self.stock_price * self.stocks_num:
                    self.__children.append(child)
                    return True
            else:
                if self >= child:
                    self.__children.append(child)
                    child.__parent = self
                    return True
        return False

    def total_net_worth(self):
        sum1 = self.stock_price * self.stocks_num
        return CompanyNode.rec_total_net_worth(self, sum1)

    @staticmethod
    def rec_total_net_worth(comNode, sum1=0):
        if len(comNode.__children) == 0:
            return sum1
        for i in range(len(comNode.__children)):
            sum1 += comNode.__children[i].stock_price * comNode.__children[i].stocks_num
            sum1 = comNode.rec_total_net_worth(comNode.__children[i], sum1)
        return sum1

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type != "total sum":
            return super().change_comparison_type(comparison_type)
        else:
            cls._comparison_type = "total sum"
            return True

    def test_node_order_validity(self):
        if self.__parent is not None:
            if self > self.__parent:
                return False
        elif self.__children != []:
            count_stocks_num = 0
            count_stock_price = 0
            for i in range(len(self.__children)):
                if self < self.__children[i]:
                    return False
        return True

    def __len__(self):
        return len(self.__children)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        str = "[" + super().__repr__() + ", "
        if self.__children == []:
            str += "[]]"
            return str
        for i in range(len(self.__children)):
            str += "[" + self.__children[i].__repr__() + "]"
        return str + "]"

    def is_ancestor(self, other):
        while other is not None:
            if self is other:
                return True
            else:
                other = other.__parent
        return False

    def __add__(self, other):
        if other.is_ancestor(self):
            raise ValueError("he is ancestor")
        the_market_cap = self.stocks_num * self.stock_price + other.stocks_num * other.stock_price
        new_stock_num = self.stocks_num + other.stocks_num
        new_stock_price = the_market_cap / new_stock_num
        temp = CompanyNode(self.name, new_stock_num, new_stock_price, self.comp_type)
        temp.__parent = copy.deepcopy(self.__parent)
        if self.is_ancestor(other):
            p = other.__parent
            p.__children.remove(other)
        if self.__children == []:
            temp.__children = copy.deepcopy(other.__children)
        elif other.__children == []:
            temp.__children = copy.deepcopy(self.__children)
        else:
            temp.__children = copy.deepcopy(self.__children)
            for i in range(len(other.__children)):
                temp.__children.append(copy.deepcopy(other.__children[i]))

        if temp.test_node_order_validity():
            return temp
        else:
            raise ValueError("not valid")

    def __lt__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup < other_companys_market_cup
            else:
                return super().__lt__(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup > other_companys_market_cup
            else:
                return super().__gt__(other)
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup == other_companys_market_cup
            else:
                return super().__eq__(other)
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup >= other_companys_market_cup
            else:
                return super().__ge__(other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup <= other_companys_market_cup
            else:
                return super().__le__(other)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "total sum":
                self_companys_market_cup = self.stocks_num * self.stock_price
                for i in range(len(self.__children)):
                    self_companys_market_cup += self.__children[i].stocks_num * self.__children[i].stock_price
                other_companys_market_cup = other.stocks_num * other.stock_price
                for i in range(len(self.__children)):
                    other_companys_market_cup += other.__children[i].stocks_num * other.__children[i].stock_price
                return self_companys_market_cup != other_companys_market_cup
            else:
                return super().__ne__(other)
        else:
            return False

    def q(self):
        res = []
        if not self is None:
            len_self = len(self.get_children())
            if len_self % 2 == 0:
                for i in range(len_self // 2):
                    res += self.get_children()[i].q()
                res.append(self)
                for i in range(len_self // 2):
                    res += self.get_children()[len(self.get_children()) // 2 + i].q()
            else:
                for i in range(len_self // 2 + 1):
                    res += self.get_children()[i].q()
                res.append(self)
                for i in range(len_self // 2 - 1):
                    res += self.get_children()[len(self.get_children()) // 2 + i + 1].q()

        return res
    def insert_rec(self,node,bool=False):
        if bool == True:
            return bool
        if not self is None:
            len_self = len(self.__children)
            if len_self % 2 == 0:
                for i in range(len_self // 2):
                    bool=self.__children[i].insert_rec(node,bool)
                    if node<self.__children[i]:
                        try:
                            self.__children[i].add_child(node)
                            return True
                        except ValueError:
                            continue
                for i in range(len_self // 2):
                    bool=self.__children[len(self.__children) // 2 + i].insert_rec(node,bool)
                    if node < self.__children[len(self.__children) // 2 + i]:
                        try:
                            self.__children[len(self.__children) // 2 + i].add_child(node)
                            return True
                        except ValueError:
                            continue
            else:
                for i in range(len_self // 2 + 1):
                    bool= self.__children[i].insert_rec(node,bool)
                    if node < self.__children[i]:
                        try:
                            self.__children[i].add_child(node)
                            return True
                        except ValueError:
                            continue
                for i in range(len_self // 2 - 1):
                    bool =self.__children[len(self.__children) // 2 + i].insert_rec(node,bool)
                    if node < self.__children[len(self.__children) // 2 + i]:
                        try:
                            self.__children[len(self.__children) // 2 + i].add_child(node)
                            return True
                        except ValueError:
                            continue
            return bool
    def remove_rec(self,name,r=None):
        if not self is None:
            len_self = len(self.__children)
            if len_self % 2 == 0:
                for i in range(len_self // 2):
                    if self.__children[i].name == name:
                        try:
                            r=self.__children[i]
                            self.__children.remove(r)
                            r.__parent = None
                            r.__children = []
                            return r
                        except ValueError:
                            continue
                    r = self.__children[i].remove_rec(name, r)

                for i in range(len_self // 2):
                    if self.__children[len(self.__children) // 2 + i].name == name:
                        try:
                           r=self.__children[len(self.__children) // 2 + i]
                           self.__children.remove(r)
                           r.__parent = None
                           r.__children = []
                           return r
                        except ValueError:
                            continue
                    r = self.__children[len(self.__children) // 2 + i].remove_rec(name, r)
            else:
                for i in range(len_self // 2 + 1):
                    if self.__children[i].name == name:
                        try:
                            r=self.__children[i]
                            self.__children.remove(r)
                            r.__parent = None
                            r.__children = []
                            return r
                        except ValueError:
                            continue
                    r = self.__children[i].remove_rec(name, r)
                for i in range(len_self // 2 - 1):
                    if self.__children[len(self.__children) // 2 + i].name == name:
                        try:
                            r = self.__children[len(self.__children) // 2 + i]
                            self.__children.remove(r)
                            r.__parent = None
                            r.__children = []
                            return r
                        except ValueError:
                            continue
                    r = self.__children[len(self.__children) // 2 + i].remove_rec(name, r)
        if r is None:
            return None
        r.__parent=None
        r.__children=[]
        return r