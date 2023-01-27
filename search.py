from operator import countOf
import os
from types import NoneType
import sorter
import synologychatsync as chat
import shutil
Paths = []
Files = []
Current_Directory = os.path.dirname(os.path.abspath(__file__))
dstmove = Current_Directory + '\Sorted'
print('Folder: ' + Current_Directory)
print(Current_Directory + '\lookup')

def run():
    for DirentryItem in os.scandir(Current_Directory + '\lookup'):
        item = str(DirentryItem).split("'")
        sorter.AddSort(item[1])
    else:
        chat.Message("SFW", "TEST - Python Search Running On AMST Files")
        chat.Message("ToDoList","Finding Files")
        sorter.Sorter.main()
