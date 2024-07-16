#include <iostream>
using namespace std;

int d,m,y,answer;
int date[12] = {31,28,31,30,31,30,31,31,30,31,30,31};

int main() {
    while(true) {
        cin >> d >> m >> y;
        if(!(d+m+y)) return 0;

        answer = 0;

        if(m>2)
            if(y%4==0 && (y%100!=0 || y%400==0))
                answer++;

        for(int i=0; i<m-1; i++)
            answer += date[i];

        answer += d;
        cout << answer << '\n';
    }

    return 0;
}