#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;

    string k = "KOREA";
    string y = "YONSEI";
    int k_i = 0, y_i = 0;
    for(char c : s) {
        if(k[k_i]==c) k_i++;
        if(y[y_i]==c) y_i++;

        if(k_i==5) {
            cout << k;
            return 0;
        } else if(y_i==6) {
            cout << y;
            return 0;
        }
    }

    return 0;
}
