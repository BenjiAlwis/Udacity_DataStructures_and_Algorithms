﻿Problem 2:
The search iin this solution is done using binary search. However, it has to be done differently to a binary search of a linear sorted array where the first item is always the smallest and the last item is always the largest. In a circular array, we do not know where the smallest and the largest item are. However, we know from the smallest item to the largest item is sorted. I modelled finding this as a binary search problem in which it is checked whether the mid item is smaller or greater than the first item. If greater, then the segment between the first item and the mid item is in order. Then we shift our search to the other half of the circular array. This process is repeated in a recursive fashion until the item is found or the first item index becomes greater than the index of the last item. This divide and conquer approach gives time complexity of O(log(n)) and space complexity is O(1) effectively making space complexity independent of the input.
