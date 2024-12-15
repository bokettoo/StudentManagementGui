import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["school_management"]
collection = db["students"]

# CustomTkinter configuration
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class CRUDApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("900x700")
        
        # Configure main window grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Top header
        self.create_header()

        # Main content frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Left side - Treeview
        self.create_treeview_section()

        # Right side - CRUD Operations
        self.create_crud_section()

    def create_header(self):
        # Header frame with title and description
        header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=("gray90", "gray20"))
        header_frame.grid(row=0, column=0, sticky="ew")
        
        title_label = ctk.CTkLabel(header_frame, 
                                   text="Student Management System", 
                                   font=("Arial", 24, "bold"),
                                   text_color=("black", "white"))
        title_label.pack(pady=15, padx=20, anchor="w")

    def create_treeview_section(self):
        # Left frame for Treeview
        left_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Treeview title
        ctk.CTkLabel(left_frame, 
                     text="Student Records", 
                     font=("Arial", 16, "bold")).pack(pady=(10, 5))

        # Treeview
        self.tree = ttk.Treeview(left_frame, 
                                 columns=("Name", "Age", "Email", "Phone", "Address"), 
                                 show='headings', 
                                 style="Custom.Treeview")
        self.tree.heading("Name", text="Name", command=lambda: self.sort_column("Name", False))
        self.tree.heading("Age", text="Age", command=lambda: self.sort_column("Age", False))
        self.tree.heading("Email", text="Email", command=lambda: self.sort_column("Email", False))
        self.tree.heading("Phone", text="Phone", command=lambda: self.sort_column("Phone", False))
        self.tree.heading("Address", text="Address", command=lambda: self.sort_column("Address", False))
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Scrollbar for Treeview
        scrollbar = ctk.CTkScrollbar(left_frame, orientation="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        self.load_entries()

    def create_crud_section(self):
        # Right frame for CRUD operations
        right_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Tabbed interface for CRUD operations
        self.tabview = ctk.CTkTabview(right_frame, corner_radius=10)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        # Create tabs
        create_tab = self.tabview.add("Add")
        edit_tab = self.tabview.add("Edit")
        delete_tab = self.tabview.add("Delete")

        # Create operation widgets in each tab
        self.create_add_tab(create_tab)
        self.create_edit_tab(edit_tab)
        self.create_delete_tab(delete_tab)

    def create_add_tab(self, tab):
        # Add Entry Frame
        frame = ctk.CTkFrame(tab, corner_radius=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Add New Student", font=("Arial", 16, "bold")).pack(pady=10)

        # Name Entry
        name_label = ctk.CTkLabel(frame, text="Student Name")
        name_label.pack(pady=(10, 5))
        self.name_entry = ctk.CTkEntry(frame, placeholder_text="Enter student name")
        self.name_entry.pack(pady=5, padx=20, fill="x")

        # Age Entry
        age_label = ctk.CTkLabel(frame, text="Student Age")
        age_label.pack(pady=(10, 5))
        self.age_entry = ctk.CTkEntry(frame, placeholder_text="Enter student age")
        self.age_entry.pack(pady=5, padx=20, fill="x")

        # Email Entry
        email_label = ctk.CTkLabel(frame, text="Student Email")
        email_label.pack(pady=(10, 5))
        self.email_entry = ctk.CTkEntry(frame, placeholder_text="Enter student email")
        self.email_entry.pack(pady=5, padx=20, fill="x")

        # Phone Entry
        phone_label = ctk.CTkLabel(frame, text="Student Phone")
        phone_label.pack(pady=(10, 5))
        self.phone_entry = ctk.CTkEntry(frame, placeholder_text="Enter student phone number")
        self.phone_entry.pack(pady=5, padx=20, fill="x")

        # Address Entry
        address_label = ctk.CTkLabel(frame, text="Student Address")
        address_label.pack(pady=(10, 5))
        self.address_entry = ctk.CTkEntry(frame, placeholder_text="Enter student address")
        self.address_entry.pack(pady=5, padx=20, fill="x")

        # Add Button
        add_button = ctk.CTkButton(frame, text="Add Student", command=self.add_entry)
        add_button.pack(pady=20, padx=20, fill="x")

    def create_edit_tab(self, tab):
        # Edit Entry Frame
        frame = ctk.CTkFrame(tab, corner_radius=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Edit Student Details", font=("Arial", 16, "bold")).pack(pady=10)

        # Name Entry
        name_label = ctk.CTkLabel(frame, text="New Student Name")
        name_label.pack(pady=(10, 5))
        self.edit_name_entry = ctk.CTkEntry(frame, placeholder_text="Enter new name")
        self.edit_name_entry.pack(pady=5, padx=20, fill="x")

        # Age Entry
        age_label = ctk.CTkLabel(frame, text="New Student Age")
        age_label.pack(pady=(10, 5))
        self.edit_age_entry = ctk.CTkEntry(frame, placeholder_text="Enter new age")
        self.edit_age_entry.pack(pady=5, padx=20, fill="x")

        # Email Entry
        email_label = ctk.CTkLabel(frame, text="New Student Email")
        email_label.pack(pady=(10, 5))
        self.edit_email_entry = ctk.CTkEntry(frame, placeholder_text="Enter new email")
        self.edit_email_entry.pack(pady=5, padx=20, fill="x")

        # Phone Entry
        phone_label = ctk.CTkLabel(frame, text="New Student Phone")
        phone_label.pack(pady=(10, 5))
        self.edit_phone_entry = ctk.CTkEntry(frame, placeholder_text="Enter new phone number")
        self.edit_phone_entry.pack(pady=5, padx=20, fill="x")

        # Address Entry
        address_label = ctk.CTkLabel(frame, text="New Student Address")
        address_label.pack(pady=(10, 5))
        self.edit_address_entry = ctk.CTkEntry(frame, placeholder_text="Enter new address")
        self.edit_address_entry.pack(pady=5, padx=20, fill="x")

        # Edit Button
        edit_button = ctk.CTkButton(frame, text="Save Changes", command=self.edit_entry, state="disabled")
        edit_button.pack(pady=20, padx=20, fill="x")
        self.edit_button = edit_button

    def create_delete_tab(self, tab):
        # Delete Entry Frame
        frame = ctk.CTkFrame(tab, corner_radius=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Delete Student", font=("Arial", 16, "bold")).pack(pady=10)

        # Delete Button
        delete_button = ctk.CTkButton(frame, text="Delete Selected Student", command=self.delete_entry, state="disabled")
        delete_button.pack(pady=20, padx=20, fill="x")
        self.delete_button = delete_button

    def add_entry(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        if not name or not age.isdigit() or not email or not phone or not address:
            messagebox.showerror("Input Error", "Please enter valid data for all fields.")
            return

        try:
            collection.insert_one({"name": name, "age": int(age), "email": email, "phone": phone, "address": address})
            messagebox.showinfo("Success", "Entry added successfully.")
            self.load_entries()
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def load_entries(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            for entry in collection.find():
                self.tree.insert("", "end", iid=str(entry["_id"]), values=(entry["name"], entry["age"], entry["email"], entry["phone"], entry["address"]))
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def on_select(self, event):
        # When a row is selected, populate the edit form with that student's details
        selected_item = self.tree.selection()
        if selected_item:
            selected_id = selected_item[0]
            student = collection.find_one({"_id": ObjectId(selected_id)})
            if student:
                self.edit_name_entry.delete(0, tk.END)
                self.edit_age_entry.delete(0, tk.END)
                self.edit_email_entry.delete(0, tk.END)
                self.edit_phone_entry.delete(0, tk.END)
                self.edit_address_entry.delete(0, tk.END)
                
                self.edit_name_entry.insert(0, student["name"])
                self.edit_age_entry.insert(0, student["age"])
                self.edit_email_entry.insert(0, student["email"])
                self.edit_phone_entry.insert(0, student["phone"])
                self.edit_address_entry.insert(0, student["address"])

                self.edit_button.configure(state="normal")
                self.delete_button.configure(state="normal")

    def edit_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an entry to edit.")
            return

        selected_id = selected_item[0]
        name = self.edit_name_entry.get()
        age = self.edit_age_entry.get()
        email = self.edit_email_entry.get()
        phone = self.edit_phone_entry.get()
        address = self.edit_address_entry.get()

        if not name or not age.isdigit() or not email or not phone or not address:
            messagebox.showerror("Input Error", "Please enter valid data for all fields.")
            return

        try:
            collection.update_one(
                {"_id": ObjectId(selected_id)}, 
                {"$set": {"name": name, "age": int(age), "email": email, "phone": phone, "address": address}}
            )
            messagebox.showinfo("Success", "Entry updated successfully.")
            self.load_entries()
            self.edit_name_entry.delete(0, tk.END)
            self.edit_age_entry.delete(0, tk.END)
            self.edit_email_entry.delete(0, tk.END)
            self.edit_phone_entry.delete(0, tk.END)
            self.edit_address_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def delete_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an entry to delete.")
            return

        selected_id = selected_item[0]
        try:
            collection.delete_one({"_id": ObjectId(selected_id)})
            messagebox.showinfo("Success", "Entry deleted successfully.")
            self.load_entries()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = CRUDApp()
    app.mainloop()
