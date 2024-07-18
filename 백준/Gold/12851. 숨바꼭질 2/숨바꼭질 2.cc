#include <iostream>
#include <queue>
#define pii pair<int,int>
#define MAX 100001
using namespace std;

int N,K,cost,now,flag;
priority_queue<pii, vector<pii>, greater<pii>> pq;
pii visited[MAX];

int main() {
    cin >> N >> K;

    pq.push({1, N});
    visited[N] = {1,1};
    flag = MAX;

    while(!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        if(now==K) flag=cost;
        if(cost>flag) break;

        for(int nnow : {2*now, now+1, now-1}) {
            if (nnow < MAX && nnow >= 0) {
                if(visited[nnow].first == cost+1)
                    visited[nnow].second += visited[now].second;
                else if(visited[nnow].first == 0) {
                    pq.push({cost+1, nnow});
                    visited[nnow] = {cost+1, visited[now].second};
                }
            }
        }
    }

    cout << visited[K].first-1 << '\n' << visited[K].second;

    return 0;
}