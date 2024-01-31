Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


CODE:


class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};



OUTPUT:

nums =[1,2,3,1]

