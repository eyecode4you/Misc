//IMPACT ON HEADER FILES EX
#include "pch.h"
#include "stack.h"
#include <iostream>
#include <string>
using namespace std;

constexpr int nums[] = { 1,2,3,4,5 };
constexpr const char *strs[] = { "one", "two", "three", "four", "five" };

int mainC() {
	try {
		Stack<int> si(5);

		cout << "si size: " << si.size() << endl;
		cout << "si top: " << si.top() << endl;

		for (int i : nums) {
			si.push(i);
		}

		cout << "si top after push: " << si.top() << endl;
		cout << "si is: " << (si.isFull() ? "" : "not ") << "full" << endl;

		while (!si.isEmpty()) {
			cout << "popped " << si.pop() << endl;
		}
	}
	catch (StackException &e) {
		cout << "Stack Error :" << e.what() << endl;
	}

	try {
		Stack<string> ss(5);

		cout << "ss size: " << ss.size() << endl;
		cout << "ss top: " << ss.top() << endl;

		for (const char *s : strs) {
			ss.push(s);
		}

		cout << "ss top after push: " << ss.top() << endl;
		cout << "ss is: " << (ss.isFull() ? "" : "not ") << "full" << endl;

		while (!ss.isEmpty()) {
			cout << "popped " << ss.pop() << endl;
		}
	}
	catch (StackException &e) {
		cout << "Stack Error :" << e.what() << endl;
	}

	return 0;
}