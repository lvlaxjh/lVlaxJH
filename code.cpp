#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>
#include<iomanip>
#include<stack>
using namespace std;

string graph[] = { "1-2-3","2-4","3-6-7","4-8","5-8","6-7","7","8" };
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
		return atoi(a.substr(4, 4).c_str()) - 1;
	}
}
int FirstAdjVex(string *graph, int v)
{
	string a = graph[v];
	if (size(a) == 1)
	{
		return 0;
	}
	else
	{
		return (atoi(a.substr(2, 2).c_str()) - 1);
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
void DFSTraverse(string *graph, int size_graph, int graph_node)
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
	int input = 0;
	cout << "输入开始节点" << "-范围:" << "0" << "-" << size(graph) << endl;
	cin >> input;
	DFSTraverse(graph, size(graph), input);
	while (1);
	return 0;
}