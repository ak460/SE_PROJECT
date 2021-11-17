from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import re
import mysql.connector


class Register():
	
	def __init__(self,root):
		self.root=root
		self.root.title('Register Page')
		self.root.geometry('1600x890+0+0')

		#variable
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.contact_var=StringVar()
		self.gender_var=StringVar()
		self.country_var=StringVar()
		self.id_var=StringVar()
		self.id_no=StringVar()
		self.password=StringVar()
		self.confirm_pass=StringVar()
		self.check_var=IntVar()
		
  
  		#images
		self.bg = ImageTk.PhotoImage(file ='bg.jpg')
		bg_lbl=Label( self.root, image= self.bg,bd=1,relief=RAISED)
		bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
                
		logo_img=Image.open('logo.jpg')
		logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
		self.photo_logo=ImageTk.PhotoImage(logo_img)

		#Title frame
		title_frame=Frame(self.root, bd=1,relief=RIDGE)
		title_frame.place(x=450, y=28,width=550,height=82)
  
		title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='USER REGISTER FORM', font=('times new roman',25,'bold'),fg='darkblue')
		title_lbl.place(x=10,y=10)

  		#information frame	
		main_frame=Frame(self.root, bd=1,relief=RIDGE)
		main_frame.place(x=450, y=110,width=550,height=580)

  
		#username
		user_name=Label(main_frame,text='Username:',font=('times new roman',16,'bold'))
		user_name.grid(row=0,column=0,padx=9,pady=9,sticky=W)
		#entry
		user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15,'bold'),width=25)
		user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
		#bind callback and Validation register
		validate_name=self.root.register(self.checkname)
		user_entry.config(validate='key',validatecommand=(validate_name,"%P"))
  
		#email
		email_name=Label(main_frame,text='Email:',font=('times new roman',16,'bold'))
		email_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)
		#entry
		email_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',15,'bold'),width=25)
		email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
  
		#contact
		contact_no=Label(main_frame,text='Contact No.:',font=('times new roman',16,'bold'))
		contact_no.grid(row=2,column=0,padx=10,pady=10,sticky=W)
		#entry
		contact_entry=ttk.Entry(main_frame,textvariable=self.contact_var,font=('times new roman',15,'bold'),width=25)
		contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
		#bind callback and Validation register
		validate_contact=self.root.register(self.checkname)
		contact_entry.config(validate='key',validatecommand=(validate_contact,"%P"))
  
  
		#gender
		gender_name=Label(main_frame,text='Select Gender:',font=('times new roman',16,'bold'))
		gender_name.grid(row=3,column=0,padx=10,pady=10,sticky=W)
		#entry
		gender_frame=Frame(main_frame)
		gender_frame.place(x=200,y=160,width=280,height=35)
  
		radio_male=Radiobutton(gender_frame,variable=self.gender_var, value='Male',text="Male",font=('times new roman',15))
		radio_male.grid(row=0, column=0,padx=10,pady=0,sticky=W)
		self.gender_var.set('Male')

		radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text="Female",font=('times new roman',15))
		radio_female.grid(row=0, column=1,padx=10,pady=0,sticky=W)
  
		#country
		country=Label(main_frame,text='Select Country: ',font=('times new roman',16,'bold'))
		country.grid(row=4,column=0,padx=10,pady=10,sticky=W)
		list=['India','UK','Nepal','Afganistan','Pakistan']
		
  		
		droplist=OptionMenu(main_frame,self.country_var, *list)
		droplist.config(width=21, font=('times new roman',15),bg='white')
		self.country_var.set("Select your country")
		droplist.grid(row=4, column=1,padx=10,pady=10,sticky=W)

		#ID TYPE
		id_type=Label(main_frame, text="Select ID type:",font=('times new roman',16,'bold'))
		id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)

		self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=('times new roman',15),justify='center',state="readonly",width=23)
		self.combo_id_type["values"]=("Select your Id","Adhar card","Passport","Driving Licence")
		self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
		self.combo_id_type.current(0)

		#ID Number
		id_no=Label(main_frame, text="ID Number: ",font=('times new roman',16,'bold'))
		id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)
  		#entry
		id_no_entry=ttk.Entry(main_frame,textvariable=self.id_no,font=('times new roman',15,'bold'),width=25)
		id_no_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

		#password
		s_password=Label(main_frame,text='Password',font=('times new roman',16,'bold'))
		s_password.grid(row=7,column=0,padx=10,pady=10,sticky=W)
		#entry
		pass_entry=ttk.Entry(main_frame,textvariable=self.password,font=('times new roman',15,'bold'),width=25)
		pass_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)
  
		#Confirm Password
		c_pass=Label(main_frame,text="Confirm Password:",font=('times new roman',16,'bold'))
		c_pass.grid(row=8,column=0,padx=10,pady=10,sticky=W)
		#entry
		pass_confirm=ttk.Entry(main_frame,textvariable=self.confirm_pass,font=('times new roman',15,'bold'),width=25)
		pass_confirm.grid(row=8,column=1,padx=10,pady=10,sticky=W)

		#check frame
		check_frame=Frame(main_frame)
		check_frame.place(x=130,y=460,width=400,height=70)
  
		check_btn=Checkbutton(check_frame,variable=self.check_var,text='Agree Our terms and conditions',font=("times new roman",16),onvalue=1,offvalue=0)
		check_btn.grid(row=0,column=0,padx=10,sticky=W)

		self.check_lbl=Label(check_frame,text='Please Agree our tearms & conditions',font=('arial',15),fg='red')
		self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

		#button frame
		btn_frame=Frame(main_frame)
		btn_frame.place(x=30,y=530,width=480,height=70)
		
		save_data=Button(btn_frame,text="Save",command=self.validation, font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='black',fg='white')
		save_data.grid(row=0,column=0,padx=1,sticky=W)

		verify_data=Button(btn_frame,command=self.verify_data,text="Verify",font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='black',fg='white')
		verify_data.grid(row=0,column=1,padx=1,sticky=W)

		clear_data=Button(btn_frame,text="Clear",command=self.clear_data,font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='black',fg='white')
		clear_data.grid(row=0,column=2,padx=1,sticky=W)
  
	#call back function 
	def checkname(self, name):
		if name.isalnum():
			return True
		if name=='':
			return True
		else:
			messagebox.showerror('Invalid', 'Not Allowed'+ name[-1])
			return False
	#checkcontact
	def checkcontact(self, contact):
		if contact.isdigit():
			return True
		if len(str(contact))==0:
			return True
		else:
			messagebox.showerror("Invalid",'Invalid Entry')
			return False

	#checkpasword
	def checkpassword(self,password):
		if len(password)<=21:
			if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
				return True
			else:
				messagebox.showinfo('Invalid','Enter valid password(exm-asd@123)')
				return False
		else:
			messagebox.showerror('Invalid',"Length try to exceed")
			return False
			
			
	def checkemail(self,email):
		if len(email)>7:
			if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):		
				return True
			else:
				messagebox.showwarning('Alert','invalid email enter valid user email')
		else:
			messagebox.showinfo('Invalid','Email length is too small')
			
	#validation
	def validation(self):
		x=y=0
		if self.name_var.get()=='':
			messagebox.showerror('Error','Please enter your name',parent=self.root)
   
		elif self.email_var.get()=='':
			messagebox.showerror('Error','Please enter your email id',parent=self.root)
       
		elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
			messagebox.showerror('Error','Please enter your Valid contact',parent=self.root)
       
		elif self.gender_var.get()=='':
			messagebox.showerror('Error','Please enter your gender',parent=self.root)
       
		elif self.country_var.get()=='' or self.country_var.get()=='Select your country':
			messagebox.showerror('Error','Please enter your country name',parent=self.root)
       
		elif self.id_var.get()=='':
			messagebox.showerror('Error','Please select your ID type',parent=self.root)
    		
       
		elif self.id_no.get()=='':
			messagebox.showerror('Error','Please select your ID type',parent=self.root)
       
		elif len(self.id_no.get())!=12:
			messagebox.showerror('Error','Please enter 12 digit ID number',parent=self.root)
       
		elif self.password.get()=='':
			messagebox.showerror('Error','Please enter your password',parent=self.root)
       
		elif self.confirm_pass.get()=='':
			messagebox.showerror('Error','Please enter your confirm password',parent=self.root)
       
		elif self.password.get()!=self.confirm_pass.get():
			messagebox.showerror('Error','Please enter your confirm password',parent=self.root)
       
		elif self.email_var.get()!=None and self.password.get()!=None :
			x=self.checkemail(self.email_var.get())
			y=self.checkpassword(self.password.get())
    			#messagebox.showerror('Error','Please enter your email id',parent=self.root)
		if(x==True) and (y==True):
			if self.check_var.get()==0:
				self.check_lbl.config(text='Please Agree our terms & Conditions',fg='red')
			else:
				self.check_lbl.config(text='Checked',fg='green')
				messagebox.showinfo('Successfully',f'Your registration successfully completed your username:{self.name_var.get()} and password:{self.password.get()}')
       
			try:
				conn=mysql.connector.connect(host='localhost',username='root',password='',database='mydata')
				my_cursur=conn.cursor()
				my_cursur.execute('Insert into register1 values(%s,%s,%s,%s,%s,%s,%s,%s)',(
				self.name_var.get(),
				self.email_var.get(),
				self.contact_var.get(),				
				self.gender_var.get(),
    			self.country_var.get(),
				self.id_var.get(),
				self.id_no.get(),
				self.password.get(),                                                                                       
                                                                                        ))
				conn.commit()
				conn.close()
				messagebox.showinfo('Successfully',f'Your registration successfully completed your username:{self.name_var.get()} and password:{self.password.get()}')
			except Exception as es:
				messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
	def verify_data(self):
		data=f'Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\ncontact:{self.contact_var.get()}\nGender:{self.gender_var.get()}\nCountry:{self.country_var.get()}\nID_Type:{self.id_var.get()}\nID_No:{self.id_no.get()}\nPassword:{self.password.get()}\n'
		messagebox.showinfo('Details',data)
  
	def clear_data(self):
		self.name_var.set('')
		self.email_var.set('')
		self.contact_var.set('')
		self.gender_var.set('Male')
		self.country_var.set('Select your country')
		self.id_var.set('')
		self.id_no.set('')
		self.password.set('')
		self.confirm_pass.set('')
		self.check_var.set(0)
		
  
if __name__ == '__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
