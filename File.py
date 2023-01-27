class Access:
    def Overwrite(File):
        f = open(File, "x")
        f.close()

    def Append(File,Text):
        f = open(File, "a")
        f.write(Text)
        f.close()

    def Read(File):
        f = open(File, "r")
        dump = f.read()
        lines = dump.split("\n")
        f.close()
        return lines

    def Create(File):
        f = open(File, "a")
        f.close()

    def ArrayFilter(Obj):
        x = Obj.split(",")
        return x

    def ReadLine(file,line):
        arr = Access.Read(file)
        #print(arr)
        for i in range(0,len(arr)):
            return Access.ArrayFilter(arr[line])
class AMST:
    def GetFileLenght(Destination):
        Access.Create(Destination)
        lines = Access.Read(Destination)
        return str(len(lines))

    def Finder(Destination,Search):
        arr = Access.Read(Destination)
        for i in range(0,len(arr)):
            Line = arr[i]
            #print(Line)
            x = (Access.ArrayFilter(Line))
            for D in x:
                #print(i)
                #print(D)
                if D.__contains__(Search):
                    return i
            i = i + 1