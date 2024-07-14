#include <iostream>
#include <vector>
#include <queue>
#define INF 1e6
using namespace std;

int V,E,K,u,v,w,cost,now;
int dist[20001];
vector<pair<int,int>> graph[20001];
priority_queue<pair<int,int>> pq;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> V >> E >> K;

    for(int i=0; i<E; i++) {
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(v,w));
    }
    for(int i=0; i<V+1; i++) {
        dist[i] = INF;
    }

    pq.push(make_pair(0,K));
    dist[K] = 0;

    while(!pq.empty()) {
        cost = -pq.top().first;
        now = pq.top().second;
        pq.pop();

        if(dist[now] < cost) continue;
        for(auto cur : graph[now]) {
            if(cur.second+dist[now] < dist[cur.first]) {
                dist[cur.first] = cur.second+dist[now];
                pq.push(make_pair(-dist[cur.first], cur.first));
            }
        }
    }

    for(int i=1; i<V+1; i++) {
        if(dist[i]>=INF) cout << "INF\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}