#include <iostream>

using namespace std;

#define M 5

int main()
{
    int N = 0;
    int res = 0;
    int growing[M] = {1,0,0,0,0};
    cin >> N;
    for (int i = 0;i < N ;i++)
    {
        int readyGrow = growing[4];
        for(int j = M-2 ;j > -1 ; j--)
        {
            growing[j + 1] = growing[j];
        }
        
        res += readyGrow;
        growing[0] = res;

        cout <<"Month"<<i + 1<<" :";
        
        for(int j = 0;j< M; j++)
        {
            cout<<growing[j]<<" ";
        }

        cout << "Growed: "<<res;
        cout<<endl;
    }
    for(int j = 0;j < 5 ; j++)
    {
        res += growing[j];
    }
    cout<<res<<endl;
    cin>>N;
}