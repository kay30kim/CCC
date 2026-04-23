//
// Created by socce on 2024-08-31.
//

#include <iostream>
#include <array>
#include <string>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	int array[5001];
	int dp_even[5001];
	int dp_odd[5001];
	for (int i = 0; i < n; i++) {
		int inp;
		cin >> inp;
		array[i] = inp;
		dp_odd[i] = 0;
	}
	cout << 0 << " ";
	if (n == 1) {
		return 0;
	}
	int smallest = 2147483647;
	for (int i = 0; i < n-1; i++) {
		dp_even[i] = abs(array[i]-array[i+1]);
		smallest = min(smallest, abs(array[i]-array[i+1]));
	}
	cout << smallest << " ";
	for (int i = 2; i < n; i++) {
		if (i % 2 == 0) { // odd length
			int small = 2147483647;
			for (int j = 0; j < n-i; j++) {
				dp_odd[j] = dp_odd[j+1] + abs(array[j]-array[j+i]);
				small = min(small, dp_odd[j]);
			}
			cout << small << " ";
		}else { // even length
			int small = 2147483647;
			for (int j = 0; j < n-i; j++) {
				dp_even[j] = dp_even[j+1] + abs(array[j]-array[j+i]);
				small = min(small, dp_even[j]);
			}
			cout << small << " ";
		}
	}
	return 0;
}