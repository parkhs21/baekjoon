#include <iostream>
#include <math.h>
using namespace std;

int N,a,b,i,j,temp,arr[100001];
int density = 2000000001;

int main() {
    cin >> N;
    for(int i=0; i<N; i++)
        cin >> arr[i];

    i = 0;
    j = N-1;
    while(i<j) {
        temp = arr[i]+arr[j];
        if(abs(temp)<density) {
            density = abs(temp);
            a = arr[i];
            b = arr[j];
            if(!density) break;
        }

        if(temp<0) i++;
        else j--;
    }

    cout << a << ' ' << b;

    return 0;
}