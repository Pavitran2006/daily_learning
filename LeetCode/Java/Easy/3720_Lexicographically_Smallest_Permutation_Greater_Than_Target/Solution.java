class Solution {
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        int bestIndex = -1;
        char bestChar = ' ';

        // Create a copy of freq to track remaining character counts during prefix matching
        int[] count = freq.clone();

        for (int i = 0; i < n; i++) {
            char targetChar = target.charAt(i);

            // Check if there is any character strictly greater than targetChar available
            for (char c = (char) (targetChar + 1); c <= 'z'; c++) {
                if (count[c - 'a'] > 0) {
                    bestIndex = i;
                    bestChar = c;
                    break; // Pick the smallest available character strictly greater than targetChar
                }
            }

            // Try to match targetChar for the next position
            if (count[targetChar - 'a'] > 0) {
                count[targetChar - 'a']--;
            } else {
                // Cannot match targetChar, so we cannot continue matching target further
                break;
            }
        }

        // If no index found where we can deviate with a larger character
        if (bestIndex == -1) {
            return "";
        }

        // Construct the result:
        // 1. Prefix: target[0...bestIndex-1]
        // 2. Pivot character: bestChar
        // 3. Remainder: all unused characters in s, sorted ascending
        StringBuilder sb = new StringBuilder();
        sb.append(target.substring(0, bestIndex));
        sb.append(bestChar);

        // Deduct used characters from original frequency array
        for (int i = 0; i < bestIndex; i++) {
            freq[target.charAt(i) - 'a']--;
        }
        freq[bestChar - 'a']--;

        // Append remaining characters in ascending order
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                sb.append((char) ('a' + i));
                freq[i]--;
            }
        }

        return sb.toString();
    }
}
