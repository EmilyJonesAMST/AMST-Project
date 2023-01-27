import Filetypes
import review
import AMST as System
from store import File as FS
from store import Log as LS
class Main:
    def Review(Path,File):
        Reviewer = input("Enter User: ")
        if (Filetypes.Locate.Staff(Reviewer) == None):
            print("No User Found")
        else:
            FN,LN,ID = Filetypes.Locate.Staff(Reviewer)
            print("Welcome: "+ FN + " " + LN)
            review.Tagger()
            Tag1,Tag2,Tag3,Tag4 = Filetypes.Other.DecodeTagArray(review.Tags)
            review.setup.run(Path)
            review.ReviewVideo(System.GetIndex(Path,File),ID,Tag1,Tag2,Tag3,Tag4)
            review.setup.Remove(Path)
            review.WriteChanges(Path)
    def Add(File,Data):
        if Data.__contains__(".mp4"):
            FS(File,Data,"Video")
        elif Data.__contains__(".jpg"):
            FS(File,Data,"Photo")
        elif Data.__contains__(".jpeg"):
            FS(File,Data,"Photo")
        elif Data.__contains__(".png"):
            FS(File,Data,"Photo")
        elif Data.__contains__(".mp3"):
            FS(File,Data,"Audio")
        else:
            FS(File,Data,"Other")

    def Log(File,Data):
        LS(File,Data)
