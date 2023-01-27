ToRename = []
Named = []
other = []
sortlist = []
duplicate = []
optional = []
sortlength = 0
from Program import Main
import synologychatsync as chat
i = 0
def AddSort(item):
    sortlist.append(item)
class Sorter:
    
    def main():
        sortlength = len(sortlist)
        print("Sorting: " + str(sortlength)+ " Files")
        for i in range(0,sortlength):
            item = sortlist[i]
            if(item.__contains__("xvideos.com_")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                ToRename.append(item)
                Main.Log("Rename.txt",item)
                if (item.__contains__("(1)")):
                    duplicate.append(item)
                    Main.Log("Duplicate.txt",item)
                sortlist[i] = ""
            i = i + 1
        

        i = 0
        for i in range(0,sortlength):
            item = sortlist[i]
            if(item.__contains__("Video - ")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                other.append(item)
                Main.Log("Sort.txt",item)
                sortlist[i] = ""
            i = i + 1
        

        i = 0
        for i in range(0,sortlength):
            item = sortlist[i]
            if(item.__contains__("(1)")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                duplicate.append(item)
                Main.Log("Duplicate.txt",item)
                Main.Add("Files.csv",item)

                sortlist[i] = "" # Option to replace sortlist item with air
            elif(item.__contains__("(2)")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                duplicate.append(item)
                Main.Log("Duplicate.txt",item)
                Main.Add("Files.csv",item)

                sortlist[i] = "" # Option to replace sortlist item with air
            elif(item.__contains__("(3)")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                duplicate.append(item)
                Main.Log("Duplicate.txt",item)
                Main.Add("Files.csv",item)

                sortlist[i] = "" # Option to replace sortlist item with air
            elif(item.__contains__("(4)")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                duplicate.append(item)
                Main.Log("Duplicate.txt",item)
                Main.Add("Files.csv",item)

                sortlist[i] = "" # Option to replace sortlist item with air
            i = i + 1
        

        i = 0
        for i in range(0,sortlength):
            item = sortlist[i]
            if(item.__contains__("XVIDEOS.COM.")):
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                optional.append(item)
                #sortlist[i] = "" # Option to replace sortlist item with air
            i = i + 1
        


        scanned = 0
        for item in sortlist:
            if item != "":
                item1 = item.replace(","," ")
                item = item1.replace("'s"," ")
                Named.append(item)
                Main.Add("Files.csv",item)
                scanned = scanned + 1
        skipped = sortlength - scanned
        
        print("To Rename: " + str(len(ToRename))+ " Files")
        print("Other: " + str(len(other))+ " Files")
        print("Duplicates: " + str(len(duplicate))+ " Files")
        print("Optionaly: " + str(len(optional))+ " Files")
        print("Skipped "+ str(skipped) + " Files")
        chat.Message("General", "Python Search Completed")
        chat.Message("General", "Found: "+ str(len(ToRename)) + " Needing to be Renamed")
        chat.Message("ToDoList", "Found: "+ str(len(ToRename)) + " Files Needing to be Renamed")
        chat.Message("General", "Found: "+ str(len(other)) + " Files Flagged as Other")
        chat.Message("General", "Found: "+ str(len(duplicate)) + " Files Are Posible Duplicates")
        chat.Message("General", "Found: "+ str(len(optional)) + " Files Flagged as Optional")
        chat.Message("General", "Found: "+ str(len(Named)) + " Files are Saved (Files Meet Name Criteria)")
        chat.Message("Reviewed", "Found: "+ str(len(Named)) + " Files Already Named")