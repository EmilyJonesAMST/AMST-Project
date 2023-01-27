from File import Access as FS
from File import AMST as AMST

def GetWatched(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[2].replace(" ","")
    if test == "False":
        return False
    else:
        return True

def GetTags(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    tag1 = arr[3].replace(" ","")
    tag2 = arr[4].replace(" ","")
    tag3 = arr[5].replace(" ","")
    tag4 = arr[6].replace(" ","")
    return (tag1,tag2,tag3,tag4)

def GetReviewer(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[7].replace(" ","")
    return test

def GetAddTime(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[8].replace(" ","")
    return test

def GetType(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[1].replace(" ","")
    return test

def GetName(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[0]
    print(test)
    return test

def GetIndex(File,VideoName):
    arr = FS.ReadLine(File,AMST.Finder(File,VideoName))
    test = arr[0]
    f = open(File, "r")
    dump = f.read()
    lines = dump.split("\n")
    for i in range(0,len(lines)):
        item = lines[i]
        if item != "":
            DiscriptionMade = item.split(",") # Target Index 3
            if DiscriptionMade[0].__contains__(test):
                return str(i)
        f.close()
    i = i + 1