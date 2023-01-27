from File import Access as FS
import os
from store import File as F
import AMST as System
import Timezone
import Filetypes

Tags = []
Array = []
NewDataSet = []
class setup:
    def run(Path):
        OldFile = FS.Read(Path)
        for line in OldFile:
            if line != "":
                Array.append(line)
                

    def Remove(Path):
        os.remove(Path)
        FS.Overwrite(Path)
def ReviewVideo(ID,Reviewer,Tag1,Tag2,Tag3,Tag4):
    OldData= Array[int(ID)].split(",")
    NewData = OldData[0]+","+OldData[1]+","+str(True)+","+Tag1+","+Tag2+","+Tag3+","+Tag4+","+Reviewer+","+Timezone.GetDT()
    
    for i in range(0,len(Array)):
        if i == int(ID):
            NewDataSet.append(NewData + "\n")
            
        else:
            NewDataSet.append(Array[i]+ "\n")
            
        i = i + 1
def WriteChanges(Path):
    for item in NewDataSet:
        FS.Append(Path,item)
    print("Complete")

#Path = "rando.txt"
#setup.run(Path)
#ReviewVideo(System.GetIndex(Path,"HI"),"Josh","1","2","3","4")
#setup.Remove(Path)
#WriteChanges(Path)

def Tagger():
    MaxTagLen = 9
    Tag1 = input("Enter First Tag: ")
    if(len(Tag1) > MaxTagLen):
        print("Tag Too Long")
    else:
        for item in Filetypes.Types.TagList:
            if item.__contains__(Tag1):
                print("Matched Tag")
                Tags.append(Tag1)

            else:
                print("unable to match tag automaticly")
                print("Please Enter Tag From The List Or Pick "+"'Other'")
                print(Filetypes.Types.TagList)
                In = input("Enter Option: ")
                if In == "Other" or "other":

                    Tags.append(Tag1)

                else:
                    for item in Filetypes.Types.TagList:
                        if item.__contains__(In):

                            Tags.append(Tag1)

                            for tagg in Tags:
                                if tagg.__contains__(Tags):
                                    print("Skipping Tag")
                                else:

                                    Tags.append(item)


    Tag2 = input("Enter Second Tag: ")
    if(len(Tag2) > MaxTagLen):
        print("Tag Too Long")
    else:
        for item in Filetypes.Types.TagList:
            if item.__contains__(Tag2):
                print("Matched Tag")
                Tags.append(Tag2)

            else:
                print("unable to match tag automaticly")
                print("Please Enter Tag From The List Or Pick "+"'Other'")
                print(Filetypes.Types.TagList)
                In = input("Enter Option: ")
                if In == "Other" or "other":

                    Tags.append(Tag2)

                else:
                    for item in Filetypes.Types.TagList:
                        if item.__contains__(In):

                            Tags.append(Tag2)

                            for tagg in Tags:
                                if tagg.__contains__(Tags):
                                    print("Skipping Tag")
                                else:

                                    Tags.append(item)


    Tag3 = input("Enter Third Tag: ")
    if(len(Tag3) > MaxTagLen):
        print("Tag Too Long")
    else:
        for item in Filetypes.Types.TagList:
            if item.__contains__(Tag3):
                print("Matched Tag")
                Tags.append(Tag3)

            else:
                print("unable to match tag automaticly")
                print("Please Enter Tag From The List Or Pick "+"'Other'")
                print(Filetypes.Types.TagList)
                In = input("Enter Option: ")
                if In == "Other" or "other":

                    Tags.append(Tag3)

                else:
                    for item in Filetypes.Types.TagList:
                        if item.__contains__(In):
                            print("Matched Tag")
                            Tags.append(Tag2)

                            for tagg in Tags:
                                if tagg.__contains__(Tags):
                                    print("Skipping Tag")
                                else:
                                    Tags.append(item)


    Tag4 = input("Enter Final Tag: ")
    if(len(Tag4) > MaxTagLen):
        print("Tag Too Long")
    else:
        for item in Filetypes.Types.TagList:
            if item.__contains__(Tag4):
                print("Matched Tag")
                Tags.append(Tag4)

            else:
                print("unable to match tag automaticly")
                print("Please Enter Tag From The List Or Pick "+"'Other'")
                print(Filetypes.Types.TagList)
                In = input("Enter Option: ")
                if In == "Other" or "other":

                    Tags.append(Tag4)

                else:

                    for item in Filetypes.Types.TagList:
                        if item.__contains__(In):
                            print("Matched Tag")
                            Tags.append(Tag4)

                            for tagg in Tags:
                                if tagg.__contains__(Tags):
                                    print("Skipping Tag")
                                else:

                                    Tags.append(item)

