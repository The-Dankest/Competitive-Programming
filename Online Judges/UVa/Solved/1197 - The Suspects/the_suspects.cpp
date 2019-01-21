#include <vector>
#include <iostream>

using namespace std;

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
    int n, m;
    cin >> n >> m;
    while (!(n == 0 && m == 0)) {
        DisjointSet groups;
        groups.addSingleton(n - 1);
        // for each group
        while (--m >= 0) {
            int i;
            cin >> i;
            int prev = -1;
            for (; i > 0; --i) {
                int next;
                cin >> next;
                if (prev >= 0) {
                    groups.merge(prev, next);
                }
                prev = next;
            }

        }
        cout << groups.setSize(0) << endl;
        cin >> n >> m;
    }
    return 0;
}