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

void swap(int* A, int i, int j) {
    int b = A[i];
    A[i] = A[j];
    A[j] = b;
}

void reverse(int* A, int i, int j){
	while(i < j){
		swap(A, i, j);
		i++;
		j--;
	}
}

void shiftRight(int* a, int s, int e){
	int temp = a[e];
	for(int i = e; i > s; i--){
		a[i] = a[i-1];
	}
	a[s] = temp;
}

int* kthPermutation(int n, int k){
	int* nums = new int[n];
	int* factorial = new int[n+1];

	factorial[0] = 1;
	factorial[1] = 1;
	nums[0] = 1;
	
	for (int i = 2; i <= n; i++) {
		nums[i-1] = i;
		factorial[i] = i*factorial[i - 1];
	}
	
	if(k <= 1){
		return nums;
	}
	if(k >= factorial[n]){
		reverse(nums, 0, n-1);
		return nums;
	}
	
	k -= 1;
	for (int i = 0; i < n-1; i++){
		int fact = factorial[n-i-1];
		int index = (k/fact);
		shiftRight(nums, i, i+index);
		k = k - fact*index;
	}
	
	return nums;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int b, x;
        cin >> b >> x;
        int p = 1;
        while (x > pow(b, p)) {
            x -= pow(b, p);
            p += 1;
        }
        int idx = x % p;
        int nth = x / p;
        int* kth;
        kth = kthPermutation(b, nth);
        cout << kth[idx] << endl;
    }
    return 0;
}
