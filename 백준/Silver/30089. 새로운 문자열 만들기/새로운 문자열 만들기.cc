#include <iostream>

using namespace std;

int T,stri,endi;
string s;
bool flag;

int main() {
    cin >> T;
    for(; T>0; T--) {
        cin >> s;

        for(int i=0; i<s.size(); i++) {
            stri = i;
            endi = s.size()-1;
            if(s[stri] == s[endi]) {
                flag = true;
                while(stri <= endi) {
                    if(s[stri++] != s[endi--]) {
                        flag = false;
                        break;
                    }
                }
                if(flag) {
                    cout << s;
                    for(int j=i-1; j>=0; j--)
                        cout << s[j];
                    cout << '\n';
                    break;
                }
            }
        }
    }

    return 0;
}
