class BoggleBoard:
    slots = ('board','DIM')
    
    def __init__(self,filename='boggle.txt'):
        file = open(filename)
        self.DIM = int(file.readline())
        self.board = [[str(c) for c in line]for line in file]
    
    def __str__(self):
        toReturn = ''
        for row in range(self.DIM):
            for col in range(self.DIM):
                toReturn += str(self.board[row][col])
                if col != self.DIM-1:
                    toReturn += ' '
            toReturn += '\n'
        return toReturn
    
def buildGraph(board):
    graph = {}
    for row in range(board.DIM):
        for col in range(board.DIM):
            tempNeighbors = []
            if col - 1 >= 0:
                tempNeighbors.append(board[row][col-1])
                if row - 1 >= 0:
                    tempNeighbors.append(board[row-1][col-1])
                if row + 1 <= board.DIM:
                    tempNeighbors.append(board[row+1][col-1])
            if col + 1 <= board.DIM:
                tempNeighbors.append(board[row][col+1])
                if row + 1 <= board.DIM:
                    tempNeighbors.append(board[row+1][col+1])
                if row - 1 >= 0:
                    tempNeighbors.append(board[row-1][col+1])
            if row - 1 >= 0:
                tempNeighbors.append(board[row-1][col])
            if row + 1 <= board.DIM:
                tempNeighbors.append(board[row+1][col])
            graph[board[row][col]] = tempNeighbors
                

def buildEnglishDict(boardSize):
    fileName = 'sowpods.txt'
    file = open(fileName)
    englishWords = set()
    for line in file:
        if len(line) >= 3 and len(line) <= boardSize**2:
            englishWords.add(line)
    return englishWords

def wordsForOnePath(startNode,graph,words):
    stack = []
    start = startNode.value
    predecessors = {}
    predecessors[start] = None
    stack.append(start)
    while stack != []:
        current = stack.pop()
        


def main():
    board = BoggleBoard()
    print(board)
    words = buildEnglishDict()
    print(True)
    

main()

