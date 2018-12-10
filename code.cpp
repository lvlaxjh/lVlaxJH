#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>
#include<iomanip>
#include<stack>
#include<queue>
using namespace std;

string graph[] = { "1-2-3","2-4","3-6-7","4-8","5-2-8","6-7","7","8" };
int edgeset[2] = { 0,0 };
bool *flag_graph = new bool[size(graph)];
void edge(string *graph, int v)
{
	if (edgeset[0] == 0)
	{
		edgeset[0] = graph[v][0] - 48;
	}
	else
	{
		if (edgeset[1] == 0)
		{
			edgeset[1] = graph[v][0] - 48;
		}
		/*else
		{
			if (edgeset[0] != 0 && edgeset[1] != 0)
			{
				cout << edgeset[0] << "->" << edgeset[1] << endl;
				edgeset[0] = edgeset[1];
				edgeset[1] = graph[v][0] - 48;
			}
		}*/
	}
	if (edgeset[0] != 0 && edgeset[1] != 0)
	{
		cout << edgeset[0] << "->" << edgeset[1] << endl;
		if (size(graph[v]) == 1)
		{
			edgeset[0] = 0;
			edgeset[1] = 0;
		}
		else
		{
			edgeset[0] = edgeset[1];
			edgeset[1] = 0;
		}
	}
}
void visit(string *graph, int v)
{
	cout << graph[v][0] << endl;
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
	edge(graph, v);
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
	//
	graph_node = graph_node - 1;
	string *graph_sort = new string[size_graph];
	int flag = 0;
	bool flag_node = false;
	for (int i = 0; i < size_graph; i++)
	{
		if (i == graph_node)
		{
			flag_node = true;
		}
		if (flag_node)
		{
			graph_sort[flag] = graph[i];
			flag++;
		}
	}
	for (int i = 0; i < graph_node; i++)
	{
		graph_sort[size_graph - graph_node + i] = graph[i];
	}
	//for (int i = 0; i < size_graph; i++)
	//{
	//	cout << graph_sort[i] << endl;
	//}
	//while (1);
	//
	for (int i = 0; i < size_graph; i++)
	{
		if (!flag_graph[i])
		{
			DFS(graph_sort, i);
		}
	}
}
void BFSTraverse(string *graph, int size_graph, int graph_node)
{
	for (int i = 0; i < size_graph; i++)
	{
		flag_graph[i] = false;
	}
	//
	queue<int> Q;
	//
	graph_node = graph_node - 1;
	string *graph_sort = new string[size_graph];
	int flag = 0;
	bool flag_node = false;
	for (int i = 0; i < size_graph; i++)
	{
		if (i == graph_node)
		{
			flag_node = true;
		}
		if (flag_node)
		{
			graph_sort[flag] = graph[i];
			flag++;
		}
	}
	for (int i = 0; i < graph_node; i++)
	{
		graph_sort[size_graph - graph_node + i] = graph[i];
	}
	for (int i = 0; i < size_graph; i++)
	{
		if (!flag_graph[i])
		{
			flag_graph[i] = true;
			visit(graph_sort, i);
			edge(graph_sort, i);
			Q.push(i);
			while (!Q.empty())
			{
				int u = Q.front();
				Q.pop();
				for (int w = FirstAdjVex(graph_sort, u); w > 0; w = NextAdjVex(graph_sort, u, w))
				{
					if (!flag_graph[w])
					{
						flag_graph[w] = true;
						visit(graph_sort, w);
						edge(graph_sort, i);
						Q.push(w);
					}
				}
			}
		}
	}
}
int main()
{
	int input = 0;
	cout << "输入开始节点" << "-范围:" << "0" << "-" << size(graph) << endl;
	cin >> input;
	//DFSTraverse(graph, size(graph), input);
	BFSTraverse(graph, size(graph), input);
	while (1);
	return 0;
}