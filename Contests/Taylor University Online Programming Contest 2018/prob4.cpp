#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <bitset>
using namespace std;
// shortcuts for "common" data types in contests
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000

int main()
{
	ios_base::sync_with_stdio(false);
	// code goes here
	int m, n;
	cin >> m >> n;
	string blah;
	cin >> blah;
	vi lastDp(m);
	vi dp(m);
	int best = 0;
	for (int i = 0; i < m; ++i) {
		string line;
		getline(cin, line);
		// cout << "Line: " << line << endl;
		for (int j = 0; j < n; ++j) {
			if (i == 0) {
				lastDp[j] = (line[j] == '0') ? 0 : 1;
			}
			else {
				if (line[j] == '0')
					dp[j] = 0;
				else {
					if (j == 0)
						dp[j] = 1;
					else {
						int corner = lastDp[j - 1];
						int top = lastDp[j];
						int left = dp[j - 1];
						if (top == 0 || corner == 0 || left == 0)
							dp[j] = 1;
						else if (top >= corner && left >= corner)
							dp[j] = min(min(corner, top), left) + 1;
						else
							dp[j] = min(min(corner, top), left) + 1;
						best = max(best, dp[j]);
					}
				}
			}
		}
		for (int j = 0; j < n; ++j)
			cout << dp[j];
		cout << endl;
		for (int j = 0; j < n; ++j)
			lastDp[j] = dp[j];
	}
	cout << best << endl;
	return 0;
}
