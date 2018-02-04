#include <iostream>
template<typename T>
class Manacher{
public:
    Manacher(){
         s=new char[1000];
         p=new int[1000];
    }
    ~Manacher(){
         delete[] s;
         delete[] p;
    }
    T min(T a,T b){return a<b?a:b;}
    void init(T a[],int n){
        s[0]='(';s[1]='#';
        int tot=1;
        for(int i=0;i<n;i++){
           s[++tot]=a[i];
           s[++tot]='#';
        }
        s[++tot]=')';
        tn=tot-1;
    }
    int manacher(T a[],int n){
        init(a,n);
        int mx=0,ans=1;id=0;
        memset(p,0,sizeof(p));
        for(int i=1;i<=tn;i++){
            if(mx>i) p[i]=min(mx-i,p[2*id-i]);
            else p[i]=1;
            while(i-p[i]>0&&s[i-p[i]]==s[i+p[i]]) p[i]++;
            if(i+p[i]>mx){
                mx=i+p[i];id=i;
            }
            if(ans<p[i]-1) ans=p[i]-1;
        }
        return ans;
    }
private:
    char *s;
    int tn;
    int *p,id;
};
