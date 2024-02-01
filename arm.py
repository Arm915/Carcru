import tkinter as tk

from tkinter import *
from tkinter import ttk

car=tk.Tk()
car.geometry('1200x600')
car.title("CarCRU")

Name=tk.StringVar()#ชื่อ
Lastn=tk.StringVar()#นามสกุล
IdenNumber=tk.StringVar()#เลขบัต ปชช
Phonenumber=tk.StringVar()#เบอร์โทร
Residence=tk.StringVar()#ที่อยู่
Day=tk.StringVar()#วันที่
Month=tk.StringVar()#เดือน
Year=tk.StringVar()#ปี
Carcru=tk.StringVar()#ราคารถ
DownPayment=tk.StringVar()#ค่าดาว%
Dowtotal=tk.StringVar()#ราคาจ่ายดาว
Rmoney=tk.StringVar()#ค่ารถ
Namecar=tk.StringVar()#ชื่อรถ
Timeperiod=tk.StringVar()#เวลาผ่อน
Instalpermonth=tk.StringVar()#ผ่อนต่อเดือน
star=tk.StringVar()



def ph():#
    Down = tk.Toplevel()
    Button(Down, image=down1, borderwidth=0,).pack(side=LEFT)

def datashow():
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                  database='db_test')
    cursor = con.cursor()
    sql = "SELECT name,lname,phone,residence,Carcru,DownPayment,Dowtotal,Timeperiod,Instalpermonth FROM carcru"
    cursor.execute(sql)
    m=str(star.get())
    cursor.close()
    con.close()
    s = ""+str(r)+""
    txtBill.insert(END, (s))
    star.set(m)

