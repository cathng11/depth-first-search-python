def findQueue(n, matrix,initialState):
    explored = [0 for i in range(n)]
    frontier = []
    result = []
    frontier = [initialState]
    explored[initialState] = 1
    print(frontier)
    node = frontier.pop(-1)
    result.append(node)
    isFirst=False
    stack = []
    stack.append(node)
    while True:
        temp_fr=[]
        
        for x in range(0, len(explored)):
            if (int(matrix[node][x]) == 1 and int(explored[x]) == 0):
                explored[x] = 1
                temp_fr.append(x)
        for t in reversed(range(0,len(temp_fr),1)):
            frontier.append(temp_fr[t])        
        if len(frontier) == 0:
            break
        else:
            print(frontier)
            for f in frontier:
                if (f in stack):
                    continue
                else:
                    stack.append(f)
            node = frontier.pop(-1)
            result.append(node)

    stackAlpha=[]
    for i in range(0, len(stack)):
        stackAlpha.append(numToAlpha(stack[i]))
    print("Stack: ", stackAlpha)
    return result

def Depth_First_Search(queue, goalTest):
    order=[]
    for index, value in enumerate(queue):
        if value == goalTest:
            for i in range(0, index+1):
                order.append(numToAlpha(queue[i]))
            break
    if len(order)==0:
        print("Khong tim thay duong di")
    else:
        print("Thu tu dinh kham pha: ",order)


def numToAlpha(result):
    switcher = {
        0: "S",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
    }
    return switcher.get(result, "Empty")


def alphaToNum(arg):
    switcher = {
        "S": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,      
    }
    return switcher.get(arg, "Empty")


with open(r'./Input_DFS.txt') as fl:
    line = fl.read().splitlines()
matrix = [[0 for i in range(int(line[0]))] for j in range(int(line[0]))]
for i in range(1, len(line)):
    matrix[i-1] = line[i]
n = int(line[0])

Depth_First_Search(findQueue(n, matrix,alphaToNum("S")), alphaToNum("G"))
