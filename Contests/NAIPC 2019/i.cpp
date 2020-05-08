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

int main()
{
	ios_base::sync_with_stdio(false);
	// code goes here

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string s;
        int k;
        cin >> k >> s;

        char big_c = 'a';
        vi c_loc;
        for (int j = 0; j < s.length(); ++j) {
            if (s[j] > big_c) {
                c_loc = vi();
                big_c = s[j];
                c_loc.push_back(j);
            } else if (s[j] == big_c) {
                c_loc.push_back(j);
            }
        }

        int num_c;
        if (k > c_loc.size()) {
            num_c = c_loc.size();
        } else if (k == c_loc.size() && c_loc[0] == 0) {
            num_c = c_loc.size();
        } else if (k == c_loc.size() && c_loc[c_loc.size() - 1] == s.length() - 1) {
            num_c = c_loc.size();
        } else if (k == c_loc.size() - 1 && c_loc[c_loc.size() - 1] == s.length() - 1 && c_loc[0] == 0) {
            num_c = c_loc.size();
        }

    }

	return 0;
}
