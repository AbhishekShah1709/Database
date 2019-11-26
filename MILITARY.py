import subprocess as sp
import pymysql
import pymysql.cursors


def GetAge():
    try:
        SoldierId = int(input("Enter Soldier Id to get Age: "))
        query = "SELECT DATE_FORMAT(NOW(), '%%Y') - DATE_FORMAT(DOB, '%%Y') - (DATE_FORMAT(NOW(), '00-%%m-%%d') < DATE_FORMAT(DOB, '00-%%m-%%d')) FROM SOLDIER where SoldierId = %d" % (SoldierId)
        cur.execute(query)
        age = cur.fetchall()
        age = age[0]
        for key, value in age.items():
            print(int(value))

    except Exception as e:
        con.rollback()
        print("Failed to find age")
        print(">>>>>>>>>>>>>", e)
    return

def AddColm():
    try:
        query = "ALTER TABLE EQUIPMENTS ADD MadeIn Varchar(50)"
        cur.execute(query)
        con.commit()
        print("New Column 'MadeIn' added to Equipments Table")
    except Exception as e:
        con.rollback()
        print("Failed to add MadeIn column to table")
        print(">>>>>>>>>>>>>", e)
    return

def AgeGrp():
    l = int(input("Enter Lower Bound of Age : "))
    r = int(input("Enter Upper Bound of Age : "))
    try:
        query = "select count(*) as count from SOLDIER where (DATE_FORMAT(NOW(), '%%Y') - DATE_FORMAT(DOB, '%%Y') - (DATE_FORMAT(NOW(), '00-%%m-%%d') < DATE_FORMAT(DOB, '00-%%m-%%d'))) >= %d and (DATE_FORMAT(NOW(), '%%Y') - DATE_FORMAT(DOB, '%%Y') - (DATE_FORMAT(NOW(), '00-%%m-%%d') < DATE_FORMAT(DOB, '00-%%m-%%d'))) <= %d" % (l, r)
        cur.execute(query)
        val = cur.fetchall()
        val = val[0]
        for key, val in val.items():
            print(key, end=" : ")
            print(val)

    except Exception as e:
        con.rollback()
        print("Failed to find count in age group")
        print(">>>>>>>>>>>>>", e)
    return


def BaseInfo():
    BaseId = int(input("Enter BaseId to get info of all soldiers there: "))
    query = "Select Position,Count(*) As Count from SOLDIER  where BaseId = %d group by Position" % (BaseId)
    try:
        cur.execute(query)
        val = cur.fetchall()
        for it in val:
            for key, val in it.items():
                print(key, end=" : ")
                print(val)
    except Exception as e:
        con.rollback()
        print("Failed to find Base Info")
        print(">>>>>>>>>>>>>", e)
    return


def ViewSoldier():
    view_soldier = "SELECT * FROM SOLDIER"
    cur.execute(view_soldier)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewBase():
    view_base = "SELECT * FROM BASE"
    cur.execute(view_base)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewDuty():
    view_duty = "SELECT * FROM DUTY"
    cur.execute(view_duty)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewEquipments():
    view_equipments = "SELECT * FROM EQUIPMENTS"
    cur.execute(view_equipments)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewEquipmentCount():
    view_equipmentcount = "SELECT * FROM EQUIPMENTCOUNT"
    cur.execute(view_equipmentcount)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewSoldierSalary():
    view_soldiersalary = "SELECT * FROM SOLDIERSALARY"
    cur.execute(view_soldiersalary)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewContact():
    view_contact = "SELECT * FROM CONTACT"
    cur.execute(view_contact)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def ViewContactInfo():
    view_contactinfo = "SELECT * FROM CONTACTINFO"
    cur.execute(view_contactinfo)
    myresult = cur.fetchall()
    if(len(myresult) == 0):
        print("Table is Empty")
        return
    for key, val in myresult[0].items():
        print(key, end="    ")
    print('\n')
    for it in myresult:
        for key, val in it.items():
            print(val, end="    ")
        print('\n')


def TotalSoldiers():
    base_count_query = "SELECT BaseId,Count(*) AS Count FROM SOLDIER GROUP BY BaseId"
    cur.execute(base_count_query)
    myresult = cur.fetchall()
    for it in myresult:
        for key, val in it.items():
            print(key, end=" : ")
            print(val)
        print('\n')


