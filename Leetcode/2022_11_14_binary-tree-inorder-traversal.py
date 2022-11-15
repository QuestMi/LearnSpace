# -*- coding: utf-8 -*- 
"""
Create on : 2022/11/14
@Author   : Xiao QingLin 
@File    : 2022_11_14_binary-tree-inorder-traversal  
"""
# 2022-11-14 二叉树（前中后）序遍历
# 二叉树遍历
# 中序遍历：https://leetcode.com/problems/binary-tree-inorder-traversal/
# # Definition for a binary tree node.
# # class TreeNode:
#     """
#     定义tree
#     """
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

"""
递归法
"""


class Solution:
    def inorderTraversal1(self, root):
        res = []

        def dfs(root, res):
            if root:
                self.dfs(root.left)
                res.append(root.val)
                self.dfs(root.right)

        dfs(root)
        return res


"""
迭代法
"""


class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


"""
颜色标记法
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        W, G = 0, 1  # 1、定义两个颜色；
        res = []  # 2、定义装结果的容器；
        stack = [(W, root)]  # 3、定义栈，并将root节点入栈；
        while stack:  # 4、遍历栈；
            color, node = stack.pop()  # 5、获取栈中元素；
            if node is None:  # 6、判断节点是否为空；
                continue
            if color == W:  # 7、判断节点是否被访问过； 否，节点入栈（右，根，左） 栈是先入后出；
                stack.append((W, node.right))
                stack.append((G, node))
                stack.append((W, node.left))
            else:  # 8、节点被访问过，直接加入到结果列表中。
                res.append(node.val)
        return res


# 前序遍历：https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        W, G = 0, 1  # 1、定义颜色；
        # 2、定义结果列表；
        res = []
        # 3、定义栈；
        stack = [(W, root)]
        # 4、遍历栈；
        while stack:
            color, node = stack.pop()
            # 5、判断节点是否存在；
            if node is None:
                continue
                # 6、判断节点是否已经访问过；否，入栈
            if color == W:
                stack.append((W, node.right))
                stack.append((W, node.left))
                stack.append((G, node))
            else:
                # 7、是，加入结果队列
                res.append(node.val)
        # 8、返回结果
        return res


# 后序遍历：https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        W, G = 0, 1  # 1、定义颜色；
        # 2、定义结果列表；
        res = []
        # 3、定义栈；
        stack = [(W, root)]
        # 4、遍历栈；
        while stack:
            color, node = stack.pop()
            # 5、判断节点是否存在；
            if node is None:
                continue
                # 6、判断节点是否已经访问过；否，入栈
            if color == W:
                stack.append((G, node))
                stack.append((W, node.right))
                stack.append((W, node.left))
            else:
                # 7、是，加入结果队列
                res.append(node.val)
        # 8、返回结果
        return res


Geek
写法


def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
