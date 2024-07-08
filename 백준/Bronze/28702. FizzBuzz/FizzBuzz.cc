#include <iostream>

using namespace std;

int main() {
    string str;
    int target = 0;

    for(int i=0; i<3; i++) {
        cin >> str;
        if(isdigit(str[0])) {
            target = stoi(str)+3-i;
            break;
        }
    }

    str = "";
    if(!(target%3)) str += "Fizz";
    if(!(target%5)) str += "Buzz";

    if(str.empty()) str = to_string(target);

    cout << str;

    return 0;
}
