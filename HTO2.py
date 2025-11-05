class Books:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_children(self):
        books = self.right - self.left + 1
        if books < 3:
            self.left_child = None
            self.right_child = None
        elif books % 3 == 0:
            self.left_child = Books(self.left, self.left + books // 3 - 1)
            self.right_child = Books(self.right - books // 3 + 1, self.right)
        elif books % 3 == 1:
            self.left_child = Books(self.left, self.left + books // 3 - 1)
            self.right_child = Books(self.right - books // 3 + 1, self.right)
        else:
            self.left_child = Books(self.left, self.left + books // 3)
            self.right_child = Books(self.right - books // 3, self.right)

    def get_books(self):
        if self.right - self.left == 1:
            return self.left + self.right
        if self.right == self.left:
            return self.left
        return self.left_child.get_books() + self.right_child.get_books()


def build(node: Books):
    node.get_children()
    if node.left_child and node.right_child:
        build(node.left_child)
        build(node.right_child)


n = int(input())
root = Books(1, n)
build(root)
print(root.get_books())


