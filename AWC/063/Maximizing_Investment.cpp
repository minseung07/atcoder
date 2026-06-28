#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1 == 1) res = (res * a) % mod;
        a = (a * a) % mod;
        n >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long n, k;
    cin >> n >> k;
    
    long long su = 0, mx = 0;
    for (long long i = 0; i < n; i++) {
        long long x;
        cin >> x;
        su += x;
        if (x > mx) {
            mx = x;
        }
    }

    su %= 1000000007;
    long long ans = (su - mx + mx * power(2, k, 1000000007)) % (1000000007);
    cout << ans << '\n';

}