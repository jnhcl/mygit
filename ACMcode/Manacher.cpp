#include <bits/stdc++.h>
#include "manacher.h"
using namespace std;

//test
int main(){
    char a[100];
    Manacher<char> ac;
    while(cin>>a){
        cout<<ac.manacher(a,int(strlen(a)))<<endl;
    }
    return 0;
}
