from tkinter import * 
root=Tk() 
root.title("Sejal's Calculator") 
root.geometry("300x400") 
value="" 
operator="" 
x=0 
def press(num):
	global value 
	value=value+str(num) 
	data.set(value)  
def op(num): 
	global value,operator,x 
	x=int(value) 
	operator=num 
	value=value+num 
	data.set(value) 
def re(): 
	global operator,x,value 
	if(operator=="+"): 
		y=int(value.split("+")[1]) 
		z=x+y 
		value=str(z)
		data.set(value) 
	if(operator=="-"): 
		y=int(value.split("-")[1]) 
		print(y) 
		z=x-y 
		value=str(z) 
		data.set(value)
	if(operator=="*"): 
		y=int(value.split("*")[1]) 
		print(y) 
		z=x*y 
		value=str(z) 
		data.set(value)
	if(operator=="/"): 
		y=int(value.split("/")[1]) 
		if(y==0): 
			value="Error" 
			data.set(value) 
		else: 
			z=int(x/y) 
			value=str(z) 
			data.set(value) 
def cls():
	global operator,value,x 
	operator=""
	x=0
	value="" 
	data.set(value) 
data=StringVar() 
row1=Label(root,anchor=SE,textvariable=data,bg="pink",font=("verdana",20)) 
row1.pack(expand=TRUE,fill="both") 
row2=Frame(root) 
row2.pack(expand=TRUE,fill="both") 
row3=Frame(root) 
row3.pack(expand=TRUE,fill="both") 
row4=Frame(root) 
row4.pack(expand=TRUE,fill="both") 
row5=Frame(root) 
row5.pack(expand=TRUE,fill="both") 
btn1=Button(row2,text="1",border=0,font=("verdana",16),command=lambda:press(1)) 
btn1.pack(expand=TRUE,fill="both",side=LEFT) 
btn2=Button(row2,text="2",border=0,font=("verdana",16),command=lambda:press(2)) 
btn2.pack(expand=TRUE,fill="both",side=LEFT) 
btn3=Button(row2,text="3",border=0,font=("verdana",16),command=lambda:press(3))
btn3.pack(expand=TRUE,fill="both",side=LEFT) 
btn_add=Button(row2,text="+",border=0,font=("verdana",16),command=lambda:op("+")) 
btn_add.pack(expand=TRUE,fill="both",side=LEFT) 
btn4=Button(row3,text="4",border=0,font=("verdana",16),command=lambda:press(4)) 
btn4.pack(expand=TRUE,fill="both",side=LEFT) 
btn5=Button(row3,text="5",border=0,font=("verdana",16),command=lambda:press(5)) 
btn5.pack(expand=TRUE,fill="both",side=LEFT) 
btn6=Button(row3,text="6",border=0,font=("verdana",16),command=lambda:press(6)) 
btn6.pack(expand=TRUE,fill="both",side=LEFT) 
btn_sub=Button(row3,text="-",border=0,font=("verdana",16),command=lambda:op("-")) 
btn_sub.pack(expand=TRUE,fill="both",side=LEFT) 
btn7=Button(row4,text="7",border=0,font=("verdana",16),command=lambda:press(7)) 
btn7.pack(expand=TRUE,fill="both",side=LEFT) 
btn8=Button(row4,text="8",border=0,font=("verdana",16),command=lambda:press(8)) 
btn8.pack(expand=TRUE,fill="both",side=LEFT) 
btn9=Button(row4,text="9",border=0,font=("verdana",16),command=lambda:press(9)) 
btn9.pack(expand=TRUE,fill="both",side=LEFT) 
btn_mul=Button(row4,text="*",border=0,font=("verdana",16),command=lambda:op("*")) 
btn_mul.pack(expand=TRUE,fill="both",side=LEFT) 
btn_clr=Button(row5,text="CLR",border=0,font=("verdana",16),command=lambda:cls()) 
btn_clr.pack(expand=TRUE,fill="both",side=LEFT) 
btn0=Button(row5,text="0",border=0,font=("verdana",16),command=lambda:press(0)) 
btn0.pack(expand=TRUE,fill="both",side=LEFT) 
btn_equal=Button(row5,text="=",border=0,font=("verdana",16),command=lambda:re()) 
btn_equal.pack(expand=TRUE,fill="both",side=LEFT) 
btn_div=Button(row5,text="/",border=0,font=("verdana",16),command=lambda:op("/")) 
btn_div.pack(expand=TRUE,fill="both",side=LEFT) 
mainloop()
