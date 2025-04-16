from tkinter import *
from tkinter.ttk import *

window=Tk()
window.title('Mathematical table generator')

title=Label(window, text = "Mathematical table")
caption=Label(window, text = "Number and Range:")

title.grid(row = 0, column = 0,columnspan = 3, pady=25)
caption.grid(column = 0,row = 1,padx=10)

theNum = IntVar()
numbers=Combobox(window,textvariable = theNum,width=5)
numbers['values'] = tuple(range(101))

endVal = IntVar()
r10=Radiobutton(window,text="10",variable=endVal,value=10)
r20=Radiobutton(window,text="20",variable=endVal,value=20)
r30=Radiobutton(window,text="30",variable=endVal,value=30)
endVal.set(10)

numbers.grid(column = 1, row = 1)
r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)

def generateMulTable():
    tables=""
    for i in range(1,endVal.get()+1):
        tables+=str(theNum.get())+"   X   "+str(i)+"   =   "+str(theNum.get()*i)+"\n"
    table.configure(text=tables)

generateButton=Button(window,text="Generate",command=generateMulTable)
table=Label(window,anchor="center")

generateButton.grid(row=4,column=1)
table.grid(row=5,column=1, pady = 25)

window.mainloop()
