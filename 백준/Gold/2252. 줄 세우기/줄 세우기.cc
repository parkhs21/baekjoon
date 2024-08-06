#include <iostream>
#include <queue>
using namespace std;

int N,M,A,B,cur;
int cnt[32001];
vector<int> graph[32001];
queue<int> q;

int main() {
    cin >> N >> M;

    for(int i=0; i<M; i++) {
        cin >> A >> B;
        cnt[B]++;
        graph[A].push_back(B);
    }

    for(int i=1; i<=N; i++)
        if(cnt[i] == 0)
            q.push(i);

    while(!q.empty()) {
        cur = q.front();
        q.pop();
        cout << cur << " ";

        for(auto next : graph[cur]) {
            cnt[next]--;
            if(cnt[next] == 0)
                q.push(next);
        }
    }
    
    return 0;
}
