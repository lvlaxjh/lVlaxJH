#include<iostream>
#include<string>
using namespace std;
int main()
{
	int num;
	int Max = 1;
	int Min = 1;
	int n = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		if (i == 0)
		{
			Max = num;
			Min = num;
		}
		else
		{
			if (num > Max)
			{
				Max = num;
			}
			if (num < Min)
			{
				Min = num;
			}
			else
			{
				num = num;
			}
		}
	}
	cout << Min << ' ' << Max;
	return 0;
}