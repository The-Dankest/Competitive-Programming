#include <iostream>
#include <vector>
#include <map>
#include <string>

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
    int j;
    cin >> j;
    for (; j > 0; --j) {
        DisjointSet set;
        map<string,int> names;
        int i;
        cin >> i;
        for (; i > 0; --i) {
            string a, b;
            cin >> a >> b;
            if (names.count(a) == 0) {
                names[a] = names.size();
                set.addSingleton(names[a]);
            }
            if (names.count(b) == 0) {
                names[b] = names.size();
                set.addSingleton(names[b]);
            }
            set.merge(names[a], names[b]);
            cout << set.setSize(names[a]) << endl;
        }
    }
	return 0;
}
