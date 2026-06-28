#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<long long> V(n);
    for (int i = 0; i < n; i++) cin >> V[i];

    // dp[i][j]: 구간 [i, j]에서의 최대 이득
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) dp[i][i] = V[i];

    for (int j = 1; j < n; j++) {
        for (int i = j-1; i >= 0; i--) {
            dp[i][j] = max(V[i] - dp[i+1][j], V[j] - dp[i][j-1]);
        }
    }

    cout << dp[0][n-1] << '\n';

}