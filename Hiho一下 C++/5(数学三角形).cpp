//http://hihocoder.com/problemset/problem/1037
#include <bits/stdc++.h>
#define REP(i,x,n) for(int i=x;i<=n;i++)
#define DEP(i,n,x) for(int i=n;i>=x;i--)
#define mem(a,x) memset(a,x,sizeof(a))
using namespace std;

const int N = 205;

int a[N][N];
int dp[N][N];
int main(){
    int n;cin >> n;
    REP(i,1,n) REP(j,1,i) cin >> a[i][j];
    REP(i,1,n) REP(j,1,i) dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + a[i][j];
    int ans=0; REP(i,1,n) ans = max(ans,dp[n][i]);
    cout << ans << endl;
    return 0;
}
