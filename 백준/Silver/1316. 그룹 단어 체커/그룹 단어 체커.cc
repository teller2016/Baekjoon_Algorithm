#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;
	string user;
	int count = 0;

	for (int i = 0; i < n; i++)
	{
		cin >> user;
		char first;
		int flag = 0;

		for (int j = 0; j < user.length(); j++)
		{
			first = user[j];

	

			while (1)
			{
				
				if (user[j] == user[j + 1])
					j++;
				else
					break;
			}

			if (user[j + 1] == '\n')
				break;

			for (int k = j+1; k < user.length(); k++)
			{
				if (user[k] == first)
					flag = 1;
			}

		}
		if (flag)
			continue;

		count++;

	}


	cout << count;
	return 0;
}