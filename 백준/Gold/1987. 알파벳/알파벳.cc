#include <iostream>
using namespace std;

int R,C;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
char graph[21][21];
bool visited[26];

int dfs(int x, int y) {
    int cost = 0;
    visited[graph[y][x] - 'A'] = true;

    for(int i=0; i<4; i++) {
        int nx = x+dx[i];
        int ny = y+dy[i];
        if(nx<0 || nx>=C || ny<0 || ny>=R) continue;

        if(!visited[graph[ny][nx]-'A']) {
            cost = max(dfs(nx, ny), cost);
        }
    }

    visited[graph[y][x] - 'A'] = false;
    return cost+1;
}

int main() {
    cin >> R >> C;
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            cin >> graph[i][j];

    cout << dfs(0,0);

    return 0;
}
