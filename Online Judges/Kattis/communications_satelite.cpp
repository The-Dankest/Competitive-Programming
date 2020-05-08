#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

struct Edge {
    float v; // first vertex
    float u; // second vertex
    float w; // weight of the edge
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

class UnionFind {                                // OOP style
private:
  vi p, rank, setSize;                           // vi p is the key part
  int numSets;
public:
  UnionFind(int N) {
    p.assign(N, 0); for (int i = 0; i < N; ++i) p[i] = i;
    rank.assign(N, 0);                           // optional speedup
    setSize.assign(N, 1);                        // optional feature
    numSets = N;                                 // optional feature
  }

  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int numDisjointSets() { return numSets; }      // optional
  int sizeOfSet(int i) { return setSize[findSet(i)]; } // optional

  void unionSet(int i, int j) {
    if (isSameSet(i, j)) return;                 // i and j are in same set
    int x = findSet(i), y = findSet(j);          // find both rep items
    if (rank[x] > rank[y]) swap(x, y);           // keep x 'shorter' than y
    p[x] = y;                                    // set x under y
    if (rank[x] == rank[y]) ++rank[y];           // optional speedup
    setSize[y] += setSize[x];                    // combine set sizes at y
    --numSets;                                   // a union reduces numSets
  }
};

int main() {
    int n;
    scanf("%d", &n);
    
    priority_queue<Edge, vector<Edge>, EdgeCompare> edges;
    UnionFind vertices (n);
    vector<Edge> satelites;

    for (int i = 0; i < n; ++i) {
        int x1, y1, r1;
        scanf("%d %d %d", &x1, &y1, &r1);
        Edge e;
        e.u = x1;
        e.v = y1;
        e.w = r1;

        for (int j = 0; j < satelites.size(); ++j) {
            Edge f = satelites[j];
            Edge g;
            g.u = j;
            g.v = i;
            g.w = sqrt(pow(e.u - f.u, 2) + pow(e.v - f.v, 2)) - f.w - e.w;
            edges.push(g);
        }

        satelites.push_back(e);
    }

    float weight = 0;
    while (vertices.numDisjointSets() != 1) {
        Edge e = edges.top();
        if (vertices.findSet(e.v) != vertices.findSet(e.u)) {
            vertices.unionSet(e.v, e.u);
            weight += e.w;
        }
        edges.pop();
    }
    printf("%f\n", weight);
}