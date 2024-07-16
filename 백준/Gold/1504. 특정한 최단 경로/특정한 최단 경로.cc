#include <iostream>
#include <vector>
#include <queue>
#define INF 10e7
using namespace std;

int N,E,v1,v2,a,b,c,cost,now;
int dist[801];
vector<pair<int,int>> graph[801];

void dijkstra(int src) {
    for(int i=0; i<N+1; i++) dist[i] = INF;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push(make_pair(0,src));
    dist[src] = 0;

    while(!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        if(dist[now] < cost) continue;
        for(auto cur : graph[now]) {
            if(dist[now]+cur.second < dist[cur.first]) {
                dist[cur.first] = dist[now]+cur.second;
                pq.push(make_pair(dist[cur.first], cur.first));
            }
        }
    }
}

int main() {
    cin >> N >> E;
    while(E--) {
        cin >> a >> b >> c;
        graph[a].push_back(make_pair(b,c));
        graph[b].push_back(make_pair(a,c));
    }
    cin >> v1 >> v2;

    dijkstra(1);
    int to_v1 = dist[v1];
    int to_v2 = dist[v2];

    dijkstra(N);
    int v1_N = dist[v1];
    int v2_N = dist[v2];

    dijkstra(v1);
    int v1_v2 = dist[v2];

    int answer = min(to_v1+v2_N, to_v2+v1_N) + v1_v2;
    if(answer >= INF) cout << -1;
    else cout << answer;

    return 0;
}