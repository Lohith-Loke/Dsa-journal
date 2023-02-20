#include <iostream>
#include <vector>

using namespace std;



class Solution
{
public:
    vector<int> merge(vector<int> &arr, int j)
    {
        int i = j - 1;
        int k = j;
        vector<int> res;
        while ((i > -1) && (k < arr.size()))
        {
            if (abs(arr[i]) < arr[k])
            {
                res.push_back(abs(arr[i]));
                i -= 1;
            }
            else
            {
                res.push_back(arr[k]);
                k += 1;
            }
        }
        while (i > -1)
        {
            res.push_back(arr[i]);
            i -= 1;
        }
        while (k < arr.size())
        {
            res.push_back(arr[k]);
            k += 1;
        }
        return res;
    }
    vector<int> sortedSquares(vector<int> &nums)
    {
        int i = 0;
        while (i < nums.size())
        {
            if (nums[i] >= 0)
            {
                break;
            }
        }
        if (i > 0)
        {
            nums = merge(nums, i);
        }
        for (int i = 0; i < nums.size(); i++)
        {
            nums[i] = nums[i] * nums[i];
        }
        return nums;
    }
};

int main()
{
    Solution s = Solution();
    vector<int> arr = {-4, -1, 0, 3, 10};
    vector<int> res = s.sortedSquares(arr);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
    return 0;
}