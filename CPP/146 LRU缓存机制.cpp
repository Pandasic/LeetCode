#include "include.hpp"
using namespace std;
/*
题目描述
设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
set(key, value)：将记录(key, value)插入该结构
get(key)：返回key对应的value值
[要求]
set和get方法的时间复杂度为O(1)
某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
若opt=1，接下来两个整数x, y，表示set(x, y)
若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
对于每个操作2，输出一个答案
示例1
输入
复制
[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
输出
复制
[1,-1]
说明
第一次操作后：最常使用的记录为("1", 1)
第二次操作后：最常使用的记录为("2", 2)，("1", 1)变为最不常用的
第三次操作后：最常使用的记录为("3", 2)，("1", 1)还是最不常用的
第四次操作后：最常用的记录为("1", 1)，("2", 2)变为最不常用的
第五次操作后：大小超过了3，所以移除此时最不常使用的记录("2", 2)，加入记录("4", 4)，并且为最常使用的记录，然后("3", 2)变为最不常使用的记录
备注:
1 \leq K \leq N \leq 10^51≤K≤N≤10 
5
 
-2 \times 10^9 \leq x,y \leq 2 \times 10^9−2×10 
9
 ≤x,y≤2×10 
9
*/

#include <unordered_map>

class LRUCache {
public:
    LRUCache(int capacity) {
        size = capacity;
    }
 
    int count = 0;
    int size = 0;
    int step = 1;
    unordered_map<int,int> data;
    unordered_map<int,int> time;
    
    int get(int key)
    {
        step++;

        if(time[key] != 0)
        {
            time[key] = step;
            return data[key];
        }
        else
        {
            return -1;
        }
    };
    
    void put(int key,int val)
    {
        step++;
        if(time[key] == 0)
            count += 1;
        data[key] = val;
        time[key] = step;
        if(count > size)
        {
            int rmKey = 0;
            int minTime = 99999999;
            for(auto p:time)
            {
                if(p.second != 0 && p.second < minTime)
                {
                    minTime = p.second;
                    rmKey = p.first;
                }
            }
            time[rmKey] = 0;
            count--;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
int main()
{
    Solution s;
    system("pause");
};