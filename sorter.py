import NASprintsimulation as chat
from utils import Video as UV
from ExcelWrite import FileWrite as Write
import search

ToRename = []
Named = []
other = []
sortlist = []
duplicate = []
optional = []
sortlength = 0



i = 0
def AddSort(item):
    sortlist.append(item)
class Sorter:
    def main():
        sortlength = len(sortlist)
        print("Sorting: " + str(sortlength)+ " Files")
        for i in range(0,sortlength):
            item = sortlist[i]
            Video,Extention = UV.Converter(item)
            exsits = UV.Revew.exsits(Video)
            if exsits:
                print("Item "+ str(i+1) + "/"+str(sortlength)+ " : " + Video + " : Already Exsits")
                
            else:
                print("Item "+ str(i+1) + "/"+str(sortlength)+ " : " + Video + " : Doesnt Exsit")
                Write(item,Extention)
        chat.Message("General", "Python Search Completed")
        

if __name__ == "__main__":
    search.run()