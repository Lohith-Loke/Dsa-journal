#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void printarr(vector<int> &res)
    {
        for (int i = 0; i < res.size(); i++)
        {
            cout << res[i] << " ";
        }
        cout << "\n--end--\n";
    }
    int len(vector<int> &arr)
    {
        return arr.size();
    }
    vector<int> merge(vector<int> &arr, int j)
    {
        vector<int> res;
        int i = j - 1;
        int k = j;
        while ((i > -1) && (k < arr.size()))
        {
            cout << abs(arr[i]) << arr[k] << "\n";
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
            i += 1;
        }
        while (k < len(arr))
        {
            res.push_back(arr[k]);
            k += 1;
        }
        return res;
    }
    vector<int> sortedSquares(vector<int> &nums)
    {
        int i = 0;
        int vc = nums.size();
        while (i < vc)
        {
            if (nums[i] >= 0)
            {
                // find first non -ve number index
                break;
            }
            i += 1;
        }
        nums = merge(nums, i);
        printarr(nums);
        for (int i = 0; i < nums.size(); i++)
        {
            nums[i] = nums[i] * nums[i];
        }
        // o(nlog(n)) aproach
        // sort(nums.begin(),nums.end());
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