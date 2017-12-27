#include <bits/stdc++.h>
#define ll long long
#define PI acos(-1)
#define bug puts("here")
#define REP(i,x,n) for(int i=x;i<=n;i++)
#define DEP(i,n,x) for(int i=n;i>=x;i--)
#define mem(a,x) memset(a,x,sizeof(a))
using namespace std;
const int N=1e6+5;
char a[N],b[N];
int f[N];
void getFail(){
    int j=0,n=strlen(b);
    f[0]=f[1]=0;
    REP(i,1,n-1){
        while(j>0&&b[i]!=b[j]) j=f[j];
        if(b[i]==b[j]) j++;
        f[i+1]=j;
    }
}
int kmp_count(){
    int j=0,n=strlen(a),m=strlen(b);
    int cnt=0;
    REP(i,0,n-1){
        while(j>0&&a[i]!=b[j]) j=f[j];
        if(a[i]==b[j]) j++;
        if(j==m){
            cnt++;
            j=f[j];
        }
    }
    return cnt;
}
int main(){
    int n;
    cin>>n;
    while(n--){
        scanf("%s",b);
        scanf("%s",a);
        getFail();
        cout<<kmp_count()<<endl;
    }
    return 0;
}
