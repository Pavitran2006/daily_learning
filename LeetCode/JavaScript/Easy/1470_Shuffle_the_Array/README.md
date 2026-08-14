# LeetCode 1470 - Shuffle the Array

## Approach
Traverse the first half of the array. For every `i`, add `nums[i]` followed by `nums[i + n]` to the result.

## Complexity
- Time: O(n)
- Space: O(n)
