#include <bits/stdc++.h>

#define FOR(i, l, r) for (int i = l; i <= r; i++)
#define REP(i, n) for (int i = 0; i < n; i++)
#define REV(i, l, r) for (int i = l; i >= r; i--)
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define pp pop_back
#define fr front
#define mp make_pair
#define fileInput(problemName) freopen((string(problemName) + ".inp").c_str(), "r", stdin); freopen((string(problemName) + ".ans").c_str(), "w", stdout);
#define fast ios_base::sync_with_stdio(0); cin.tie(NULL);

const int inf = 1e9 + 7;

using namespace std;

int main()
{
    fileInput("sum");
    fast;
    cin >> a >> b;
    int ans = a;
    for (int i = 1; i <= b; i++) {
        ans += 1;
    }
    cout << ans << endl;
    return (0);
}