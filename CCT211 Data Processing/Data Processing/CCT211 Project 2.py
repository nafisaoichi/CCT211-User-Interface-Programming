import tkinter
import tkinter.messagebox
import csv

# File to store data
FILE_NAME = "student_record.csv"

# Function to read data from the CSV file and display it in the UI
def read_data():
    table = []
    with open(FILE_NAME, mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            table.append(line)
    for widget in display_area.winfo_children():
        widget.destroy()
    for row_num in range(len(table)):
        for column_num in range(len(table[row_num])):
            cell_value = table[row_num][column_num]
            cell_label = tkinter.Label(display_area, text=cell_value, borderwidth=1, relief="solid", padx=5, pady=5)
            cell_label.grid(row=row_num, column=column_num, sticky="nsew")

# Function to write data to the CSV file
def write_data():
    if not student_number_value.get().isdigit() or not (9 <= len(student_number_value.get()) <= 11):
        tkinter.messagebox.showerror("Input Error", "Student Number must be 9 to 11 digits.")
        return
    if not name_value.get() or not age_value.get().isdigit() or not grade_value.get().isdigit():
        tkinter.messagebox.showerror("Input Error", "Please fill in all fields with valid data.")
        return
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_number_value.get(), name_value.get(), age_value.get(),
                         years_of_study_value.get(), grade_value.get()])
    tkinter.messagebox.showinfo("Success", "Record added successfully!")
    read_data()

# Function to delete a record from the CSV file
def delete_data():
    table = []
    with open(FILE_NAME, mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            table.append(line)
    new_table = [row for row in table if row[0] != student_number_value.get()]
    if len(new_table) == len(table):
        tkinter.messagebox.showerror("Error", "Student Number not found.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_table)
    tkinter.messagebox.showinfo("Success", "Record deleted successfully!")
    read_data()

# Function to update a record in the CSV file
def update_data():
    table = []
    updated = False
    with open(FILE_NAME, mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            table.append(line)
    for row in table:
        if row[0] == student_number_value.get():
            row[1] = name_value.get() if name_value.get() else row[1]
            row[2] = age_value.get() if age_value.get() else row[2]
            row[3] = years_of_study_value.get() if years_of_study_value.get() else row[3]
            row[4] = grade_value.get() if grade_value.get() else row[4]
            updated = True
    if not updated:
        tkinter.messagebox.showerror("Error", "Student Number not found.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)
    tkinter.messagebox.showinfo("Success", "Record updated successfully!")
    read_data()

# GUI Setup
window = tkinter.Tk()
window.title("CCT211 Student Information for Fall 2024")

# Input Variables
student_number_value = tkinter.StringVar()
name_value = tkinter.StringVar()
age_value = tkinter.StringVar()
years_of_study_value = tkinter.StringVar()
grade_value = tkinter.StringVar()

# Input Fields
tkinter.Label(window, text="Student Number").grid(row=0, column=0, padx=5, pady=5)
tkinter.Entry(window, textvariable=student_number_value).grid(row=0, column=1, padx=5, pady=5)

tkinter.Label(window, text="Name").grid(row=1, column=0, padx=5, pady=5)
tkinter.Entry(window, textvariable=name_value).grid(row=1, column=1, padx=5, pady=5)

tkinter.Label(window, text="Age").grid(row=2, column=0, padx=5, pady=5)
tkinter.Entry(window, textvariable=age_value).grid(row=2, column=1, padx=5, pady=5)

tkinter.Label(window, text="Years of Study").grid(row=3, column=0, padx=5, pady=5)
years_of_study_value.set("Select Year")
tkinter.OptionMenu(window, years_of_study_value, "1", "2", "3", "4", "5+").grid(row=3, column=1, padx=5, pady=5)

tkinter.Label(window, text="Grade").grid(row=4, column=0, padx=5, pady=5)
tkinter.Entry(window, textvariable=grade_value).grid(row=4, column=1, padx=5, pady=5)

# Buttons
tkinter.Button(window, text="Add", command=write_data).grid(row=5, column=0, padx=5, pady=5)
tkinter.Button(window, text="Update", command=update_data).grid(row=5, column=1, padx=5, pady=5)
tkinter.Button(window, text="Delete", command=delete_data).grid(row=6, column=0, padx=5, pady=5)
tkinter.Button(window, text="Show Data", command=read_data).grid(row=6, column=1, padx=5, pady=5)

# Display Area for Table
display_area = tkinter.Frame(window)
display_area.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Run the Application
read_data()
window.mainloop()
