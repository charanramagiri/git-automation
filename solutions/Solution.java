package solutions;
public class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        //write your code 
        int n = nums.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (nums[j] < nums[i]) {
                    count++;
                }
            }
            result[i] = count;
        }

        return result;
    }
}
