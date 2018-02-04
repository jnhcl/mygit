# include <bits/stdc++.h>
using namespace std;

int dfs(TreeNode *root,int k){
     map<int,int>vis;
     int ans = 0;key = k;
     check(root,0,0,vis,ans);
     return ans;
}
