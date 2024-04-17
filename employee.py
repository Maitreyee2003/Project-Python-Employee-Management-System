from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")
        self.root.title("Employee Management System")

        #Variables
        self.var_dept=StringVar()
        self.var_name=StringVar()
        self.var_desig=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcombo=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_age=StringVar()
        self.var_employeeid=StringVar()


        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',32,'bold'),fg='black',bg='white')
        lbl_title.place(x=0,y=0,width=1280,height=40)

        # logo
        img_logo=Image.open('python_project_images/2.png')
        img_logo=img_logo.resize((40,40),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=200,y=0,width=40,height=40)
        
        #Img frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=40,width=1280,height=120)

        #1st image
        img1=Image.open('python_project_images/9.jpg')
        img1=img1.resize((450,120),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=450,height=120)

        #2nd image
        img2=Image.open('python_project_images/3.png')
        img2=img2.resize((450,120),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=450,y=0,width=450,height=120)

        #3rd image
        img3=Image.open('python_project_images/7.jpg')
        img3=img3.resize((450,120),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=850,y=0,width=450,height=120)

        #main frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=170,width=1250,height=500)

        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',10,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1210,height=235)
        
        #Labels and Entry fields
        lbl_dept=Label(upper_frame,font=('arial',10,'bold'),text='Department:',bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dept,font=('arial',10,'bold'),width=20,state='readonly')
        combo_dept['value']=('Select Department','HR','Software Engineer','Manager','Finance','Security')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #Name
        lbl_name=Label(upper_frame,font=('arial',10,'bold'),text='Name:',bg='white')
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',10,'bold'))
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #Designation
        lbl_Designation=Label(upper_frame,font=('arial',10,'bold'),text='Designation:',bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_desig,width=22,font=('arial',10,'bold'))
        txt_Designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Email
        lbl_email=Label(upper_frame,font=('arial',10,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',10,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,font=('arial',10,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',10,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        
        #Married
        lbl_married_status=Label(upper_frame,font=('arial',10,'bold'),text='Married Status:',bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        combo_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',10,'bold'),width=20,state='readonly')
        combo_txt_married['value']=('UnMarried','Married')
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2,column=3,padx=2,pady=8,sticky=W)

        #DOB
        lbl_dob=Label(upper_frame,font=('arial',10,'bold'),text='Date Of Birth:',bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',10,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #Date of joining
        lbl_doj=Label(upper_frame,font=('arial',10,'bold'),text='Date Of Joining:',bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',10,'bold'))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #ID proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcombo,state='readonly',font=('arial',10,'bold'),width=20)
        com_txt_proof['value']=('Select ID Proof','PAN Card','Addhar Card','Voter ID','Driving Licence')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',10,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        #Gender
        lbl_gender=Label(upper_frame,font=('arial',10,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state='readonly',font=('arial',10,'bold'),width=20)
        com_txt_gender['value']=('Male','Female','Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #Phone
        lbl_ph=Label(upper_frame,font=('arial',10,'bold'),text='Phone Number:',bg='white')
        lbl_ph.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_ph=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',10,'bold'))
        txt_ph.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Country
        lbl_country=Label(upper_frame,font=('arial',10,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',10,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #Salary(CTC)
        lbl_ctc=Label(upper_frame,font=('arial',10,'bold'),text='Salary(CTC):',bg='white')
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',10,'bold'))
        txt_ctc.grid(row=2,column=5,sticky=W,padx=2,pady=7)

        #Age
        lbl_age=Label(upper_frame,font=('arial',10,'bold'),text='Age:',bg='white')
        lbl_age.grid(row=3,column=4,padx=2,pady=7,sticky=W)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',10,'bold'))
        txt_age.grid(row=3,column=5,sticky=W,padx=2,pady=7)

        #EmployeeID
        lbl_EmpID=Label(upper_frame,font=('arial',10,'bold'),text='Employee ID:',bg='white')
        lbl_EmpID.grid(row=4,column=4,padx=2,pady=7,sticky=W)

        txt_EmpID=ttk.Entry(upper_frame,textvariable=self.var_employeeid,width=22,font=('arial',10,'bold'))
        txt_EmpID.grid(row=4,column=5,sticky=W,padx=2,pady=7)


        #Button frame
        button_frame=Frame(main_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1000,y=25,width=170,height=210)

        #add button
        btn_save=Button(button_frame,text="Save",command=self.add_data,font=('Bahnschrift',15,'bold'),width=14,bg='blue',fg='white')
        btn_save.grid(row=0,column=0,padx=1,pady=5)

        #update button
        btn_update=Button(button_frame,text="Update",command=self.update_data,font=('Bahnschrift',15,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        #delete button
        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=('Bahnschrift',15,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)
 
        #clear button
        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=('Bahnschrift',15,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',10,'bold'),fg='red')
        down_frame.place(x=10,y=245,width=1210,height=235)

        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',10,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1200,height=50)

        search_by=Label(search_frame,font=('Bahnschrift',13,'bold'),text='Search By',bg='skyblue',fg='black')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        #Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',11,'bold'),width=24)
        com_txt_search['value']=('Select Option','Phone','Id_proof','Name','Employee ID','Department')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=30,font=('arial',10,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",command=self.search_data,font=('Bahnschrift',13,'bold'),width=17,fg='black',bg='skyblue')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('Bahnschrift',13,'bold'),width=17,fg='black',bg='skyblue')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        btn_back=Button(search_frame,text="Back",font=('Bahnschrift',13,'bold'),width=17,fg='black',bg='skyblue')
        btn_back.grid(row=0,column=5,padx=5)
        #***************************Employee Table*************************
        #Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1200,height=160)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","desig","email","address","married","dob","doj","idproofcombo","ifproof","gender","phone","country","salary","age","employeeid",),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)  

        Scroll_x.config(command=self.employee_table.xview)
        Scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married')
        self.employee_table.heading('dob',text='Date Of Birth')
        self.employee_table.heading('doj',text='Date of Joining')
        self.employee_table.heading('idproofcombo',text='ID Type')
        self.employee_table.heading('ifproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        self.employee_table.heading('age',text='Age')
        self.employee_table.heading('employeeid',text='Employee ID')

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("desig",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcombo",width=100)
        self.employee_table.column("ifproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.column("age",width=100)
        self.employee_table.column("employeeid",width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #*************Function Declaration***************************
    #Add
    def add_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='Maitreyee123',database='python_employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )',(

                                                                                    self.var_dept.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_desig.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_married.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_doj.get(),
                                                                                    self.var_idproofcombo.get(),
                                                                                    self.var_idproof.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_country.get(),
                                                                                    self.var_salary.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_employeeid.get()
                                                                                                                ))  
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added!!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

     #Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username='root',password='Maitreyee123',database='python_employee_management_system')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()         

    #Get Cursor
        
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dept.set(data[0])
        self.var_name.set(data[1])
        self.var_desig.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcombo.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        self.var_age.set(data[14])
        self.var_employeeid.set(data[15])

    #update
    def update_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                update=messagebox.askyesno('update','Are you sure to update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Maitreyee123',database='python_employee_management_system')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,ID_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s,Age=%s,Employee_id=%s where id_proof=%s',(


                                                                                    self.var_dept.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_desig.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_married.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_doj.get(),
                                                                                    self.var_idproofcombo.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_country.get(),
                                                                                    self.var_salary.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_employeeid.get(),
                                                                                    self.var_idproof.get()
                                                                                    
                                                                                                ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success',"Employee Succesfully Updates",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                
                
    #Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error',"All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete',"Are you are delete this employee",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Maitreyee123',database='python_employee_management_system')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success',"Employee Succesfully Updates",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                

    #Reset
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_name.set("")
        self.var_desig.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcombo.set("Selcet ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        self.var_age.set("")
        self.var_employeeid.set("")

    #search by
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','Please Select Option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Maitreyee123',database='python_employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



   






if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()       