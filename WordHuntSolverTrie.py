import copy

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
    
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def _charToIndex(self,ch):
        return ord(ch)-ord('A')
 
 
    def insert(self,key):
         
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True
 
    def search(self, key):
         
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord
        
    def isPromising(self, key): # Added a function to check if given characters are prefixes of a word in Trie.
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        
        return True 

def traverse(i, j, word, usedCoordinates, trie, answers):

    # check manually all possible directions

    if (i + 1, j) not in usedCoordinates and i + 1 < 4:
        if trie.isPromising(word + grid[i + 1][j]):
            usedCoordinates.append((i + 1, j))
            traverse(i + 1, j, word + grid[i + 1][j], usedCoordinates, trie, answers)
            usedCoordinates.remove((i + 1, j))

    if (i - 1, j) not in usedCoordinates and i - 1 >= 0:
        if trie.isPromising(word + grid[i - 1][j]):
            usedCoordinates.append((i - 1, j))
            traverse(i - 1, j, word + grid[i - 1][j], usedCoordinates, trie, answers)
            usedCoordinates.remove((i - 1, j))
    
    if (i, j + 1) not in usedCoordinates and j + 1 < 4:
        if trie.isPromising(word + grid[i][j + 1]):
            usedCoordinates.append((i, j + 1))
            traverse(i, j + 1, word + grid[i][j + 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i, j + 1))
    
    if (i, j - 1) not in usedCoordinates and j - 1 >= 0:
        if trie.isPromising(word + grid[i][j - 1]):
            usedCoordinates.append((i, j - 1))
            traverse(i, j - 1, word + grid[i][j - 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i, j - 1))
        
    if (i + 1, j + 1) not in usedCoordinates and i + 1 < 4 and j + 1 < 4:
        if trie.isPromising(word + grid[i + 1][j + 1]):
            usedCoordinates.append((i + 1, j + 1))
            traverse(i + 1, j + 1, word + grid[i + 1][j + 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i + 1, j + 1))
    
    if (i - 1, j - 1) not in usedCoordinates and i - 1 >= 0 and j - 1 >= 0:
        if trie.isPromising(word + grid[i - 1][j - 1]):
            usedCoordinates.append((i - 1, j - 1))
            traverse(i - 1, j - 1, word + grid[i - 1][j - 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i - 1, j - 1))

    if (i + 1, j - 1) not in usedCoordinates and i + 1 < 4 and j - 1 >= 0:
        if trie.isPromising(word + grid[i + 1][j - 1]):
            usedCoordinates.append((i + 1, j - 1))
            traverse(i + 1, j - 1, word + grid[i + 1][j - 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i + 1, j - 1))
    
    if (i - 1, j + 1) not in usedCoordinates and i - 1 >= 0 and j + 1 < 4:
        if trie.isPromising(word + grid[i - 1][j + 1]):
            usedCoordinates.append((i - 1, j + 1))
            traverse(i - 1, j + 1, word + grid[i - 1][j + 1], usedCoordinates, trie, answers)
            usedCoordinates.remove((i - 1, j + 1))

    if (trie.search(word) and word not in answers):
        if not any(answer['word'] == word for answer in answers):
            answers.append({'word': word , 'coordinates': copy.deepcopy(usedCoordinates), 'index': len(answers)})
                        
                        
    return
if __name__ == "__main__":

# Dictionary
    with (open("/Users/ramygad/Vs Code/Word Hunt/processedDictionary.txt", "r")) as f:
        dictionary = f.read().splitlines()
    
    # Populate Trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word)


    while True:

        while True:
            letters = input()
            if len(letters) == 16:
                break
            else:
                print("Please enter 16 letters.")
        letters = letters.upper()
        grid = [['' for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                grid[i][j] = letters[i * 4 + j]

        answers = []
        for i in range(4):
            for j in range(4):
                
                # usedCoordinates is a list of coordinates that we have already used
                usedCoordinates = []
                usedCoordinates.append((i, j))
                word = ""
                word += grid[i][j]
                traverse(i, j, word, usedCoordinates, trie, answers)
                # Sort by longest words at the bottom.
                answers.sort(key=lambda x: (len(x['word']), x['index']), reverse=False)

        for answer in answers:
            print("Word:", answer['word'])
        #     print("Coordinates:", answer['coordinates'])

        answer = input("again? y/n: ")
        if answer == "n":
            break
        if answer == "y":
            continue
