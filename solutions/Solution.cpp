
#include <vector>
using namespace std;
class Solution {
    public:
        vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
            // write your code here
            int n = nums.size();
            vector<int> result(n, 0);
    
            for (int i = 0; i < n; ++i) {
                int count = 0;
                for (int j = 0; j < n; ++j) {
                    if (nums[j] < nums[i]) {
                        count++;
                    }
                }
                result[i] = count;
            }
    
            return result;
        }
    };

