#include <iostream>
#include <stack>
using namespace std;

int N,M,answer,nvalue;
int graph[500][500];
bool visited[500][500];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void dfs(int x, int y, int depth, int value) {
    for(int i=0; i<4; i++) {
        int nx = x+dx[i];
        int ny = y+dy[i];
        if(nx<0 || nx>=M || ny<0 || ny>=N) continue;
        if(visited[ny][nx]) continue;

        int nvalue = value+graph[ny][nx];
        if(depth==3) {
            answer = max(nvalue, answer);
        } else {
            visited[ny][nx] = true;
            dfs(nx, ny, depth+1, nvalue);
            visited[ny][nx] = false;
        }
    }
}

int main() {
    cin >> N >> M;
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
            cin >> graph[i][j];

    for(int i=0; i<N; i++) {
        for(int j=0; j<M; j++) {
            visited[i][j] = true;
            dfs(j,i,1,graph[i][j]);
            visited[i][j] = false;
        }
    }

    for(int i=1; i<N-1; i++) {
        for(int j=1; j<M-1; j++) {
            nvalue = graph[i][j];
            for(int k=0; k<4; k++)
                nvalue += graph[i+dx[k]][j+dy[k]];
            for(int k=0; k<4; k++)
                answer = max(answer,nvalue-graph[i+dx[k]][j+dy[k]]);
        }
    }

    for(int i=0; i<N-2; i++) {
        int temp[2] = {0,M-1};
        for(auto j : temp) {
            nvalue = graph[i][j]+graph[i+1][j]+graph[i+2][j];
            if(j==0) nvalue += graph[i+1][j+1];
            else nvalue += graph[i+1][j-1];
            answer = max(answer, nvalue);
        }
    }
    for(int j=0; j<M-2; j++) {
        int temp[2] = {0,N-1};
        for(auto i : temp) {
            nvalue = graph[i][j]+graph[i][j+1]+graph[i][j+2];
            if(i==0) nvalue += graph[i+1][j+1];
            else nvalue += graph[i-1][j+1];
            answer = max(answer, nvalue);
        }
    }

    cout << answer;

    return 0;
}