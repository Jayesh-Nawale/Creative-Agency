import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import sqlite3

window=tk.Tk()
window.title("Client and Employee Details") 

frame=tk.Frame(window, bg="#DFB5FF")
frame.pack()

def submit():
    ClientName = client_name_entry.get()
    if ClientName:
        CompanyName = company_name_entry.get()
        EmployeeName = employee_entry.get()
        VideoEditorName = video_editor_entry.get()
        GraphicDesignerName = graphic_designer_entry.get()
        ClientWorkStatus = status_entry.get()
        
        conn = sqlite3.connect('Client_data.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Client_Data 
                (ClientName TEXT, CompanyName TEXT PRIMARY KEY, EmployeeName TEXT, VideoEditorName TEXT, GraphicDesignerName TEXT, 
                ClientWorkStatus TEXT)'''
        conn.execute(table_create_query)

        data_insert_query = '''INSERT INTO Client_Data (ClientName, CompanyName, EmployeeName, VideoeditorName, GraphicDesignerName, ClientWorkStatus) 
                VALUES (?,?,?,?,?,?)'''
        data_insert_tuple = (ClientName, CompanyName, EmployeeName, VideoEditorName, GraphicDesignerName, ClientWorkStatus)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

        client_name_entry.delete(0, END)
        company_name_entry.delete(0, END)
        employee_entry.delete(0, END)
        video_editor_entry.delete(0, END)
        graphic_designer_entry.delete(0, END)
        status_entry.delete(0, END)
        
        messagebox.showinfo(title="Success", message="Entry submitted successfully!")
    else:
        tk.messagebox.showwarning(title="Error", message="Client Name required")

    

def update(): 
    def fetch_record():
        search_id = Company_entry.get()

        conn = sqlite3.connect('Client_data.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM Client_Data WHERE CompanyName=?''', (search_id,))
        search_result = cursor.fetchone()

        conn.close()

        if search_result:
            updated_cn_entry.delete(0, tk.END)
            updated_cn_entry.insert(0, search_result[0])
            updated_emp_entry.delete(0, tk.END)
            updated_emp_entry.insert(0, search_result[2])
            updated_vid_entry.delete(0, tk.END)
            updated_vid_entry.insert(0, search_result[3])
            updated_graphic_entry.delete(0, tk.END)
            updated_graphic_entry.insert(0, search_result[4])
            updated_work_entry.delete(0, tk.END)
            updated_work_entry.insert(0, search_result[5])
        else:
            tk.messagebox.showwarning(title="Error", message="No record found!") 

    def updaterecord():
        Clname = updated_cn_entry.get()
        Emp = updated_emp_entry.get()
        Video = updated_vid_entry.get()
        Graphic = updated_graphic_entry.get()
        Clientstaus = updated_work_entry.get()
        Companyname = Company_entry.get()
        conn= sqlite3.connect("Client_data.db")
        cursor= conn.cursor()
            
        cursor.execute('''UPDATE Client_Data SET ClientName=?, EmployeeName=?, VideoEditorName=?, GraphicDesignerName=?, CLientWorkStatus=?
                      WHERE CompanyName=?''',(Clname, Emp, Video, Graphic, Clientstaus, Companyname))
        conn.commit()
        conn.close()
        addroot.destroy()

    addroot = Toplevel(master=window)
    addroot.grab_set()
    addroot.geometry("380x480")
    addroot.title("Update record")

    Company_label= tk.Label(addroot, text="Enter Company Name:", padx=20, pady=10)
    Company_label.grid(row=0, column=2)
    Company_entry= Entry(addroot)
    Company_entry.grid(row=1, column=2)

    btn_fetch = Button(addroot, text="Fetch Record", command=fetch_record)
    btn_fetch.grid(row=3,column=2, padx=20, pady= 10)

    updated_cn_label=tk.Label(addroot, text="Updated Client Name:")
    updated_cn_label.grid(row=5,column=2, padx=20, pady=10)
    updated_cn_entry = Entry(addroot)
    updated_cn_entry.grid(row=5, column=3,padx=20, pady=10)
            
    updated_emp_label=tk.Label(addroot, text="Updated Employee Name:")
    updated_emp_label.grid(row=7,column=2,padx=20, pady=10)
    updated_emp_entry = Entry(addroot)
    updated_emp_entry.grid(row=7,column=3,padx=20, pady=10)
            
    updated_vid_label=tk.Label(addroot, text="Updated Video Editor:")
    updated_vid_label.grid(row=8,column=2,padx=20, pady=10)
    updated_vid_entry = Entry(addroot)
    updated_vid_entry.grid(row=8,column=3,padx=20, pady=10)

    updated_graphic_label=tk.Label(addroot, text="Updated Graphic Designer:")
    updated_graphic_label.grid(row=9,column=2,padx=20, pady=10)
    updated_graphic_entry = Entry(addroot)
    updated_graphic_entry.grid(row=9,column=3,padx=20, pady=10)
            
    updated_work_label=tk.Label(addroot, text="Updated Client Work Status:")
    updated_work_label.grid(row=10,column=2,padx=20, pady=10)
    updated_work_entry = Entry(addroot)
    updated_work_entry.grid(row=10,column=3,padx=20, pady=10)
            
        
    btn = tk.Button(addroot, text="Update", command=updaterecord)
    btn.grid(row=13,column=2,padx=21, pady=10)
    




