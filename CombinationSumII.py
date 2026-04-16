#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
from typing import List


# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
#     [1,1,6],
#     [1,2,5],
#     [1,7],
#     [2,6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
#     [1,2,2],
#     [5]
# ]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(answer, temp_list, candidates, total_left, index):
            if total_left < 0:
                return
            elif total_left == 0:
                answer.append(temp_list.copy())
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    if total_left < candidates[i]:
                        break
                    temp_list.append(candidates[i])
                    backtrack(
                        answer,
                        temp_list,
                        candidates,
                        total_left - candidates[i],
                        i + 1,
                        )
                    temp_list.pop()

        result = []
        candidates.sort()
        backtrack(result, [], candidates, target, 0)
        return result