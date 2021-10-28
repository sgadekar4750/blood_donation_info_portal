from itertools import count
from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font
import mysql.connector as Mysqlconnector
import tkinter.messagebox as MessageBox

LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting of the different page layouts
        for F in (Home_Page, Page1, Page2, Login1,Admin):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home_Page)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
############################################  startpage ############################################
  
class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
    # create a background image 
        load = Image.open("login.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)   
   #Create Button
        myFont = font.Font(family='Helvetica',size=20)
        img1 =ImageTk.PhotoImage(Image.open("person.png"))
        Admin = Button(self, text='Admin',command=lambda : controller.show_frame(Login1),font=myFont,borderwidth=0,
                                              compound=TOP,image=img1,height=110)
        Admin.image = img1                                                                                           
        Admin.place(x=1200, y=40)
        
        img2 = ImageTk.PhotoImage(Image.open("Donor1.jpg"))
        Donor =Button( self, text = "Donor",command = lambda : controller.show_frame(Page1),font=myFont,width=200,
                                                                                compound=LEFT,image=img2,height=110)
        Donor.image = img2
        Donor.place(x=250, y=450)
        
        
        img3 = ImageTk.PhotoImage(Image.open("Receiever.png"))
        Receiver = Button( self, text = "Receiver",command = lambda : controller.show_frame(Page2),font=myFont,width=200,
                                                                                image=img3,compound=LEFT,height=110)
        Receiver.image = img3
        Receiver.place(x=921, y=450)

############################################ login Page ############################################

class Login1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("BloodAni.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        self.t_uname=Entry(self,width=15,font=("bold",20))
        self.t_uname.place(x=625,y=250)
        self.t_pwd=Entry(self,show ="*",width=15,font=("bold",20))
        self.t_pwd.place(x=625,y=300)
        self.title=Label(self,text="Admin Login",fg="#050505",font=("bold",25),background="#2f85c0")
        self.title.place(x=625,y=150)
        self.uname=Label(self,text="Username",fg="#050505",font=("bold",15),background="#2f85c0")
        self.uname.place(x=500,y=253)
        self.password=Label(self,text="Password",fg="#050505",font=("bold",15),background="#2f85c0")
        self.password.place(x=500,y=303)
        self.Back = tk.Button(self, text ="Home Page",command = lambda : controller.show_frame(Home_Page),width=10,
                                                                                             font=("bold",12))
        self.Back.place(x=720,y=350)

        def Validate(self):
                if self.t_uname.get()=="" or self.t_pwd.get()=="":
                        MessageBox.showerror("Error","Enter User Name and  Password")
                else:
                     try:
                        log = Mysqlconnector.connect(host="localhost",user = "root",password = "3334444s",database = "blood",charset="utf8")
                        db=log.cursor()
                        db.execute("select * FROM login WHERE User_Name = '%s' and password = '%s' "%(self.t_uname.get(),self.t_pwd.get()))
                        myresult = db.fetchone()
    
                        if myresult == None:
                                MessageBox.showerror('Error', "Login failed,Invalid Username or Password.Try again!!!")
                        else:
                                MessageBox.showinfo("Information","You login Successfully...!")
                                log.close()
                                controller.show_frame(Admin)
                                clear(self)
                     except Exception as es:
                        MessageBox.showerror("Error",f"Error Due to : {str(es)}")     
  
        def clear(self):
                self.t_uname.delete(0,END)
                self.t_pwd.delete(0,END)

        self.submit=Button(self,text="Login",command=lambda:[Validate(self)],width=7,font=("bold",12))
        self.submit.place(x=625,y=350)
        
        

############################################  Admin page ############################################

class Admin(tk.Frame):
        def __init__(self, parent,controller):
            ttk.Notebook.__init__(self, parent)
            tabControl = ttk.Notebook(self)
            tabControl.pack()
            tab1 = Frame(tabControl,width=1366,height=725)
            tab1.pack()
            tabControl.add(tab1,text='Blood Receiving')
            tab2 = Frame(tabControl,width=1366,height=725)
            tab2.pack()
            tabControl.add(tab2,text='Blood Donation')

            load = Image.open("A.jpg")
            render = ImageTk.PhotoImage(load)
            img = Label(tab1, image=render)
            img.image = render
            img.place(x=0, y=0)

            load = Image.open("A.jpg")
            render = ImageTk.PhotoImage(load)
            img = Label(tab2, image=render)
            img.image = render
            img.place(x=0, y=0) 

            def Log_Out():
                MessageBox.showinfo("Information","You Logout successfully ")
                controller.show_frame(Login1)    
            
            img4 =ImageTk.PhotoImage(Image.open("logout.jpg"))
            Log_Out.image = img4
            Log_Out=Button(tab1,command=Log_Out,compound=CENTER,image=img4,width=140,height=43)
            Log_Out.place(x=1210,y=15)
            
            Heading = Label(tab1,text="Blood Bank Details",font=("bold",30))
            Heading.place(x=525,y=5)

            myFont = font.Font(family='Helvetica',size=15)

####################################  FRAME  1    ########################################################################
            labelb1 = Label(tab1,text="Receiving",bg="#068cff",font=myFont)
            labelb1.place(x=650,y=320)
            frameb1 = Frame(tab1,relief=SUNKEN , height=37,borderwidth=2,background='#0693ff')
            frameb1.place(x=325,y=350)
            
            fram1=Frame(tab1,width=1250, relief=SUNKEN) 
            fram1.place(x=15,y=461)
            
            vsb = Scrollbar(fram1,orient=VERTICAL)
            vsb.pack(side=RIGHT,fill=Y)
            hsb = Scrollbar(fram1,orient=HORIZONTAL)
            hsb.pack(side=BOTTOM,fill=X)   
            
            cols =  ('Id','Name','Phone_No','Address','Pincode','District','State','Blood_Group','Blood_Bag')
            listBox = ttk.Treeview(fram1, columns=cols,show='headings',height='9',yscrollcommand=vsb.set,xscrollcommand=hsb.set,
                                                                        selectmode="extended")
            listBox.pack(fill='both')

            vsb.config(command=listBox.yview)
            hsb.config(command=listBox.xview)

            listBox.column('Id',width=80,minwidth=80,anchor=CENTER,stretch=NO)
            listBox.column('Name',width=238,minwidth=238,anchor=W,stretch=NO)
            listBox.column('Phone_No',width=140,minwidth=140,anchor=CENTER,stretch=NO)
            listBox.column('Address',width=328,minwidth=328,anchor=W,stretch=NO)
            listBox.column('Pincode',width=114,minwidth=114,anchor=CENTER,stretch=NO)
            listBox.column('District',width=149,minwidth=149,anchor=CENTER,stretch=NO)
            listBox.column('State',width=106,minwidth=106,anchor=CENTER,stretch=NO)
            listBox.column('Blood_Group',width=85,minwidth=85,anchor=CENTER,stretch=NO)
            listBox.column('Blood_Bag',width=70,minwidth=70,anchor=CENTER,stretch=NO)
           
            for col in cols:
               listBox.heading(col, text=col)

            Id1 = tk.IntVar()
            Name1 = tk.StringVar()
            Phone_No1 = tk.IntVar()
            Address1 = tk.StringVar()
            Pincode1 = tk.IntVar()
            District1 = tk.StringVar()
            State1 = tk.StringVar()
            Blood_Group1 = tk.StringVar()
            Blood_Bag1 = tk.IntVar()

            Idlabel1 = Label(tab1,text="Id",font=("bold",11))
            Idlabel1.place(x=85,y=110)
            Idlabel = Entry(tab1,width=10,textvariable=Id1)
            Idlabel.place(x=350,y=110)
            Idlabel.configure(state='disabled')
                
            Name = Entry(tab1,textvariable=Name1,width=35,font=("bold",12))
            Name.place(x=960,y=110)
            name1 = Label(tab1,text="Blood Bank Name",font=("bold",11))
            name1.place(x=715,y=110)

            Phone_No = Entry(tab1,textvariable=Phone_No1,width=20,font=("bold",12))
            Phone_No.place(x=350,y=154)
            phone_No1 = Label(tab1,text="Blood Bank Phone_No",font=("bold",11))
            phone_No1.place(x =85,y=154)

            Address = Entry(tab1,textvariable=Address1,width=35,font=("bold",12))
            Address.place(x=960,y=154)
            address1 = Label(tab1,text="Blood Bank Address ",font=("bold",11))
            address1.place(x=715,y=154)

            Pincode = Entry(tab1,textvariable=Pincode1,width=15,font=("bold",12))
            Pincode.place(x=350,y=198)
            pincode1 = Label(tab1,text="Blood Bank Pincode",font=("bold",11))
            pincode1.place(x=85,y=198)
            
            District = ttk.Combobox(tab1, width = 25, textvariable = District1,font=("bold",12))
            District['values'] = ('Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur',
                              'Dhule','Gadchiroli','Gondia','Hingoli','Jalgaon','Jalna','Kolhapur', 'Latur', 'Mumbai City',
                              'Mumbai Suburban','Nagpur','Nanded','Nandurbar','Nashik','Osmanabad','Parbhani','Pune',
                              'Raigad','Ratnagiri','Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim',
                              'Yavatmal','Palghar')
            District.place(x=960,y=198)
            district1 = Label(tab1,text="Blood Bank District",font=("bold",11))
            district1.place(x=715,y=198)
   
            State = Entry(tab1,width=15,font=("bold",12))
            State.place(x=350,y=242)
            state1 = Label(tab1,text="Blood Bank State",font=("bold",11))
            state1.place(x=85,y=242)
            State.insert(END,"Maharashtra",)

            Blood_Group = ttk.Combobox(tab1, width = 20, textvariable = Blood_Group1,font=("bold",12))
            Blood_Group['values']=('O-','O+','A-','A+','B-','B+','AB-','AB+')
            Blood_Group.place(x=960,y=242)
            Blood = Label(tab1,text="Blood Group available",font=("bold",11))
            Blood.place(x=715,y=242)

            Blood_Bag = Entry(tab1, width = 13, textvariable = Blood_Bag1 ,font=("bold",12))
            Blood_Bag.place(x=350,y=286)
            Blood_Bags = Label(tab1,text="No of Blood Bag ",font=("bold",11))
            Blood_Bags.place(x=85,y=286)

            def OnDoubleClick(event):
                global selected
                global values               
                selected = listBox.focus()
                values = listBox.item(selected,'values')
                
                Idlabel.configure(state='normal')
                Idlabel.delete(0,END)
                Idlabel.insert(0,values[0])
                Idlabel.configure(state='readonly')
                Name.insert(0,values[1])
                Phone_No.insert(0,values[2])
                Address.insert(0,values[3])
                Pincode.insert(0,values[4])
                District.insert(0,values[5])
                Blood_Group.insert(0,values[7])
                Blood_Bag.insert(0,values[8])
            
            listBox.bind('<Double 1>',OnDoubleClick)
            listBox.pack()

            log = Mysqlconnector.connect(host="localhost",user = "root",password = "3334444s",database = "blood")
            db=log.cursor()

            ######################  Receiver start ##############################

            def Eclear():
                Idlabel.configure(state='normal')
                Idlabel.delete(0,END)
                Idlabel.configure(state='disabled')
                Name.delete(0,END)
                Phone_No.delete(0,END)
                Address.delete(0,END)
                Pincode.delete(0,END)              
                District.delete(0,END)
                Blood_Group.delete(0,END)
                Blood_Bag.delete(0,END)

            def Insert_Data1():
                nonlocal Name,Phone_No,Address,Pincode,District,State,Blood_Group,Blood_Bag

                e1 = Name.get()
                e2 = Phone_No.get()
                e3 = Address.get()
                e4 = Pincode.get()
                e5 = District.get()
                e6 = State.get()
                e7 = Blood_Group.get()
                e8 = Blood_Bag.get()
                try:
                   query="INSERT INTO rdetails (Name,Phone_No,Address,Pincode,District,State,Blood_Group,Blood_Bag)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                   value = (e1,int(e2),e3,int(e4),e5,e6,e7,int(e8))
                   db.execute(query,value)
                   log.commit()
                   MessageBox.showinfo("Information","Data inserted successfully...!")
                   Show_all1()
                except Exception as es:
                   MessageBox.showerror("Error",f"Data not inserted successfully \n Error Due to : {str(es)}")
                   log.rollback()  

            img1 =ImageTk.PhotoImage(Image.open("Add.jpg"))
            Insert_Data1.image = img1
            Insert_Data = Button( frameb1, text = "  Add",command = Insert_Data1,font=myFont,width=120,
                                                                                compound=LEFT,image=img1,height=20)
            Insert_Data.pack(side=LEFT,padx=10)

            def Update_Data1():
                nonlocal Name,Phone_No,Address,Pincode,District,State,Blood_Group,Blood_Bag

                e1 = Name.get()
                e2 = Phone_No.get()
                e3 = Address.get()
                e4 = Pincode.get()
                e5 = District.get()
                e6 = State.get()
                e7 = Blood_Group.get()
                e8 = Blood_Bag.get()

                try:
                    if MessageBox.askyesno("Confirm Please","Are you want to update the Data ?"):
                        listBox.item(selected,values = (values[0],e1,e2,e3,e4,e5,e6,e7))
                        query="UPDATE rdetails  SET Name=%s,Phone_No=%s,Address=%s,Pincode=%s,District=%s,State=%s,Blood_Group=%s,Blood_Bag=%s WHERE Id = %s "
                        db.execute(query,(e1,int(e2),e3,int(e4),e5,e6,e7,int(e8),int(values[0])))
                        log.commit()
                        MessageBox.showinfo("Information","Data Updated Successfully ...!")
                        Show_all1()
                except Exception as es:
                    print(es)
                    MessageBox.showerror("Error",f"Data not Updated successfully \n Error Due to : {str(es)}")
            
            img2 =ImageTk.PhotoImage(Image.open("Update.jpg"))
            Update_Data1.image = img2
            Update_Data = Button(  frameb1, text = "  Update",command = Update_Data1,font=myFont,width=120,
                                                                                compound=LEFT,image=img2,height=20)
            Update_Data.pack(side=LEFT,padx=10)

            def Delete_Data1():                
                try:
                   selected = listBox.selection()
                   print(listBox.item(selected)['values'])
                   value = listBox.item(selected)['values'][0]
                   query="DELETE FROM rdetails WHERE Id = '%s'"
                   db.execute(query,(value,))
                   log.commit()
                   MessageBox.showinfo("Information","Data Deleted Successfully ...!")
                   Show_all1()
                except Exception as es:
                    print(es)
                    MessageBox.showerror("Error",f"Data not Deleted successfully \n Error Due to : {str(es)}")
            
            img3 =ImageTk.PhotoImage(Image.open("Delete.jpg"))
            Delete_Data1.image = img3
            Delete_Data = Button( frameb1, text = "  Delete",command = Delete_Data1,font=myFont,width=120,
                                                                                compound=LEFT,image=img3,height=20)
            Delete_Data.pack(side=LEFT,padx=10)

            def Show_all1():
                Eclear()
 
                listBox.delete(*listBox.get_children())

                db=log.cursor()
                query ="SELECT * FROM rdetails"
                db.execute(query)
                records = db.fetchall()
                log.commit()
                    
                global count
                count = 0
                
                if records == None:
                    print("No record avalaible.")
                    MessageBox.showinfo("Information","No record avalaible.")
                else:
                    for record in records:
                       listBox.insert(parent='',index='end',values=record)
                       count +=1
                       print("Total records are :",(count))
                       print(record)
        
            img4 =ImageTk.PhotoImage(Image.open("Show.jpg"))
            Show_all1.image = img4
            Show_all = Button( frameb1, text = "  Show All",font=myFont,width=120,command=Show_all1,
                                                                        compound=LEFT,image=img4,height=20)
            Show_all.pack(side=LEFT,padx=10)

            def Delete_all():
                db=log.cursor()
                db.execute("DELETE  from  rdetails")
                log.commit()
                MessageBox.showinfo("Information","All Data Delete Successfully.")
                Show_all1()

            img5 =ImageTk.PhotoImage(Image.open("deleteall.jpg"))
            Delete_all.image = img5
            Delete_all = Button( frameb1, text = "Delete All",font=myFont,width=120,command = Delete_all,
                                                                        compound=LEFT,image=img5,height=20)
            Delete_all.pack(side=LEFT,padx=10)

           ###############################  Receiver end  ################################
            S = StringVar()
        
            def search_Receiver():        
                s1 = S.get()
                query = "SELECT * FROM rdetails WHERE Name LIKE '%"+s1+"%'"
                db.execute(query)
                rows = db.fetchall()
                log.commit()
                ent1.delete(0,END)

                if rows == None:
                    MessageBox.showinfo("Information","Sorry no "+{str(s1)}+"Available")
                else:    
                    for record in rows:
                       listBox.delete(*listBox.get_children())
                       listBox.insert(parent='',index='end',values=record)
            
            ent1 = Entry(tab1,textvariable=S,width=35,font=("bold",12))
            ent1.place(x=425,y=413)
            btn = Button(tab1,text='Search Receiver',command = search_Receiver,height=1)
            btn.place(x=800,y=413)

###################################################  FRAME  2   ############################################################
            labelb2 = Label(tab2,text="Donation",bg="#068cff",font=myFont)
            labelb2.place(x=650,y=310)
            frameb2 = Frame(tab2,relief=SUNKEN , height=37,borderwidth=2,background='#0693ff')
            frameb2.place(x=325,y=340)
            
            fram3=Frame(tab2,width=1250, relief=SUNKEN) 
            fram3.place(x=93,y=461)

            Heading = Label(tab2,text="Blood Bank Details",font=("bold",30))
            Heading.place(x=525,y=5)
            
            vsb = Scrollbar(fram3,orient=VERTICAL)
            vsb.pack(side=RIGHT,fill=Y)
            hsb = Scrollbar(fram3,orient=HORIZONTAL)
            hsb.pack(side=BOTTOM,fill=X)   
            
            cols =  ('Id','Name','Phone_No','Address','Pincode','District','State')
            listBox2 = ttk.Treeview(fram3, columns=cols,show='headings',height='9',yscrollcommand=vsb.set,xscrollcommand=hsb.set,
                                                                        selectmode="extended")
            listBox2.pack(fill='both')

            vsb.config(command=listBox2.yview)
            hsb.config(command=listBox2.xview)

            listBox2.column('Id',width=80,minwidth=80,anchor=CENTER,stretch=NO)
            listBox2.column('Name',width=238,minwidth=238,anchor=W,stretch=NO)
            listBox2.column('Phone_No',width=140,minwidth=140,anchor=CENTER,stretch=NO)
            listBox2.column('Address',width=328,minwidth=328,anchor=W,stretch=NO)
            listBox2.column('Pincode',width=114,minwidth=114,anchor=CENTER,stretch=NO)
            listBox2.column('District',width=149,minwidth=149,anchor=CENTER,stretch=NO)
            listBox2.column('State',width=106,minwidth=106,anchor=CENTER,stretch=NO)
           
            for col in cols:
               listBox2.heading(col, text=col)

            Idlabel1 = Label(tab2,text="Id",font=("bold",11))
            Idlabel1.place(x=85,y=111)
            Idlabel = Entry(tab2,width=10,textvariable=Id1)
            Idlabel.place(x=350,y=111)
            Idlabel.configure(state='disabled')
                
            Name = Entry(tab2,textvariable=Name1,width=35,font=("bold",12))
            Name.place(x=960,y=111)
            name1 = Label(tab2,text="Blood Bank Name",font=("bold",11))
            name1.place(x=715,y=111)

            Phone_No = Entry(tab2,textvariable=Phone_No1,width=20,font=("bold",12))
            Phone_No.place(x=350,y=155)
            phone_No1 = Label(tab2,text="Blood Bank Phone_No",font=("bold",11))
            phone_No1.place(x =85,y=155)

            Address = Entry(tab2,textvariable=Address1,width=35,font=("bold",12))
            Address.place(x=960,y=155)
            address1 = Label(tab2,text="Blood Bank Address ",font=("bold",11))
            address1.place(x=715,y=155)

            Pincode = Entry(tab2,textvariable=Pincode1,width=15,font=("bold",12))
            Pincode.place(x=350,y=199)
            pincode1 = Label(tab2,text="Blood Bank Pincode",font=("bold",11))
            pincode1.place(x=85,y=199)
            
            District = ttk.Combobox(tab2, width = 25, textvariable = District1,font=("bold",12))
            District['values'] = ('Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur',
                              'Dhule','Gadchiroli','Gondia','Hingoli','Jalgaon','Jalna','Kolhapur', 'Latur', 'Mumbai City',
                              'Mumbai Suburban','Nagpur','Nanded','Nandurbar','Nashik','Osmanabad','Parbhani','Pune',
                              'Raigad','Ratnagiri','Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim',
                              'Yavatmal','Palghar')
            District.place(x=960,y=199)
            district1 = Label(tab2,text="Blood Bank District",font=("bold",11))
            district1.place(x=715,y=199)
   
            State = Entry(tab2,width=15,font=("bold",12))
            State.place(x=350,y=243)
            state1 = Label(tab2,text="Blood Bank State",font=("bold",11))
            state1.place(x=85,y=243)
            State.insert(END,"Maharashtra",)


            def OnDoubleClick1(event):
                global selected
                global values               
                selected = listBox.focus()
                values = listBox.item(selected,'values')
                
                Idlabel.configure(state='normal')
                Idlabel.delete(0,END)
                Idlabel.insert(0,values[0])
                Idlabel.configure(state='readonly')
                Name.insert(0,values[1])
                Phone_No.insert(0,values[2])
                Address.insert(0,values[3])
                Pincode.insert(0,values[4])
                District.insert(0,values[5])

            listBox2.bind('<Double 1>',OnDoubleClick1)
            listBox2.pack()

            myFont = font.Font(family='Helvetica',size=15)

            log = Mysqlconnector.connect(host="localhost",user = "root",password = "3334444s",database = "blood")
            db=log.cursor()
 
         ########################   Donor Start  ########################

            def Eclear2():
                Idlabel.configure(state='normal')
                Idlabel.delete(0,END)
                Name.delete(0,END)
                Phone_No.delete(0,END)
                Address.delete(0,END)
                Pincode.delete(0,END)              
                District.delete(0,END)
                Blood_Group.delete(0,END)
            
            def Insert2(): 
                nonlocal Name,Phone_No,Address,Pincode,District,State

                e1 = Name.get()
                e2 = Phone_No.get()
                e3 = Address.get()
                e4 = Pincode.get()
                e5 = District.get()
                e6 = State.get()
                
                try:
                   query="INSERT INTO ddetails (Name,Phone_No,Address,Pincode,District,State)values(%s,%s,%s,%s,%s,%s)"
                   value = (e1,int(e2),e3,int(e4),e5,e6)
                   db.execute(query,value)
                   log.commit()
                   MessageBox.showinfo("Information","Data inserted successfully...!")
                   Show2()
                except Exception as es:
                   MessageBox.showerror("Error",f"Data not inserted successfully \n Error Due to : {str(es)}")
                   log.rollback() 

            img6 =ImageTk.PhotoImage(Image.open("Add.jpg"))
            Insert2.image = img6
            Insert = Button(frameb2, text = "  Add",command = Insert2,font=myFont,width=120,
                                                                                compound=LEFT,image=img6,height=20)
            Insert.pack(side=LEFT,padx=10)

            def Update2():
                nonlocal Name,Phone_No,Address,Pincode,District,State

                e1 = Name.get()
                e2 = Phone_No.get()
                e3 = Address.get()
                e4 = Pincode.get()
                e5 = District.get()
                e6 = State.get()
                
                try:
                 listBox.item(selected,values = (int(values[0]),e1,e2,e3,e4,e5,e6))
                 if MessageBox.askyesno("Confirm Please","Are you want to update the Data ?"):
                    query="UPDATE ddetails  SET Name=%s, Phone_No=%s ,Address=%s,Pincode=%s,District=%s,State=%s WHERE Id = %s "
                    db.execute(query,(e1,int(e2),e3,int(e4),e5,e6,int(values[0])))
                    log.commit()
                    MessageBox.showinfo("Information","Data Updated Successfully ...!")
                    Show2()
                except Exception as es:
                   print(es)
                   MessageBox.showerror("Error",f"Data not Updated successfully \n Error Due to : {str(es)}")
                    

            img7 =ImageTk.PhotoImage(Image.open("Update.jpg"))
            Update2.image = img7
            Update = Button( frameb2, text = "  Update",command = Update2,font=myFont,width=120,
                                                                                compound=LEFT,image=img7,height=20)
            Update.pack(side=LEFT,padx=10)

            def Delete2():
                try:
                   selected = listBox.selection()[0]
                   print(listBox.item(selected)['values'])
                   value = listBox.item(selected)['values'][0]
                   if MessageBox.askyesno("Confirm Please","Are you want to update the Data ?"):
                      query="DELETE FROM ddetails WHERE Id = '%s'"
                      db.execute(query,(value,))
                      log.commit()
                      MessageBox.showinfo("Information","Data Deleted Successfully ...!")
                      Show2()
                except Exception as es:
                    print(es)
                    MessageBox.showerror("Error",f"Data not Deleted successfully \n Error Due to : {str(es)}")
            
            img8 =ImageTk.PhotoImage(Image.open("Delete.jpg"))
            Delete2.image = img8
            Delete = Button(frameb2, text = "  Delete",command = Delete2,font=myFont,width=120,
                                                                                compound=LEFT,image=img8,height=20)
            Delete.pack(side=LEFT,padx=10)

            def Show2():
                Eclear2()

                listBox2.delete(*listBox2.get_children())
                
                db=log.cursor()
                db.execute("SELECT * from ddetails")
                records = db.fetchall()
                log.commit()
                    
                global count
                count = 0
            
                for record in records:
                    listBox2.insert(parent='',index='end',values=record)
                    count +=1
                    print("Total records are :",(count))
                    print(record)

        
            img9 =ImageTk.PhotoImage(Image.open("Show.jpg"))
            Show2.image = img9
            Show = Button(frameb2, text = "  Show All",font=myFont,width=120,command=Show2,
                                                                        compound=LEFT,image=img9,height=20)
            Show.pack(side=LEFT,padx=10)

            def DeleteAll2():
                if MessageBox.askyesno("Confirm Please","Are you want to update the Data ?"):
                  db=log.cursor()
                  db.execute("DELETE  from ddetails")
                  log.commit()
                  MessageBox.showinfo("Information","All Data Delete Successfully.")
                  Show2()               

            img10 =ImageTk.PhotoImage(Image.open("deleteall.jpg"))
            DeleteAll2.image = img10
            DeleteAll = Button(frameb2, text = "  Delete All",font=myFont,width=120,command=DeleteAll2,
                                                                        compound=LEFT,image=img10,height=20)
            DeleteAll.pack(side=LEFT,padx=10)

            ############################   Donor end  ##############################

            D =  StringVar() 

            def search_D():
                s1 = D.get()
                query = "SELECT * FROM ddetails WHERE Name LIKE '%"+s1+"%'"
                db.execute(query)
                rows = db.fetchall()
                log.commit()
                ent2.delete(0,END)

                if rows == 0:
                    MessageBox.showinfo("Information","Sorry no "+{str(s1)}+"Available")
                else:
                   for row in rows:
                      listBox.delete(*listBox.get_children())
                      listBox.insert(parent='',index='end',values=row)


            ent2 = Entry(tab2,textvariable=D,width=35,font=("bold",12))
            ent2.place(x=425,y=407)
            btn = Button(tab2,text='Search Donor',command=search_D,height=1)
            btn.place(x=800,y=407)
               

############################################  page 1  ############################################

class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("blood.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0) 

#Create Frams  
        fram1=ttk.Frame(self,width=1356, relief=SUNKEN) 
        fram1.place(x=6,y=362) 

        vsb = Scrollbar(fram1,orient=VERTICAL)
        vsb.pack(side=RIGHT,fill=Y)
        hsb = Scrollbar(fram1,orient=HORIZONTAL)
        hsb.pack(side=BOTTOM,fill=X)   
            
        cols =  ('Id','Name','Phone_No','Address','Pincode','District','State')
        listBox = ttk.Treeview(fram1, columns=cols,show='headings',height='13',yscrollcommand=vsb.set,xscrollcommand=hsb.set,
                                                                        selectmode="extended")
        listBox.pack(fill='both')

        vsb.config(command=listBox.yview)
        hsb.config(command=listBox.xview)

        listBox.column('Id',width=80,stretch=NO)
        listBox.column('Name',width=270,anchor=W,stretch=NO)
        listBox.column('Phone_No',width=160,anchor=W,stretch=NO)
        listBox.column('Address',width=340,anchor=W,stretch=NO)
        listBox.column('Pincode',width=130,anchor=W,stretch=NO)
        listBox.column('District',width=186,anchor=W,stretch=NO)
        listBox.column('State',width=170,anchor=W,stretch=NO)

        District3 = tk.StringVar()
        State3 = tk.StringVar()

#create dropbox 
        ttk.Label(self, text = "select  the  State :", font = ("Times New Roman", 15),width=17).place(x=50,y=138)
        State = ttk.Combobox(self, width = 20, textvariable = State3,font = ("Times New Roman", 15))
        State['values'] = ('Maharashtra')
        State.place(x=300,y=137)
        State.current(0)
        
#create dropbox
        ttk.Label(self, text = "select the District :", font = ("Times New Roman", 15),width=17).place(x=824,y=138)
        District= ttk.Combobox(self, width = 20, textvariable = District3,font = ("Times New Roman", 15))
        District['values'] = ('Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur',
                              'Dhule','Gadchiroli','Gondia','Hingoli','Jalgaon','Jalna','Kolhapur', 'Latur', 'Mumbai City',
                              'Mumbai Suburban','Nagpur','Nanded','Nandurbar','Nashik','Osmanabad','Parbhani','Pune',
                              'Raigad','Ratnagiri','Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim',
                              'Yavatmal','Palghar')
        District.place(x=1100,y=137)
        District.current(0)

        label = Label(self,text='Donor',font=("bold",30),width=5)
        label.place(x=635,y=7)

        label2 = Label(self,text='List of the place where you Donate your blood',font=("bold",25))
        label2.place(x=365,y=310)

        button1 = tk.Button(self, text ="Home Page",command = lambda : controller.show_frame(Home_Page),
                                                              height=1,width=8,font=("Times New Roman", 15))
        button1.place(x=1258,y=8)
           
        for col in cols:
            listBox.heading(col, text=col)
        
        def cleard():
            District.delete(0,END)
            State.delete(0,END)
        
        log = Mysqlconnector.connect(host="localhost",user = "root",password = "3334444s",database = "blood",charset="utf8") 

        def Submit():
            nonlocal District,State

            e11 = District.get()
            e12 = State.get()
                       
            db = log.cursor()
            query=(" SELECT * FROM ddetails WHERE District = %s  " )
            value = (e11,)
            db.execute(query,value)
            records = db.fetchall()
            cleard()
            log.commit()
            listBox.delete(*listBox.get_children())           
                    
            global count
            count = 0

            try:
               for record in records:
                   listBox.insert(parent='',index='end',values=record)
                   count +=1
                   print("Total records are :",(count))
                   print(record)
            except Exception as es:
                print(es)
                MessageBox.showerror("Error",f"Data not Display successfully \n Error Due to : {str(es)}")

        submit=Button(self,text="Submit",width=7,font=("bold",12),command= Submit)
        submit.place(x=650,y=200)

############################################  page  2  ############################################        

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("blood.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0) 

#Create Frams  
        fram1=ttk.Frame(self,width=1356,height=392, relief=SUNKEN) 
        fram1.place(x=6,y=374)

        vsb = Scrollbar(fram1,orient=VERTICAL)
        vsb.pack(side=RIGHT,fill=Y)
        hsb = Scrollbar(fram1,orient=HORIZONTAL)
        hsb.pack(side=BOTTOM,fill=X)   
            
        cols =  ('Id','Name','Phone_No','Address','Pincode','District','State','Blood Group','Blood Bag')
        listBox = ttk.Treeview(fram1, columns=cols,show='headings',height='13',yscrollcommand=vsb.set,xscrollcommand=hsb.set,
                                                                        selectmode="extended")
        listBox.pack(fill='both')

        vsb.config(command=listBox.yview)
        hsb.config(command=listBox.xview)

        listBox.column('Id',width=80,stretch=NO,anchor=CENTER)
        listBox.column('Name',width=225,anchor=W,stretch=NO)
        listBox.column('Phone_No',width=140,anchor=W,stretch=NO)
        listBox.column('Address',width=285,anchor=W,stretch=NO)
        listBox.column('Pincode',width=120,anchor=W,stretch=NO)
        listBox.column('District',width=156,anchor=W,stretch=NO)
        listBox.column('State',width=150,anchor=W,stretch=NO)
        listBox.column('Blood Group',width=80,anchor=CENTER,stretch=NO)
        listBox.column('Blood Bag',width=100,anchor=CENTER,stretch=NO)

        District1 =tk.StringVar()
        State1 =tk.StringVar()
        Blood_Group1 =tk. StringVar()

        #create dropbox 
        
        ttk.Label(self, text = "select the State :",font = ("Times New Roman", 15),width=17).place(x=50,y=132)
        State = ttk.Combobox(self, width = 20, textvariable = State1,font = ("Times New Roman", 15))
        State['values'] = ('Maharashtra')
        State.place(x=310,y=131)
        State.current(0)
        
#create dropbox
        ttk.Label(self, text = "select the District :", font = ("Times New Roman", 15),width=17).place(x=824,y=132)
        District = ttk.Combobox(self, width = 20, textvariable = District1,font = ("Times New Roman", 15))
        District['values'] = ('Ahmednagar','Akola','Amravati','Aurangabad','Beed','Bhandara','Buldhana','Chandrapur',
                              'Dhule','Gadchiroli','Gondia','Hingoli','Jalgaon','Jalna','Kolhapur', 'Latur', 'Mumbai City',
                              'Mumbai Suburban','Nagpur','Nanded','Nandurbar','Nashik','Osmanabad','Parbhani','Pune',
                              'Raigad','Ratnagiri','Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim',
                              'Yavatmal','Palghar')
        District.place(x=1100,y=131)
        District.current(0)

#create dropbox
        ttk.Label(self, text = "select the Blood Group :", font = ("Times New Roman", 15),width=19).place(x=450,y=190)       
        Blood_Group = ttk.Combobox(self, width = 20, textvariable = Blood_Group1,font = ("Times New Roman", 15))
        Blood_Group['values']=('O-','O+','A-','A+','B-','B+','AB-','AB+')
        Blood_Group.place(x=720,y=190)
        Blood_Group.current(0)

        label = Label(self,text='Receiver',font=("bold",30),width=7)
        label.place(x=600,y=7)

        label2 = Label(self,text='List of the place where you Receive the blood',font=("bold",25))
        label2.place(x=385,y=322)
       
        button1 = tk.Button(self, text ="Home Page",command = lambda : controller.show_frame(Home_Page),
                                                              height=1,width=8,font=("Times New Roman", 15))
        button1.place(x=1258,y=8)
           
        for col in cols:
            listBox.heading(col, text=col) 

        log = Mysqlconnector.connect(host="localhost",user = "root",password = "3334444s",database = "blood",auth_plugin='mysql_native_password') 

        def clearr():
            District.delete(0,END)
            State.delete(0,END)
            Blood_Group.delete(0,END)
        
        def Submit():
            nonlocal District,State,Blood_Group

            e5 = District.get()
            e6 = State.get()
            e7 = Blood_Group.get()           

            db = log.cursor()
            query=(" SELECT * FROM rdetails WHERE District = %s AND Blood_Group = %s " )
            value = (e5,e7)
            db.execute(query,value)
            records = db.fetchall()
            clearr()
            log.commit()
            listBox.delete(*listBox.get_children())
                   
            global count
            count = 0

            try:
               for record in records:
                   listBox.insert(parent='',index='end',values=record)
                   count +=1
                   print("Total records are :",(count))
                   print(record)
            except Exception as es:
                print(es)
                MessageBox.showerror("Error",f"Data not Display successfully \n Error Due to : {str(es)}")

        submit=Button(self,text="Submit",width=7,font=("bold",12),command= Submit)
        submit.place(x=645,y=255)
   
# Driver Code

app = tkinterApp()
app.state("zoomed")
app.title("Blood Bank Information System")
app.mainloop()