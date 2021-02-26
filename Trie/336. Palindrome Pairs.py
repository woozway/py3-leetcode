"""
1. Clarification
2. Possible solutions
     - trie
     - hash
     - trie + Manacher (to be continued)
3. Coding
4. Tests
"""


# T=O(n*m^2), S=O(n*m)
class Node:
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def insert(s: str, index: int):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index

        def findWord(s: str, left: int, right: int) -> int:
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag

        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        tree = [Node()]
        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)
        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])
        return ret


# # T=O(n*m^2), S=O(n*m)
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         def findWord(s: str, left: int, right: int) -> int:
#             return indices.get(s[left:right + 1], -1)
# 
#         def isPalindrome(s: str, left: int, right: int) -> bool:
#             return (sub := s[left:right + 1]) == sub[::-1]
# 
#         n = len(words)
#         indices = {word[::-1]: i for i, word in enumerate(words)}
#         ret = list()
#         for i, word in enumerate(words):
#             m = len(word)
#             for j in range(m + 1):
#                 if isPalindrome(word, j, m - 1):
#                     leftId = findWord(word, 0, j - 1)
#                     if leftId != -1 and leftId != i:
#                         ret.append([i, leftId])
#                 if j and isPalindrome(word, 0, j - 1):
#                     rightId = findWord(word, j, m - 1)
#                     if rightId != -1 and rightId != i:
#                         ret.append([rightId, i])
#         return ret
