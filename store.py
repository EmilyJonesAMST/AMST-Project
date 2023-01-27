import Filetypes
import Timezone
from File import Access as FS
from File import AMST as AMST
import AMST as system
class Array:
    Files = []
    class files:
        def append(Item):
            if (Array.Files.__contains__(Item)):
                print("Skipping: "+ Item + " | Reason: Item Already Located in File |")
            else:
                #print("Adding: "+ Item )
                Array.Files.append(Item)

        def Retreve(index):
            return Array.Files[index]

    Stored = []
    class stored:
        def append(Item,File):
            if (Array.Stored.__contains__(Item)):
                print("Skipping: "+ Item + " | Reason: Item Already Added |")
            else:
                #print("Adding: "+ str(Item) )
                FS.Append(File,str(Item))
                Array.Stored.append(Item)
                
        def Retreve(index):
            return Array.Stored[index]

        def View():
            print(Array.Stored)

    Everything = []
    class everything:
        def append(Item,File):
            if (Array.Everything.__contains__(Item)):
                print("Skipping: "+ Item + " | Reason: Item Already Added |")
            else:
                #print("Adding: "+ str(Item) )
                FS.Append(File,str(Item))
                Array.Everything.append(Item)
                
        def Retreve(index):
            return Array.Everything[index]

        def View():
            print(Array.Everything)
def File(File,Name,Type):
# print("Storing: "+ Name)
    Array.files.append(Name)
    Array.stored.append((Name+","+Type+","+str(False)+","+"tag1"+","+"tag2"+","+"tag3"+","+"tag4"+","+"None"+","+Timezone.GetDT()+"\n"),File)
    Array.everything.append((Name+","+Type+","+str(False)+","+"tag1"+","+"tag2"+","+"tag3"+","+"tag4"+","+"None"+","+Timezone.GetDT()+"\n"),"Everything.csv")

def Log(File,Name):
# print("Storing: "+ Name)
    Array.files.append(Name)
    Array.stored.append((Name+","+Timezone.GetDT()+"\n"),File)
    Array.everything.append((Name+","+"Log Item"+","+str(False)+","+"tag1"+","+"tag2"+","+"tag3"+","+"tag4"+","+"None"+","+Timezone.GetDT()+"\n"),"Everything.csv")

#File("HI There","Bannna",1,2,3,4,"Emily")
#File("Hello There","Orange",1,2,3,4,"Josh")
#File("Text Goes Here","Strawberry",1,2,3,4,"Charlotte")