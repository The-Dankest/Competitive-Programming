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

struct Edge {
    int v; // first vertex
    int u; // second vertex
    int w; // weight of the edge
};

struct EdgeCompare {
    bool operator()(Edge a, Edge b) {
        if (a.w == b.w) {
            if (a.u == b.u) {
                return a.v > b.v;
            }
            return a.u > b.u;
        }
        return a.w > b.w;
    }
};

class DisjointSet {
    int nSets;
	std::vector<int> parent;
public:
    DisjointSet() : nSets(0) { ; }
    DisjointSet(int n) {
        nSets = 0;
        resize(n);
    }
	int count() const { return nSets; }
    
	void resize(int v) {
		if (parent.size() > unsigned(v)) { return; }
		int oldSize = parent.size();
		parent.resize(v+1, -1);
		nSets += v - oldSize + 1;
	}
	int find(int value) {
		if (parent[value] < 0) { return value; }
		if (parent[parent[value]] < 0) { return parent[value]; }

		int prnt = find(parent[value]);
		parent[value] = prnt;
		return prnt;
    }
    int set_size(int v) { return -parent[find(v)]; }
    int are_joined(int u, int v) { return (find(u) == find(v)); }
	void join(int u, int v) {
		if ((u = find(u)) == (v = find(v))) { return; }

		--nSets;
		if (parent[v] < parent[u]) { std::swap(u,v); }
		parent[u] += parent[v];
		parent[v] = u;
	}
    
}; 

int main() {

    priority_queue<Edge, vector<Edge>, EdgeCompare> edges;
    DisjointSet vertices;
    vector<Edge> mwst;


    int n, m;
    cin >> n >> m;
    int v, u, w;
    while (cin >> v >> u >> w) {
        Edge e {v, u, w};
        edges.push(e);
        if (max(v, u) >= vertices.count()) {
            vertices.resize(max(v, u));
        }
    }

    while (!edges.empty()) {
        Edge e = edges.top();
        if (!vertices.are_joined(e.v, e.u)) {
            vertices.join(e.v, e.u);
        }
        if (vertices.count() == 1) {
            break;
        }
        edges.pop();
    }

    return 0;
}