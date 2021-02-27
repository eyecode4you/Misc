// TYPE INFERENCE EX
#include "pch.h"
#include <iostream>
#include <typeinfo>
#include <string>
using namespace std;

/*	3:
	lT - lefthand side argument
	lR - righthand side argument
	tf - template function*/
template <typename lT, typename rT>
auto tf(const lT &lhs, const rT &rhs) { //auto return type derived from expression of return
	return lhs + rhs;
}

int main() {
	//1
	int i = 47;
	const char * cstr = "This is a C-Style String";
	const string sclass = string("This is a String Class String");

	auto x = "This is a C-String"; //Strong, typesafe
	decltype(x) y; //declaretype, derives type based on expression x(C-String), y will be derived of type x

	//typeid() to get internal name of types
	cout << "Type of i is: " << typeid(i).name() << endl;
	cout << "Type of cstr is: " << typeid(cstr).name() << endl;
	cout << "Type of sclass is: " << typeid(sclass).name() << endl;
	cout << "Type of x is: " << typeid(x).name() << endl;
	cout << "Type of y is: " << typeid(y).name() << "\n" << endl;

	/*	2: Make string class iterator (it)
		begin() returns iterator, auto declares type of iterator*/
	for (auto it = sclass.begin(); it != sclass.end(); ++it) {
		cout << *it << " ";
	}
	cout << endl;

	//2: Range-based example of above
	for (auto c : sclass) {
		cout << c << " ";
	}
	cout << "\n" << endl;

	//3
	auto z = tf<string, const char *>(sclass, cstr);
	cout << "z is " << z << endl;
	cout << "type of z is " << typeid(z).name() << endl;

	return 0;
}