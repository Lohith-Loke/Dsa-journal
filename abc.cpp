/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *Solution::getIntersectionNode(ListNode *A, ListNode *B)
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if (A == NULL || B == NULL)
    {
        return NULL;
    }
    ListNode *a = A;
    ListNode *b = B;
    while (a != b)
    {
        a = a == NULL ? B : a->next;
        b = b == NULL ? A : b->next;
    }
    return a;
}
int main(int argc, char const *argv[])
{
    1 1
0
3 5 2 3
    return 0;
}
