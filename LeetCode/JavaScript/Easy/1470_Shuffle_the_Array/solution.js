/**
 * LeetCode 1470 - Shuffle the Array
 *
 * Given [x1, x2, ..., xn, y1, y2, ..., yn],
 * return [x1, y1, x2, y2, ..., xn, yn].
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function shuffle(nums, n) {
    const result = [];

    for (let i = 0; i < n; i++) {
        result.push(nums[i]);
        result.push(nums[i + n]);
    }

    return result;
}
