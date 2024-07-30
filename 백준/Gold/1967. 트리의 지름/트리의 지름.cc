#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int V,a,b,c,max_node,max_cost;
bool visited[100001];
vector<pair<int,int>> graph[100001];


void dfs(int root, int cost) {
    visited[root] = true;

    if(cost > max_cost) {
        max_cost = cost;
        max_node = root;
    }

    for(auto& node : graph[root])
        if(!visited[node.first])
            dfs(node.first, cost+node.second);
}

int main() {
    cin >> V;
    for(int i=0; i<V-1; i++) {
        cin >> a >> b >> c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }

    dfs(1,0);

    memset(visited, false, sizeof(visited));
    max_cost = 0;
    dfs(max_node, 0);

    cout << max_cost;

    return 0;
}
