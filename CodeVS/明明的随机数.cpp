#include<iostream>
#include<string>
#include<time.h>
#include<algorithm>
using namespace std;
int main()
{
	int all_num;
	cin >> all_num;
	int *num_array = new int[all_num];
	for (int i = 0; i < all_num; i++)
	{
		cin >> num_array[i];
	}
	sort(num_array, num_array + all_num);
	int flag1 = 0;
	int flag2 = 0;
	int num = 0;
	for (int n = 0; n < all_num; n++)
	{
		num++;
		flag1 = num_array[n];
		if (n + 1 != all_num)
		{
			flag2 = num_array[n + 1];
		}
		else
		{
			break;
		}
		if (flag1 == flag2)
		{
			num_array[n] = 0;
			num--;
		}
	}
	cout << num << endl;
	for (int a = 0; a < all_num; a++)
	{
		if (num_array[a] != 0)
		{
			cout << num_array[a] << " ";
		}
	}
	return 0;
}