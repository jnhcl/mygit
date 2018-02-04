//http://hihocoder.com/problemset/problem/1044
/*
״ѹDP��
    ��dp(i,j)��ʾ����(1->i)��jΪѡ��������������
    ��Ϊ��m��������λ�ã�����ֻ��Ҫ����i-m��i��״̬
    max m = 20 �� �� 1 << 20 = 1024 * 1024
    �ɼ�״̬���� ��״ѹ����

*/
#include <bits/stdc++.h>
#define REP(i,x,n) for(int i=x;i<=n;i++)
#define DEP(i,n,x) for(int i=n;i>=x;i--)
#define mem(a,x) memset(a,x,sizeof(a))
#define ll long long
using namespace std;

const int N = 1005;

ll dp[2][1<<10],a[N];

int count_1(int x){
    int ret = 0;
    while(x > 0){
        ret++; x -= x&-x;
    }
    return ret;
}

int main(){
#ifndef ONLINE_JUDGE
      freopen("in.txt","r",stdin);
#endif // ONLINE_JUDGE
   int n,m,q;
   cin >> n >> m >> q;
   mem(dp,0);
   REP(i,1,n) cin >> a[i];
   REP(i,1,n) REP(j,0,(1<<m)-1){
       if(count_1(j)>q) continue;
       int c = i&1;
       if(count_1(j>>1)==q)
           dp[c][j] = dp[1-c][j>>1];
       else
           dp[c][j] = max(dp[1-c][j>>1],dp[1-c][j>>1|1<<(m-1)]);
       if(j&1) dp[c][j] += a[i];
   }
   cout << *max_element(dp[n&1],dp[n&1]+(1<<m)-1) << endl;
   return 0;
}
