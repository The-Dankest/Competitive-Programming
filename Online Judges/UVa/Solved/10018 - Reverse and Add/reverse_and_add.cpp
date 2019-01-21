#include <iostream>

using namespace std;

unsigned int n_rev(unsigned int a) {
    unsigned int b = 0;
	while(a != 0)
	{
		int rem = a % 10;
		b = b * 10 + rem;
		a /= 10;
	}
    return b;
}

bool is_p(unsigned int a) {
    unsigned int b = n_rev(a);
    return a == b;
}

int main() {

    unsigned int n;
    cin >> n;
    for (; n > 0; --n) {

        unsigned int a;
        int iter = 0;
        cin >> a;
        do {
            a += n_rev(a);
            ++iter;
        } while (!is_p(a));

        cout << iter << " " << a << endl;

    }

    return 0;
}