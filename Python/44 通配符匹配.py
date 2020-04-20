#超时了 记忆法+递归 然后 超时了QAQ
# 大佬的动态规划
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub("\*+","*",p)#去除重复的*
        a = max(len(s),len(p))
        if s == "" and (p == "" or p == "*"):
            return True
        self.dp = [[True for i in range(a)] for i in range(a)]
        return self.isMatch_part(s,p,0,0)

    def isMatch_part(self, s: str, p: str,itor_s,itor_p):
        while itor_s < len(s) and itor_p < len(p):
            if p[itor_p] == "*":
                if self.dp[itor_p][itor_s]:
                    for i in range(itor_s,len(s)+1):
                        if self.isMatch_part(s,p,i,itor_p+1):
                            return True
                        else:
                            self.dp[itor_p][itor_s] = False
                    return False
                else:
                    return False
            elif p[itor_p] == "?":
                pass
            else:
                if p[itor_p] != s[itor_s]:
                    return False
            itor_s += 1
            itor_p += 1
        if itor_s == len(s) and itor_p == len(p):
            return True
        elif itor_s == len(s) and p[-1]=="*" and itor_p == len(p)-1:
            return True
        else:
            return False

s = Solution()
print(s.isMatch("ho","ho**"))