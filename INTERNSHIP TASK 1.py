import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Management System")

        # Frame for contact form
        form_frame = tk.Frame(root)
        form_frame.pack(padx=10, pady=10)

        # Name input
        tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Phone input
        tk.Label(form_frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Email input
        tk.Label(form_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Address input
        tk.Label(form_frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(form_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(form_frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

        # Listbox for displaying contacts
        self.contacts_listbox = tk.Listbox(root, width=50)
        self.contacts_listbox.pack(padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone and email and address:
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            self.clear_entries()
            self.refresh_contacts_listbox()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def view_contacts(self):
        self.refresh_contacts_listbox()

    def search_contact(self):
        query = self.name_entry.get()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            contact['name'] = self.name_entry.get()
            contact['phone'] = self.phone_entry.get()
            contact['email'] = self.email_entry.get()
            contact['address'] = self.address_entry.get()
            self.clear_entries()
            self.refresh_contacts_listbox()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.refresh_contacts_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def refresh_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
