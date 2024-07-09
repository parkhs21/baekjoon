#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    if(N<3) cout << 1;
    else if(N<6) cout << 2;
    else cout << 3;

    return 0;
}
