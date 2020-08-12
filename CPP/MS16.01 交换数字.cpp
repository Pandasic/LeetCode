#include "include.hpp"
using namespace std;
/*
面试题 16.01. 交换数字
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：

输入: numbers = [1,2]
输出: [2,1]
提示：

numbers.length == 2
通过次数7,529提交次数9,116
*/

class Solution {
public:
    vector<int> swapNumbers(vector<int>& numbers) {
        swap(numbers[0],numbers[1]);
        return numbers;
    }
};
/*或运算中自身对自身异或等于0，自身对0异或等于自身*/
class Solution {
public:
    vector<int> swapNumbers(vector<int>& numbers) {
        numbers[0]=numbers[0]^numbers[1];
        numbers[1]=numbers[0]^numbers[1];
        numbers[0]=numbers[0]^numbers[1];
        return numbers;
        return numbers;
    }
};

int main()
{
    Solution s;
    system("pause");
};