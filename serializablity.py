from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True


        recStack[v] = False
        return False


    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v+1)

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)


        print stack


print "Type the file name"
file=raw_input(">")
text=open(file)
print text.read()
text.close()

abc=int(raw_input("Enter no of transactions"))



print "Copying the file in LIST"
schedule=[]
with open(file) as file :
    for line in file :
        line=line.strip()
        schedule.append(line)

print schedule

x=len(schedule)

g = Graph(abc)
edgelist=[]

for i in range(0,x):

    key=schedule[i]
    j=i+1

    while j<x:

        print schedule[i],"   ",schedule[j]

        if (schedule[i][0] == 'R' and schedule[j][0] == 'R'):
            print "Read Read Condition Detected"
        elif ((schedule[i][0] == 'R' and schedule[j][0] == 'W') or (schedule[i][0] == 'W' and schedule[j][0] == 'R') or (schedule[i][0] == 'W' and schedule[j][0] == 'W')):
            if ((schedule[i][1] != schedule[j][1]) and (schedule[i][2] == schedule[j][2])):
                edgelist.append(schedule[i][1]+schedule[j][1])
                g.addEdge(schedule[i][1],schedule[j][1])
                print "Conflict Condition Match AND Edge is created in Graph"


            else:
                print "No Conflict Condition Match"

        j=j+1
        if(j==x):
            print ""


print "Edge List Created is"
print edgelist
print "\n"

print "Now applying Cycle Detection Algorithm "

if g.isCyclic() == 1:
    print "Not Seriazable"
else:
    print "Seriazable \n"
    print "Following is a Topological Sort of the Graph\n"
    g.topologicalSort()
    print "\n"