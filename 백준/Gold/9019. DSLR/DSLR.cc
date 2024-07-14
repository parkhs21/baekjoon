#include <iostream>
#include <queue>

using namespace std;

int T,A,B,n,D,S,L,R;
string op;

string bfs(int src, int dest) {
    bool visited[10001] = {false,};
    queue<pair<int,string>> q;

    q.push(make_pair(src, ""));
    visited[src] = true;

    while(!q.empty()) {
        n = q.front().first;
        op = q.front().second;
        q.pop();

        if(n==dest) return op;

        D = (2*n)%10000;
        if(!visited[D]) {
            visited[D] = true;
            q.push(make_pair(D,op+'D'));
        }
        S = (n==0 ? 9999 : n-1);
        if(!visited[S]) {
            visited[S] = true;
            q.push(make_pair(S,op+'S'));
        }
        L = n/1000 + (n%1000)*10;
        if(!visited[L]) {
            visited[L] = true;
            q.push(make_pair(L,op+"L"));
        }
        R = n/10 + (n%10)*1000;
        if(!visited[R]) {
            visited[R] = true;
            q.push(make_pair(R,op+'R'));
        }
    }

    return "";
}

int main() {
    cin >> T;
    for(; T>0; T--) {
        cin >> A >> B;
        cout << bfs(A,B) << '\n';
    }

    return 0;
}