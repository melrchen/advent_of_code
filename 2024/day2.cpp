#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>
#include <cmath>

using namespace std;

int is_valid(vector<int> v) {
    //  to be valid it has to be all increasing or all decreasing
    //  and only be min 1 max 3
    int valid = 1;
    for (int i = 1; i < v.size(); i++) {
        if (i > 1) {
            if ((v[i] > v[i-1]) != (v[i-1] > v[i-2])) {
                valid = 0;
                break;
            }
        }
        int diff = abs(v[i] - v[i-1]);
        if (diff < 1 || diff > 3) {
            valid = 0;
            break;
        }
    }
    return valid;
}



int main() {

    ifstream input_file ("inputs/day2.txt");
    string input_line;

    int part1 = 0;
    int part2 = 0;

    if ( input_file.is_open() ) { // always check whether the file is open
        while (getline(input_file, input_line)) {
            stringstream iss(input_line);
            int number;
            vector<int> v;
            while ( iss >> number ) {
                v.push_back(number);
            }
            part1 += is_valid(v);

            // accept one bad character
            if (is_valid(v)) {
                part2++;
            } else {
                for (int i = 0; i < v.size(); i++) {
                    vector<int> new_v;
                    copy(v.begin(), v.end(), back_inserter(new_v));
                    new_v.erase(new_v.begin()+i);
                    if (is_valid(new_v)) {
                        part2++;
                        break;
                    }
                }
            }
        }
    }

    cout << "part 1: " << part1 << endl;
    cout << "part 2: " << part2 << endl;
    return 0;
}
