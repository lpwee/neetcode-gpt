from typing import List
from collections import Counter

class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed

        corpus = list(corpus)
        res = []

        for _ in range(num_merges):

            c = Counter(zip(corpus[:-1], corpus[1:]))
            (s1, s2), _ = min(c.items(), key=lambda x: (-x[1], x[0]))
            new_token = s1 + s2 # most common pair

            i, n = 0, len(corpus) - 1

            new_corpus = []
            while i < n:
                if corpus[i] + corpus[i+1] == new_token:
                    new_corpus.append(new_token)
                    i += 2
                else:
                    new_corpus.append(corpus[i])
                    i += 1
            
            corpus = new_corpus
            res.append([s1, s2])

        return res