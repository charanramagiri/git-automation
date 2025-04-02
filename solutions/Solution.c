#include <stdio.h>

// Function to find how many numbers are smaller than each element in the array
void smallerNumbersThanCurrent(int* nums, int n, int* result) {
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (nums[j] < nums[i]) {
                count++;
            }
        }
        result[i] = count;
    }
}
