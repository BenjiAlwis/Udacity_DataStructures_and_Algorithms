## Represents a single node in the Trie
 
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
       
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        suffixes=[]
        if  suffix != '':#self.is_word and
            suffixes.append(suffix)

        if len(self.children) == 0:
            return suffixes

        for char in self.children:
            suffixes+=self.children[char].suffixes(suffix+char)
        
        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
                if char not in node.children:
                    node.insert(char)
                node = node.children[char]    
        node.isWord = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

        
 
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
    
prefixNode = MyTrie.find("anthol") 
if prefixNode!=None:
    assert prefixNode.suffixes() == [ "o", "og", "ogy"]    
prefixNode = MyTrie.find("fact") 
if prefixNode!=None:
    assert prefixNode.suffixes() == [ "o", "or", "ory"] 
prefixNode = MyTrie.find("") 
if prefixNode!=None:
    print('\n'.join(prefixNode.suffixes()))
prefixNode = MyTrie.find("factory") 
if prefixNode!=None:
    assert prefixNode.suffixes() == []
prefixNode = MyTrie.find("floor") 
if prefixNode!=None:
    assert prefixNode.suffixes() == []


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='');


