#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int visited[9];
int arr[9];
void dfs(int cnt)
{
	if (cnt == m)
	{
		for (int i = 0; i < m; i++)
			cout << arr[i] << " ";
		cout << "\n";
		return;
	}
	
	for (int i = 1; i <= n; i++)
	{
		if (!visited[i])
		{
			visited[i] = 1;
			arr[cnt] = i;
			dfs(cnt + 1);
			visited[i] = 0;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie();
	cout.tie();

	cin >> n >> m;

	dfs(0);

	return 0;
}