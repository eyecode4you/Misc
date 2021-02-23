//template function example
//Based on C++ Templates and the STL By: Bill Weinman, LinkedIn Learning


#include "pch.h"
#include <string>
#include <iostream>
using namespace std;

template <class X>
X maxof(const X &a, const X &b) {
	return a > b ? a : b;
}

// Template Specialization will be built depending on type, here type is replaced by type
//"type" maxof(const "type" &a, const "type" &b) {
//	return a > b ? a : b;
//}

int main() {
	int a = 7, b = 9;
	cout << "MAX: " << maxof(a, b) << endl; //maxof<int>
	cout << "MAX: " << maxof<short int>(a, b) << endl; //maxof<short int>
	cout << "MAX: " << maxof<long int>(a, b) << endl; //maxof<long int>

	float c = 7, d = 9;
	cout << "MAX: " << maxof(c, d) << endl; //maxof<float>

	char e = '7', f = '9';
	cout << "MAX: " << maxof(e, f) << endl; //maxof<char>

	string g = "seven", h = "nine"; //"seven" is > Alphabetically
	cout << "MAX: " << maxof(g, h) << endl; //maxof<string>

	return 0;
}
