int majorityElement(vector<int>& nums) {
    int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int mid = nums.size() / 2;
    int count1 = 0, count2 = 0, count3 = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == nums[mid - 1]) {
            count1++;
        } else if (nums[i] == nums[mid]) {
            count2++;
        } else if (nums[i] == nums[mid + 1]) {
            count3++;
        }
    }
    if (count1 >= nums.size() / 2) {
        return nums[mid - 1];
    } else if (count2 >= nums.size() / 2) {
        return nums[mid];
    } else if (count3 >= nums.size() / 2) {
        return nums[mid + 1];
    }
    return -1;
}
}