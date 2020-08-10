from tkinter import *
from backend import Database

database = Database()



def get_selected_row(event):
	global selected_tuple
	index=lstbox.curselection()[0]
	selected_tuple=lstbox.get(index)
	return(selected_tuple)


def viewall():
	lstbox.delete(0,END)
	row=database.view()
	for i in row:
		lstbox.insert(END, i)

def search_ent():
	lstbox.delete(0,END)
	row=database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	for i in row:
		lstbox.insert(END, i)

def add_ent():
	database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	lstbox.delete(0,END)
	lstbox.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update():
	database.update(selected_tuple [0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	lstbox.delete(0,END)
	row=database.view()
	for i in row:
		lstbox.insert(END, i)


def delete():
	database.delete(selected_tuple[0])
	lstbox.delete(0,END)
	row=database.view()
	for i in row:
		lstbox.insert(END, i)


def close():
	window.quit()

	

window =Tk()


l1 = Label(window, text ="Title")
l1.grid(row=0, column =0)

l2 = Label(window, text ="Author")
l2.grid(row=0, column =2)

l3 = Label(window, text ="Year")
l3.grid(row=1, column =0)

l4 = Label(window, text ="ISBN")
l4.grid(row=1, column =2)



title_text=StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0, column =1)

author_text=StringVar()
e2 = Entry(window, textvariable= author_text)
e2.grid(row=0, column =3)

year_text=StringVar()
e3 = Entry(window, textvariable= year_text)
e3.grid(row=1, column =1)

isbn_text=StringVar()
e4 = Entry(window, textvariable= isbn_text)
e4.grid(row=1, column =3)



b1 = Button(window, text ="View all", width=12, command=viewall)
b1.grid(row=2, column =3)

b2 = Button(window, text ="Search entry",width=12, command=search_ent)
b2.grid(row=3, column =3)

b3 = Button(window, text ="Add entry",width=12, command=add_ent)
b3.grid(row=4, column =3)

b4 = Button(window, text ="Update",width=12, command=update)
b4.grid(row=5, column =3)

b5 = Button(window, text ="Delete", width=12, command=delete)
b5.grid(row=6, column =3)

b6 = Button(window, text ="Close", width=12, command=close)
b6.grid(row=7, column =3)



lstbox = Listbox(window, height=6, width =35)
lstbox.grid(row=2, column=0, rowspan=6, columnspan=2)
lstbox.bind('<<ListboxSelect>>', get_selected_row)

sb1 =Scrollbar(window)
sb1.grid(row=2, column =2, rowspan=6)

lstbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=lstbox.yview)





window.mainloop()