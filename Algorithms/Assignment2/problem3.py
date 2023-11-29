import sys

class Node:
    def __init__(self, freq, letter, left=None, right=None):
        self.freq = freq
        self.char = letter
        self.left = left
        self.right = right
        self.code = ''
        


class Queue:
    def __init__(self, char_str):
        self.graph_nodes = list()
        self.char_map = dict()
        for ch in char_str:
            if ch in self.char_map:
                self.char_map[ch] += 1  
            else: 
                self.char_map[ch] = 1  
        for char,freq in self.char_map.items():
            self.graph_nodes.append(Node(freq, char))
    
    def sort(self):
        self.graph_nodes = sorted(self.graph_nodes, key=lambda x: x.freq, reverse=True)
        
    def combine_nodes(self):
        self.sort()
        n1 = self.graph_nodes.pop()
        n2 = self.graph_nodes.pop()
        if n1.freq <= n2.freq:
            n1.code = '0'
            n2.code = '1'
            new_node = Node((n1.freq + n2.freq),'',n1,n2)
        else:
            n1.code = '1'
            n2.code = '0' 
            new_node = Node((n1.freq + n2.freq),'',n2,n1)
        self.graph_nodes.append(new_node) 
        
    
    def get_root(self):
        while len(self.graph_nodes)>1:
            self.combine_nodes()
        if len(self.graph_nodes) > 0:
            return self.graph_nodes[0]
        return None

class Tree:
    def __init__(self,node):
        self.root = node
        self.codes = dict()
    
    def get_root(self):
        return self.root
    
    def DFT_Coding(self,node,prev=''):
        
        if node.freq == -1:
            node_code = ''
        else:
            node_code = prev + node.code
        if(node.char is not None and node.char != ''):
            self.codes[node.char] = node_code 
        if (node.left is None) and (node.right is None):
            return  
        if(node.left):
            self.DFT_Coding(node.left, node_code)
        if(node.right):
            self.DFT_Coding(node.right, node_code)
        return self.codes  
    
    
    def Huffman_Encode(self,char_str,code_dict):
        str_code = ''
        for ch in char_str:
            if ch in code_dict.keys():
                str_code = str_code + code_dict[ch]
            
        return str_code
                
    def Huffman_Decode(self,root,encoded_str):
        head=root
        decoded_str = ""
        for enc in encoded_str:
            if enc == '0':
                head=head.left
            elif enc == '1':
                head=head.right
            if head.left is None and head.right is None:
                decoded_str += head.char
                head=root
        return decoded_str

def huffman_encoding(data):
    if len(data)>0:
        data+=" "
    queue = Queue(data)                
    root = queue.get_root()
    if root is not None:
        tree = Tree(root)
        code_dict = tree.DFT_Coding(root)
        str1 = tree.Huffman_Encode(data,code_dict)
        return tree,str1
    return None,None

def huffman_decoding(data,tree):
    root = tree.get_root()
    str2 = tree.Huffman_Decode(root,data)
    return str2

first_line = "My Algorithms and Data Structure Course"               
print ("The size of the data is: {}\n".format(sys.getsizeof(first_line)))
print ("The content of the data is: {}\n".format(first_line))
tree,str1=huffman_encoding(first_line)
if tree is not None:
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(str1, base=2))))
    print ("The content of the encoded data is: {}\n".format(str1))
    str2 = huffman_decoding(str1,tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(str2)))
    print ("The content of the encoded data is: {}\n".format(str2))
else:
    print('Empty or invalid string ')

print('Case2')    
second_line = "My Second Course is Self Driving Car Engineer"               
print ("The size of the data is: {}\n".format(sys.getsizeof(second_line)))
print ("The content of the data is: {}\n".format(second_line))
tree,str1=huffman_encoding(second_line)
if tree is not None:
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(str1, base=2))))
    print ("The content of the encoded data is: {}\n".format(str1))
    str2=huffman_decoding(str1,tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(str2)))
    print ("The content of the encoded data is: {}\n".format(str2))
else:
    print('Empty or invalid string ')
 
print('Case3')
third_line = "I am enjoying them"               
print ("The size of the data is: {}\n".format(sys.getsizeof(third_line)))
print ("The content of the data is: {}\n".format(third_line))
tree,str1=huffman_encoding(third_line)
if tree is not None:
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(str1, base=2))))
    print ("The content of the encoded data is: {}\n".format(str1))
    #str1="1000111101010011011010101000011111101101111111011010111011111010101010001111001000"
    str2=huffman_decoding(str1,tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(str2)))
    print ("The content of the encoded data is: {}\n".format(str2))
else:
    print('Empty or invalid string ')
    
#Edge Cases
print('Edge Case 1')
fourth_line = ""               
print("My fourth string is")
print(fourth_line)
tree,str1=huffman_encoding(fourth_line)
if tree is not None:
    print("Encoded as")
    print(str1)
    huffman_decoding("11101010100000001",tree)
    print("The following encoded line")
    print("11101010100000001")
    print("is decoded back into")
    print(str2)
    print("\n")
else:
    print('Empty or invalid string ')

print("\n")    
print('Edge Case 2')
fifth_line = "**"               
print("My fifth string is")
print(fifth_line)
tree,str1=huffman_encoding(fifth_line)
if tree is not None:
    print("Encoded as")
    print(str1)
    str2=huffman_decoding("11101010100000001",tree)
    print("The following encoded line")
    print("11101010100000001")
    print("is decoded back into")
    print(str2)
    print("\n")
else:
    print('Empty or invalid string ') 
    
    
print("\n")    
print('Edge Case 3')
sixth_line = "eeeeeenjoyyiingg really eeeenjoyyyyiingg"               
print("My sixth string is")
print(sixth_line)
tree,str1=huffman_encoding(sixth_line)
if tree is not None:
    print("Encoded as")
    print(str1)
    str2=huffman_decoding("10101010101000111001101111111100000000",tree)
    print("The following encoded line")
    print("10101010101000111001101111111100000000")
    print("is decoded back into")
    print(str2)
    print("\n")
    
else:
    print('Empty or invalid string ')   
    
print("\n")    
print('Edge Case 4')
sixth_line = "AAAAAAAAAAAAAAAAA"               
print("My sixth string is")
print(sixth_line)
tree,str1=huffman_encoding(sixth_line)
if tree is not None:
    print("Encoded as")
    print(str1)
    str2=huffman_decoding("10101010101000111001101111111100000000",tree)
    print("The following encoded line")
    print("10101010101000111001101111111100000000")
    print("is decoded back into")
    print(str2)
    print("\n")
    
else:
    print('Empty or invalid string ')    
