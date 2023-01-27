import datetime
x = datetime.datetime.now()
shortday = x.strftime("%a")
longday = x.strftime("%A")
day = x.strftime("%d")
month = x.strftime("%m")
year = x.strftime("%Y")
hour = x.strftime("%H")
Min = x.strftime("%M")
shortmonthname = x.strftime("%b")
longmonthname = x.strftime("%B")

def GetTime():
    return(hour + ":" + Min)

def GetDay(Text):
    if Text:
        return(longday)
    else:
        return(day)

def GetDT():
    date = GetDate()
    time = GetTime()
    return(date + " " + time)

def GetDate():
    return(""+day+"/"+month+"/"+year)

def GetTime():
    return(hour + ":" + Min)

def GetTime():
    return(hour + ":" + Min)