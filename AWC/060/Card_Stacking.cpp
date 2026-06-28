#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

    mt19937_64 rng(random_device{}());
    vector<ll> hashes(25);
    for (int i = 0; i <25; i++) hashes[i] = rng();

    vector<ll> cards(n);

}