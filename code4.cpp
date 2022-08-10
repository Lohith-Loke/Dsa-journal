#include <cstdlib>
#include <iostream>
#include <vector>
#include <time.h>
using namespace std;

void bubbleSort(vector<int> &vec)
{
    int len=vec.size()-1;
    for (size_t i = 0; i < len; ++i)
    {
        for (size_t j = 0; j < len-i; ++j)
        {
            if (vec.at(j) > vec.at(j + 1))
                swap(vec.at(j), vec.at(j + 1));
        }
    }
}

int main()
{
    vector<int> l;
    srand(time(0));
    for (int i = 0; i < 100; i++)
    {
        l.push_back(rand());
    }
     
    bubbleSort(l);
     int len = l.size();
    if (len % 2 != 0)
    {
        cout << "median = " << l[len / 2] << endl;
    }
    else
    {
        int m = len / 2;
        double avg = (double)(l[m] + l[m - 1]) / 2;
        cout << "median " << avg << endl;
    }
    return 0;
}
