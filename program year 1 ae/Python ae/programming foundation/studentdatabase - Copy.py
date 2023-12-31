from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog

students = []

def load_data():
    students = []
    lstStudents.delete(0, END)
    filename = filedialog.askopenfilename(title= 'Open', filetypes= [("Text file", "*.txt")])
    with open(filename, "r") as f:
        for line in f.readlines():
            name, age, grade = line.strip().split(",")
            students.append((name, int(age), float(grade)))
    fill_data()

def fill_data():
    for i in range(len(students)):
        lstStudents.insert(END, students[i][0])

def lstStudent_select(event):
    current_selection = lstStudents.curselection()
    if len(current_selection) > 0:
        index = current_selection[0]
        student = students(index)
        txtName.delete(0, END)
        txtName.insert(0, student[0])
        txtAge.delete(0, END)
        txtAge.insert(0, student[1])
        txtGrade.delete(0, END)
        txtGrade.insert(0, student[2])

def btnAdd_clicked():
    name = txtName.get()
    age = int(txtAge.get())
    grade = int(txtGrade.get())
    students.append((name, age, grade))         # add to list students
    lstStudents.insert(END, name)               # add to listbox lstStudents
    msgbox.showinfo("Add Student", "Student added successfully!", parent=window, icon="info")

def is_selected(title, message):
    current_selection = lstStudents.curselection()
    if len(current_selection) == 0:  # no selection
        msgbox.showerror(title, message, parent=window, icon="error")
        return False
    return True

def btnEdit_clicked():
    if not is_selected("Edit Student", "Please select a student to edit."):
        return
    index = lstStudents.curselection()[0]
    name = txtName.get()
    age = int(txtAge.get())
    grade = int(txtGrade.get())
    students[index] = (name, age, grade)        # update list students
    lstStudents.delete(index)                   # delete from listbox lstStudents
    lstStudents.insert(index, name)             # add to listbox lstStudents
    msgbox.showinfo("Edit Student", "Student edited successfully!", parent=window, icon="info")

def btnDelete_clicked():
    if not is_selected("Delete Student", "Please select a student to delete."):
        return
    index = lstStudents.curselection()[0]
    students.pop(index)                         # delete from list students
    lstStudents.delete(index)                   # delete from listbox lstStudents
    msgbox.showinfo("Delete Student", "Student deleted successfully!", parent=window, icon="info")

def btnSave_clicked():
    filename = filedialog.asksaveasfilename(title= 'Save', filetypes= [("Text files", "*.txt")])
    with open(filename, "w") as f:
        for student in students:
            f.write("{},{},{}\n".format(student[0], student[1], student[2]))
        f.close()
    msgbox.showinfo("Save", "Data saved sucessfully", parent = window, icon = "info")


window = Tk()
window.title('Student management')
window.geometry("600x600")

lblSelectStudent = Label(window, text = "Select Student")
lblSelectStudent.grid(column= 0, row= 0, sticky= 'w',padx= 10)

lstStudents = Listbox(window, height= 8)
lstStudents.grid(column= 0, row= 1, sticky= 'w', rowspan= 4, padx= 10)
lstStudents.bind('<<ListboxSelect>>', lstStudent_select)

lblName = Label(window, text= 'Name')
lblName.grid(column= 1, row= 1, sticky= 'w', padx= 10)

txtName = Entry(window, width= 20)
txtName.grid(column= 2, row= 1, sticky= 'w', padx= 10, columnspan= 3)

lblAge = Label(window, text= 'Age')
lblAge.grid(column= 1, row= 2, sticky= 'w', padx= 10)

txtAge = Entry(window, width= 20)
txtAge.grid(column=2, row= 2, sticky= 'w', padx= 10, columnspan= 3)

lblGrade = Label(window, text= 'Grade')
lblGrade.grid(column=1, row= 3, sticky= 'w', padx= 10)

txtGrade = Entry(window, width= 20)
txtGrade.grid(column= 2, row= 3, sticky= 'w', padx= 10, columnspan= 3)

btnAdd = Button(window, text= 'Add', command= btnAdd_clicked)
btnAdd.grid(column= 2, row= 4, sticky= 'w', padx= 3)

btnEdit = Button(window, text= 'Edit', command= btnEdit_clicked)
btnEdit.grid(column= 3, row= 4, sticky= 'w', padx= 3)

btnDelete = Button(window, text= 'Delete', command= btnDelete_clicked)
btnDelete.grid(column= 4, row= 4, sticky= 'w', padx= 3)

btnLoad = Button(window, text= 'Load', command= load_data)
btnLoad.grid(column= 0, row= 5, sticky= 'w', padx= 3, pady= 3)

btnSave = Button(window, text= 'Save', command= btnSave_clicked)
btnSave.grid(column= 0, row=6, sticky= 'w', padx= 3, pady= 3)


window.mainloop()
