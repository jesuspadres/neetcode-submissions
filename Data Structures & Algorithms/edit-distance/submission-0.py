class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[x for x in range(len(word1) + 1)] for y in range(len(word2)+1)]

        for i in range(len(cache)):
            cache[i][0] = i

        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if word1[col-1] == word2[row-1]:
                    cache[row][col] = cache[row-1][col-1]
                else:
                    cache[row][col] = 1 + min(cache[row-1][col-1], cache[row][col-1], cache[row-1][col])

        return cache[-1][-1]


"""  
  m o n e y 
m 0 1 2 3 4
o 1 0 1 2 3
n 2 1 0 1 2
k 3 2 1 1 2
e 4 3 2 1 2
y 5 4 3 2 1
s 6 5 4 3 2"""