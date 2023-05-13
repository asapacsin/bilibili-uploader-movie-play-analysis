

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.head = None
        self.parent = None
    def add_left(self,val):
        self.left = Node(val)
        if self.noParent():
            self.left.head = self
        else:
            self.left.head=self.head
        self.left.parent = self
    
    def add_right(self,val):
        self.right = Node(val)
        if self.noParent():
            self.right.head = self
        else:
            self.right.head=self.head
        self.right.parent = self

    def goLeaf(self,node,array):
        if node.left == None:
            array.append(node)
            return
        self.goLeaf(node.left,array)
        self.goLeaf(node.right,array)

    def getLeafArray(self):
        array = []
        tmp = self
        while True:
            self.goLeaf(tmp,array)
    def noParent(self):
        if self.parent == None:
            return True
        return False

def recursion(node,store_array,count_deep,deep):
    #if count_deep smaller than deep
    if count_deep < deep:
        #goto left node
        if node.left == None:
            node.add_left(None)
            node.add_right(None)
            count_deep -=1
        count_deep += 1
        recursion(node.left,store_array,count_deep,deep)
        recursion(node.right,store_array,count_deep,deep)
    else:
        store_array.append(node.head)

def init_store(deep):
    if deep == 0:
        return
    start = Node(None)
    start.add_left(None)
    start.add_right(None)
    store_array = []
    recursion(start,store_array,0,deep)
    return store_array

def deepcopy(arr):
    copy_arr = []
    for node in arr:
        copy_arr.append(node)
    return copy_arr

def imple_find_combine(arr,pop_index,combination):
    copy_arr = deepcopy(arr)
    print('get')
    pop_node = copy_arr.pop(pop_index)
    size = len(copy_arr)
    for i in range(size):
        imple_find_combine(copy_arr,i,combination)
    combination.append(pop_node)


def find_combination(gem):
    combination = []
    size =  len(gem)
    for i in range(size):
        imple_find_combine(gem,i,combination)
    return combination

def calculate_value(tree):
    value = ['']
    tmp = tree
    middle_traverse(tmp,value)
    return value[0]

def check_combination(gem_arr,tree,p,target):
    Node_array = tree.getLeafArray()    
    size = len(Node_array)
    for i in range(size):
        Node_array[i].val = gem_arr[i]
    value = calculate_value(tree)
    if int(value)%p == target:
        return 1
    return 0

def middle_traverse(node,value):
    value[0] += '1'
    value[0] += node.val
    if node.left == None:
        value[0] += '9'
        return
    else:
        middle_traverse(node.left)
        middle_traverse(node.right)
    value[0] += '9'
    

def main():
    gem = [3,21,3]
    deep = len(gem)-2
    p=7
    target = 5
    #create an array include all combination of node tree with deep
    tree_store = init_store(deep)
    count = 0
    for tree in tree_store:
        gem_array = find_combination(gem)
        size_gem = len(gem_array)
        for i in range(size_gem):
            count += check_combination(gem_array[i],tree,p,target)
    print(count)

main()
