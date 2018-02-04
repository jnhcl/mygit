/*************************************************************************
	> File Name: stack_getmin.cpp
	> Author:zsy 
	> Mail: 1607041983@qq.com
	> Created Time: 2018年02月04日 星期日 21时56分31秒
 ************************************************************************/

#include <iostream>
#include <stack>
using namespace std;
class myStack{
public:
    void push(int newNum){
        if(stackMin.empty())
            stackMin.push(newNum);
        else if(newNum<=getmin())
            stackMin.push(newNum);
        stackData.push(newNum);
    }
    int pop(){
        int value=stackData.top();
        stackData.pop();
        if(value==getmin())
            stackMin.pop();
        return value;
    }
    int getmin(){
        return stackMin.top();
    }
private:
    stack<int>stackData;
    stack<int>stackMin;
}
