#include <iostream>
#include <map>
#include <queue>
using namespace std;

struct node {
    int idx;
    int cnt;
};

int N,M,x,y;
bool flag;
map<int,int> m;
queue<node> q;
node cur;

int main() {
    cin >> N >> M;
    for(int i=0; i<N+M; i++) {
        cin >> x >> y;
        m[x] = y;
    }

    q.push(node{1,0});
    while(!q.empty()) {
        cur = q.front();
        q.pop();

        if(cur.idx >= 94) {
            cout << cur.cnt+1;
            return 0;
        }

        flag = false;
        for(int i=cur.idx+6; i>cur.idx; i--) {
            if(m[i]==0 && !flag) {
                q.push(node{i,cur.cnt+1});
                flag = true;
            } else if(m[i]!=0) {
                q.push(node{m[i],cur.cnt+1});
            }
        }

    }

    return 0;
}