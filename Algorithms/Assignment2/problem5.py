import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
        
    def calc_hash(self,str):
      sha = hashlib.sha256()
      hash_str = str.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
  

class Blockchain: 
    def __init__(self): 
        self.tail = None
    
    def append(self,timestamp, data):
        if self.tail is None:
            self.tail = Block(data, None)
            return
        self.tail = Block(data, self.tail)
    
    def add_block(self, data):
        if self.tail is None:
            self.tail = Block(data, None)
            return
        self.tail = Block(data, self.tail)
        
    def to_list(self):
        out = []          
        node = self.tail 
        while node is not None:      
            out.append([node.data,node.hash])
            node = node.previous_hash
        return out
    
    def search(self,data):
        if self.tail is None:
            retun 
        node = self.tail 
        while node is not None:      
            if node.data == data:
             return node
            node = node.previous_hash
        return None
    
    def size(self):
        length = 0
        node = self.tail 
        while node is not None:      
            length += 1
            node = node.previous_hash
        return length

    def printl(self):
        print(self.to_list())
        
print("Test 1")

blockChain = Blockchain()
blockChain.add_block('1')
blockChain.add_block('2')
blockChain.add_block('3')
blockChain.add_block('4')
blockChain.add_block('5')
blockChain.add_block('6')
blockChain.add_block('7')

print(blockChain.printl())
blockchain = Blockchain()
print(blockchain.size())
blockchain.append(time.time(),'test string')
print(blockchain.size())
print(blockchain.to_list())

blockchain.append(time.time(),'test string1')
blockchain.append(time.time(),'test string2')
blockchain.append(time.time(),'test string3')
blockchain.append(time.time(),'test string4')
print(blockchain.size())
print(blockchain.to_list())
block = blockchain.search('test string1')
if block is not None:
 print(block.data)
else:
 print('Not Found')   
block = blockchain.search('test string6')
if block is not None:
 print(block.data)
else:
 print('Not Found')  
print("\n")
print("Edge Case1")
blockchain.append(time.time(),'')
print(blockchain.size())
print(blockchain.to_list())
block = blockchain.search('')
if block is not None:
 print(block.data)
else:
 print('Not Found')  

print("\n")
print("Edge Case2")
tm=time.time()
blockchain.append(tm,'***')
blockchain.append(tm,'?????')
print(blockchain.size())
print(blockchain.to_list())
block = blockchain.search('test string7')
if block is not None:
 print(block.data)
else:
 print('Not Found')  
block = blockchain.search('test string8')
if block is not None:
 print(block.data)
else:
 print('Not Found')


print("\n")
print("Edge Case3")
tm=time.time()
blockchain.append(tm,'')
blockchain.append(tm,'')
print(blockchain.size())
print(blockchain.to_list())
block = blockchain.search('test string1')
if block is not None:
 print(block.data)
else:
 print('Not Found')  
block = blockchain.search('test string8')
if block is not None:
 print(block.data)
else:
 print('Not Found')  
