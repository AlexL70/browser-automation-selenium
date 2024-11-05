import tkinter as tk
import os
from main import WebAutomation


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Web Automation GUI')
        # Login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)
        tk.Label(self.login_frame, text='Username:').grid(
            row=0, column=0, sticky='w')
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, sticky='ew')
        tk.Label(self.login_frame, text='Password:').grid(
            row=1, column=0, sticky='w')
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky='ew')
        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)
        tk.Label(self.form_frame, text='Full Name:').grid(
            row=0, column=0, sticky='w')
        self.fullname_entry = tk.Entry(self.form_frame)
        self.fullname_entry.grid(row=0, column=1, sticky='ew')
        tk.Label(self.form_frame, text='Email:').grid(
            row=1, column=0, sticky='w')
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=1, column=1, sticky='ew')
        tk.Label(self.form_frame, text='Current Address:').grid(
            row=2, column=0, sticky='w')
        self.current_address_entry = tk.Entry(self.form_frame)
        self.current_address_entry.grid(row=2, column=1, sticky='ew')
        tk.Label(self.form_frame, text='Permanent Address:').grid(
            row=3, column=0, sticky='w')
        self.permanent_address_entry = tk.Entry(self.form_frame)
        self.permanent_address_entry.grid(row=3, column=1, sticky='ew')
        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)
        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(
            row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(
            row=0, column=1, padx=5)

    def submit_data(self):
        self.wa = WebAutomation(os.getcwd())
        self.wa.login(self.username_entry.get(), self.password_entry.get())
        self.wa.fill_form(self.fullname_entry.get(), self.email_entry.get(),
                          self.current_address_entry.get(), self.permanent_address_entry.get())
        self.wa.download_file()

    def close_browser(self):
        self.wa.close_browser()


app = App()
app.root.mainloop()
