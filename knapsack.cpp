
int unboundedKnapsack(int k, vector<int> arr)
{

	int i = 0;
	int j = 1; 
	vector<int> multiples(1, arr[0]);

	while(i < arr.length()){

		if (multiples[j-1] + arr[i] > k){
			i++;
		}
		multiples.push_back(multiples[j-1] + arr[i]);
		j++;
	} 

	cout << multiples;

	return 0;
}


int main()
{
	vector<int> arr{3,7,9,11}
	unboundedKnapsack(13, arr)
	return 0;
}