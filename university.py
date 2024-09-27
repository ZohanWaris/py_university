import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class uni():
    def __init__(self,root):
        self.root = root
        self.root.title("university Management")
        self.root.configure(bg="pink")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.root.geometry(f"{self.width}x{self.height}+0+0")

        label = tk.Label(self.root, text="Univerity Mangement System", bg=self.clr(220,180,150),font=("Arial",50,"bold"),bd=4, relief="groove")
        label.pack(side="top", fill="x")

        # input frame

        inFrame = tk.Frame(self.root, bg=self.clr(180,150,220), bd=4, relief="ridge")
        inFrame.place(width=self.width/3, height=self.height-180, x=30,y=100)

        rnLbl = tk.Label(inFrame,text="RollNo:",bg=self.clr(180,150,220),fg="white",font=("Arial",15,"bold"))
        rnLbl.grid(row=0, column=0,padx=20,pady=20)
        self.rnIn = tk.Entry(inFrame, bd=1, width=17, font=("Arial",20,"bold"))
        self.rnIn.grid(row=0, column=1, padx=10,pady=20)

        nameLbl =tk.Label(inFrame,text="Name:",bg=self.clr(180,150,220),fg="white",font=("Arial",15,"bold"))
        nameLbl.grid(row=1,column=0, padx=20,pady=20 )
        self.nameIn = tk.Entry(inFrame, bd=1, width=17, font=("Arial",20,"bold"))
        self.nameIn.grid(row=1, column=1, padx=10,pady=20)

        subLbl= tk.Label(inFrame,text="Subject:",bg=self.clr(180,150,220),fg="white",font=("Arial",15,"bold"))
        subLbl.grid(row=2,column=0, padx=20,pady=20)
        self.subIn = tk.Entry(inFrame, bd=1, width=17, font=("Arial",20,"bold"))
        self.subIn.grid(row=2, column=1, padx=10,pady=20)

        gradeLbl = tk.Label(inFrame,text="CGPA:",bg=self.clr(180,150,220),fg="white",font=("Arial",15,"bold"))
        gradeLbl.grid(row=3,column=0, padx=20,pady=20)
        self.gradeIn = tk.Entry(inFrame, bd=1, width=17, font=("Arial",20,"bold"))
        self.gradeIn.grid(row=3, column=1, padx=10,pady=20)


        addrLbl = tk.Label(inFrame,text="Address:",bg=self.clr(180,150,220),fg="white",font=("Arial",15,"bold"))
        addrLbl.grid(row=4,column=0, padx=20,pady=20)
        self.addrIn =tk.Entry(inFrame, bd=1, width=17, font=("Arial",20,"bold"))
        self.addrIn.grid(row=4, column=1, padx=10,pady=20)

        regBtn = tk.Button(inFrame,command=self.insertFun, text="Register", bg="light gray",bd=2,relief="raised", font=("Arial",20,"bold"),width=20)
        regBtn.grid(row=6,column=0, padx=30, pady=30,columnspan=2)


        # info Frame

        self.infoFrame = tk.Frame(self.root,bg=self.clr(180,220,150),bd=4, relief="ridge")
        self.infoFrame.place(width=self.width/2+110,height=self.height-180, x=self.width/3+80, y=100)

        optLbl = tk.Label(self.infoFrame, text="Options:",bg=self.clr(180,220,150),font=("Arial",15))
        optLbl.grid(row=0,column=0, padx=20, pady=10)

        self.options= ttk.Combobox(self.infoFrame, width=12,font=("Arial",15), values=("RollNo","Subject","All"))
        self.options.set("Select One")
        self.options.grid(row=0,column=1,padx=20, pady=10)

        valLbl=tk.Label(self.infoFrame, text="Value:",bg=self.clr(180,220,150),font=("Arial",15))
        valLbl.grid(row=0, column=2, padx=20, pady=10)
        self.optIn =tk.Entry(self.infoFrame, width=15, bd=1,font=("Arial",15))
        self.optIn.grid(row=0, column=3, padx=20, pady=10)
        
        srchBtn = tk.Button(self.infoFrame, command=self.searchFun,text="Search", bd=2, relief="raised", bg="sky blue", font=("Arial",15), width=10)
        srchBtn.grid(row=1, column=0, padx=40, pady=10)

        updBtn = tk.Button(self.infoFrame, command=self.updateFun,text="Update", bd=2, relief="raised", bg="sky blue", font=("Arial",15), width=10)
        updBtn.grid(row=1, column=1, padx=40, pady=10)

        delBtn = tk.Button(self.infoFrame, command=self.delFun,text="Delete", bd=2, relief="raised", bg="sky blue", font=("Arial",15), width=10)
        delBtn.grid(row=1, column=2, padx=40, pady=10,columnspan=2)
        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.infoFrame, bd=3, relief="sunken")
        tabFrame.place(width=self.width/2+70,height=self.height-320, x=20, y=120)

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal",bg="brown")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical",bg="brown")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, columns=("rollNo","name", "sub", "gpa","addr"),xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set)
        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("rollNo", text="Roll_No")
        self.table.heading("name", text="Name")
        self.table.heading("sub", text="Subject")
        self.table.heading("gpa", text="Grade")
        self.table.heading("addr", text="Address")
        self.table["show"]= "headings"

        self.table.column("rollNo", width=120)
        self.table.column("name", width=120)
        self.table.column("sub", width=120)
        self.table.column("gpa", width=120)
        self.table.column("addr", width=120)

        self.table.pack(fill="both", expand=1)

    def insertFun(self):
        rn = int(self.rnIn.get())
        name = self.nameIn.get()
        sub =  self.subIn.get()
        grade = self.gradeIn.get()
        addr =  self.addrIn.get()

        if rn and name and sub and grade and addr:
            try:
                self.dbFun()
                self.cur.execute("insert into uni(rollNo,name, subject,cgpa,addr) values(%s,%s,%s,%s,%s)",(rn,name,sub,grade,addr))
                self.con.commit()
                tk.messagebox.showinfo("Success",f"Student: {name} is registered Successfuly")
                

                self.tabFun()
                self.table.delete(*self.table.get_children())
                self.cur.execute("select * from uni where rollNo=%s",(rn))
                row = self.cur.fetchone()
                self.table.insert('',tk.END,values=row)

                self.con.close()
                self.rnIn.delete(0,tk.END)
                self.nameIn.delete(0,tk.END)
                self.subIn.delete(0,tk.END)
                self.gradeIn.delete(0,tk.END)
                self.addrIn.delete(0,tk.END)
            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")

        else:
            tk.messagebox.showerror("Error","Please Fill All Input Fields")

    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="admin", database="rec")
        self.cur = self.con.cursor()
   
    def clr(self,r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def searchFun(self):
        val1 = self.options.get()
        val2 = self.optIn.get()

        if val1=="RollNo":
            val2_int = int(val2)
            try:
                self.dbFun()
                self.cur.execute("select * from uni where rollNo=%s",val2_int)
                row = self.cur.fetchone()
                if row:
                    self.tabFun()
                    self.table.delete(*self.table.get_children())
                    self.table.insert('',tk.END,values=row)
                    self.con.close()
                else:
                    tk.messagebox.showerror("Error","No student Exists with this RollNo")

            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")
        
        elif val1=="Subject":
            try:
              self.dbFun()
              self.cur.execute("select * from uni where subject=%s",val2) 
              data = self.cur.fetchall() 
              if data:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert('',tk.END,values=i)
                    self.con.close()
              else:
                tk.messagebox.showerror("Error","No Student Exists with this Subject")
            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")

        elif val1=="All":
            try:
                self.dbFun()
                self.cur.execute("select * from uni")
                data = self.cur.fetchall()
                if data:
                    self.tabFun()
                    self.table.delete(*self.table.get_children())
                    for j in data:
                        self.table.insert('',tk.END,values=j)
                    self.con.close()        
                else:
                    tk.messagebox.showerror("Error","No Data Exist")
            
            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")

    def updateFun(self):
        
        
        self.updFrame = tk.Frame(self.root, bg="gray", bd=3,relief="ridge")
        self.updFrame.place(width=self.width/3, height=self.height-450, x=self.width/2, y=250)

        lbl =tk.Label(self.updFrame,text="New Subject:",bg="gray", fg="white", font=("Arial",15))
        lbl.grid(row=0, column=0, padx=10, pady=30)
        self.valIn = tk.Entry(self.updFrame, width=17, bd=2, font=("Arial",15,"bold"))
        self.valIn.grid(row=0,column=1, padx=10, pady=30)

        okBtn = tk.Button(self.updFrame,text="OK",command=self.updFun, bg="light gray",font=("Arial",20,"bold"), bd=2, relief="raised",width=20)
        okBtn.grid(row=1, column=0,padx=30, pady=30,columnspan=2)

    def updFun(self):
        val1 = self.options.get()
        val2 = self.optIn.get()

        newVal = self.valIn.get()
        if val1=="RollNo":
            val2_int = int(val2) 
            try:
                self.dbFun()
                
                self.cur.execute("update uni set subject= %s where rollNo= %s",(newVal,val2_int))
                self.con.commit()
                self.cur.execute("select * from uni where rollNo= %s",val2_int)
                row = self.cur.fetchone()
                if row:
                    tk.messagebox.showinfo("Success",f"Subject is Replaced with: {newVal}")
                    self.tabFun()
                    self.table.delete(*self.table.get_children())
                    self.table.insert('',tk.END,values=row)
                    self.con.close()
                    self.updFrame.destroy()
                else:
                    tk.messagebox.showerror("Error","No student Exists with this RollNo")
                    self.updFrame.destroy()

            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")
                self.updFrame.destroy()

        elif val1=="Subject":
            try:
              self.dbFun()
        
              self.cur.execute("update uni set subject= %s where subject= %s",(newVal,val2))
              self.con.commit()

              self.cur.execute("select * from uni where subject=%s",newVal) 
              data = self.cur.fetchall() 
              if data:
                tk.messagebox.showinfo("Success",f"Subject: {val2} is Replaced with: {newVal}")
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert('',tk.END,values=i)
                    self.con.close()
                    self.updFrame.destroy()
                    
              else:
                tk.messagebox.showerror("Error","No Student Exists with this Subject")
                self.updFrame.destroy()
            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")
                self.updFrame.destroy()

        else:
            tk.messagebox.showerror("Error",f"Select Only RollNo or Subject")
            self.updFrame.destroy()

    def delFun(self):
        val1 = self.options.get()
        val2 = self.optIn.get()

        if val1=="RollNo":
            val2_int = int(val2)
            try:
                self.dbFun()
                self.cur.execute("delete from uni where rollNo=%s",val2_int)
                self.con.commit()
                tk.messagebox.showinfo("Success",f"Data of student {val2_int} is revomed")
                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")

        elif val1=="Subject":
            try:
                self.dbFun()
                self.cur.execute("delete from uni where subject= %s", val2)
                self.con.commit()
                tk.messagebox.showinfo("Success",f"Data of students with Subject {val2} is/are revomed")
                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error",f"Error: {e}")

root = tk.Tk()
obj = uni(root)
root.mainloop()