#include<iostream>
#include<string>
#include<stdio.h>
#include<iomanip>
using namespace std;
int main()
{
	int i = 0;

	string s[1000];

	while (cin >> s[i]) {
		i++;
	}

	while (i--) {
		cout << s[i] << ' ';
	}

	return 0;
}