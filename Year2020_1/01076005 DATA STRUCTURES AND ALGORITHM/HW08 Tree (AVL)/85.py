class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2, h + 1) - 1
            current = self.root
            if self.num + 1 > max_node:
                while current.left is not None:
                    current = current.left
                current.left = Node(val)
                self.num += 1
            elif self.num + 1 == max_node:
                while current.right is not None:
                    current = current.right
                current.right = Node(val)
                self.num += 1
            else:
                # print(max_node - ((max_node - (pow(2, h) - 1)) / 2))
                if self.num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
                    insert_subtree(current.left, self.num -
                                   round(pow(2, h) / 2), val)
                else:
                    insert_subtree(current.right, self.num - pow(2, h), val)
                self.num += 1


def insert_subtree(r, num, val):
    if r is not None:
        h = height(r)
        max_node = pow(2, h + 1) - 1
        current = r
        if num + 1 > max_node:
            while current.left is not None:
                current = current.left
            current.left = Node(val)
            return
        elif num + 1 == max_node:
            while current.right is not None:
                current = current.right
            current.right = Node(val)
            return
        if num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
            insert_subtree(current.left, num - round(pow(2, h) / 2), val)
        else:
            insert_subtree(current.right, num - pow(2, h), val)
    else:
        return


def height(root):
    if root is None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print('     ' * level, node)
        print_tree(node.left, level + 1)


exp = ''


def check_binary_search_tree(root):
    def inorder(node):
        global exp
        if node is not None:
            inorder(node.left)
            exp += str(node) + ' '
            inorder(node.right)
    inorder(root)
    lst = list(map(int, exp.split()))
    if min(lst) < 0 or max(lst) > 100:
        return False
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    return True


if __name__ == '__main__':
    tree = Tree()
    data = input("Enter Input : ").split()
    for e in data:
        tree.insert(int(e))
    print_tree(tree.root)
    print(check_binary_search_tree(tree.root))