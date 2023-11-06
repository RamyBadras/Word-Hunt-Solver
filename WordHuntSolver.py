import copy

def promising(word, dictionary):
    for w in dictionary:
        if w.startswith(word):
            return True
    return False

def checkIfInDictionary(word, dictionary):
    for w in dictionary:
        if w == word:
            return True
    return False

def traverse(i, j, word, usedCoordinates, cutDictionary, answers):

    # check manually all possible directions

    if (i + 1, j) not in usedCoordinates and i + 1 < 4:
        if promising(word + grid[i + 1][j], cutDictionary):
            usedCoordinates.append((i + 1, j))
            traverse(i + 1, j, word + grid[i + 1][j], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i + 1, j))

    if (i - 1, j) not in usedCoordinates and i - 1 >= 0:
        if promising(word + grid[i - 1][j], cutDictionary):
            usedCoordinates.append((i - 1, j))
            traverse(i - 1, j, word + grid[i - 1][j], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i - 1, j))

    if (i, j + 1) not in usedCoordinates and j + 1 < 4:
        if promising(word + grid[i][j + 1], cutDictionary):
            usedCoordinates.append((i, j + 1))
            traverse(i, j + 1, word + grid[i][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i, j + 1))

    if (i, j - 1) not in usedCoordinates and j - 1 >= 0:
        if promising(word + grid[i][j - 1], cutDictionary):
            usedCoordinates.append((i, j - 1))
            traverse(i, j - 1, word + grid[i][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i, j - 1))

    if (i + 1, j + 1) not in usedCoordinates and i + 1 < 4 and j + 1 < 4:
        if promising(word + grid[i + 1][j + 1], cutDictionary):
            usedCoordinates.append((i + 1, j + 1))
            traverse(i + 1, j + 1, word + grid[i + 1][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i + 1, j + 1))

    if (i - 1, j - 1) not in usedCoordinates and i - 1 >= 0 and j - 1 >= 0:
        if promising(word + grid[i - 1][j - 1], cutDictionary):
            usedCoordinates.append((i - 1, j - 1))
            traverse(i - 1, j - 1, word + grid[i - 1][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i - 1, j - 1))

    if (i + 1, j - 1) not in usedCoordinates and i + 1 < 4 and j - 1 >= 0:
        if promising(word + grid[i + 1][j - 1], cutDictionary):
            usedCoordinates.append((i + 1, j - 1))
            traverse(i + 1, j - 1, word + grid[i + 1][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i + 1, j - 1))

    if (i - 1, j + 1) not in usedCoordinates and i - 1 >= 0 and j + 1 < 4:
        if promising(word + grid[i - 1][j + 1], cutDictionary):
            usedCoordinates.append((i - 1, j + 1))
            traverse(i - 1, j + 1, word + grid[i - 1][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers)
            usedCoordinates.remove((i - 1, j + 1))

    if checkIfInDictionary(word, cutDictionary) and word not in answers:
        answers.append(word)

    return

if __name__ == "__main__":

    # Dictionary
    with (open("processedDictionary.txt", "r")) as f:
        dictionary = f.read().splitlines()

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
            # remove all words from possibleWords that don't start with this letter.
            cutDictionary = copy.deepcopy(dictionary)
            cutDictionary = [w for w in cutDictionary if w.startswith(word)]
            traverse(i, j, word, usedCoordinates, copy.deepcopy(cutDictionary), answers)
            # Sort by longest words at the bottom.
            answers.sort(key=len, reverse=False)
            
    for i in answers:
        print(i)