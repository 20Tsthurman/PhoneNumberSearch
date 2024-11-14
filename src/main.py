import os
from tkinter import *
from tkinter import messagebox, ttk
from .phone_converter import PhoneNumberConverter

def create_ui():
   root = Tk()
   root.title("Phone Number Word Converter")
   root.geometry("500x400")
   root.configure(bg='#f0f0f0')  # Light gray background

   # Setup converter and load dictionary
   converter = PhoneNumberConverter()
   current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   dictionary_path = os.path.join(current_dir, "data", "dictionary.txt")
   
   try:
       converter.load_words(dictionary_path)
   except Exception as e:
       messagebox.showerror("Error", f"Dictionary load failed: {e}")
       root.destroy()
       return

   # Create main frame
   main_frame = Frame(root, bg='#f0f0f0')
   main_frame.pack(expand=True, padx=20, pady=20)

   # Title and input section
   Label(main_frame, text="Phone Number to Words", 
         font=('Arial', 16, 'bold'), bg='#f0f0f0').pack(pady=10)
   
   Label(main_frame, text="Enter a 10-digit phone number:", 
         font=('Arial', 12), bg='#f0f0f0').pack()

   # Phone number entry with formatting
   number_var = StringVar()
   number_entry = Entry(main_frame, textvariable=number_var, 
                       font=('Arial', 14), width=15,
                       justify='center')
   number_entry.pack(pady=10)

   # Results display
   results_frame = Frame(main_frame, bg='#f0f0f0')
   results_frame.pack(fill='both', expand=True, pady=10)
   
   results_text = Text(results_frame, height=10, width=40,
                      font=('Arial', 11), wrap=WORD,
                      bg='white', relief='solid')
   results_text.pack(side=LEFT, expand=True)
   
   # Add scrollbar to results
   scrollbar = ttk.Scrollbar(results_frame, orient='vertical', 
                            command=results_text.yview)
   scrollbar.pack(side=RIGHT, fill='y')
   results_text.configure(yscrollcommand=scrollbar.set)

   def convert_number():
       # Clear previous results
       results_text.delete(1.0, END)
       
       number = number_var.get().strip()
       if not number.isdigit() or len(number) != 10:
           messagebox.showerror("Invalid Input", 
                              "Please enter exactly 10 digits")
           return
           
       # Get and display results
       results = converter.convert_number(number)
       if results:
           results_text.insert(END, "Possible word representations:\n\n")
           for result in results:
               results_text.insert(END, f"{result}\n")
       else:
           results_text.insert(END, "No word representations found.")

   # Convert button with hover effect
   convert_btn = Button(main_frame, text="Convert", command=convert_number,
                       font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white',
                       activebackground='#45a049', width=15)
   convert_btn.pack(pady=15)

   root.mainloop()

if __name__ == "__main__":
   create_ui()