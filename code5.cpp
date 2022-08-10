#include <vector>
#include <iostream>
using namespace std;

int searchNumOccurrence(vector<int> &V, int k, int start, int end)
{
    if (start > end)
        return 0;
    int mid = (start + end) / 2;
    if (V[mid] < k)
        return searchNumOccurrence(V, k, mid + 1, end);
    if (V[mid] > k)
        return searchNumOccurrence(V, k, start, mid - 1);
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
}

int main(int argc, char const *argv[])
{
    vector<int> V;
    for (size_t i = 0; i < 100; i++)
    {
        V.push_back(10);
    }
    searchNumOccurrence(V,10,0,V.size());
    return 0;
}
