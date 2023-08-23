from CompanyNode import CompanyNode
import copy


class CompanyTree:
    def __init__(self, root=None):
        if root is None:
            self.__root = None
        if isinstance(root, CompanyNode):
            if root.get_parent() is None:
                self.__root = root
            else:
                raise ValueError("its not root")
        else:
            raise ValueError("its not CompanyNode")

    def set_root(self, root):
        if root is None:
            self.__root = None
            return None
        if isinstance(root, CompanyNode):
            if root.__parent is not None:
                return False
            else:
                self.__root = root
                return True
        else:
            return False

    def get_root(self):
        return copy.deepcopy(self.__root)

    def __str__(self):
        str = ""
        if self.__root is None:
            return str
        q = [self.__root]
        while q:
            count = len(q)
            while count > 0:
                for j in range(len(q)):
                    temp = q.pop(0)
                    str += temp.__str__() + " * "
                    for i in range(len(temp.get_children())):
                        q.append(temp.get_children()[i])
                    count -= 1
                str = str[:-3]
                str += "\n"
        return str[:-1]

    def __iter__(self):
        temp = self.__root.q()
        return iter(temp)

    def __next__(self):
        pass

    def insert_node(self, node):
        if self.__root is None:
            self.__root=node
        if isinstance(node, CompanyNode):
            if node.get_parent() is None:
                if node.test_node_order_validity():
                   for i in self:
                       if i.name == node.name:
                           return False
                   return self.__root.insert_rec(node)
        return False

        if isinstance(node, CompanyNode):
            if node.get_parent() is None:
                if node.test_node_order_validity():
                   for i in self:
                       if i.name == node.name:
                           return False
                   return self.__root.insert_rec(node)
        return False

    def remove_node(self, name):
        return self.__root.remove_rec(name)
