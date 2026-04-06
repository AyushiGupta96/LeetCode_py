#Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

#The most naïve approach is to traverse each possible substring of length m in the haystack and check if it is equal to the needle.

# First substring of length m will start at index 0 in the haystack and will end at index (m - 1) + 0.
# The second substring of length m will start at index 1 in the haystack and will end at index (m - 1) + 1, i.e. m.
# The third substring of length m will start at index 2 in the haystack and will end at index (m - 1) + 2 i.e. m + 1.
# Thus, if a substring ends at index (m - 1) + k, then it starts at index k. We know that the last substring ends at index (n - 1). Thus, to find starting index k of the last substring, we can equate (n - 1) with (m - 1) + k, to get k = (n-1) - (m-1), or k = n - m.
#
# Thus, the last substring of length m will start at index n - m in the haystack and will end at index n - 1.
# We will create a window of size m and slide it across the haystack. We will keep track of the starting index of the window in a variable window_start. For every window_start, we will iterate till window_start + m. During each iteration,
#
# if the i
# th
# character in the window is equal to the i
# th
# character in the needle, then we will increment i by 1.
# If the i
# th
# character in the window is not equal to the i
# th
# character in the needle, then we conclude that the substring of length m starting from index window_start cannot be equal to the needle, and we will reset window_start to window_start + 1.
# If all the i
# th
# characters in the window are equal to the i
# th
# characters of needle, then we will return the window_start.
#
# Algorithm
# Declare m and n as variables, and initialize them with the length of needle and haystack respectively.
#
# Declare the window_start variable, and initialize it with 0. Now, iterate window_start till starting index of the last substring of length m, i.e till n - m.
#
# For each window_start, iterate variable i from 0 to m - 1. Check if the i
# th
# character in the window i.e index window_start + i is equal to the i
# th
# character in the needle, if yes, then increment i by 1. If not, reset window_start to window_start + 1.
#
# If all the i
# th
# characters in the window are equal to the i
# th
# characters of needle, then return the window_start.
#
# If we are done iterating over all values of window_start and none of them return a match, then return -1.
#
# Example: Let haystack be "mississippi" and needle be “issipi”. The sliding window algorithm would get executed like this.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        for window_start in range(n-m+1):
            for i in range(m):
                if needle[i] != haystack[window_start +i]:
                    break
                if i==m-1:
                    return window_start
        return -1