def delete():
    def deleterecord():
        Compname = CompanyName.get()

        conn = sqlite3.connect('Client_data.db')
        cursor = conn.cursor()
        
        cursor.execute('''DELETE FROM Client_Data WHERE CompanyName=?''', (Compname,))
        conn.commit()
        conn.close()
        
        popup=Toplevel(master=addroot)
        popup.grab_set()
        popup.geometry("100x100")
        popup.config()
        tk.Label(popup, text="Client Data deleted Successfully", padx=20, pady=10).pack(anchor="center")
        
        addroot.destroy()
        
    addroot = Toplevel(master=window)
    addroot.grab_set()
    addroot.geometry("470x200")
    addroot.title("Delete record")
    addroot.config()

    tk.Label(addroot, text="Enter Company Name:", padx=20, pady=10).pack()
    CompanyName = tk.Entry(addroot)
    CompanyName.pack(padx=20, pady=10)

    btn = tk.Button(addroot, text="Delete", command=deleterecord)
    btn.pack(padx=20, pady=10)
    
def clear_fields():
    clientname_entry.delete(0, END)
    companyname_entry.delete(0, END)
    employee_entry.delete(0, END)
    video_editor_entry.delete(0, END)
    graphic_designer_entry.delete(0, END)
    clientworkstatus_entry.delete(0, END)

def display_search_results(results):
        results_window=Toplevel(master=window)
        results_window.geometry("600x400")
        treeview = ttk.Treeview(results_window)
        treeview.pack()

        treeview["columns"] = ( "Client Name", "Company Name", "Employee Name", "Video Editor", "Graphic Designer", "Work Status")

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("Client Name", anchor=E, width=70)
        treeview.column("Company Name", anchor=E, width=100)
        treeview.column("Employee Name", anchor=E, width=70)
        treeview.column("Video Editor", anchor=E, width=70)
        treeview.column("Graphic Designer", anchor=E, width=70)
        treeview.column("Work Status", anchor=E, width=70)

        treeview.heading("#0", text="", anchor=W)
        treeview.heading("Client Name", text="Company Name", anchor=W)
        treeview.heading("Company Name", text="Client Name", anchor=W)
        treeview.heading("Employee Name", text="Employee Name", anchor=W)
        treeview.heading("Video Editor", text="Video Editor", anchor=W)
        treeview.heading("Graphic Designer", text="Graphic Designer", anchor=W)
        treeview.heading("Work Status", text="Work Status", anchor=W)

        for row in results:
            treeview.insert("", END, values=row)

def display():
    conn= sqlite3.connect('Client_data.db')
    cursor= conn.cursor()

    results_window=Toplevel(master=window)
    treeview = ttk.Treeview(results_window)
    treeview.pack()

    treeview["columns"] = ( "Client Name", "Company Name", "Employee Name", "Video Editor", "Graphic Designer", "Work Status")

    cursor.execute("SELECT * from Client_Data")
    data= cursor.fetchall()

    treeview.column("#0", width=0, stretch=NO)
    treeview.column("Client Name", anchor=E, width=70)
    treeview.column("Company Name", anchor=E, width=100)
    treeview.column("Employee Name", anchor=E, width=70)
    treeview.column("Video Editor", anchor=E, width=70)
    treeview.column("Graphic Designer", anchor=E, width=70)
    treeview.column("Work Status", anchor=E, width=70)

    treeview.heading("#0", text="", anchor=W)
    treeview.heading("Client Name", text="Company Name", anchor=W)
    treeview.heading("Company Name", text="Client Name", anchor=W)
    treeview.heading("Employee Name", text="Employee Name", anchor=W)
    treeview.heading("Video Editor", text="Video Editor", anchor=W)
    treeview.heading("Graphic Designer", text="Graphic Designer", anchor=W)
    treeview.heading("Work Status", text="Work Status", anchor=W)

    for row in data:
        treeview.insert("", END, values=row)


action_frame=tk.LabelFrame(frame, bg="#DFB5FF",text="Actions")
action_frame.grid(row=0, column=0)
btn_update = Button(action_frame, text="Update", command=update)
btn_update.grid(row=0, column=0,padx=20, pady=10)
btn_delete = Button(action_frame, text="Delete", command=delete)
btn_delete.grid(row=0, column=2,padx=20, pady=10)
btn_display = Button(action_frame, text="Display", command=display)
btn_display.grid(row=0, column=3,padx=20, pady=10)

user_info_frame=tk.LabelFrame(frame, bg="#DFB5FF", text="Client Information")
user_info_frame.grid(row=1, column=0, padx=20, pady=10)

client_name_label=tk.Label(user_info_frame, text="Client Name")
client_name_label.grid(row=1, column=0)
company_name_label=tk.Label(user_info_frame, text="Company Name")
company_name_label.grid(row=1, column=1)

client_name_entry=tk.Entry(user_info_frame)
client_name_entry.grid(row=2, column=0)
company_name_entry=tk.Entry(user_info_frame)
company_name_entry.grid(row=2, column=1)

employee_label=tk.Label(user_info_frame, text="Employee Name")
employee_label.grid(row=3, column=0)
employee_entry=tk.Entry(user_info_frame)
employee_entry.grid(row=4, column=0)

video_editor_label=tk.Label(user_info_frame, text="Video Editor Assigned")
video_editor_label.grid(row=3, column=1)
video_editor_entry=tk.Entry(user_info_frame)
video_editor_entry.grid(row=4, column=1)

graphic_designer_label=tk.Label(user_info_frame, text="Graphic Designer Assigned")
graphic_designer_label.grid(row=5, column=0)
graphic_designer_entry=tk.Entry(user_info_frame)
graphic_designer_entry.grid(row=6, column=0)

status_label=tk.Label(user_info_frame, text="Client Work Status")
status_label.grid(row=5, column=1)
status_entry=tk.Entry(user_info_frame)
status_entry.grid(row=6, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=3, pady=5)


button=tk.Button(frame, text="Submit", command=submit)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

display_label = Label(window, text="")
display_label.pack()

window.mainloop()