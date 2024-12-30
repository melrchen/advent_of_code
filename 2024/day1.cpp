#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <cmath>

int main() {
    using namespace std;
    ifstream input_file ("inputs/day1.txt");
    string input_line;
    vector<int> list_1;
    vector<int> list_2;

    if ( input_file.is_open() ) { // always check whether the file is open
        while (getline(input_file, input_line)) {
            list_1.push_back(stoi(input_line.substr(0, 5)));
            list_2.push_back(stoi(input_line.substr(8, 5)));
        }
    }
    sort(list_1.begin(), list_1.end());
    sort(list_2.begin(), list_2.end());

    int sum = 0;

    for (int i = 0; i < list_1.size(); i++) {
        sum += abs(list_1[i] - list_2[i]);
    }
    cout << "part 1: " << sum << endl;

    int sum2 = 0;
    for (int i = 0; i < list_1.size(); i++) {
        sum2 += list_1[i] * count(list_2.begin(), list_2.end(), list_1[i]);
    }

    cout << "part 2: " << sum2 << endl;
    return 0;
}