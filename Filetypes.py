
class Types():
    TagList =    ["Les,Goth,Teen,Jap,Bondage,Anal,Teach,Mums In Control,Nun,Cartoon,Furry,Medical,MTT,Cam,Teese,Fucked"]
    StaffList =  ["Emily.Jones,Joshua.Akester,Eleanor.Monks,Charlotte.Smith"] # Firstname.Lastname Must Contain Dot
    StaffRoles = ["AMST CEO,AMST Developer,AMST Review Team,AMST Obtainer"]
class Other:
    def DecodeTagArray(Array):
        return Array[0],Array[1],Array[2],Array[3]
class Locate:
    def Staff(Name):
        if len(Types.StaffList) == len(Types.StaffRoles):
            for StaffRaw in Types.StaffList:
                Staff = StaffRaw.split(",")
                for i in range(0,len(Staff)):
                    FoundName = Staff[i]
                    if (FoundName.__contains__(Name)):
                        Names = FoundName.split(".")
                        FirstName = Names[0]
                        LastName = Names[1]
                        StaffID = str(i + 1)
                        return (FirstName,LastName,StaffID)
