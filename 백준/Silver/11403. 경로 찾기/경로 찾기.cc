#include <iostream>
using namespace std;

int N,graph[100][100];

int main() {
    cin >> N;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            cin >> graph[i][j];

    for(int k=0; k<N; k++)
        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                if(graph[i][k] & graph[k][j])
                    graph[i][j] = 1;

    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++)
            cout << graph[i][j] << ' ';
        cout << '\n';
    }

    return 0;
}