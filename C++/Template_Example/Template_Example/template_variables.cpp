//Template Variables Example
#include "pch.h"
#include <iostream>
using namespace std;

template<typename Z>
constexpr Z pi = Z(3.1415926535897932385L);

template<typename Z>
Z area_of_circle(const Z &r){
	return r * r * pi<Z>;
}

int mainB() {
	cout.precision(20);
	cout << "Pi:" << pi<long double> << endl; //reduced precision (Windows)
	cout << "Area of Circle r=3: " << area_of_circle<long double>(3) << endl;
	return 0;
}