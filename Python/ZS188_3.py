class Solution1:
    def minTime(self, n: int, edges, hasApple) -> int:
        tree = {}
        for e in edges:
            tree[e[1]] = e[0]

        print(tree)
        v = [-1 for n in range(len(hasApple))]
        v[0] = 0
        for i in range(len(hasApple)):
            if (hasApple[i]):
                v[i] = 0

        while(max(v[1:]) != -1):
            for i in range(1,len(v)):
                if v[i] != -1:
                    if v[tree[i]] == -1:
                        v[tree[i]] = 0
                    v[tree[i]] += v[i] + 2
                    v[i] = -1
        print(v)
        return v[0]

class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        self.pathVal = None
        self.father = None

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        #构建树
        root = TreeNode(0)
        queue = []
        queue.append(root)
        while len(queue) != 0:
            nowNode = queue.pop(0)
            if hasApple[nowNode.val]:
                nowNode.pathVal = 0
            for e in edges:
                if e[0] == nowNode.val:
                    if nowNode.left == None:
                        nowNode.left = TreeNode(e[1])
                        nowNode.left.father = nowNode
                        queue.append(nowNode.left)
                    elif nowNode.right == None:
                        nowNode.right = TreeNode(e[1])
                        nowNode.right.father = nowNode
                        queue.append(nowNode.right)
        
        def LRD(node):
            if not node:
                return 
            LRD(node.left)
            LRD(node.right)
            if node.father == None:
                return
            if node.pathVal != None:
                if node.father.pathVal == None:
                    node.father.pathVal = 0
                node.father.pathVal += node.pathVal +2

        LRD(root)
        if root.pathVal == None:
            return 0
        else:
            return root.pathVal
            

        

s =Solution()
print(s.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
                    
