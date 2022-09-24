#include <iostream>
#include <string.h>
using namespace std;

int stoi_fun(string a)
{
    int sum = 0;
    for (char i : a)
    {
        sum *= 10;
        sum += (int)(i - '0');
    }
    return sum;
}

string incrementTime(string a)
{
    int hours = stoi_fun(a.substr(0, 2));
    int min = stoi_fun(a.substr(3, 5));
    int carry = (min + 1) / 60;
    min = (min + 1) % 60;
    hours = (hours + carry) % 24;
    string hour = "" + to_string(hours);
    if (hour.length() == 1)
        hour = "0" + hour;
    string minutes = "" + to_string(min);
    if (minutes.length() == 1)
        minutes = "0" + minutes;
    // cout<<hour<<" "<<minutes<<"\n";
    return hour + ":" + minutes;
}

class Solution
{
public:
    int solve(string A)
    {
        int min = 0;
        string B = A;
        while (true)
        {
            // cout<<B<<" ";
            if (B[0] == B[4] && B[1] == B[3])
                break;
            B = incrementTime(B);
            min++;
        }
        return min;
    }
};

int main()
{
    Solution s;
    cout << s.solve("00:00") << "\n";
    cout << s.solve("23:59") << "\n";
    cout << s.solve("00:01") << "\n";
    cout << s.solve("01:00") << "\n";
    cout << s.solve("01:01") << "\n";
    cout << s.solve("01:02") << "\n";
    cout << s.solve("01:03") << "\n";
    cout << s.solve("06:04") << "\n";
    return 0;
}
