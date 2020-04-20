A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"


#无向图 从A到N点 的随机移动概率
class Node:
    def __init__(self,id,val = 0):
        self.id = id
        self.LinkedNode = []
        self.addTemp = 0
        self.val = val

    #更新数值
    def update(self):
        self.val = self.addTemp
        self.addTemp = 0

    #流向其他节点
    def flow(self):
        addVal = self.val/len(self.LinkedNode)
        for node in self.LinkedNode:
            node.addTemp += addVal

def main():
    Nodes = \
    {
        A:Node(A,0),\
        B:Node(B,0),\
        C:Node(C,0),\
        D:Node(D,0),\
        E:Node(E,0),\
        F:Node(F,0),\
        G:Node(G,81*3*9*6),\
        H:Node(H,0),\
    }

    Nodes[A].LinkedNode = [Nodes[B],Nodes[D],Nodes[F]]
    Nodes[B].LinkedNode = [Nodes[A],Nodes[C],Nodes[H]]
    Nodes[C].LinkedNode = [Nodes[B],Nodes[D],Nodes[G]]
    Nodes[D].LinkedNode = [Nodes[A],Nodes[C],Nodes[E]]
    Nodes[E].LinkedNode = [Nodes[D],Nodes[F],Nodes[G]]
    Nodes[F].LinkedNode = [Nodes[A],Nodes[E],Nodes[H]]
    Nodes[G].LinkedNode = [Nodes[C],Nodes[E],Nodes[H]]
    Nodes[H].LinkedNode = [Nodes[B],Nodes[G],Nodes[F]]

    for i in range(12):
        sum = 0
        print(i+1,":",end = '')
        for node in Nodes.values():
            node.flow()
        for node in Nodes.values():
            node.update()
        for key,node in Nodes.items():
            print ("%s :%1f " % (key,node.val),end =" ")
            sum += node.val
        print("sum:",sum)

if __name__ == "__main__":
    main()