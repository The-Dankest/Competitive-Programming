#include <queue>
#include <iostream>
#include <utility>
#include <tuple>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    priority_queue<tuple<int,int,int,string>, vector<tuple<int,int,int,string> >, less<tuple<int,int,int,string> > > oldest;
    priority_queue<tuple<int,int,int,string>, vector<tuple<int,int,int,string> >, greater<tuple<int,int,int,string> > > youngest;
    for (; n > 0; --n) {
        string name;
        int day, month, year;
        cin >> name >> day >> month >> year;
        tuple<int,int,int,string> person;
        get<0>(person) = year;
        get<1>(person) = month;
        get<2>(person) = day;
        get<3>(person) = name;
        oldest.push(person);
        youngest.push(person);
    }
    cout << get<3>(oldest.top()) << endl;
    cout << get<3>(youngest.top())<< endl;
    return 0;
}