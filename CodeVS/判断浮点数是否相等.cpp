#include<iostream>
#include<string>
using namespace std;
int main()
{
	double a = 0.0;
	double b = 0.0;
	cin >> a >> b;
	int c = (a / 0.000001) % 100000;
	int d = (b / 0.000001) % 100000;
	//while (1);
	if (a == b)
	{
		cout << "yes";
	}
	else
	{
		cout << "no";
	}

	return 0;
}