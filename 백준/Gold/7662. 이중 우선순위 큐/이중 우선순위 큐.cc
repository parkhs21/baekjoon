#include <iostream>
#include <queue>
#include <map>
using namespace std;

int T,Q,n;
char op;
priority_queue<int> max_pq;
priority_queue<int, vector<int>, greater<int>> min_pq;
map<int, int> cnt;

void clean() {
    while(!min_pq.empty() && cnt[min_pq.top()]==0)
        min_pq.pop();
    while(!max_pq.empty() && cnt[max_pq.top()]==0)
        max_pq.pop();
}

int main() {
    cin >> T;
    for(; T>0; T--) {
        cin >> Q;

        max_pq = priority_queue<int>();
        min_pq = priority_queue<int, vector<int>, greater<int>>();
        cnt = map<int,int>();

        for(; Q>0; Q--) {
            cin >> op >> n;

            if(op=='I') {
                max_pq.push(n);
                min_pq.push(n);
                cnt[n]++;
            } else if(n==1) {
                if(max_pq.empty()) continue;
                cnt[max_pq.top()]--;
                max_pq.pop();
                clean();
            } else {
                if(min_pq.empty()) continue;
                cnt[min_pq.top()]--;
                min_pq.pop();
                clean();
            }
        }
        if(max_pq.empty() || min_pq.empty()) cout << "EMPTY\n";
        else cout << max_pq.top() << " " << min_pq.top() << '\n';
    }

    return 0;
}
