#include <iostream>

using namespace std;

int main() {

    unsigned int b1, c1, g1, b2, c2, g2, b3, c3, g3;
    unsigned int bcg, bgc, cbg, cgb, gbc, gcb;
    unsigned int min_moves;
    while (cin >> b1 >> g1 >> c1 >> b2 >> g2 >> c2 >> b3 >> g3 >> c3) {
        bcg = c1 + g1 + b2 + g2 + b3 + c3;
        bgc = c1 + g1 + b2 + c2 + b3 + g3;
        cbg = b1 + g1 + c2 + g2 + b3 + c3; 
        cgb = b1 + g1 + b2 + c2 + c3 + g3;
        gbc = b1 + c1 + c2 + g2 + b3 + g3;
        gcb = b1 + c1 + b2 + g2 + c3 + g3;
        min_moves = min(min(bcg, bgc), min(min(cbg, cgb), min(gbc, gcb)));
        if (min_moves == bcg) {
            cout << "BCG " << min_moves << endl;
        } else if (min_moves == bgc) {
            cout << "BGC " << min_moves << endl;
        } else if (min_moves == cbg) {
            cout << "CBG " << min_moves << endl;
        } else if (min_moves == cgb) {
            cout << "CGB " << min_moves << endl;
        } else if (min_moves == gbc) {
            cout << "GBC " << min_moves << endl;
        } else if (min_moves == gcb) {
            cout << "GCB " << min_moves << endl;
        }
    }
    return 0;
}