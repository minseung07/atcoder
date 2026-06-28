#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long n, m;
    cin >> n >> m;

    vector<long long> P(n);
    for (long long i = 0; i < n; i++) {
        cin >> P[i];
    }

    if (n == 1) {
        if (P[0] <= m) cout << "Yes" << '\n';
        else cout << "No" << '\n';
    }
    else {
        long long g = gcd(P[0], P[1]);
        if (P[0] / g > m / P[1]) {
            cout << "No" << '\n';
            return 0;
        }
        long long res = P[0] / g * P[1];
        for (int i = 1; i < n; i++) {
            g = gcd(res, P[i]);
            if (res / g > m / P[i]) {
                cout << "No" << '\n';
                return 0;
            }
            res = res / g * P[i];
        }
        if (res <= m) cout << "Yes" << '\n';
        else cout << "No" << '\n';
    }



}