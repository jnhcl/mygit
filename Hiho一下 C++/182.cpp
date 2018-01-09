#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;map<string,int>purchase;
    for(int i=0;i<n;i++){
        set<string>filt;
        int m;cin>>m;
        string id,date,price;
        for(int j=0;j<m;j++){
            cin>>id>>date>>price;
            filt.insert(id+price);
        }
        for(auto& it : filt){
            purchase[it]++;
        }
    }
    for(auto& it : purchase){
        if(it.second==n)
            cout<<it.first.substr(0,9)<<endl;
    }
    return 0;
}
