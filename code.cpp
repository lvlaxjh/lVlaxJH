#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>
#include<iomanip>
#include<stack>
using namespace std;

string graph[] = { "v1-v2-v3","v2-v4","v3-v6-v7","v4-v8","v5-v8","v6-v7","v7","v8" };
bool *flag_graph = new bool[size(graph)];
void visit(string *graph, int v)
{
	cout << graph[v] << endl;
}
int NextAdjVex(string *graph, int v, int w)
{
	string a = graph[v];
	if (a.find(to_string(w + 1)) == (size(a) - 1))
	{
		return 0;
	}
	else
	{
		return atoi(a.substr(7, 7).c_str()) - 1;
	}
}
int FirstAdjVex(string *graph, int v)
{
	string a = graph[v];
	if (size(a) == 2)
	{
		return 0;
	}
	else
	{
		return (atoi(a.substr(4, 4).c_str()) - 1);
	}
}
void DFS(string *graph, int v)
{
	flag_graph[v] = true;
	visit(graph, v);
	for (int w = FirstAdjVex(graph, v); w > 0; w = NextAdjVex(graph, v, w))
	{
		if (!flag_graph[w])
		{
			DFS(graph, w);
		}
	}
}
void DFSTraverse(string *graph, int size_graph)
{
	for (int i = 0; i < size_graph; i++)
	{
		flag_graph[i] = false;
	}
	for (int i = 0; i < size_graph; i++)
	{
		if (!flag_graph[i])
		{
			DFS(graph, i);
		}
	}
}

int main()
{
	DFSTraverse(graph, size(graph));
	while (1);
	return 0;
}