

from typing import NoReturn


class Item():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node():
    def __init__(self, item):
        self.element_list = [item.key]
        self.node_list = [item]
    # ---- print ----

    def _PrintNode(self):
        # for i in self.element_list:
        #     print(i)
        return self.element_list
    # ---- print ----

    def _InsertNode(self, item):
        pass


class b_tree():
    def __init__(self):
        self.root = None
        self.left_node = None
        self.right_node = None

    # ---- print ----

    def _PrintRoot(self):
        s = "-"*5
        print(s, self.root.key, s)

    def _PrintLeftNode(self):
        if self.left_node is None:
            print("-"*5, "left empty", "-"*5)
        else:
            print("-"*5, self.left_node._PrintNode(), "-"*5)

    def _PrintRightNode(self):
        if self.right_node is None:
            print("-"*5, "right empty", "-"*5)
        else:
            print("-"*5, self.right_node._PrintNode(), "-"*5)

    def _PrintTree(self):
        self._PrintRoot()
        self._PrintLeftNode()
        self._PrintRightNode()
    # ----------------------

    def _InsetRootItem(self, item_key, item_value="temp"):
        if self.root != None:
            if self.root.key > item_key:
                self.left_node = self._InsertNodeItem(
                    self.left_node, item_key, item_value)
            else:
                self.right_node = self._InsertNodeItem(
                    self.right_node, item_key, item_value)
        else:
            self.root = Item(item_key, item_value)

    def _InsertNodeItem(self, select_node, item_key, item_value):
        if select_node is None:
            return Node(Item(item_key, item_value))
        else:
            # if select_node.key
            pass

    def _InsertLeftNode(self):
        if self.left_node is None:
            pass
        pass

    def _InsertRightNode(self):
        """
        docstring
        """
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
    b._InsetRootItem(l[0])
    b._InsetRootItem(l[1])
    b._PrintTree()

    print("-"*5, 1, "-"*5)
