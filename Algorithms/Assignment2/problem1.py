from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.Cache = OrderedDict()
        self.CacheMaxLength = capacity
    
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.Cache:
            val = self.Cache[key]
            del self.Cache[key]
            self.Cache[key] = val
            print(val)
            return val
        else:
            print("-1")
            return -1
    
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at 
        #capacity remove the oldest item. 
        
        if key in self.Cache:
            del self.Cache[key]
            self.Cache[key] = value
        elif len(self.Cache) < self.CacheMaxLength:
            self.Cache[key] = value
        elif self.CacheMaxLength > 0:
            self.Cache.popitem(last=False)
            self.Cache[key] = value
        else:
            print("Cache Capacity is zero")
            return


#Test Cases 
print("First Test")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
   


print("Second Test")
our_cache = LRU_Cache(5)

our_cache.set(11, 11);
our_cache.set(12, 12);
our_cache.set(13, 13);
our_cache.set(14, 14);
our_cache.set(15, 15);
our_cache.set(16, 16);
our_cache.set(137, 137);
our_cache.set(138, 138);
our_cache.set(139, 139);

our_cache.get(11)       # returns -1 because 11 has been replaced
our_cache.get(12)       # returns -1 because 12 has been replaced
our_cache.get(137)      # returns 137

our_cache.set(140, 140) 
our_cache.set(141, 141)
our_cache.set(142, 142)

our_cache.get(138)      # returns -1 because 138 has been replaced since it was not recently used within the window size of 5
our_cache.get(137)      # returns 137 because it has been used recently

print("Third Test")
our_cache = LRU_Cache(5)

our_cache.set(11, 11);
our_cache.set(12, 12);
our_cache.set(13, 13);
our_cache.set(14, 14);
our_cache.set(15, 15);
our_cache.set(16, 16);
our_cache.set(11, 11);
our_cache.set(138, 138);
our_cache.set(139, 139);

our_cache.get(15)      # returns 15

our_cache.set(140, 140) 

our_cache.get(11)      # returns 11  because 11 has been reset recently
our_cache.get(16)      # returns -1

print("Edge Case 1- Testing a cache of zero size")
our_cache = LRU_Cache(0)
#Capacity is zero - attempts to add items will fail
our_cache.set(11, 11);
our_cache.set(12, 12);
our_cache.set(13, 13);
our_cache.set(14, 14);
our_cache.set(15, 15);
our_cache.set(16, 16);
our_cache.set(11, 11);
our_cache.set(138, 138);
our_cache.set(139, 139);

our_cache.get(15)      # returns -1

our_cache.set(140, 140) 

our_cache.get(11)      # returns -1
our_cache.get(16)      # returns -1

print("Edge Case 2- Testing a cache of negative size")
our_cache = LRU_Cache(-1)
#Capacity is zero - attempts to add items will fail
our_cache.set(11, 11);
our_cache.set(12, 12);
our_cache.set(13, 13);
our_cache.set(14, 14);
our_cache.set(15, 15);
our_cache.set(16, 16);
our_cache.set(11, 11);
our_cache.set(138, 138);
our_cache.set(139, 139);

our_cache.get(15)      # returns -1

our_cache.set(140, 140) 

our_cache.get(11)      # returns -1
our_cache.get(16)      # returns -1

print("Edge Case 3- Testing a cache of very high size")
our_cache = LRU_Cache(1000000000000)

our_cache.set(11, 11);
our_cache.set(12, 12);
our_cache.set(13, 13);
our_cache.set(14, 14);
our_cache.set(15, 15);
our_cache.set(16, 16);
our_cache.set(11, 11);
our_cache.set(138, 138);
our_cache.set(139, 139);

our_cache.get(15)      # returns 15, if the cache space has been allocated

our_cache.set(140, 140) 

our_cache.get(11)      # returns 11, if the cache space has been allocated
our_cache.get(16)      # returns 16, if the cache space has been allocated
