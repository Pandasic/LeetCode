class Solution:
    def gardenNoAdj(self, N: int, paths):
        s = [0 for i in range(N)]
        dist = [[0 for i in range(N)] for j in range(N)]
        for p in paths:
            dist[p[0] - 1][p[1] - 1] = 1
            dist[p[1] - 1][p[0] - 1] = 1

        color,area,k = 0,0,0
        s[0]=1
        area=1
        color=1
        while(area<N):
            while(color<=4):
                if(area>=N):
                    break;
                k=0
                while((k<area) and (s[k] * dist[area][k]!=color)):
                    k+=1
                if(k<area):
                    color += 1
                else:
                    s[area]=color;
                    area += 1
                    color=1
            if(color>4):
                area=area-1
                color=s[area]+1
        return s

s = Solution()
print(s.gardenNoAdj(4,[[1,2],[3,4]]))

