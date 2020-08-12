#include "include.hpp"
using namespace std;
/*
题目描述
187. 重复的DNA序列
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
通过次数18,303提交次数41,042
*/
/*
思路1 Hash缓存
*/
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        set<string> temp;
        set<string> rtn;
        if(s.size()<10)
            return vector<string>();
        for(int i=0;i<s.size()-10+1;i++)
        {
            string nowStr = s.substr(i,10);
            if(temp.count(nowStr) == 0)
            {
                temp.insert(nowStr);
            }
            else
            {
                rtn.insert(nowStr);
            }
        }
        return vector<string>(rtn.begin(),rtn.end());
    }
};
/*
思路二 使用旋转哈希 每个片段对应一个数字 下一个数字的哈希值可以通过上一个哈希值计算出来*/
/*思路三 位操作
将所哟进行二进制编码 
添加末尾 1 很简单，和上面的思路一样：

左移以释放最后两位：bitmask <<= 2。
添加 1 到最后两位：bitmask |= 1。
现在的问题是删除前导 2。换句话说，问题是将 2L 位和 (2L + 1) 位设置为零。

我们可以使用一个技巧去重置第 n 位的值：bitmask &= ~(1 << n)。

这个技巧很简单：

1 << n 是设置第 n 位为 1。
~(1 << n) 是设置第 n 位为 0，且全部低位为 1。
bitmask &= ~(1 << n) 是将 bitmask 第 n 位设置为 0。
技巧的简单使用方法是先设置第 2L 位，然后再设置 (2L + 1) 位：bitmask &= ~(1 << 2 * L) & ~(1 << (2 * L + 1)。可以简化为 bitmask &= ~(3 << 2 * L)：

3 = (11)_23=(11) 
2
​	
 ，因此可以设置第 2L 位和第 (2L + 1) 位为 1。
~(3 << 2 * L) 会设置第 2L 位 和第 (2L + 1) 位为 0，且所有低位为 1。
bitmask &= ~(3 << 2 * L) 则会将 bitmask 第 2L 和第 (2L + 1) 位设置为 0。
*/
int main()
{
    Solution s;
    system("pause");
};