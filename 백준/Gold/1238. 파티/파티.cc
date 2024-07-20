#include <iostream>
#include <queue>
#define pii pair<int,int>
using namespace std;

int N,M,X,a,b,c,answer;
int graph[1001][1001],to_dist[1001],from_dist[1001];;

void to_dijkstra(int src) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    int cost,now,ncost;

    for(int i=0; i<N+1; i++) to_dist[i] = 100001;
    pq.push({0,src});
    to_dist[X] = 0;

    while(!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        for(int i=1; i<N+1; i++) {
            ncost = graph[now][i];
            if(!ncost) continue;
            if(to_dist[i] < ncost) continue;
            if(ncost+cost < to_dist[i]) {
                to_dist[i] = ncost+cost;
                pq.push({to_dist[i], i});
            }
        }
    }
}

void from_dijkstra(int dest) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    int cost,now,ncost;

    for(int i=0; i<N+1; i++) from_dist[i] = 100001;
    pq.push({0,dest});
    from_dist[X] = 0;

    while(!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        for(int i=1; i<N+1; i++) {
            ncost = graph[i][now];
            if(!ncost) continue;
            if(from_dist[i] < ncost) continue;
            if(ncost+cost < from_dist[i]) {
                from_dist[i] = ncost+cost;
                pq.push({from_dist[i], i});
            }
        }
    }
}

int main() {
    cin >> N >> M >> X;
    for(int i=0; i<M; i++) {
        cin >> a >> b >> c;
        graph[a][b] = c;
    }

    to_dijkstra(X);
    from_dijkstra(X);

    answer = 0;
    for(int i=1; i<N+1; i++)
        answer = max(to_dist[i]+from_dist[i], answer);

    cout << answer;

    return 0;
}


