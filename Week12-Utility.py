        #https://github.com/brevenj/Week12-Utility.git
        #Breven Jackson
        #CSCI 102
        #Week 11 - Part B 

def PrintOutput(x):
    print("OUTPUT",x)

def LoadFile(file):
    x = open(file,'r')
    lines = x.readlines()
    lines = list(map(lambda x:x.strip(),lines))
    return lines

def UpdateString(s, l, n):
    mylist = []
    for i in range(len(s)):
        mylist.append(s[i])
    mylist[n] = l
    s = ''.join(map(str, mylist))
    print('OUTPUT',s)
    
def FindWordCount(list1,string):
    count = 0
    list1 = (''.join(list1))
    list1 = list1.split()
    for word in list1:
        if word == string:
            count += 1
    return count
    
def ScoreFinder(players,scores,name):
    namelist = []
    for i in range(len(name)):
        namelist.append(name[i])
    namelist[0] = namelist[0].upper()
    namestring = ''.join(map(str, namelist))
    x = players.index(namestring)
    print(namestring,'got a score of',scores[x])

def Union(list1,list2):
    for i in list1:
        if list1.count(i) > 1:
            list1.remove(i)
    for i in list2:
        if list2.count(i) > 1:
            list2.remove(i)
    for i in list2:
        list1.append(i)
    return list1

def Intersection(x,y):
    newlist = []
    for word in x:
        if word in y:
            newlist.append(word)
    return newlist

def NotIn(x,y):
    newlist = []
    for word in x:
        if word not in y:
            newlist.append(word)
    return newlist

def main():
    players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
    scores = [5, 8, 10, 6, 10, 4]
    players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
    ScoreFinder(players, scores, "jill")
    PrintOutput(Union(scores, players))
    a = LoadFile("alice.txt")
    PrintOutput(str(FindWordCount(a, "Alice")))
    PrintOutput(Intersection(players, players2))
    PrintOutput(NotIn(players2, players))

    
