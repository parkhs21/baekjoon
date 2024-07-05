#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int T;
    cin >> T;

    for(; T>0; T--) {
        int x1,y1,x2,y2,N,answer;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> N;

        answer = 0;
        for(; N>0; N--) {
            int cx,cy,r;
            cin >> cx >> cy >> r;

            bool in1, in2;
            in1 = false;
            in2 = false;
            if(pow(x1-cx,2) + pow(y1-cy,2) < pow(r,2))
                in1 = true;
            if(pow(x2-cx,2) + pow(y2-cy,2) < pow(r,2))
                in2 = true;

            if(in1 && !in2) answer++;
            if(!in1 && in2) answer++;
        }

        cout << answer << '\n';
    }

    return 0;
}
