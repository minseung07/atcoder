#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int h, w;
    cin >> h >> w;

    vector<pair<int, int>> res;

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            char x;
            cin >> x;
            if (x == 'T') {
                res.push_back({i, j});
            }
        }
    }

    if (res.empty()) {
        cout << 0 << '\n';
    }
    else {
        cout << res.size() << '\n';
        for (auto &[i, j] : res) {
            cout << i+1 << " " << j+1 << '\n';
        }
    }


}