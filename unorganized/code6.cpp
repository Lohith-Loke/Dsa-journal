// include nessory header file and using namespace std;
#include <vector>
#include <iostream>
#include <time.h>
using namespace std;

int findMinPath(vector<vector<int>> &V, int r, int c)
{
    int R = V.size();
    int C = V[0].size();
    if (r >= R || c >= C)
        return 100000000; // Infinity
    if (r == R - 1 && c == C - 1)
        return 0;
    return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
}

int main()
{
    // create a vector of vector of int and fill it with random values
    vector<vector<int>> V;
    srand(time(NULL));
    for (size_t i = 0; i < 3; i++)
    {
        vector<int> row;
        for (size_t j = 0; j < 3; j++)
        {
            row.push_back(rand() % 100);
        }
        V.push_back(row);
    }
    // print the vector
    for (size_t i = 0; i < V.size(); i++)
    {
        for (size_t j = 0; j < V[i].size(); j++)
        {
            cout << V[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
