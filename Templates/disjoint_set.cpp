#include <vector>
#include <algorithm>

using namespace std;

class disjoint_set {
    int size;
	std::vector<int> parents;
public:
    disjoint_set() { size = 0;}
    disjoint_set(int n) { size = 0; resize(n); }

	int size() const { return size; }
    
    int set_size(int v) { return -parents[find_parent(v)]; }
    int are_joined(int u, int v) { return (find_parent(u) == find_parent(v)); }
    
	void resize(int s) {
		if (parents.size() > unsigned(s)) { return; }
		int oldSize = parents.size();
		parents.resize(s + 1, -1);
		size += s - oldSize + 1;
	}
    
	int find_parent(int value) {
		if (parents[value] < 0) { return value; }
		if (parents[parents[value]] < 0) { return parents[value]; }

		int prnt = find_parent(parents[value]);
		parents[value] = prnt;
		return prnt;
    }
	
	void join(int u, int v) {
		if ((u = find_parent(u)) == (v = find_parent(v))) { return; }
		--size;
		if (parents[v] < parents[u]) { std::swap(u,v); }
		parents[u] += parents[v];
		parents[v] = u;
	} 
}; 