#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;
class Solution
{
private:
    int split(vector<int> a, int ramax = -1)
    {
        int len = a.size();
        int armax = ramax;
        if (len > 1)
        {
            int min_ele = *min_element(a.begin(), a.end());
            // cout << min_ele;
            int minElementIndex = std::min_element(a.begin(), a.end()) - a.begin();
            int area = min_ele * len;
            cout << area;
            armax = max(area, armax);
            // split is possible

            a.erase(a.begin() + minElementIndex);
            size_t const half_size = a.size() / 2;

            vector<int> half1(a.begin(), a.begin() + half_size);
            vector<int> half2(a.begin() + half_size + 1, a.end());
            cout << "\nhalf 1\n";
            for (auto x : half1)
            {
                cout << x << " ";
            }
            cout << "\nhalf 2\n";
            for (auto x : half2)
            {
                cout << x << " ";
            }
            if (half1.size()>0){
                split(half1)
            } 
            return max(armax,)
        }
        else
        {
            if (armax > 0)
            {
                return armax;
            }
            else
            {
                return max(armax, 1 * a[0]);
            }
        }
        // its a single reactangle
    }

public:
    int solve(vector<int> a)
    {
        // split and check area
        return split(a);
    }
};

int main()
{
    vector<int> hights = {2, 3};
    Solution a = Solution();
    cout << a.solve(hights);
}
