#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

set<size_t> used;
vector<int> vals(10,0);
int m = 1;
int res = 0;

void dfs(size_t n,int count)
{
    if(count == 0)
    {
        if(used.count(n) == 0 && n%m == 0) 
        {
            used.insert(n);
            res++;
        }
    }

    for(int i = 0;i<10;i++)
    {
        if(n == 0 && i == 0)
            continue;
        if(vals[i] != 0)
        {
            vals[i]--;
            dfs(n*10+i,count - 1);
            vals[i]++;
        }
    } 
}

int main()
{
    string s;
    cin>>s>>m;
    for(char c:s)
    {
        vals[c-'0'] += 1;
    }
    dfs(0,s.size());
    cout<<res;
}