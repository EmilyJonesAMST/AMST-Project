from File import Access as FS
class Video:
    def Extention(File):
        StrLen = len(File)
        LastLetter = StrLen
        SearchLetter = LastLetter - 1
        Extention = ""
        while True:
            if File[SearchLetter] == ".":
                break
            else:
                Extention = Extention + str(File[SearchLetter])
                SearchLetter = SearchLetter - 1
        rev = Extention[::-1]
        return rev
    
    def AfterExtentionConvert(File,RemIn):
        remove = len(File) - RemIn
        str = File[:remove] + "" + File[len(File):]
        Output = str.replace(".", "" )
        return Output

    def Converter(File):
        extention = Video.Extention(File)
        Name = Video.AfterExtentionConvert(File,len(extention))
        return Name,extention

    def types(Extention):
        if Extention.lower() == "mp4":
            return "Video"
        elif Extention.lower() == "jpg":
            return "Image"
        elif Extention.lower() == "jpeg":
            return "Image"
        elif Extention.lower() == "png":
            return "Image"
        else:
            return "Unknown"
    class Revew:
        def exsits(File):
            Lines = FS.Read("Videos.csv")
            for Items in Lines:
                Item = Items.split(",")
                #print(Item)
                #print(len(Item))
                if len(Item) == 1:
                    for i in range(0,len(Item)):
                        if Items.__contains__(File):
                            Out = True
                            return Out
            # index 6

                    