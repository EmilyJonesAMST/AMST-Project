from File import Access as FS
from utils import Video as UV
from Timezone import GetDT as DateTime
def FileWrite(Video,Extention):
    Type = UV.types(Extention)
    #Video ID , Name , Tag 1, Tag 2, Tag 3, Tag 4, Watched, Reviewer, Rating, Max Rating, Date Updated, Date Added
    lines = FS.Read("Videos.csv")
    VideoID = len(lines)
    if Type == "Video":
        Output = ""+ str(VideoID) + ","+ Video + ","+Type+",None,None,None,None,False,None,0,5,"+ DateTime() + ","+ DateTime() + "\n"
    else:
        if Type == "Unknown":
            Output = ""+ str(VideoID) + ","+ Video + ","+Type+",.,.,.,.,False,None,0,5,"+ DateTime() + ","+ DateTime() + "\n"
        else:
            Output = ""+ str(VideoID) + ","+ Video + ","+Type+",.,.,.,.,.,.,0,5,"+ DateTime() + ","+ DateTime() + "\n"
    FS.Append("Videos.csv",Output)