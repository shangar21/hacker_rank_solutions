#include <bits/stdc++.h>
#include <cmath>
#define FOR(x, to) for (x = 0; x < (to); ++x)
#define FORR(x, arr) for (auto& x : arr)

using namespace std;

vector<string> split_string(string);

void print_vector(vector<int> vec) {
  FORR(x, vec) cout << "|" << x;
  cout << "|" << endl;
}

int merge(vector<int>& arr, int l, int m, int r)
{
	int count = 0;
	int n1 = m-l+1;
	int n2 = r-m;
	int L[n1], R[n2];

	for (int i = 0; i < n1; i++)
	{
		L[i] = arr[l + i];
	}
	
	for (int j = 0; j < n2; j++)
	{
		R[j] = arr[m + 1 + j];
	}

	int i = 0;
	int j = 0;
	int k = l;

	while(i<n1 && j<n2)
	{
		if(L[i] <= R[j])
		{
			arr[k] = L[i];
			i++;
		}
		else{
			count += m-i;
			arr[k] = R[j];
			j++;
		}
		k++;
	}

	while(i < n1)
	{
		arr[k] = L[i];
		i++;
		k++;
	}

	while(j < n2)
	{
		arr[k] = R[j];
		j++;
		k++;
	}

	return count;
}

int mergeSort(vector<int>& arr, int l, int r)
{
	int count = 0;

    if (r-l <= 1)
    {
        return 0;
    }

    int m = (l+r)/2;
    count += mergeSort(arr, l, m);
    count += mergeSort(arr, m+1, r);
    count += merge(arr, l, r, (l+r)/2);

    return count;
}


// Complete the countInversions function below.
long countInversions(vector<int> arr) {
    return mergeSort(arr, 0, arr.size()-1);

}

int main()
{
	vector<int> arr{2,1,3,1,2};
	int count = countInversions(arr);
	print_vector(arr);
	printf("%d\n", count);
}