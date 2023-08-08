from tkinter import *

root = Tk()

'''def result():
	fp = open('abo.txt','w')
	fp.write(f'{name.get(),age.get()}')
	fp.close
	'''
global amount
global balance
global net_balance
balance = 5000

def res():
	with open('abo.txt','r') as f:
		f.read(f'{balance}')
		f.close()



def dep():
	with open('abo.txt','w') as f:
		f.write(f'{amount.get()}')
		f.close()


amount = IntVar()
net_balanced = IntVar()

Label(root, text= ' Enter amount').pack()

Entry(root,textvariable=amount).pack()

Button(root,text='Click',command=dep).pack()
	
'''
#global name
name = StringVar()
age = IntVar()

Label(root,text = ' Enter your name').grid(row=0)
Entry(root, textvariable = name).grid(row=0,column = 1)

Label(root, text = 'Age').grid(row=1)
Entry(root, textvariable = age).grid(row=1,column=1)

Button(root,text = 'Submit',command = result).grid()
'''

root.mainloop()