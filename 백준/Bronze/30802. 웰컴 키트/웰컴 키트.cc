#include <iostream>

using namespace std;

int main() {
    int N,T,P,sizes[6];

    cin >> N;
    for(int i=0; i<6; cin >> sizes[i++]);
    cin >> T >> P;

    int answer = 0;
    for(int size: sizes) {
        if(!size) continue;
        answer += (size-1)/T+1;
    }

    cout << answer << '\n';
    cout << N/P << " " << N%P;

    return 0;
}
