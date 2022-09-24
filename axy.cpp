#include <iostream>
#include <stack>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

vector<int> loaddata(vector<int> a, bool rev = false)
{
    if (rev)
    {
        reverse(a.begin(), a.end());
    }
    stack<int> s;
    vector<int> left;
    s.push(0);
    left.push_back(0);
    for (int i = 1; i < a.size(); i++)
    {
    l1:
        if (a[i] <= a[s.top()])
        {
            s.pop();
            if (s.empty())
            {
                s.push(i);
                left.push_back(0);
            }
            else
            {
                goto l1;
            }
        }
        else
        {
            // a is larger compared to so its top left=stack +1
            left.push_back(s.top() + 1);
            s.push(i);
        }
    }

    return left;
}

int main()
{
    vector<int> a = {1, 1};
    vector<int> left = loaddata(a);
    vector<int> r = loaddata(a, true);
    stack<int> s;
    cout << "a=\n";
    for (int i =   0; i <a.size(); i++)
    {
        cout << a[i] << " ";
    }
    cout << " \nright \n";
    reverse(r.begin(), r.end());
    for (int i = 0; i < r.size(); i++)
    {
        r[i] = a.size()-1 - r[i];
        cout << r[i] << " ";
        }
    cout << " \nleft \n";

    for (int i = 0; i < left.size(); i++)
    {
        cout << left[i] << " ";
    }
    int area = 0;
    int armax= -1;
    cout << " \narea \n";

    for (int i = 0; i < a.size(); i++)
    {
        // cout << a[i] << " \n";
        // cout<<r[i] - left[i] + 1<<"\n";

        area = a[i] * (r[i] - left[i] + 1);
        cout << area << " ";
        armax=max(armax,area);
    }
    cout<<"\narmax="<<armax;
    return 0;
}