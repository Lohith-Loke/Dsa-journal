#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;
class Solution
{
private:
    int rev(int i)
    {
        int remainder = 0;
        int rev = 0;
        while (i != 0)
        {
            remainder = i % 10;
            rev = rev * 10 + remainder;
            i /= 10;
        }
        return rev;
    }

public:
    int countNicePairs(vector<int> &nums)
    {
        int len = nums.size();
        vector<int> revarr;

        for (size_t i = 0; i < len; i++)
        {
            cout <<rev(nums[i]) << '\n';
            revarr.push_back(rev(nums[i]));
        }
        map<int, int> data;
        for (size_t i = 0; i < nums.size(); i++)
        {
            
        }
        
        return 0;
    }
};
int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<int> num = {42, 11, 1, 97};
    s.countNicePairs(num);
    return 0;
}
