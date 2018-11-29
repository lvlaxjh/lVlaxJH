#include<iostream>
#include<string>
#include<stdio.h>
#include<iomanip>
using namespace std;
int main()
{
	double a = 0.0;
	double b = 0.0;
	cin >> a >> b;
	cout << int(a*b / 100 + 0.5) * 10;
}