def databest():
    name = (Name.get())
    lastn = Lastn.get()
    phonenumber = Phonenumber.get()
    residence = Residence.get()
    carcru = Carcru.get()
    downPayment = DownPayment.get()
    dowtotal = Dowtotal.get()
    timeperiod = Timeperiod.get()
    instalpermonth = Instalpermonth.get()
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                      database='db_test')
    cursor = con.cursor()
    sql = """INSERT INTO carcru(name,lname,phone,residence,Carcru,DownPayment,Dowtotal,Timeperiod,Instalpermonth)
    VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
    cursor.execute(sql,(name,lastn,phonenumber,residence,carcru,downPayment,dowtotal,timeperiod,instalpermonth))
    con.commit()
    con.close()

def showName(i):#
    namecar=(i.widget["text"])
    Namecar.set(namecar)

def down():#
    global total2
    Down=int(DownPayment.get())
    cartotal=int(Carcru.get())
    if Down < 5 :
        dow = "เงินดาวไม่พอ"
    elif Down > 100 :
        dow = "จำนวนเกิน100%"
    elif Down < 10 :
        dow = (cartotal * Down) / 100
        total1 = int(cartotal-dow)
        total2 = int(total1 * 0.0258)+total1
    elif Down < 20 :
        dow = (cartotal * Down) / 100
        total1 = int(cartotal-dow)
        total2 = int(total1 * 0.0103)+total1
    else:
        dow = (cartotal * Down) / 100
        total1 = int(cartotal-dow)
        total2 = int(total1 * 0.0087)+total1
    Dowtotal.set(dow)
    Rmoney.set(total2)

def instalpermonth():#
    ctype= int(Timeperiod.get())
    Total = int(Rmoney.get())
    if ctype < 48:
        arm =  int(Total / ctype)
    elif ctype < 60:
        arm = int(Total / ctype)
    else:
        arm = int(Total / ctype)
    Instalpermonth.set(arm)

def Data():#
    name = (Name.get())
    day = (Day.get())
    month = (Month.get())
    year = Year.get()
    lastn = Lastn.get()
    idenNumber = IdenNumber.get()
    phonenumber = Phonenumber.get()
    residence = Residence.get()
    carcru = Carcru.get()
    downPayment = DownPayment.get()
    dowtotal = Dowtotal.get()
    rmoney = Rmoney.get()
    namecar = Namecar.get()
    timeperiod = Timeperiod.get()
    instalpermonth = Instalpermonth.get()
    slip = "\t\t\t\tCarCru\n\t\t\t     เอกสารสัญญาซื้อรถ\n\n" \
           "\t\t\t\t\tวัน" + str(day) + "\tเดือน" + str(month) + "\tปี" + str(year) + "\n\n\t     ชื่อนามสกุล  " + str(name) + \
           "\t\t"+ str(lastn) + "\t\tอายุ  "  + str(21) + "  ปี  สัญชาติ  "+ str('ไทย') +"\n\tเลขบัตประชาชน" + str(idenNumber) + "\n\tที่อยู่ " \
            + str(residence) + "\n\tเบอร์โทร  " + str(phonenumber) + "\n\n\tรถรุ่น  "+ str(namecar) \
           +"\t\t\tราคารถ   "+ str(carcru) +"\t\tบาท" "\n\tดาวน์  "  + str(downPayment) + "  %\t\t\tเป็นเงิน  " + str(dowtotal) + \
           "\t\tบาท\n\tค่าจัดไฟแนนซ์   " + str(rmoney) + "\t\tบาท\tระยะเวลาผ่อน  " + str(timeperiod) + "\t เดือน\n\tผ่อนเดือนละ\t " \
           + str(instalpermonth) + "\tบาท\n\n\n\n\t ลงชื่อ...............ผู้ขาย\t\t\t\tลงชื่อ...............ผู้รับโอน\n\n\n\t    " \
                         "(..............)\t\t\t\t   (..............)\n\n\t    เซ็นรับรองว่าเป็นลายมือจริง\n\n\n" \
                         "\t ลงชื่อ...............ผู้รับโอน\t\t\t\tลงชื่อ...............ผู้ยื่นคำร้อง\n\n\n\t    (..............)\t\t\t\t " \
                         "  (..............)\n\n\t"
    txtBill.insert(END, (slip))

history=tk.LabelFrame(car,text="ข้อมูลลูกค้า",width=580,height=280,labelanchor='n',bg="#CCFFFF",bd=10,fg = "black",
                       font = "Castellar 17 underline")
history.grid(column=0,row=0,padx=5,pady=5)
Carlist=tk.LabelFrame(car,text="คำนวน",width=580,height=300,labelanchor='n',bg = "#CCFFFF",bd=10,fg = "black",
                       font = "Castellar 17 underline")
Carlist.grid(column=0,row=1,padx=5,pady=5)
TxT=tk.LabelFrame(car,text="สัญญา",width=590,height=590,labelanchor='n',bg = "#CCFFFF",bd=10,fg = "black",
                       font = "Castellar 17 underline")
TxT.place(x=600,y=295,anchor="w")

name=tk.Label(history,text="ชื่อลูกค้า :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
name.place(x=71,y=30,anchor="w")
Lastname=tk.Label(history,text="นามสกุล :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
Lastname.place(x=72,y=60,anchor="w")
idenNumber=tk.Label(history,text="เลขบัตประชาชน :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
idenNumber.place(x=10,y=90,anchor="w")
TransactionDate=tk.Label(history,text="เบอร์โทรศัพ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
TransactionDate.place(x=46,y=120,anchor="w")
residence=tk.Label(history,text="ที่อยู่ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
residence.place(x=105,y=150,anchor="w")
phonenumber=tk.Label(history,text="วันที่ทำรายการ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF')
phonenumber.place(x=23,y=180,anchor="w")

name=tk.Entry(history,bg='#FDF5E6',textvariable=Name,width=25).place(x=170,y=30,anchor="w")
Lastname=tk.Entry(history,bg='#FDF5E6',textvariable=Lastn,width=25).place(x=170,y=60,anchor="w")
idenNumber=tk.Entry(history,bg='#FDF5E6',textvariable=IdenNumber,width=25).place(x=170,y=90,anchor="w")
phonenumber=tk.Entry(history,bg='#FDF5E6',textvariable=Phonenumber,width=25).place(x=170,y=121,anchor="w")
residence=tk.Entry(history,bg='#FDF5E6',textvariable=Residence,width=55).place(x=170,y=150,anchor="w")

day=ttk.Combobox(car,value=['Day', '1', '2', '3', '4', '5', '6', '7','8', '9', '10',
                               '11', '12', '13', '14', '15', '16','17', '18', '19', '20',
                               '21', '22', '23', '24', '25','26', '27',
                               '28', '29', '30', '31'],width=3,textvariable=Day)
day.current(0)
day.place(x=180,y=215,anchor="w")

month=ttk.Combobox(car,value=["Month",'Jan','Feb','Mar','Apr','May',
                                        'Jun','Jul','Aug','Sep','Oct','Nov','Dec'],width=5,textvariable=Month)
month.current(0)
month.place(x=225,y=215,anchor="w")

year = ttk.Combobox(car, value=["Year",'2021','2022','2023','2024','2025',
                                       '2026','2027','2028','2029','2030'],width=5,textvariable=Year)
year.current(0)
year.place(x=281,y=215,anchor="w")

Button(car,text='อัตตราผ่อน', command=ph,font=("times 14 ")).place(x=240,y=250,anchor="w")

tk.Label(Carlist,text="เลือกรถรุ่น :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=5,y=30,anchor="w")
carlist=tk.Radiobutton(Carlist,font=("times 15 "),text='CarCruStandard',variable=Carcru,value=789000,indicatoron = 0)
carlist.bind("<Button-1>",showName)
carlist.place(x=105,y=30,anchor="w")
carlist=tk.Radiobutton(Carlist,font=("times 15 "),text='CarCruPro',variable=Carcru,value=990000,indicatoron = 0)
carlist.bind("<Button-1>",showName)
carlist.place(x=250,y=30,anchor="w")
carlist=tk.Radiobutton(Carlist,font=("times 15 "),text='CarCruPremium',variable=Carcru,value=1009000, indicatoron = 0)
carlist.bind("<Button-1>",showName)
carlist.place(x=353,y=30,anchor="w")
tk.Label(Carlist,text="ราคา :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=47,y=70,anchor="w")
carType=tk.Entry(Carlist,font=("times 16 "),width=13,textvariable=Carcru).place(x=105,y=70,anchor="w")
tk.Label(Carlist,text="บาท",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=70,anchor="w")
tk.Label(Carlist,text="เงินดาวน์ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=18,y=100,anchor="w")
downpayment=tk.Entry(Carlist,font=("times 16 "),width=13,textvariable=DownPayment).place(x=105,y=100,anchor="w")
tk.Label(Carlist,text="%",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=105,anchor="w")
tk.Label(Carlist,text="เงินดาวน์ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=18,y=130,anchor="w")
dowtotal=tk.Entry(Carlist,font=("times 16 "),width=13,textvariable=Dowtotal).place(x=105,y=130,anchor="w")
tk.Label(Carlist,text="บาท",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=130,anchor="w")
tk.Label(Carlist,text="จัดไฟแนนซ์ :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=1,y=160,anchor="w")
rmoney=tk.Entry(Carlist,font=("times 16 "),width=13,textvariable=star).place(x=105,y=160,anchor="w")
tk.Label(Carlist,text="บาท",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=160,anchor="w")
tk.Button(Carlist,text="คำนวนราคาจัดยอด",font=("times 10 "),command=down).place(x=310,y=100,anchor="w")
tk.Button(Carlist,text="ราคาผ่อนต่อเดือน",font=("times 10 "),command=instalpermonth).place(x=315,y=200,anchor="w")
tk.Label(Carlist,text="เลือกผ่อน :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=13,y=200,anchor="w")
installmentperiod=tk.Radiobutton(Carlist,font=("times 15 "),text='48',variable=Timeperiod,value=48,indicatoron = 0)
installmentperiod.place(x=120,y=200,anchor="w")
installmentperiod=tk.Radiobutton(Carlist,font=("times 15 "),text='60',variable=Timeperiod,value=60,indicatoron = 0)
installmentperiod.place(x=160,y=200,anchor="w")
installmentperiod=tk.Radiobutton(Carlist,font=("times 15 "),text='72',variable=Timeperiod,value=72,indicatoron = 0)
installmentperiod.place(x=200,y=200,anchor="w")
tk.Label(Carlist,text="เดือน",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=200,anchor="w")
rmoney1=tk.Entry(Carlist,font=("times 16 "),width=13,textvariable=Instalpermonth).place(x=105,y=238,anchor="w")
tk.Label(Carlist,text="ผ่อนเดือน :",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=10,y=238,anchor="w")
tk.Label(Carlist,text="บาท",font=("times 16 "),bg="#CCFFFF",fg ='#0022FF').place(x=260,y=238,anchor="w")
tk.Button(Carlist,text="โชใบสัญญา",font=("times 10 "),command=Data).place(x=320,y=240,anchor="w")
tk.Button(Carlist,text="เอาเข้าdata",font=("times 10 "),command=datashow).place(x=450,y=240,anchor="w")

txtBill=Text(TxT,height=34, width=70)
txtBill.pack(side=TOP, fill=X)

car.mainloop()