def HighestJob():
    highest_query = "SELECT * FROM SOLDIERSALARY ORDER BY SALARY DESC LIMIT 1"
    cur.execute(highest_query)
    myresult = cur.fetchall()
    myresult = myresult[0]
    for key, val in myresult.items():
        print(key, end=" : ")
        print(val)


def LowestJob():
    lowest_query = "SELECT * FROM SOLDIERSALARY ORDER BY SALARY LIMIT 1"
    cur.execute(lowest_query)
    myresult = cur.fetchall()
    myresult = myresult[0]
    for key, val in myresult.items():
        print(key, end=" : ")
        print(val)


def Countofequip():
    BaseId = int(
        input("Enter BaseId to get info of all Equipments present there: "))
    query = "Select WeaponName,Price,Count from EQUIPMENTS JOIN EQUIPMENTCOUNT on EQUIPMENTS.WeaponId = EQUIPMENTCOUNT.WeaponId where BaseId = %d" % (
        BaseId)
    try:
        cur.execute(query)
        val = cur.fetchall()
        # print(val[0])
        # print(val[1])
        for it in val:
            for key, value in it.items():
                print(key, end=" : ")
                print(value)
            print('\n')

    except Exception as e:
        con.rollback()
        print("Failed to find equipments")
        print(">>>>>>>>>>>>>", e)
    return


def AddContactInfo():
    try:
        print("Enter Contact Info: ")
        soldierid = int(input("Enter SoldierId: "))
        contactno = input("Enter ContactNo: ")
        if len(contactno) != 10:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", "Not a valid Contact Number")
            return
        parent = input("Enter Parent's Name: ")
        streetaddress = input("Street Address: ")
        city = input("City: ")
        state = input("State: ")
        pincode = int(input("Pincode: "))

        contactinfo_query = """INSERT INTO CONTACTINFO(ContactNumber, Parent, StreetAddress, Pincode, City, Stat ) VALUES('%s','%s','%s',%d,'%s','%s')""" % (
            contactno, parent, streetaddress, pincode, city, state)

        contact_query = """INSERT INTO CONTACT(SoldierId, ContactNumber) VALUES(%d,'%s')""" % (
            soldierid, contactno)

        cur.execute(contactinfo_query)
        cur.execute(contact_query)
        print("New Contact Info successfully inserted into the database")
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database111")
        print(">>>>>>>>>>>>>", e)
        flag = 1

    return


