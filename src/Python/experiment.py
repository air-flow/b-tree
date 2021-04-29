

class Item():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node():
    def __init__(self, item):
        self.element_list = [item.key]
        self.node_list = [item]

    def __insert_node(self, item):
        pass


class b_tree():
    def __init__(self):
        self.root = None
        self.left_node = None
        self.right_node = None

    def __inset_root_item(self, item_key, item_value="temp"):
        if self.root != None:
            pass
            # insert node func call
        else:
            self.root = Item(item_key, item_value)

    def __insert_node_item(self, select_node, item_key, item_value):
        if select_node is None:
            select_node = Node(Item(item_key, item_value))
        else:
            # if select_node.key
            pass


if __name__ == "__main__":
    #    5
    # 1 2  3 4
    max_node = 5  # m = 5

    l = list(range(1, 6))
    print(l)

    b = b_tree()
    # for i in l:
    # b_tree.__inset_item(i)
    # print(b)
    b.__inset_root_item(l[0])
    
