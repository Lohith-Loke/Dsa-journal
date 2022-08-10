#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

class Solution
{
private:
    void tostring(vector<string> v)
    {
        int len = v.size();
        for (int i = 0; i < len; i++)
        {
            cout << v[i] << ' ';
        }
    }

public:
    vector<string> fizzBuzz(int A)
    {
        vector<string> a(A);
        string data = "-1";
        for (int i = 1; i < A; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                // data = "FizzBuzz";
                printf("FizzBuzz\n");
                a.push_back("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                // data = "Fizz";
                printf("Fizz\n");
                   a.push_back("Fizz");

            }
            else if (i % 5 == 0)
            {
                printf("Buzz\n");
                // data = "Buzz";
            }
            else {
                printf("%d\n",i);
            }
        }
        tostring(a);
        return a;
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    s.fizzBuzz(20);
    // printf("hello ");
    return 0;
}
