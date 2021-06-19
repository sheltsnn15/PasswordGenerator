#import libs
import os.path

#import module
import tkinter as Tkinter
import Generator as pg
from tkinter import messagebox

# Tkinter Main Class
class Window(Tkinter.Tk):
	def __init__(self, *args, **kwargs):
		Tkinter.Tk.__init__(self, *args, **kwargs)
		self['padx']=10
		self['pady']=10
		self.passwordPanel()
		self.customisePswPanel()

	def infoBox(self, msg):
		messagebox.showinfo("Information Box", message=msg)

	def errorBox(self, msg):
		messagebox.showerror("Error Box", message=msg)

	def newFile(self):
		with open('passwords.txt', 'r') as fh:
			fh.write('passwords.txt')

	# append info to file
	def appendToFile(self):
		with open('passwords.txt', 'a') as fh:
			# get password use
			use = self.passwordUse.get()
			# get password
			psw = self.password.get()
			fh.write('\nUsed for: ' + use + '\nPassword: ' + psw + '\n')

	def checkForFile(self):
		file_exists = os.path.isfile('passwords.txt')
		# check if file exists
		if file_exists:
			self.appendToFile()
		else:
			# create new file and append info to that file
			self.newFile()
			self.appendToFile()

	def passwordPanel(self):
		self.password = Tkinter.StringVar()
		self.passwordLength = Tkinter.IntVar()
		self.passwordUse = Tkinter.StringVar()
		self.passwordLength.set(4)
		frame = Tkinter.LabelFrame(self, text='Password')
		frame.pack(side='left', expand='yes', fill='both')
		frame['padx']=5
		frame['pady']=5
		Tkinter.Label(frame, text='Use For:').pack(side='top', fill='x')
		Tkinter.Entry(frame, textvariable = self.passwordUse).pack(side='top', fill='x')
		Tkinter.Button(frame, text='Generate', command=self.generatePassword).pack(side='top', fill='x')
		Tkinter.Label(frame, textvariable=self.password).pack(side='top', fill='x')
		Tkinter.Button(frame, text='Copy To Clipboard', command=lambda:[self.clipboardCopy(), self.checkForFile()]).pack(side='top', fill='x')
		frame1 = Tkinter.LabelFrame(frame, text='Password Length')
		frame1.pack(side='top', expand='yes', fill='both', pady=5, padx=5, ipadx=5, ipady=5)
		Tkinter.Spinbox(frame1, from_=4, to_=100, textvariable=self.passwordLength).pack()
		return

	def clipboardCopy(self):
		# get generated password
		pas = self.password.get()
		# check if password is generated
		# if true, copy to clipboard
		if pas == "  ":
			self.errorBox("Generate password first")
		# else display error message
		else:
			# clear password
			self.clipboard_clear()
			# append to clipboard
			self.clipboard_append(pas)
			# inform user
			self.infoBox("Copied")
		return

	def generatePassword(self):
		# populate PswGenerator class constructor
		pasg = pg.PswGenerate(
			length=self.passwordLength.get(),
			digit=self.selectedCB[0].get(),
			uppercase=self.selectedCB[1].get(),
			lowercase=self.selectedCB[2].get(),
			punctuation=self.selectedCB[3].get()
			)
		#check is aleast one customise button is selected
		try:
			# generate password
			self.password.set(pasg.generate())
		except:
			self.errorBox("Select one password customise button")
		return

	def customisePswPanel(self): # method to create password customise controls
		# create a frame to host controls
		frame = Tkinter.LabelFrame(self, text='Customise Password')
		frame.pack(side='left')
		frame['padx'] = 10
		frame['pady'] = 10
		self.selectedCB = []
		l = 18
		for i in ['Digits', 'Uppercase', 'Lowercase', 'Punctuation']:
			i = ' ' * (l - len(i)) + i
			var = Tkinter.IntVar()
			var.set(1)
			Tkinter.Checkbutton(frame, text=i, variable=var).pack(side='top', expand='yes', fill='both')
			self.selectedCB.append(var)
		var.set(0)
		return

Window(className=" Password Generator").mainloop()
