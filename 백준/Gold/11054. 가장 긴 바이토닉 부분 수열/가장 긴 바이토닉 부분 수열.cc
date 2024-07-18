#include <iostream>
using namespace std;

int N,answer;
int s[1000],max_dp[1000],min_dp[1000];

int main() {
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> s[i];
        max_dp[i] = 1;
        min_dp[i] = 1;
    }

    for(int i=0; i<N; i++)
        for(int j=0; j<i; j++)
            if(s[j] < s[i])
                max_dp[i] = max(max_dp[i], max_dp[j]+1);

    for(int i=N-1; i>=0; i--)
        for(int j=N-1; j>i; j--)
            if(s[i] > s[j])
                min_dp[i] = max(min_dp[i], min_dp[j]+1);

    answer = 0;
    for(int i=0; i<N; i++)
        answer = max(max_dp[i]+min_dp[i], answer);

    cout << answer-1;

    return 0;
}