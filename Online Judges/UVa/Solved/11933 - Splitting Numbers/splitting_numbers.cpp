#include <iostream>

using namespace std;

int main ()
{
    unsigned int n;
    cin >> n;
    while (n != 0) {

        unsigned int a = 0, b = 0;

        int setBits = 0;
        unsigned int mask = 0x1;
        // loop through all bits
        for (; mask != 0; mask <<= 1) {
            if ((n & mask) > 0) {
                ++setBits;
                if (setBits % 2 == 0) {
                    b |= mask;
                } else {
                    a |= mask;
                }
            }
        }

        cout << a << " " << b << endl;

        cin >> n;
    }
 
    return 0;
}