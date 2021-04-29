

from _typeshed import NoneType


class Item():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class b_tree(object):
    def __init__(self):
        self.root = None
        self.node = None

    def __inset_item(self, Item):
        if self.root != None:
            pass
        else:
            self.root = Item


if __name__ == "__main__":

    max_node = 5  # m = 5

    l = list(range(10))
    print(l)