def AddPosition():
    try:
        print("Enter new Salary details: ")
        pos1 = input("Enter Position: ")
        salary1 = int(input("Enter salary: "))

        if salary1 < 0:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", "Invalid Salary")
            return

        salary_query = """INSERT INTO SOLDIERSALARY(Position, Salary) VALUES('%s',%d)""" % (
            pos1, salary1)

        print("New Salary successfully inserted into the database")
        cur.execute(salary_query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddBase():
    try:
        print("Enter new Base details: ")

        # baseid = int(input("Enter BaseID: "))
        basetype = input("Enter Base Location: ")

        base_query = """INSERT INTO BASE(Baselocation) VALUES('%s')""" % (
            basetype)

        print("New Base successfully inserted into the database")
        cur.execute(base_query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddDuty():
    try:
        print("Enter new Duty details: ")
        # dutyid = int(input("Enter DutyID: "))
        dutytype = input("Enter DutyType: ")

        duty_query = """INSERT INTO DUTY(DutyType) VALUES('%s')""" % (
            dutytype)

        print("New Duty successfully inserted into the database")
        cur.execute(duty_query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def BuyAEquipment():
    val = 0
    try:
        query = "select count(*) as cnt from information_schema.columns where table_name = 'EQUIPMENTS'"
        cur.execute(query)
        val = cur.fetchall()
        val = val[0]
        val = val['cnt']
    except Exception as e:
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
        return 

    if val == 3:
        try:
            row = {}
            print("Enter new weapon's details: ")
            row["WeaponName"] = input("Weapon Name: ")
            # row["WeaponId"] = int(input("Weapon-Id: "))
            row["Price"] = int(input("Price: "))

            if row["Price"] < 0:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>", "Invalid Price")
                return

            query1 = """INSERT INTO EQUIPMENTS(WeaponName, Price) VALUES('%s', %d)""" % (
                row["WeaponName"], row["Price"])
            cur.execute(query1)
            con.commit()
            print("New Equipment inserted into database")

        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
        return 
    elif val == 4:
        try:
            row = {}
            print("Enter new weapon's details: ")
            row["WeaponName"] = input("Weapon Name: ")
            # row["WeaponId"] = int(input("Weapon-Id: "))
            row["Price"] = int(input("Price: "))

            if row["Price"] < 0:
                print("Failed to insert into database")
                print(">>>>>>>>>>>>>", "Invalid Price")
                return
            row["MadeIn"] = input("MadeIn : ")
            query1 = """INSERT INTO EQUIPMENTS(WeaponName, Price,MadeIn) VALUES('%s', %d,'%s')""" % (
                row["WeaponName"], row["Price"],row['MadeIn'])
            cur.execute(query1)
            con.commit()
            print("New Equipment inserted into database")

        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
        return


def AddEquipmenttoBase():
    try:
        row = {}
        print("Enter Weapon's and Base details: ")
        row["WeaponId"] = int(input("Weapon-Id: "))
        row["BaseId"] = int(input("Base-Id: "))
        row["Count"] = int(input("Count: "))

        if row["Count"] < 0:
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", "Invalid Count")
            return

        query = """INSERT INTO EQUIPMENTCOUNT(WeaponId, BaseId, Count) VALUES(%d, %d, %d)""" % (
            row["WeaponId"], row["BaseId"], row["Count"])

        cur.execute(query)
        con.commit()
        print("New Equipment inserted into Base")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def check(arg):
    query3 = "Select count(*) as cnt from SOLDIER where SoldierId = %d" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0

def check3(arg):
    query3 = "Select count(*) as cnt from BASE where BaseId = %d" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0

def check2(arg):
    query3 = "Select count(*) as cnt from DUTY where DutyId = %d" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0

def check1(arg):
    query3 = "Select count(*) as cnt from EQUIPMENTS where WeaponId = %d" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0



def check(arg):
    query3 = "Select count(*) as cnt from SOLDIER where SoldierId = %d" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0

def RemoveBase():
    print("Enter Base ID: ")
    delete_id = int(input("BaseId: "))
    a = check3(delete_id)
    if a == 0:
        print("No row with given Id")
        return
    try:
        query1 = "DELETE FROM BASE where BaseId = %d" % (delete_id)
        cur.execute(query1)
        con.commit()
        print("Base has been removed")
    except Exception as e:
        con.rollback()
        print("Failed to remove from database")
        print(">>>>>>>>>>>>>", e)

def RemoveDuty():
    print("Enter Duty ID: ")
    delete_id = int(input("DutyId: "))
    a = check2(delete_id)
    if a == 0:
        print("No row with given Id")
        return
    try:
        query1 = "DELETE FROM DUTY where DutyId = %d" % (delete_id)
        cur.execute(query1)
        con.commit()
        print("Duty has been removed")
    except Exception as e:
        con.rollback()
        print("Failed to remove from database")
        print(">>>>>>>>>>>>>", e)

def RemoveEquipment():
    print("Enter Equipment's ID: ")
    delete_id = int(input("EquipmentId: "))
    a = check1(delete_id)
    if a == 0:
        print("No row with given Id")
        return
    try:
        query1 = "DELETE FROM EQUIPMENTS where WeaponId = %d" % (delete_id)
        cur.execute(query1)
        con.commit()
        print("Equipment has been removed")
    except Exception as e:
        con.rollback()
        print("Failed to remove from database")
        print(">>>>>>>>>>>>>", e)

def RemoveSoldier():
    print("Enter Soldier's ID: ")
    delete_id = int(input("SoldierId: "))
    a = check(delete_id)
    if a == 0:
        print("No row with given Id")
        return
    try:
        query1 = "DELETE FROM SOLDIER where SoldierId = %d" % (delete_id)
        cur.execute(query1)
        con.commit()
        print("Soldier has retired")
    except Exception as e:
        con.rollback()
        print("Failed to remove from database")
        print(">>>>>>>>>>>>>", e)

def UpdateDuty():
    SoldierId = int(input("Enter Soldier Id of Soldier to Update: "))
    a = check(SoldierId)
    if a == 0:
        print("No row with given Id")
        return
    print("Enter soldier's new Duty Id: ")
    new_duty_id = int(input("New duty id: "))
    query_duty = "UPDATE SOLDIER SET DutyId =  %d where SoldierId = %d" % (
        new_duty_id, SoldierId)

    try:
        cur.execute(query_duty)
        con.commit()
        print("Soldier's duty changed sucessfully")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdateBase():
    SoldierId = int(input("Enter Soldier Id of Soldier to Update: "))
    a = check(SoldierId)
    if a == 0:
        print("No row with given Id")
        return
    print("Enter Soldier's New Base Id: ")
    new_base_id = int(input("New base id: "))
    query_base = "UPDATE SOLDIER SET BaseId = %d where SoldierId = %d" % (
        new_base_id, SoldierId)

    try:
        cur.execute(query_base)
        con.commit()
        print("Soldiers is posted to new location")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def UpdatePosition():
    SoldierId = int(input("Enter Soldier Id of Soldier to Update: "))
    a = check(SoldierId)
    if a == 0:
        print("No row with given Id")
        return
    print("Enter Soldier's New Position")
    new_position = input("New Position :")
    query_base = "UPDATE SOLDIER SET Position = '%s' where SoldierId = %d" % (
        new_position, SoldierId)

    try:
        cur.execute(query_base)
        con.commit()
        print("Soldier's Position is changed")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def checkb(arg1, arg2):
    query3 = "Select count(*) as cnt from EQUIPMENTCOUNT where WeaponId = %d and BaseId = %d" % (arg1, arg2)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0


def UpdateCount():
    print("Enter WeaponId: ")
    ch_weaponid = int(input("Weapon-Id: "))

    print("Enter BaseId: ")
    ch_baseid = int(input("Base-Id: "))
    a = checkb(ch_weaponid, ch_baseid)
    if a == 0:
        print("No row with given Weapon and Base Id")
        return

    print("Enter New Count: ")
    ch_count = int(input("Count: "))

    if ch_count < 0:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", "Invalid Count")
        return

    count_query = "UPDATE EQUIPMENTCOUNT SET Count = %d where BaseId = %d and WeaponId = %d" % (
        ch_count, ch_baseid, ch_weaponid)

    try:
        cur.execute(count_query)
        con.commit()
        print("New Count is changed")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def checkp(arg):
    query3 = "Select count(*) as cnt from SOLDIERSALARY where Position = '%s'" % (arg)
    try:
        cur.execute(query3)
        val = cur.fetchall()
        val = val[0]
        return val['cnt']
    except Exception as e:
        con.rollback()
        print("Failed to run query")
        print(">>>>>>>>>>>>>", e)
    return 0


def UpdateSalary():
    Position = input("Enter Position of which to update Salary: ")
    a = checkp(Position)
    if a == 0:
        print("No row with given Position")
        return
    new_salary = int(input("New Salary of " + Position + " : "))

    if new_salary < 0:
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", "Invalid Salary")
        return

    query = "UPDATE SOLDIERSALARY SET Salary = %d where Position = '%s'" % (
            new_salary, Position)
    try:
        cur.execute(query)
        con.commit()
        print("Salary of " + Position + " Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return


def SoldierStatistics():
    """
    Function prints a report containing
    the number of hours per week the employee works,
    hourly pay, projects employee works on and so on
    """
    print("Not implemented")


def AddNewSoldier():
    try:
        row = {}
        print("Enter new soldier's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Mname"] = name[1]
        row["Lname"] = name[2]
        row["Gender"] = input("Gender: ")
        # row["SoldierId"] = int(input("Soldier-Id: "))
        row["BaseId"] = int(input("Base-Id: "))
        row["DutyId"] = int(input("Duty-Id: "))
        row["JoiningDate"] = input("Joining Date (YYYY-MM-DD): ")
        row["DOB"] = input("D.O.B (YYYY-MM-DD): ")
        row["HeadId"] = int(input("Head-Id: "))
        row["Position"] = input("Position: ")
        row["Category"] = int(
            input("Category (1 for Land,2 for Navy,3 for Airforce): "))

        """
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

    #    query3 = """INSERT INTO AGE(DOB) VALUES('%s')""" %(row["DOB"])

    #    print(query3)
     #   cur.execute(query3)
      #  con.commit()

        query = """INSERT INTO SOLDIER(Fname, Mname, Lname, Gender,BaseId, DutyId, JoiningDate, DOB, HeadId, Position, Category) VALUES('%s', '%s', '%s', '%s', %d, %d, '%s', '%s', %d, '%s', %d)""" % (
            row["Fname"], row["Mname"], row["Lname"], row["Gender"], row["BaseId"], row["DutyId"], row["JoiningDate"], row["DOB"], row["HeadId"], row["Position"], row["Category"])

        cur.execute(query)
        con.commit()

        print("New Soldier's Data Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        AddNewSoldier()
    elif(ch == 2):
        AddBase()
    elif(ch == 3):
        AddDuty()
    elif(ch == 4):
        AddPosition()
    elif(ch == 5):
        AddContactInfo()
    elif(ch == 6):
        BuyAEquipment()
    elif(ch == 7):
        AddEquipmenttoBase()
    elif(ch == 8):
        RemoveSoldier()
    elif(ch == 9):
        UpdateDuty()
    elif(ch == 10):
        UpdateBase()
    elif(ch == 11):
        UpdatePosition()
    elif(ch == 12):
        UpdateCount()
    elif(ch == 13):
        UpdateSalary()
    elif (ch == 14):
        HighestJob()
    elif(ch == 15):
        LowestJob()
    elif(ch == 16):
        Countofequip()
    elif(ch == 17):
        TotalSoldiers()
    elif(ch == 18):
        GetAge()
    elif(ch == 19):
        ViewSoldier()
    elif(ch == 20):
        ViewBase()
    elif(ch == 21):
        ViewDuty()
    elif(ch == 22):
        ViewEquipments()
    elif(ch == 23):
        ViewEquipmentCount()
    elif(ch == 24):
        ViewSoldierSalary()
    elif(ch == 25):
        ViewContact()
    elif(ch == 26):
        ViewContactInfo()
    elif(ch == 27):
        BaseInfo()
    elif(ch == 28):
        AgeGrp()
    elif(ch == 29):
        AddColm()
    elif(ch == 30):
        RemoveBase()
    elif(ch == 31):
        RemoveDuty()
    elif(ch == 32):
        RemoveEquipment()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='MILITARY',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Add a New soldier", end="\t\t\t\t\t")
                print("2. Add a New Base")
                print("3. Add a New Duty", end="\t\t\t\t\t")
                print("4. Add a New Position")
                print("5. Add Contact Info", end="\t\t\t\t\t")
                print("6. Buy a New Equipment")
                print("7. Add equipment to base", end="\t\t\t\t")
                print("8. Fire an soldier")
                print("9. Update Soldier's Duty", end="\t\t\t\t")
                print("10. Update Soldier's Base")
                print("11. Update Soldier's Position", end="\t\t\t\t")
                print("12. Update Count of Weapon at a Base")
                print("13. Update Salary of a Position", end="\t\t\t\t")
                print("14. Highest Paid Position")
                print("15. Lowest Paid Position", end="\t\t\t\t")
                print("16. All Equipments present at some base")
                print("17. Total Soldiers in a base", end="\t\t\t\t")
                print("18. Get Age of Soldier")
                print("19. View SOLDIER Table", end="\t\t\t\t\t")
                print("20. View BASE Table")
                print("21. View DUTY Table", end="\t\t\t\t\t")
                print("22. View EQUIPMENTS Table")
                print("23. View EQUIPMENTCOUNT Table", end="\t\t\t\t")
                print("24. View SOLDIERSALARY Table")
                print("25. View CONTACT Table", end="\t\t\t\t\t")
                print("26. View CONTACTINFO Table")
                print("27. All Positions at some base", end="\t\t\t\t")
                print("28. Number of Soldiers in Age group")
                print("29. Add Field 'Made In' to EQUIPMENTS Table", end="\t\t")
                print("30. Remove a Base")
                print("31. Remove a Duty", end="\t\t\t\t\t")
                print("32. Remove a Equipment")
                print("33. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 33:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
