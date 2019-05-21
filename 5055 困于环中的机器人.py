class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = 0
        s = 0
        d_s = [[1,0],[0,-1],[-1,0],[0,1]]
        pos = [0,0]
        for i in range(12):
            for c in instructions:
                if c == 'L':
                    d += 1
                if c == 'R':
                    d -= 1
                d = d % 4
                if c == 'G':
                    pos = self.add_pos(pos,d_s[d])
            print(pos)
            if pos == [0,0]:
                return True
        return False

    def add_pos(self, p1,p2):
        return [p1[0]+p2[0],p1[1]+p2[1]]

s = Solution()
print(s.isRobotBounded("LLLRLLLRLLGLLGGRGLLLGGLRRRRRGLRLRLRLGGRGRGRLLLLLLGLLRLGLGLRLGGGRR"))