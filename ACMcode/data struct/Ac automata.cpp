#include <bits/stdc++.h>
using namespace std;
const int SIGMA = 26;
const int N = 1e6+5;
class ac_automata
{
public:
    ac_automata()
    {
        root = new node();
        for(int i=0; i<26; i++)
        {
            root->next[i] = NULL;
        }
        root->fail = NULL;
        root->cnt = 0;
    }
    struct node
    {
        node *next[SIGMA];
        node *fail;
        int cnt;
    };
    void insert_str(char *s)
    {
        int n=strlen(s),c;
        node *p=root;
        for(int i=0; i<n; i++)
        {
            c = s[i]-'a';
            if(p->next[c]==NULL)
            {
                node *newNode = new node();
                for(int j=0; j<26; j++)
                    newNode->next[j] = NULL;
                newNode->fail = NULL;
                newNode->cnt = 0;
                p->next[c] = newNode;
            }
            p = p->next[c];
        }
        p->cnt++;
    }
    void add_fail()
    {
        queue<node *>que;
        que.push(root);
        node *p,*tmp;
        while(!que.empty())
        {
            tmp = que.front();
            que.pop();
            for(int i=0; i<26; i++)
            {
                if(tmp->next[i]==NULL) continue;
                if(tmp == root)
                {
                    tmp->next[i]->fail = root;
                }
                else
                {
                    p = tmp->fail;
                    while(p!=NULL)
                    {
                        if(p->next[i]!=NULL)
                        {
                            tmp->next[i]->fail = p->next[i];
                            break;
                        }
                        p = p->fail;
                    }
                    if(p==NULL) tmp->next[i]->fail = root;
                }
                que.push(tmp->next[i]);
            }
        }
    }
    int check_str(char *str)
    {
        node *p = root,*tmp;
        int n=strlen(str),c,ret = 0;
        for(int i=0; i<n; i++)
        {
            c = str[i]-'a';
            while(!p->next[c] && p!=root) p = p->fail;
            p = p->next[c];
            if(!p) p = root;
            tmp = p;
            while(tmp!=root)
            {
                if(tmp->cnt==-1) break;
                ret += tmp->cnt;
                tmp->cnt = -1;
                tmp = tmp->fail;
            }
        }
        return ret;
    }
    void del(node *rt){
         for(int i=0; i<26; i++) if(rt->next[i]!=NULL)
            del(rt->next[i]);
         delete rt;
    }
    ~ac_automata(){
        del(root);
    }
private:
    node *root;
};
char a[N];
int main()
{
    int T;cin>>T;
    while(T--)
    {
        ac_automata ac;
        int n;cin>>n;
        for(int i=0;i<n;i++)
        {
           scanf("%s",a);ac.insert_str(a);
        }
        scanf("%s",a);ac.add_fail();
        printf("%d\n",ac.check_str(a));
    }
    return 0;
}
