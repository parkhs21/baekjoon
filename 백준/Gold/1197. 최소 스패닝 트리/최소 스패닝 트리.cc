#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct edge {
    int cost;
    int a;
    int b;

    bool operator<(edge e) const {
        return cost<e.cost;
    }
};

int V,E,A,B,C,answer,cnt,parent[10001];
vector<edge> graph;

int find(int x) {
    if(parent[x] == x)return x;
    return find(parent[x]);
}

bool merge(edge now) {
    int x = find(now.a);
    int y = find(now.b);
    if(x==y) return false;

    if(x<y) parent[x] = y;
    else parent[y] = x;
    answer += now.cost;
    return true;
}

int main() {
    cin >> V >> E;
    for(int i=0; i<E; i++) {
        cin >> A >> B >> C;
        graph.push_back(edge{C,A,B});
    }

    for(int i=0; i<V+1; i++)
        parent[i] = i;

    answer = 0;
    cnt = 0;
    sort(graph.begin(), graph.end());

    for(auto e : graph) {
        if(merge(e)) cnt += 1;
        if(cnt>=V-1) break;
    }

    cout << answer;

    return 0;
}
