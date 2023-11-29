Problem 5:
This solution is based on a tree based approach where the characters in a word are stored in a hierarchical fashion. During the search, a matching character will retrieve all node sequences as relevant suffixes. For example, when the letter ‘a’ is supplied, all stored words starting with the letter ‘a’ can be retrieved easily due to the hierarchical arrangement of the letters.

TrieNode:

__init__ method
O(1) for both time and space complexity

Insert method
Time complexity depends on the number of total words stored in the tree (n). This makes the time complexity O(n). The worst case of space consumption will be when the words have no common characters (i.e. no sharing of space). This makes the space complexity O(n).

Suffixes method
Time complexity of this operation does not depend on the length of the word and only depend on the number of words stored. So it is O(n)
No memory allocation during this operation and space complexity is O(1)


Trie:

__init__ method
O(1) for both time and space complexity

Insert method
Time complexity depends on the length of the word (w), that is being searched and the number of total words stored in the tree (n). This makes the time complexity O(w*n). The worst case of space consumption will be when the words have no common characters (i.e. no sharing of space). This makes the space complexity O(n).

Find method
Time complexity is similar to the insert method and it is equal to O(w*n).However, no memory allocation during find and space complexity is O(1)


