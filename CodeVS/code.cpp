#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>
#include<iomanip>
#include<stack>
using namespace std;
int main()
{
	stack<string> sta;
	string b = "";
	char  strs[100];
	cin.getline(strs, 100);
	char *ptr;
	char *p;
	ptr = strtok(strs, " ");
	while (ptr != NULL) {
		sta.push(ptr);
		ptr = strtok(NULL, " ");
	}
	while (!sta.empty())
	{
		cout << sta.top() << " ";
		sta.pop();
	}

	while (1);
	return 0;
}