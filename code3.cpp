#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int kthSmallest(vector<vector<int>> &matrix, int k)
    {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (size_t i = 0; i < matrix.size(); i++)
        {
            vector<int> a = matrix[i];
            for (size_t j = 0; j < a.size(); j++)
            {
                // cout << a[j] << " ";
                pq.push(a[j]);
            }
            // cout << "\n";
        }

        while (pq.empty() == false)
        {
            if (k == 1)
            {
                return pq.top();
            }
            pq.pop();
            k--;
        }
        return -1;
    }
};
// [[1,5,9],[10,11,13],[12,13,15]]
int main(int argc, char const *argv[])
{
    // vector<int> a={1,5,9};
    // vector<vector<int>> z = {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};
    vector<vector<int>> z = {{-5}};

    Solution s = Solution();
    s.kthSmallest(z, 1);

    return 0;
}
