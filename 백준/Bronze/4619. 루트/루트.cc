#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int B,N,temp;
    while(true) {
        cin >> B >> N;
        if(!B && !N) break;

        temp = int(pow(B, 1./N));
        if(pow(temp, N)+pow(temp+1, N) > 2*B) cout << temp << '\n';
        else cout << temp+1 << '\n';
    }

    return 0;
}
