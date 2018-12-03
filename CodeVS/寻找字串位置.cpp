#include<iostream>

#include<cstring>

using namespace std;

string a, b;

int main()

{

cin >> a >> b;

cout << a.find(b) + 1 << endl;

return 0;

}