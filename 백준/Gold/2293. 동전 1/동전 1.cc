#include <iostream>
using namespace std;

int n,k,cur;
int arr[100];
int dp[10001];

int main() {
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> arr[i];

    dp[0] = 1;
    for(int i=0; i<n; i++) {
        cur = arr[i];
        for(int j=cur; j<=k; j++)
            dp[j] += dp[j-cur];
    }

    cout << dp[k];

    return 0;
}
