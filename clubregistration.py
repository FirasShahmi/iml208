import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title('Student Club Registration')
root.geometry('1024x1024')
root.configure(bg='#1A1A1A')

# Data structure to store registrations
registrations = []

# Function to handle the registration submission
def register():
    full_name = full_name_entry.get()
    Matriks = Matriks_entry.get()
    faculty = faculty_entry.get()
    semester = semester_entry.get()
    phone_number = phone_number_entry.get()
    ic = ic_entry.get()
    email = email_entry.get()

    if not full_name or not email:
        messagebox.showerror("Error", "Please fill in the required fields.")
    else:
        try:
            # Convert numeric fields to float
            Matriks = float(Matriks)
            semester = float(semester)
            phone_number = float(phone_number)
            ic = float(ic)
            # Additional validations if needed

            registration = {
                "Full Name": full_name,
                "Matriks": Matriks,
                "Faculty": faculty,
                "Semester": semester,
                "Phone Number": phone_number,
                "IC": ic,
                "Email": email,
            }
            registrations.append(registration)
            update_registration_list()
            clear_fields()
            messagebox.showinfo("Registration Successful", "Thank you for registering!")

        except ValueError:
            messagebox.showerror("Error", "Invalid input for numeric fields. Please enter valid numbers.")

def clear_fields():
    full_name_entry.delete(0, tk.END)
    Matriks_entry.delete(0, tk.END)
    faculty_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    ic_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def update_registration_list():
    registration_list.delete(0, tk.END)
    for i, registration in enumerate(registrations, start=1):
        registration_list.insert(tk.END, f"Registration {i}: "
            f"Full Name: {registration['Full Name']}, Matriks: {registration['Matriks']}, "
            f"Faculty: {registration['Faculty']}, Semester: {registration['Semester']}, "
            f"Phone Number: {registration['Phone Number']}, IC: {registration['IC']}, "
            f"Email: {registration['Email']}")

def delete_registration():
    selected_index = registration_list.curselection()
    if selected_index:
        index = selected_index[0]
        registrations.pop(index)
        update_registration_list()

def edit_registration():
    selected_index = registration_list.curselection()
    if selected_index:
        index = selected_index[0]
        registration = registrations[index]
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Registration")
        edit_window.geometry('400x600')
        
        # Create and pack widgets in the edit window
        full_name_label = tk.Label(edit_window, text="Full Name:", font=("Arial", 16))
        full_name_label.pack()
        
        full_name_edit = tk.Entry(edit_window, font=("Arial", 16))
        full_name_edit.insert(0, registration["Full Name"])
        full_name_edit.pack()
        
        Matriks_label = tk.Label(edit_window, text="Matriks:", font=("Arial", 16))
        Matriks_label.pack()
        
        Matriks_edit = tk.Entry(edit_window, font=("Arial", 16))
        Matriks_edit.insert(0, registration["Matriks"])
        Matriks_edit.pack()
        
        faculty_label = tk.Label(edit_window, text="Faculty:", font=("Arial", 16))
        faculty_label.pack()
        
        faculty_edit = tk.Entry(edit_window, font=("Arial", 16))
        faculty_edit.insert(0, registration["Faculty"])
        faculty_edit.pack()
        
        semester_label = tk.Label(edit_window, text="Semester:", font=("Arial", 16))
        semester_label.pack()
        
        semester_edit = tk.Entry(edit_window, font=("Arial", 16))
        semester_edit.insert(0, registration["Semester"])
        semester_edit.pack()
        
        phone_number_label = tk.Label(edit_window, text="Phone Number:", font=("Arial", 16))
        phone_number_label.pack()
        
        phone_number_edit = tk.Entry(edit_window, font=("Arial", 16))
        phone_number_edit.insert(0, registration["Phone Number"])
        phone_number_edit.pack()
        
        ic_label = tk.Label(edit_window, text="IC:", font=("Arial", 16))
        ic_label.pack()
        
        ic_edit = tk.Entry(edit_window, font=("Arial", 16))
        ic_edit.insert(0, registration["IC"])
        ic_edit.pack()
        
        email_label = tk.Label(edit_window, text="Email:", font=("Arial", 16))
        email_label.pack()
        
        email_edit = tk.Entry(edit_window, font=("Arial", 16))
        email_edit.insert(0, registration["Email"])
        email_edit.pack()
        
        def save_changes():
            registration["Full Name"] = full_name_edit.get()
            registration["Matriks"] = Matriks_edit.get()
            registration["Faculty"] = faculty_edit.get()
            registration["Semester"] = semester_edit.get()
            registration["Phone Number"] = phone_number_edit.get()
            registration["IC"] = ic_edit.get()
            registration["Email"] = email_edit.get()
            edit_window.destroy()
            update_registration_list()
        
        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, font=("Arial", 16))
        save_button.pack()

frame = tk.Frame(bg='#1E1E1E')

# Create and pack widgets
title_label = tk.Label(root, text="Student Club Registration:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 30))
title_label.pack()

full_name_label = tk.Label(root, text="Full Name:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
full_name_label.pack()

full_name_entry = tk.Entry(root, font=("Arial", 16))
full_name_entry.pack()

Matriks_label = tk.Label(root, text="Matriks:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
Matriks_label.pack()

Matriks_entry = tk.Entry(root, font=("Arial", 16))
Matriks_entry.pack()

faculty_label = tk.Label(root, text="Faculty:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
faculty_label.pack()

faculty_entry = tk.Entry(root, font=("Arial", 16))
faculty_entry.pack()

semester_label = tk.Label(root, text="Semester:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
semester_label.pack()

semester_entry = tk.Entry(root, font=("Arial", 16))
semester_entry.pack()

phone_number_label = tk.Label(root, text="Phone Number:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
phone_number_label.pack()

phone_number_entry = tk.Entry(root, font=("Arial", 16))
phone_number_entry.pack()

ic_label = tk.Label(root, text="IC:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
ic_label.pack()

ic_entry = tk.Entry(root, font=("Arial", 16))
ic_entry.pack()

email_label = tk.Label(root, text="Email:", bg='#1A1A1A', fg='#FF3399', font=('Arial', 16))
email_label.pack()

email_entry = tk.Entry(root, font=("Arial", 16))
email_entry.pack()

register_button = tk.Button(root, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=register)
register_button.pack()

edit_button = tk.Button(root, text="Edit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=edit_registration)
edit_button.pack()

delete_button = tk.Button(root, text="Delete", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_registration)
delete_button.pack()

registration_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), bg='#00688B', fg='#FFFFFF')
registration_list.pack()

update_registration_list()  # Initial display of registrations

frame.pack()

# Start the main loop
root.mainloop()
