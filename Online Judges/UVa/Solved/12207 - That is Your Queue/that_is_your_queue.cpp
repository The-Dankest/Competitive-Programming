#include <list>
#include <map>
#include <iostream>

using namespace std;

int main() {
    int count = 1, n, m;
    cin >> n >> m;
    while (n != 0) {
        cout << "Case " << count++ << ":" << endl;
        list<int> line;
        for (int i = 1; i <= min(n, 1000); ++i) {
            line.push_back(i);
        }
        for (int i = 0; i < m; ++i) {
            char a;
            int x;
            cin >> a;
            if (a == 'E') {
                cin >> x;
                line.remove(x);
                line.push_front(x);
            } else {
                cout << line.front() << endl;
                line.push_back(line.front());
                line.pop_front();
            }
        }
        cin >> n >> m;
    }
    return 0;
}