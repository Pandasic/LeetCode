#include "include.hpp"
using namespace std;
/*
题目描述
*/

class Solution {
    public:
    int peakIndexInMountainArray(vector<int>& A) {
        int i = 0;
        while (A[i]<A[i+1])
        {
            i++
        }
        return i;
    }
}

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int lo = 0, hi = A.size() - 1;
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (A[mi] < A[mi + 1])
                lo = mi + 1;
            else
                hi = mi;
        }
        return lo;
    }
};

int main()
{
    Solution s;
    system("pause");
};