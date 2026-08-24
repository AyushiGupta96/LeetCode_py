#You are given a string s and an array of strings words. All the strings of words are of the same length.
import collections
from typing import List


#A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

#For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
#Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



#Example 1:

#Input: s = "barfoothefoobarman", words = ["foo","bar"]

#Output: [0,9]

#Explanation:

#The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
#The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

#Example 2:

#Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

#Output: []

#Explanation:

#There is no concatenated substring.

#Example 3:

#Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

#Output: [6,9,12]

#Explanation:

#The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
#The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
#The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
#Initialize some variables:

#n as the length of s.
#k as the length of words
#wordLength as the length of each word in words.
#substringSize as wordLength * k, which represents the size of each valid substring.
#wordCount as a hash table that tracks how many times a word occurs in words.
#Create a function check that takes a starting index i and returns if a valid substring starts at index i:

#Create a copy of wordCount to make use of for this particular index. Let's call it remaining. Also, initialize an integer wordsUsed which tracks how many matches we have found so far.
#Iterate starting from i. Iterate until i + substringSize - we know that each valid substring will have this size, so we don't need to go further. At each iteration, we will be checking for a word - and we know each word has a length of wordLength, so increment by wordLength each time.
#If the variable we are iterating with is j, then at each iteration, check for a word sub = s.substring(j, j + wordLength).
#If sub is in remaining and has a value greater than 0, then decrease its count by 1 and increase wordsUsed by 1. Otherwise, break out of the loop.
#At the end of it all, if wordsUsed == k, that means we used up all the words in words and have found a valid substring. Return true if so, false otherwise.
#Now that we have this function check, we can just check all possible starting indices. Because a valid substring has a length of substringSize, we only need to iterate up to n - substringSize. Build an array with all indices that pass check and return it.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        length = len(words[0])
        size = length * k
        count = collections.Counter(words)

        def check(i):
            #copy the original dictionary to use for this index
            remaining = count.copy()
            used = 0

            #each iteration will check for a match in words
            for j in range(i,i+size,length):
                sub = s[j : j + length]
                if remaining[sub]>0:
                    remaining[sub] -=1
                    used +=1
                else:
                    break
                #valid if we used all the words
            return used == k
        answer = []
        for i in range(n - size + 1):
            if check(i):
                answer.append(i)
        return answer