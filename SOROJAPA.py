from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import time

B_COLOR = "white"
FONTT = "Helvetica 10 bold"
T_FONTT = "Arial 10 bold"
F_COLOR = "green"
T_F_COLOR = "purple"
E_DB = "PAUL.db"
N_DB = "Names_10.db"
l_B_COLOR = "grey"
l_FONTT = "Helvetica 10 bold"
l_T_FONTT = "Arial 10 bold"
l_F_COLOR = "green"
l_T_F_COLOR = "purple"

r_B_COLOR = "lightblue"
r_FONTT = "Helvetica 10 bold"
r_T_FONTT = "Arial 15 bold"
r_F_COLOR = "green"
r_T_F_COLOR = "purple"

c_B_COLOR = "black"
c_FONTT = "Helvetica 10 bold"
c_T_FONTT = "Arial 10 bold"
c_F_COLOR = "green"
c_T_F_COLOR = "purple"

class ENTRY:
    def __init__(self , wn , *args , **kwargs):
        self.E_DB =E_DB
     
        self.N_DB = N_DB 
        self.names = [ ]
        try:
            conn = sqlite3.connect(self.E_DB)
            c = conn.cursor()
            c.execute("""CREATE TABLE entries (date text, reg text , make text , model text , booker text, charges int , paid int ,  balance int , remark text)""")
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:

            pass
        try:
            conn = sqlite3.connect(self.N_DB)
            c = conn.cursor()
            c.execute("SELECT * FROM name")
            data = c.fetchall()
            if data == []:
                self.names = ["NAMES"]
            for i in data:
                self.names.append(i[0])                
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
                self.names =["NAMES"]
                pass
            
            
        self.l_B_COLOR ,l_B_COLOR = "grey","grey"
        self.l_FONTT,l_FONTT = "Helvetica 10 bold","Helvetica 10 bold"
        self.l_T_FONTT,l_T_FONTT = "Arial 10 bold","Arial 10 bold"
        self.l_F_COLOR, l_F_COLOR= "purple","green"
        self.l_T_F_COLOR, l_T_F_COLOR= "purple","purple"

        self.r_B_COLOR,r_B_COLOR = "lightblue","lightblue"
        self.r_FONTT,r_FONTT = "Helvetica 10 bold","Helvetica 10 bold"
        self.r_T_FONTT, r_T_FONTT= "Arial 15 bold","Arial 15 bold"
        self.r_F_COLOR,r_F_COLOR = "green","green"
        self.r_T_F_COLOR, r_T_F_COLOR = "purple","purple"

        self.c_B_COLOR,c_B_COLOR = "black","black"
        self.c_FONTT ,c_FONTT ="Helvetica 10 bold","Helvetica 10 bold"
        self.c_T_FONTT, c_T_FONTT= "Arial 10 bold","Arial 10 bold"
        self.c_F_COLOR, c_F_COLOR= "green","green"
        self.c_T_F_COLOR, c_T_F_COLOR= "purple","purple"

        
        self.wn = wn

        self.left = Frame(wn , width = 900,height =600, bg =l_B_COLOR  )
        self.left.pack(side =RIGHT)

        self.c= Frame(wn , width = 100,height = 600, bg =r_B_COLOR)
        self.c.pack(side = LEFT)

        self.right = Frame(wn , width = 400,height = 600, bg =  c_B_COLOR)
        self.right.pack( )

        #LABELS
        
        TT = time.localtime()
        watch = str(TT[0]) + "/"+str(TT[1])+"/"+ str(TT[2])

        l1 = Label(self.right , text = "ENTRIES:" , fg = r_T_F_COLOR , bg = c_B_COLOR , font = r_T_FONTT)
        l1.place(x = 0 , y = 0)
        
        l1 = Label(self.right , text = "REG NO :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 20 , y = 100)
        l2 = Label(self.right , text = "MAKE :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l2.place(x = 20 , y = 150)
        l3 = Label(self.right , text = "MODEL :" ,  fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l3.place(x = 20 , y = 200)
        l4 = Label(self.right, text = "CHARGES :" ,   fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l4.place(x = 20 , y = 250)
        l5 = Label(self.right , text = "AMOUNT PAID :" ,  fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l5.place(x = 20 , y = 300)
        l6 = Label(self.right , text = " REMARKS :" ,   fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l6.place(x = 20 , y = 350)
        l7 = Label(self.right , text = "BOOKED BY :" ,  fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l7.place(x = 20 , y = 400)
        l8 = Label(self.right , text = "BALANCE :",   fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l8.place(x = 20 , y = 500)
        self.l9 = Label(self.right , text = " ",   fg = c_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        self.l9.place(x = 150 , y = 530)

        self.e1 = Entry(self.right , width = 20, font = FONTT)
        self.e1.place(x =160 , y = 100)
        self.e2 = Entry(self.right , width = 20, font = FONTT)
        self.e2.place(x = 160 , y = 150)
        self.e3 = Entry(self.right , width = 20, font = FONTT)
        self.e3.place(x = 160 , y = 200)
        self.e4 = Entry(self.right , width = 20, font = FONTT)
        self.e4.place(x = 160 , y = 250)
        self.e5 =Entry(self.right , width = 20, font = FONTT)
        self.e5.place(x = 160 , y = 300)
        self.e6 = Entry(self.right , width = 20, font = FONTT)
        self.e6.place(x = 160 , y = 350)
#_____________________________BUTTONS
        submit = Button(self.right , text = "Submit",  font = FONTT , command = self.Submit)
        submit.place(x = 210 , y = 450)


        entry_b = Button(self.c , text = "ENTRY", width = 10  ,  font = FONTT)
        entry_b.place(x = 0 , y = 150)
        
        stats_b = Button(self.c , text = "STATS", width = 10  ,  font = FONTT, command= self.Stats)
        stats_b.place(x = 0 , y = 200)
        
        add_b = Button(self.c , text = "ADD NEW", width = 10  ,  font = FONTT, command= self.Add)
        add_b.place(x = 0 , y = 250)

        close_b = Button(self.c , text = "CLOSE" , width = 10 ,  font = FONTT, command = self.Close)
        close_b.place(x = 0 , y = 400)

        self.clicked = StringVar()
        self.clicked.set("NAMES")

        self.menu = OptionMenu(self.right , self.clicked , *self.names)
        self.menu.place(x = 180 , y =  400)
        
        
        
        
#____________________________________LEFT BLOCK
        title  =  Label(self.left , text = "TODAYS ENTRIES: "+watch , fg = r_T_F_COLOR , bg = l_B_COLOR , font = r_T_FONTT)
        title.place(x = 10 , y = 0)

        title  =  Label(self.left , text = "---SOROJAPA_AUTO_WORKS--- \n---DAILY JOB CARD--- \n---"+"---",bg = l_B_COLOR,fg = r_T_F_COLOR,font = "Helvetica 19 bold")
        title.place(x = 190 , y = 360)

        title  =  Label(self.left , text = "From Skye Softwares\nProject no_2:\nCompleted on 2020/20/9 6:19 PM", fg =  c_B_COLOR, bg = l_B_COLOR)# , font = r_T_FONTT)
        title.place(x = 300 , y = 535)

        
        self.tree = ttk.Treeview(self.left, height = 10)
        self.tree['columns'] = ("ID" , "REG no","BOOKER" , "CHARGES","PAID" , "BALANCE")

        self.tree.column("#0", width = 50, minwidth = 25)
        self.tree.column("ID", anchor = W, width = 150)
        self.tree.column("REG no", anchor = W,  width = 100)
        self.tree.column("BOOKER", anchor = CENTER, width = 125)
        self.tree.column("CHARGES", anchor = CENTER, width = 125)
        self.tree.column("PAID", anchor = CENTER, width = 125)        
        self.tree.column("BALANCE", anchor =CENTER, width = 125)
        
                
        self.tree.heading("#0" , text = "ID" , anchor = W)
        self.tree.heading("ID" , text = "DATE" , anchor = W)
        self.tree.heading("REG no" , text = "REG no", anchor = W)
        self.tree.heading("BOOKER" , text = "BOOKER" , anchor = CENTER)
        self.tree.heading("CHARGES" , text = "CHARGES" , anchor = CENTER)
        self.tree.heading("PAID" , text = "PAID" , anchor = CENTER)        
        self.tree.heading("BALANCE" , text = "BALANCE" , anchor =CENTER)
        self.tree.place(x = 20 , y = 80)


#_______________________FUNCTIONS
    def sum(self ):
           try:
                r =   float(self.e5.get())- float(self.e4.get())
                return 0 , r
           except ValueError:
                messagebox.showwarning(title = "ERROR" , message = "Enter The Correct Values Amount Paid/Charges \nUse numbers/Avoid spaces btn the digits")
                return 1 , "NULL"

    def empty_checker(self , x):
        new_input = ""
        con = 0
        t = 0
        if x == "":
            messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
            con = 1
        else:
                for i in x:
                    if t == 0:
                        if i == " ":
                              continue
                        else:
                            new_input +=i
                    else:
                        new_input +=i
                if new_input == "":
                    messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
                    con = 1
                else:
                    return con , new_input

    def Submit(self):
        TT = time.localtime()
        Watch = str(TT[0]) + "/"+str(TT[1])+"/"+ str(TT[2])
        try:
            if str(self.clicked.get()) != "NAMES":
                entries = [self.e1.get(), self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get(),self.e6.get()]
                new = [ ]
                m = self.e5.get()
                foo = 1
                for entry in entries:
                    x , y = self.empty_checker(entry)
                    if x == 1:
                        break
                    else:
                        if foo == 1:
                            new.append(y)
                        else:
                            new.append(entry)
                    foo +=1
                
                if x == 0:
                    ch = messagebox.askyesno(title = "CONTINUE?..." , message = " REG no:  " +str(entries[0])+
                                                                                                                      "\nMAKE:   " +str(entries[1])+
                                                                                                                      "\nMODEL:  " +str(entries[2]) +
                                                                                                                       "\nCHARGES:  " +str(entries[3])+"Ksh"+
                                                                                                                        "\nCASH PAID:  " +str(entries[4]) +"Ksh"+
                                                                                                                         "\nBOOKED BY:  "+str(self.clicked.get()))

                    c ,bal = self.sum()
                    if ch == 1 and c == 0:
                        self.e1.delete(0 , END)
                        self.e2.delete(0 , END)
                        self.e3.delete(0 , END)
                        self.e4.delete(0 , END)
                        self.e5.delete(0 , END)
                        self.e6.delete(0 , END)
                    

                    
                        new.insert(0 , Watch)
                    
                        new.append(bal)
                        new.append(self.clicked.get())
                        self.l9.destroy()
                        self.l9 = Label(self.right , text = str(new[7]) +str("$"),fg = self.l_F_COLOR , bg = self.c_B_COLOR , font = self.r_T_FONTT)
                        self.l9.place(x = 150 , y = 530)
                    
                        entries = tuple(new)
                        conn = sqlite3.connect(self.E_DB)
                        c = conn.cursor()
                        c.execute("insert into entries (date , reg  , make , model  , charges  , paid, remark, balance,booker  ) values( ?,?,?,?,?,?,?,?,?)" , entries)
                        conn.commit()
                        conn.close()
                    

            else:
                messagebox.showwarning(title = "ERROR" , message = "Add/Pick name")
            conn = sqlite3.connect(self.E_DB)
            c = conn.cursor()
            c.execute("SELECT * FROM entries WHERE date = ?" ,( Watch,))
            data = c.fetchall()
            count =1
            try:
                for record in self.tree.get_children():
                     self.tree.delete(record)
            except Exception:
                pass
            
            for i in range (len(data)):
                 stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                 self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                 count +=1
            conn.commit()
            conn.close()
            
        except TypeError:
            pass
    def Stats(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        STATS(root)
        
    def Add(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        ADD(root)
        
    def Close(self):
        choice = messagebox.askyesno(title = "Exit" , message = "Exit ?")
        if choice == 1:
            self.wn.destroy()
        else:
            pass
E_DB = "PAUL.db"
N_DB = "Names_10.db"

class STATS:
    def __init__(self,  wn , *args , **kwargs):
        self.E_DB =E_DB 

        self.N_DB = N_DB 
        self.names = []
        try:
            conn = sqlite3.connect(self.N_DB)
            c = conn.cursor()
            c.execute("SELECT * FROM name")
            data = c.fetchall()
            if data == []:
                self.names = ["NAMES"]
            for i in data:
                self.names.append(i[0])                
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
                self.names =["NAMES"]
                pass
        
        self.E_DB = "ENTRY_0.db"
        self.N_DB = "Names_0.db"

        l_B_COLOR = "grey"
        l_FONTT = "Helvetica 10 bold"
        l_T_FONTT = "Arial 10 bold"
        l_F_COLOR = "green"
        l_T_F_COLOR = "purple"

        r_B_COLOR = "lightblue"
        r_FONTT = "Helvetica 10 bold"
        r_T_FONTT = "Arial 15 bold"
        r_F_COLOR = "green"
        r_T_F_COLOR = "purple"

        c_B_COLOR = "black"
        c_FONTT = "Helvetica 10 bold"
        c_T_FONTT = "Arial 10 bold"
        c_F_COLOR = "green"
        c_T_F_COLOR = "purple"

        self.wn = wn
        self.right = Frame(wn , width = 300,height =600, bg =l_B_COLOR  )
        self.right.pack(side =RIGHT)

        self.c= Frame(wn , width = 100,height = 600, bg =r_B_COLOR)
        self.c.pack(side = LEFT)

        self.left  = Frame(wn , width = 900,height = 600, bg =  c_B_COLOR)
        self.left.pack( )

        #LABELS
        l1 = Label(self.left , text = "STATS:" , fg = r_T_F_COLOR, bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 0 , y = 0)
        
        l1 = Label(self.left , text = "INQUIRE BY:" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 0 , y = 30)

        l1 = Label(self.left , text = "REG NO :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 20 , y = 70)
        l2 = Label(self.left  , text = "DATE :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l2.place(x = 20 , y = 100)
        l3 = Label(self.left  , text = "BOOKER :" ,  fg = r_F_COLOR  , bg = c_B_COLOR , font = r_FONTT)
        l3.place(x = 20 , y = 130)
        

        self.tree = ttk.Treeview(self.left)
 
        self.tree['columns'] = ("ID" , "REG no","BOOKER" , "CHARGES","PAID" , "BALANCE")

        self.tree.column("#0", width = 50, minwidth = 25)
        self.tree.column("ID", anchor = W, width = 150)
        self.tree.column("REG no", anchor = W,  width = 100)
        self.tree.column("BOOKER", anchor = CENTER, width = 125)
        self.tree.column("CHARGES", anchor = CENTER, width = 125)
        self.tree.column("PAID", anchor = CENTER, width = 125)        
        self.tree.column("BALANCE", anchor = CENTER, width = 125)
        
                
        self.tree.heading("#0" , text = "ID" , anchor = W)
        self.tree.heading("ID" , text = "DATE" , anchor = W)
        self.tree.heading("REG no" , text = "REG no", anchor = W)
        self.tree.heading("BOOKER" , text = "BOOKER" , anchor = CENTER)
        self.tree.heading("CHARGES" , text = "CHARGES" , anchor = CENTER)
        self.tree.heading("PAID" , text = "PAID" , anchor = CENTER)        
        self.tree.heading("BALANCE" , text = "BALANCE" , anchor = CENTER)
        self.tree.place(x = 20 , y = 190)


        self.e1 = Entry(self.left, width = 20, font = FONTT)
        self.e1.place(x =200 , y = 70)
        self.e3 = Entry(self.left , width = 20, font = FONTT)
        self.e3.place(x = 200 , y = 100)
#______________________________________BUTTONS
        entry_b = Button(self.c , text = "ENTRY", width = 10  ,  font = FONTT,command = self.Entry)
        entry_b.place(x = 0 , y = 150)
        
        stats_b = Button(self.c , text = "STATS", width = 10  ,  font = FONTT)
        stats_b.place(x = 0 , y = 200)
        
        add_b = Button(self.c , text = "ADD NEW", width = 10  ,  font = FONTT , command= self.Add)
        add_b.place(x = 0 , y = 250)

        close_b = Button(self.c , text = "CLOSE", width = 10  ,  font = FONTT, command = self.Close)
        close_b.place(x = 0 , y = 400)

        Go1 = Button(self.left , text = "Search" ,  width = 10 ,font = FONTT,command = self.search2)
        Go1.place(x = 400 , y = 70)
        
        Go2 = Button(self.left , text = "Search" ,  width = 10 ,font = FONTT    ,command = self.search1)
        Go2.place(x = 400 , y = 105)
        
        Go3 = Button(self.left , text = "Search" ,  width = 10 ,font = FONTT,command = self.search3)
        Go3.place(x = 400 , y = 140)

        Bal_p =  Button(self.left , text = "BALANCE +VE" ,  width = 20 ,font = FONTT , command = self.pos_bal)
        Bal_p.place(x = 600 , y = 20)
        
        Bal_n =  Button(self.left , text = "BALANCE -VE" ,  width = 20 ,font = FONTT, command = self.neg_bal)
        Bal_n.place(x = 600 , y = 80)

        look = Button(self.left , text = "Lookup" , width = 10,font = FONTT, command = self.look_up)
        look.place(x = 20, y = 430)

        close = Button(self.left , text = "Close" ,font = FONTT, command = self.close1)
        close.place(x = 690, y =  430)

        show_all = Button(self.left , text = "Show all" , width = 10,font = FONTT, command= self.drop)
        show_all.place(x = 200 , y = 20)

        
        self.clicked = StringVar()
        self.clicked.set("NAMES")     

        self.menu = OptionMenu(self.left , self.clicked , *self.names)
        self.menu.place(x = 200 , y =  130)
#__________________________________FUNCTIONS
    def look_up(self):
         choice = self.tree.selection()
         if choice == ():
             messagebox.showwarning(title = "ERROR" , message = "PIck an Item From The List")
         else:
                self.destroy()
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                c.execute("SELECT *  FROM entries WHERE oid = ? ", choice)
                data = c.fetchall()
                self.L1 = Label(self.right , text = "STAT DETAIL: "+str(data[0][1]) , fg = l_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L1.place(x = 10 , y = 10)
                
                self.L2 = Label(self.right , text = "DATE: "+str(data[0][0]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L2.place(x = 10 , y = 60)
                
                self.L3 = Label(self.right , text = "REG No:  "+str(data[0][1]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L3.place(x = 10 , y = 110)

                self.L4 = Label(self.right , text = "MAKE: "+str(data[0][2]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L4.place(x = 10 , y = 160)
                
                self.L5 = Label(self.right , text = "MODEL:  "+str(data[0][3]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L5.place(x = 10 , y = 210)

                self.L6 = Label(self.right , text = "BOOKED BY:  "+str(data[0][4]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L6.place(x = 10 , y = 240)
                
                self.L7 = Label(self.right , text = "WORKSHOP CHARGES:  "+str(data[0][5])+" Ksh", fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L7.place(x = 10 , y = 290)
                
                self.L8 = Label(self.right , text = "AMOUNT PAID:  "+str(data[0][6])+" Ksh", fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L8.place(x = 10 , y = 340)

                self.L9 = Label(self.right , text = "BALANCE: "+str(data[0][7])+" Ksh" , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L9.place(x = 10 , y = 390)

                self.L10 = Label(self.right , text = "REMARK: ", fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L10.place(x = 10 , y = 440)

                self.L11 = Label(self.right , text = str(data[0][8]) , fg = c_T_F_COLOR , bg = l_B_COLOR, font = l_T_FONTT)
                self.L11.place(x = 10 , y = 490)
                
               
                conn.commit()
                conn.close()
    def destroy(self):
        try:
            self.L1.destroy()
            self.L2.destroy()
            self.L3.destroy()
            self.L4.destroy()
            self.L5.destroy()
            self.L6.destroy()
            self.L7.destroy()
            self.L8.destroy()
            self.L9.destroy()
            self.L10.destroy()
            self.L11.destroy()
            
        except Exception:
            pass
    def neg_bal(self):
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                c.execute("SELECT *  FROM entries  ")
                data = c.fetchall()
                count  = 1
                try:
                    for record in self.tree.get_children():
                                 self.tree.delete(record)
                except Exception:
                            pass
                        
                for i in range (len(data)):
                    if int(data[i][7]) < 0:
                         stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                         self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                         count=  count +1
                    else:
                        continue
                conn.commit()
                conn.close()

    def pos_bal(self):
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                c.execute("SELECT *  FROM entries   ")
                data = c.fetchall()
                count  = 1
                try:
                    for record in self.tree.get_children():
                                 self.tree.delete(record)
                except Exception:
                            pass
                        
                for i in range (len(data)):
                    if int(data[i][7]) > 0:
                         stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                         self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                         count=  count +1
                    else:
                        continue
                conn.commit()
                conn.close()
        
    def drop(self):
       
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                c.execute("SELECT *  FROM entries   ")
                data = c.fetchall()
                count  = 1
                try:
                    for record in self.tree.get_children():
                                 self.tree.delete(record)
                except Exception:
                            pass
                        
                for i in range (len(data)):
                         stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                         self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                         count +=1
                conn.commit()
                conn.close()
                
    def close1(self):
                try:
                    self.destroy()
                    for record in self.tree.get_children():
                                 self.tree.delete(record)
                except Exception:
                            pass
    def search3(self):#BOOKER       
        if self.clicked.get() == "NAMES":
            messagebox.showwarning(title = "ERROR" , message = "PIck/Add a name")
        else:
            conn = sqlite3.connect("PAUL.db" )
            c = conn.cursor()
            r  = (self.clicked.get(),)
            c.execute("SELECT * FROM entries  WHERE  booker = ?  ", r)
            data = c.fetchall()
            if data == []:
                messagebox.showwarning(title = "ERROR" , message = self.clicked.get() + " Appears To Have Not Booked Anything")
            else:
                        count  = 1
                        try:
                            for record in self.tree.get_children():
                                 self.tree.delete(record)
                        except Exception:
                            pass
                        
                        for i in range (len(data)):
                             stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                             self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                             count +=1
                        conn.commit()
                        conn.close()
               
        
    def search2(self):#REG no
        try:  
            x , y = self.empty_checker(self.e1.get())
            if x == 0:
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                r  = (y,)
                c.execute("SELECT * FROM entries  WHERE  reg= ?  ", r)
                data = c.fetchall()
                if data == []:
                    messagebox.showwarning(title = "ERROR" , message = "The Reg No Entered Doesnt Appear to be in the database\nCheck If The Spelling Is Correct Or Youve Entered The Correct Values")
                else:
                        count  = 1
                        try:
                            for record in self.tree.get_children():
                                 self.tree.delete(record)
                        except Exception:
                            pass
                        
                        for i in range (len(data)):
                             stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                             self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                             count +=1
                        conn.commit()
                        conn.close()

          
        except TypeError:
             pass
        
    def search1(self):#DATE
        try:
            x , y = self.empty_checker(self.e3.get())
            if x == 0:
                new = ""
                for i in y:
                    if i == "-" or i == ":":
                        new +="/"
                    elif i== " ":
                        continue
                    else:
                        new +=i
                conn = sqlite3.connect("PAUL.db" )
                c = conn.cursor()
                r  = (new,)
                c.execute("SELECT * FROM entries   WHERE  date= ?  ", r)
                data = c.fetchall()
                count =1
                if data == []:
                    messagebox.showwarning(title = "ERROR" , message = "The Date Entered Doesnt Appear To Be In The Database\nCheck If The Format Is Correct(YY/MM/DD YY:MM:DD YY-MM-DD) \nOr Youve Entered The Wrong Values")
                else:
                        try:
                            for record in self.tree.get_children():
                                 print(record)
                                 self.tree.delete(record)
                        except Exception:
                            pass
                        
                        for i in range (len(data)):
                             stuff= [data[i][0], data[i][1],data[i][4],data[i][5],data[i][6] ,data[i][7]]
                             self.tree.insert(parent= '', index = 'end' , iid = count , text = count ,values =(stuff))
                             count +=1
                        conn.commit()
                        conn.close()
                
        except TypeError:
             pass
        
    def empty_checker(self , x):
        new_input = ""
        con = 0
        t = 0
        if x == "":
            messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
            con = 1
        else:
                for i in x:
                    if t == 0:
                        if i == " ":
                              continue
                        else:
                            new_input +=i
                    else:
                        new_input +=i
                if new_input == "":
                    messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
                    con = 1
                else:
                    return con , new_input
        
    def Entry(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        ENTRY(root)
        
    def Add(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        ADD(root)
        
    def Close(self):
        choice = messagebox.askyesno(title = "Exit" , message = "Exit ?")
        if choice == 1:
            self.wn.destroy()
        else:
            pass


        
class ADD:
    def __init__(self , wn , *args , **kwargs):
        self.E_DB =E_DB
        self.N_DB = N_DB 
        try:

            conn = sqlite3.connect(self.N_DB)
            c = conn.cursor()
            c.execute("""CREATE TABLE name (names text)""")
            conn.commit()
            conn.close()
            
        except sqlite3.OperationalError:
            pass
            
        self.l_B_COLOR ,l_B_COLOR = "grey","grey"
        self.l_FONTT,l_FONTT = "Helvetica 10 bold","Helvetica 10 bold"
        self.l_T_FONTT,l_T_FONTT = "Arial 10 bold","Arial 10 bold"
        self.l_F_COLOR, l_F_COLOR= "purple","green"
        self.l_T_F_COLOR, l_T_F_COLOR= "purple","purple"

        self.r_B_COLOR,r_B_COLOR = "lightblue","lightblue"
        self.r_FONTT,r_FONTT = "Helvetica 10 bold","Helvetica 10 bold"
        self.r_T_FONTT, r_T_FONTT= "Arial 15 bold","Arial 15 bold"
        self.r_F_COLOR,r_F_COLOR = "green","green"
        self.r_T_F_COLOR, r_T_F_COLOR = "purple","purple"

        self.c_B_COLOR,c_B_COLOR = "black","black"
        self.c_FONTT ,c_FONTT ="Helvetica 10 bold","Helvetica 10 bold"
        self.c_T_FONTT, c_T_FONTT= "Arial 10 bold","Arial 10 bold"
        self.c_F_COLOR, c_F_COLOR= "green","green"
        self.c_T_F_COLOR, c_T_F_COLOR= "purple","purple"

        
        self.wn = wn
        
        
        self.c= Frame(wn , width = 100,height = 600, bg =r_B_COLOR)
        self.c.pack(side = LEFT)

        self.right = Frame(wn , width = 450,height = 600, bg =  c_B_COLOR)
        self.right.pack( )
#_________________LABELS
        l1 = Label(self.right , text = "ADD NEW:" , fg = r_T_F_COLOR, bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 0 , y = 0)        
        l1 = Label(self.right , text = "NAME :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 20 , y = 70)
        
        l1 = Label(self.right  , text = "LOOK UP NAMES :" , fg = r_F_COLOR , bg = c_B_COLOR , font = r_FONTT)
        l1.place(x = 20 , y = 150)
        
        self.e1 = Entry(self.right, width = 20, font = FONTT)
        self.e1.place(x =100 , y = 70)

        self.t = Listbox(self.right, height = 12,  width = 34, font = FONTT)
        self.t.place(x = 100 , y = 200)
        
#_________________BUTTONS
        
        Go1 = Button(self.right , text = "ADD" ,  width = 10 ,font = FONTT,command = self.add_name)
        Go1.place(x = 300 , y = 70)
        
        Go2 = Button(self.right, text = "Search" ,  width = 10 ,font = FONTT    ,command = self.search)
        Go2.place(x = 300 , y = 150)
        
        close = Button(self.right , text = "Close" ,  width = 10,font = FONTT , command =self.close)
        close.place(x = 300, y =  460)
        
        delete = Button(self.right , text = "Remove " ,  width = 10,font = FONTT , command =self.Remove)
        delete.place(x = 100, y =  460)
        
        entry_b = Button(self.c , text = "ENTRY", width = 10  ,  font = FONTT,command = self.Entry)
        entry_b.place(x = 0 , y = 150)
        
        stats_b = Button(self.c , text = "STATS", width = 10  ,  font = FONTT, command= self.Stats)
        stats_b.place(x = 0 , y = 200)
        
        add_b = Button(self.c , text = "ADD NEW", width = 10  ,  font = FONTT )#, command= self.Add)
        add_b.place(x = 0 , y = 250)

        close_b = Button(self.c , text = "CLOSE", width = 10  ,  font = FONTT, command = self.Close)
        close_b.place(x = 0 , y = 400)
#____________________FUNCTONS
        
    def Remove(self):
        conn = sqlite3.connect(self.N_DB)
        c = conn.cursor()
        c.execute("SELECT oid,* FROM name")
        data =  c.fetchall()

        try:
            OID = data[self.t.index(self.t.curselection())]
            ch = messagebox.askyesno(title = "CONTINUE?..." , message = "DELETE " + str(OID[1]) + str(" FROM DATABASE ??"))
            if ch == 0:
                pass
            else:
                OID = (OID[0], )
                c.execute("DELETE  FROM name WHERE oid = ?  " ,OID )
            
        except TclError:
            messagebox.showwarning(title = "ERROR" , message = "Select Something From The List First")

        conn.commit()
        conn.close()
        self.search()
        
        
        
    
    def close(self):
        self.t.delete(0 , END)            
        
    def search(self):
            conn = sqlite3.connect(self.N_DB)
            c = conn.cursor()
            c.execute("SELECT oid,* FROM name")
            data = c.fetchall()
            self.t.delete(0 , END)            
            if data == [ ]:
                pass
            else:
                for index, i in enumerate(data):
                    self.t.insert(index+1 ,str(index+1)+": " + str(i[1]) )#+str("    ID: ")+str(i[0]))                
                
            
        
    def empty_checker(self , x):
        new_input = ""
        con = 0
        t = 0
        if x == "":
            messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
            con = 1
        else:
                for i in x:
                    if t == 0:
                        if i == " ":
                              continue
                        else:
                            new_input +=i
                    else:
                        new_input +=i
                if new_input == "":
                    messagebox.showwarning(title = "ERROR" , message = "Please Fill The Entire Form")
                    con = 1
                else:
                    return con , new_input
                
    def add_name(self):
        try:
            x, y = self.empty_checker(self.e1.get())
            if x == 0:
                conn = sqlite3.connect(self.N_DB)
                c = conn.cursor()
                r = [self.e1.get(),  ]
                c.execute("SELECT * FROM name")
                data = c.fetchall()
                try:
                    data.index(tuple(r))
                    messagebox.showwarning(title = "ERROR" , message = "The Name Already Exist")
                except ValueError:
                    c.execute("insert into name (names) values (?)" ,r)
                    conn.commit()
                    conn.close()
                    self.e1.delete(0 , END)
                    self.search()
        except TypeError:
                pass
            
    def Entry(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        ENTRY(root)
        
    def Stats(self):
        self.wn.destroy()
        root = Tk()
        root.resizable(width=False, height=False)
        STATS(root)
        
    def Close(self):
        choice = messagebox.askyesno(title = "Exit" , message = "Exit ?")
        if choice == 1:
            self.wn.destroy()
        else:
            pass
        
       
        
'''conn = sqlite3.connect(E_DB)
c = conn.cursor()
c.execute("SELECT oid FROM entries")
data = c.fetchall()
for i in data:
    c.execute("DELETE   FROM entries WHERE oid = ? ", i  )

conn.commit()
conn.close()        
'''
root = Tk()
root.resizable(width=False, height=False) 
#ADD(root)
ENTRY(root)
#STATS(root)
root.mainloop()
