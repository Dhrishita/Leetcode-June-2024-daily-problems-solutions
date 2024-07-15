# Definition for a binary tree node.
from collections import defaultdict
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes={}
        children=set()
        for parent,child,isLeft in descriptions:
            if parent not in nodes:
                nodes[parent]=TreeNode(parent)
            if child not in nodes:
                nodes[child]=TreeNode(child)
                
            if isLeft:
                nodes[parent].left=nodes[child]
            else:
                nodes[parent].right=nodes[child]
            
            children.add(child)
            
        root=None
        for parent,child,isLeft in descriptions:
            if parent not in children:
                root=nodes[parent]
                break
        return root