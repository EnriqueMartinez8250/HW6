import random
# wordcloud dictionary
#Cleaned it up a little bit compared to the one posted on the canvas page
wordCloud = {
    'NBA': 1.0,
    'game': 0.6739130434782609,
    'Nuggets': 0.5869565217391305,
    'playoff': 0.3695652173913043,
    'li li': 0.34782608695652173,
    's': 0.32608695652173914,
    'MVP': 0.30434782608695654,
    'Denver Nuggets': 0.30434782608695654,
    'Denver': 0.2391304347826087,
    'Joel Embiid': 0.2391304347826087,
    'season': 0.21739130434782608,
    'night': 0.1956521739130435,
    'will': 0.1956521739130435,
    'team': 0.1956521739130435,
    'ol li': 0.17391304347826086,
    'Sunday': 0.15217391304347827,
    'play': 0.15217391304347827
}

#### OBST Algorithms 
#### Source for the algorithm https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
def optCost(freq, i, j):
    # Base cases    
    if j < i:     
        return 0
    if j == i:    
        return freq[i]
    fsum = Sum(freq, i, j)
     
    Min = 999999999999
    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1) +
                optCost(freq, r + 1, j))
        if cost < Min:
            Min = cost
    return Min + fsum
 

def optimalSearchTree(keys, freq, n):
    return optCost(freq, 0, n - 1)
 
def Sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


#####################Used chatGPT to guide me on how to use this below
top_n = 50 
words = list(wordCloud.items())
words = sorted(words, key=lambda x: x[1], reverse=True)[:top_n]
random.shuffle(words)

# Extract keys and frequencies
keys = [word[0] for word in words]
freqs = [word[1] for word in words]

# Compute the cost of traversing an OBST
n = len(keys)
obst_cost = optimalSearchTree(keys, freqs, n)
print("OBST Cost:", obst_cost)

####################Used chatGPT to guide me on how to use this above

# BST functions
def create_node(key, freq):
    return {'key': key, 'freq': freq, 'left': None, 'right': None}

def insert_node(node, key, freq):
    if node is None:
        return create_node(key, freq)
    
    if key < node['key']:
        node['left'] = insert_node(node['left'], key, freq)
    else:
        node['right'] = insert_node(node['right'], key, freq)
    
    return node

def weighted_cost(node, depth):
    if node is None:
        return 0
    return node['freq'] * depth + weighted_cost(node['left'], depth+1) + weighted_cost(node['right'], depth+1)

# Create a regular BST and insert words with their frequencies
bst_root = None
for word, freq in words:
    bst_root = insert_node(bst_root, word, freq)

# Compute the cost of traversing a regular BST
bst_cost = weighted_cost(bst_root, 1)
print("Regular BST Cost:", bst_cost)

# Compare the costs and analyze the performance difference
print("OBST Cost:", obst_cost)
print("Regular BST Cost:", bst_cost)
