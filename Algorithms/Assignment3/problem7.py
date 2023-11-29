
class RouteTrie:
    def __init__(self,handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler=handler
    def insert(self, path,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for part in path:
                if part not in node.children:
                    node.insert(part)
                node = node.children[part]    
        node.handler = handler
    def find(self, prefix):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for part in prefix:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler
    def get_handler(self):
        return self.handler
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}
    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)
        self.nfh = not_found_handler
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        if len(path)!=0:
            self.router.insert(parts, handler)
    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts = self.split_path(path)
        if len(parts) == 0:
            return self.get_router_handler()
        handler = self.router.find(parts)
        if handler is not None:
            return handler
        else:
            return self.nfh
    def get_router_handler(self):
        return self.router.get_handler()
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here  
        if path is None or len(path)==0 or path=='/':
            return []
        parts = path.split(sep='/')
        return [part for part in parts if part != '']
    
    
 # Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
   

