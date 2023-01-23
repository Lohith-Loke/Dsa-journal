vector<long long> nextLargerElement(vector<long long> a, int n){
        vector<ll> ng(n , -1);

        vector<ll> list; // we will store index


        for(int i = 0;i<n;i++){
            ll cur = a[i];
            while(list.size() != 0 && a[list.back()] < cur){
                ng[list.back()] = cur;
                list.pop_back(); // 0(1)
            }
            list.push_back(i);
        }

        return ng;

    }