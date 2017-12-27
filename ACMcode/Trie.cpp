#include <bits/stdc++.h>
#define ll long long
#define PI acos(-1)
#define bug puts("here")
#define REP(i,x,n) for(int i=x;i<=n;i++)
#define DEP(i,n,x) for(int i=n;i>=x;i--)
#define mem(a,x) memset(a,x,sizeof(a))
using namespace std;
const int N=1e6+5;
char a[N];
const int SIGMA=30;
int pt[N][SIGMA],sz=0;
int cnt[N];
void insert(char *s){
     int p=0;
     REP(i,0,strlen(s)-1){
         int v=s[i]-'a';
         if(!pt[p][v]){
              mem(pt[sz],0);
              pt[p][v]=++sz;
              cnt[sz]=0;
         }
         p=pt[p][v];
         ++cnt[p];
     }
}
int search(char *s){
     int ans=0,p=0;
     REP(i,0,strlen(s)-1){
          int v=s[i]-'a';
          if(!pt[p][v]) return 0;
          p=pt[p][v];
     }
     return cnt[p];
}

int main(){
    int n;
    cin>>n;
    while(n--){
        scanf("%s",a);
        insert(a);
    }
    int m;
    cin>>m;
    while(m--){
        scanf("%s",a);
        printf("%d\n",search(a));
    }
    return 0;
}
