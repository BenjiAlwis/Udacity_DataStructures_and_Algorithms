Problem 7:
The internal mechanisms of this solution is similar to the solution for problem 5 since a hierarchy of webpages are used instead of words. The trie data structure forms the core of this solution. In problem 5, characters were stored in a hierarchy and in this problem parts of urls are stored in a hierarchy. The main difference occurs when it handles edge cases such as “root handlers''.

RouteTrie:

__init__ method
O(1) for both time and space complexity

Insert method
The time complexity is O(n*w) where w is the length of the path (url) and n is the number of total words stored in the tree. Space complexity is O(n) as well given that there will not be any sharing of space in the worst case scenario where there are not any commonalities between the words.

Find method
Similar to the previous method, the time complexity is O(n*w) where w is the length of the path (url) and n is the number of total words stored in the tree. 
Space complexity is O(1) since there is no new memory allocations.

get_handler method
O(1) for both time and space complexity

RouteTrieNode:

__init__ method
O(1) for both time and space complexity

Insert method
Time complexity depends on the number of total words stored in the tree (n). This makes the time complexity O(n). The worst case of space consumption will be when the words have no common characters (i.e. no sharing of space). This makes the space complexity O(n).

Router:

__init__ method
O(1) for both time and space complexity

add_handler method
O(1) time complexity - however it calls another method which has time complexity of O(n*w). Space complexity depends on thw number of parts in the url-so O(n).


lookup method
O(1) time complexity - however it calls another method which has time complexity of O(n*w). Space complexity depends on thw number of parts in the url-so O(n).

get_router_handler method
O(1) for both time and space complexity

split_path method
O(n) for both time and space complexity when n is number of parts in the url.













