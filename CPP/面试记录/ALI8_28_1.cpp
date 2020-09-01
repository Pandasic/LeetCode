#include <iostream>

using namespace std;
int main()
{
    int len = 0;
    cin>>len;
    string a,b;
    cin>>a>>b;
    int diff = 0;
    int zerodiff = 0,onediff = 0;
    int zerosame = 0,onesame = 0;
    int res = 0;
    for(int i = 0;i<len;i++)
    {
        if(a[i] != b[i])
        {
            if(a[i] == '0')
                zerodiff++;
            if(a[i] == '1')
                onediff++;
        }
        else
        {
            if(a[i] == '0')
                zerosame++;
            if(a[i] == '1')
                onesame++;
        }
    }
    diff = onediff + zerodiff;
    int diffmax = onediff>zerodiff?onediff:zerodiff;
    int samemax = onesame>zerosame?onediff:zerodiff;
    res = diffmax<(samemax+1)?diffmax:(samemax+1);
    cout<<res;
    system("pause");
}