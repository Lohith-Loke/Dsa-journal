string Solution::solve(string A) {
    int i;
    vector<string>tokens;
    string token;
    string result;
    for (int i =0;i<A.size();i++){
        if (A[i]==" "){
            if (token!=""){
                tokens.push_back(token);
                token=""; 
                continue;
            }
            else{
                continue;
            }
        }
        token.push_back(A[i]);
    }
    result.append(" ");
    for(i=tokens.size()-1;i>=0;i--)
        result.append(tokens[i]+' ');
    // result;
        
    A=result;      
    return A;
}

int main(){
    Solution s=Solution();
    s.solve('abcd abcd');
}