from Tkinter import *

def calculate(*args):
    try:
        n = int(input.get())
        m = bool(True)
        if n < 2:
            m = False
        if not n & 1:
            m = False
        for x in range(3, int(n**0.5)+1):
            if n % x == 0:
                m = False
        if n == 2:
            m = True
        if m == False:
            output.set("That number is Composite.")
        else:
            output.set("That number is Prime.")
    except ValueError:
        pass

root = Tk()
root.title("Prime Tester")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0,weight=1)

input = StringVar()
output = StringVar()

number_entry = Entry(mainframe, textvariable=input)
number_entry.grid(column=0, row=0, sticky=(W, E))

number_output = Label(mainframe, bg="blue", fg="white", textvariable=output)
number_output.grid(column=0, row=1, columnspan=2, sticky=(W, E))
go = Button(mainframe, text="Calculate", command=calculate)
go.grid(column=1, row=0, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1)

number_entry.focus()
root.resizable(True,False)
root.columnconfigure(0,weight=1)
root.bind('<Return>', calculate)

root.mainloop()