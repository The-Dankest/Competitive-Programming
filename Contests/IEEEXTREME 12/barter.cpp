#include <bits/stdc++.h>
using namespace std;
// shortcuts for "common" data types in contests
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000
#define FOR(i,a) for (int i = 0; i < a; ++i)
#define FORI(it,v) for (auto it = (v).begin(); it != (v).end(); ++it)
#define MOD 998244353

template<typename T>
void printvi(vector<T> v, string sep=" ", string bookend="") {
    cout << bookend << ((bookend == "") ? "" : " ");
    for (T n : v)
        cout << n << sep;
    cout << bookend << endl;
}

void printvii(vector<ii> v, string sep=" ", string bookend="") {
    cout << bookend << ((bookend == "") ? "" : " ");
    for (ii p : v)
        cout << "(" << p.first << "," << p.second << ")" << sep;
    cout << bookend << endl;
}

vector<vector<pair<int, ll>>> adjlist;
map<string, int> goods;
vi dfs_num;
bool gotthere;

ll gcdExtended(ll a, ll b, ll &x, ll &y) {
    if (a == 0) {
        x = 0, y = 1;
        return b;
    }

    ll x1, y1;
    ll gcd = gcdExtended(b%a, a, x1, y1);
    x = y1 - (b/a) * x1;
    y = x1;
    return gcd;
}

ll modDivide(ll a, ll b, ll m)
{
    a = a % m;
    ll x, y;
    gcdExtended(b, m, x, y);
    ll inv = (x%m + m) % m;
    return (inv * a) % m;
}

int dfs(int u, int v)
{
    ll ans = 1;
    dfs_num[u] = 1;
    gotthere = u == v;
    if (!gotthere) {
        FOR(i, (int)adjlist[u].size()) {
            ii s = adjlist[u][i];
            if (dfs_num[s.first] == 0) {
                ll mid = dfs(s.first, v);
                if (gotthere) {
                    if (s.second >= 0)
                        ans = (mid * s.second) % MOD;
                    else
                        ans = modDivide(mid, -1 * s.second, MOD);
                }
            }
            if (gotthere) break;
        }
    }
    return ans;
}


int main()
{
    ios_base::sync_with_stdio(false);
    // code goes here
    int n; cin >> n;
    adjlist.assign(2*n, vector<pair<int, ll>>(0, pair<int, ll>()));
    dfs_num.assign(n, 0);
    gotthere = false;
    FOR(i, n) {
        string a, b;
        ll amt;
        cin >> a >> b >> amt;
        if (goods.count(a) == 0)
            goods[a] = goods.size() - 1;
        if (goods.count(b) == 0)
            goods[b] = goods.size() - 1;
        adjlist[goods[a]].push_back(make_pair(goods[b], amt));
        adjlist[goods[b]].push_back(make_pair(goods[a], -1 * amt));
    }
    int q; cin >> q;
    FOR(i, q) {
        string a, b; cin >> a >> b;
        dfs_num.assign(n, 0);
        ll ans = dfs(goods[a], goods[b]);
        cout << (gotthere ? ans : -1) << endl;
    }

    return 0;
}
