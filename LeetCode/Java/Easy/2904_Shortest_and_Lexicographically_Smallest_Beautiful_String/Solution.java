class Solution {
    public String shortestBeautifulString(String s, int k) {
        int n = s.length();
        int left = 0;
        int count = 0;
        String ans = "";

        for (int right = 0; right < n; right++) {
            if (s.charAt(right) == '1') {
                count++;
            }

            while (count == k) {
                while (left <= right && s.charAt(left) == '0') {
                    left++;
                }
                String sub = s.substring(left, right + 1);
                if (ans.isEmpty() || sub.length() < ans.length() || (sub.length() == ans.length() && sub.compareTo(ans) < 0)) {
                    ans = sub;
                }
                if (s.charAt(left) == '1') {
                    count--;
                }
                left++;
            }
        }

        return ans;
    }
}
