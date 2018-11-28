#include<iostream>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	int num = 0;
	int all = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		all = all + num;
	}
	cout << all;

	return 0;
}