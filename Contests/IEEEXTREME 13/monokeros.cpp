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

struct Node {
    int value;
    Node* left;
    Node* right;
};

#define MAXN 200000
Node tree[MAXN];
int len = 0;
int height = 0;

void insert(Node* curnode, int value, int depth) {
    if (value <= curnode->value) {
        if (curnode->left != nullptr) {
            insert(curnode->left, value, depth + 1);
        } else {
            tree[len] = {value, nullptr, nullptr};
            curnode->left = &tree[len++];
            height = max(depth + 1, height);
        }
    } else {
        if (curnode->right != nullptr) {
            insert(curnode->right, value, depth + 1);
        } else {
            tree[len] = {value, nullptr, nullptr};
            curnode->right = &tree[len++];
            height = max(depth + 1, height);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    // code goes here
    int n; cin >> n;
    FOR(_, n) {
        int v; cin >> v;
        if (len == 0) {
            tree[len++] = {v, nullptr, nullptr};
            cout << 1;
        } else {
            insert(&tree[0], v, 1);
            cout << " " << height;
        }
    }
    cout << endl;

    return 0;
}