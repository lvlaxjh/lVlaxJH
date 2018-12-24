#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>
#include<iomanip>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

int main()
{
	int size_of_num = 0;
	cin >> size_of_num;
	int *all_num = new int[size_of_num];
	for (int i = 0; i < size_of_num; i++)
	{
		cin >> all_num[i];
	}
	sort(all_num, all_num + size_of_num);
	for (int i = 0; i < size_of_num; i++)
	{
		cout << all_num[i] << ' ';
	}

	return 0;
}