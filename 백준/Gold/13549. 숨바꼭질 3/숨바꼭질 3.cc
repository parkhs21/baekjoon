#include <iostream>
#include <queue>
#define MAX 100001
using namespace std;

int N,K,cost,now;
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
bool visited[MAX];

int main() {
    cin >> N >> K;

    pq.push({0, N});
    visited[N] = true;

    while(!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        if(now==K) {
            cout << cost;
            return 0;
        }

        if(2*now < MAX && !visited[2*now]) {
            pq.push({cost, 2*now});
            visited[2*now] = true;
        }
        if(now+1 < MAX && !visited[now+1]) {
            pq.push({cost+1, now+1});
            visited[now+1] = true;
        }
        if(now-1 >= 0 && !visited[now-1]) {
            pq.push({cost+1, now-1});
            visited[now-1] = true;
        }
    }

    return 0;
}