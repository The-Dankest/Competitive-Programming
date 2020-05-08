#include <bits/stdc++.h>
using namespace std;
// shortcuts for "common" data types in contests
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> T_AdjList;
typedef vector<vii> T_WAdjList;
#define INF 1000000000
#define FOR(i,a) for (int i = 0; i < a; ++i)
#define FORI(it,v) for (auto it = (v).begin(); it != (v).end(); ++it)
#define ROUND(d) (int)((double)(d) + 0.5)

int main()
{

    int n;
    cin >> n;
    vector<string> bets;
    vector<int> correct_bets;
    for (int i = 0; i < n; ++i) {
        string b;
        cin >> b;
        bets.push_back(b);
    }

    int max_num = pow(2, bets[0].length);
    int ans = max_num;

    for (int i = 0; i < max_num; ++i) {
        vector<int> correct_for
        for (int j = 0; j < n; ++j) {
            char b = (i & (1 << j) == 1)? '1' : '0';
            for (int k = 0; k < n; ++k) {
                
            }
        }
    }

    cout << ans << endl;

    return 0;
}
