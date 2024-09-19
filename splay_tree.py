# Splay tree and its transformations - search, insert and delete


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        # Key lies in left subtree
        if key < root.key:
            if root.left is None:
                return root

            # Zig-Zig (Left Left)
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)

            # Zig-Zag (Left Right)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)

            return root if root.left is None else self._right_rotate(root)

        # Key lies in right subtree
        else:
            if root.right is None:
                return root

            # Zag-Zig (Right Left)
            if key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)

            # Zag-Zag (Right Right)
            elif key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)

            return root if root.right is None else self._left_rotate(root)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._splay(self.root, key)

        if self.root.key == key:
            return

        new_node = Node(key)

        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def delete(self, key):
        if self.root is None:
            return

        self.root = self._splay(self.root, key)

        if self.root.key != key:
            return

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self._splay(self.root.left, key)
            self.root.right = temp

    def pre_order(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)


# Example usage
if __name__ == "__main__":
    tree = SplayTree()

    # Insertion
    tree.insert(100)
    tree.insert(50)
    tree.insert(200)
    tree.insert(40)
    tree.insert(60)
    tree.insert(150)

    print("Pre-order traversal after insertion:")
    tree.pre_order(tree.root)
    print()

    # Searching
    print("Search for 60:", tree.search(60))  # Splay 60 to root
    print("Pre-order traversal after search:")
    tree.pre_order(tree.root)
    print()

    # Deletion
    tree.delete(50)
    print("Pre-order traversal after deleting 50:")
    tree.pre_order(tree.root)
