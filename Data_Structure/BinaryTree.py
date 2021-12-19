import random


def BT():
    class BTNode:
        def __init__(self, val=None):
            self.left = None
            self.right = None
            self.val = val

        def insertNode(self, val):
            if not self.val:
                self.val = val
                return

            if self.left or self.right:
                if self.left:
                    self.left.insertNode(val)

                if self.right:
                    self.right.insertNode(val)

            elif not self.left or not self.right:
                if not self.left:
                    self.left = BTNode(val)
                    return

                if not self.right:
                    self.right = BTNode(val)
                    return

        def inorder(self, vals):
            if self.left is not None:
                self.left.inorder(vals)
            if self.val is not None:
                vals.append(self.val)
            if self.right is not None:
                self.right.inorder(vals)
            return vals

        def postorder(self, vals):
            if self.left is not None:
                self.left.postorder(vals)
            if self.right is not None:
                self.right.postorder(vals)
            if self.val is not None:
                vals.append(self.val)
            return vals

        def preorder(self, vals):
            if self.val is not None:
                vals.append(self.val)
            if self.left is not None:
                self.left.preorder(vals)
            if self.right is not None:
                self.right.preorder(vals)
            return vals

    bt = BTNode()
    for i in range(10):
        bt.insertNode(random.randrange(1, 100, 1))

    print("inorder:")
    print(bt.inorder([]))
    print("#")

    print("postorder:")
    print(bt.postorder([]))
    print("#")

    print("inorder:")
    print(bt.inorder([]))
    print("#")

BT()
