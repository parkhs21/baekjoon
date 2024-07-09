#include <iostream>
#include <math.h>
using namespace std;

int N,i;
bool flag;

int main() {
    cin >> N;
    if(N==1) {
        cout << 0;
        return 0;
    }

    flag = false;
    for(i=2; i<=sqrt(N); i++) {
        if(N%i == 0) {
            flag = true;
            break;
        }
    }

    if(flag) cout << N-N/i;
    else cout << N-1;

    return 0;
}
