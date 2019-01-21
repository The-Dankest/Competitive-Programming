#include <iostream>
#include <vector>
#include <queue>

using namespace std;
typedef vector<int> vi;

class DisjointSet {
	int nSets;
	std::vector<int> parent;
public:
	DisjointSet() : nSets(0) { ; }
	int NumberOfSets() const { return nSets; }
	
	void addSingleton(int v) {
		if (parent.size() > unsigned(v)) { return; }
		int oldSize = parent.size();
		parent.resize(v+1, -1);
		nSets += v - oldSize + 1;
	}
	
	int find(int value) {
		// am I at a root or the child of the root
		if (parent[value] < 0) { return value; }
		if (parent[parent[value]] < 0) { return parent[value]; }

		int prnt = find(parent[value]);
		parent[value] = prnt;
		return prnt;
	}
	
	// Merge the set containing u with the set containing v
	void merge(int u, int v) {
		if ((u = find(u)) == (v = find(v))) { return; }

		--nSets;
		if (parent[v] < parent[u]) { std::swap(u,v); }
		parent[u] += parent[v];
		parent[v] = u;
	}

	int setSize(int v) { return -parent[find(v)]; }
}; 

int main() {
    int i;
    cin >> i;
    for (; i > 0; --i) {
        int n, m;
        cin >> n >> m;
		DisjointSet set;
		set.addSingleton(n);
        priority_queue<int> bigs;
        for (int j = 0; j < m; ++j) {
            int a, b;
            cin >> a >> b;
            set.merge(a, b);
            bigs.push(set.setSize(a));
		}
		if (!bigs.empty()) {	
			cout << bigs.top() << endl;
		} else {
			cout << "1" << endl;
		}
	}
	return 0;
}
