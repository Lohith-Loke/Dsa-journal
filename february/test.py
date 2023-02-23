def generate_subsequences(arr):
    if len(arr) == 0:
        return [[]]  # base case: empty array has one subsequence, which is the empty sequence
    else:
        subseqs_without_first = generate_subsequences(arr[1:])  # recursive call without first element
        subseqs_with_first = [[arr[0]] + subseq for subseq in subseqs_without_first]  # add first element to each subsequence
        return subseqs_without_first + subseqs_with_first  # combine the two sets of subsequences
s="file"
print(generate_subsequences(s))
