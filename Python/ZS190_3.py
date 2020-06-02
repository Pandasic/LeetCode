class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.res = 0
        if root == None :
            return

        def part(root,path):
            if root == None:
                return
            if root.left == None and root.right == None:
                path = path + [root.val]
                #print(path)
                if len(path) == 1:
                    self.res += 1
                    return
                    
                m = {}
                for p in path:
                    if p not in m:
                        m[p] = 0
                    m[p] += 1
                singleCount = 0
                for v in m.values():
                    if v%2 == 1:
                        singleCount += 1
                if singleCount <= 1:
                    self.res += 1
            else:
                part(root.left ,path + [root.val])
                part(root.right,path + [root.val])
        part(root,[])
        return self.res