//http://hihocoder.com/problemset/problem/1043
#include <bits/stdc++.h>
#define REP(i,x,n) for(int i=x;i<=n;i++)
#define DEP(i,n,x) for(int i=n;i>=x;i--)
#define mem(a,x) memset(a,x,sizeof(a))
#define ll long long
using namespace std;

const int N = 1e5 + 5;

ll sum[N],a[N][2];

int main(){
   int n,val;
   cin >> n >> val; mem(sum,0);
   REP(i,1,n) cin >> a[i][0] >> a[i][1];
   REP(i,1,n) REP(j,0,val) if(j >= a[i][0])
        sum[j] = max(sum[j],sum[j-a[i][0]] + a[i][1]);
   cout << *max_element(sum,sum + val +1) << endl;
   return 0;
}
