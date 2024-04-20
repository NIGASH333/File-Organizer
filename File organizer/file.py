import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def organize_files(source_dir):
    extensions_mapping = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
        'Audios': ['.mp3', '.wav', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.msi'],
        'Scripts': ['.py', '.sh', '.bat'],
        'Others': []  # Default folder for files with unknown extensions
    }

    # Create directories if they don't exist
    for folder in extensions_mapping.keys():
        if not os.path.exists(os.path.join(source_dir, folder)):
            os.makedirs(os.path.join(source_dir, folder))

    # Iterate over files in source directory
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Find the directory to move the file to
            destination_folder = 'Others'  # Default to 'Others' if extension not found
            for folder, extensions in extensions_mapping.items():
                if file_ext in extensions:
                    destination_folder = folder
                    break

            # Move the file to the corresponding directory
            source_file_path = os.path.join(source_dir, filename)
            destination_file_path = os.path.join(source_dir, destination_folder, filename)
            shutil.move(source_file_path, destination_file_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def submit_folder():
    folder_path = folder_entry.get()
    if folder_path:
        organize_files(folder_path)
        messagebox.showinfo("Success", "Files organized successfully!")

# Create a Tkinter window
root = tk.Tk()
root.title("File Organizer")

# Load the image using Pillow
image = Image.open("D:/project/1.jpeg")

# Resize the image to the desired width and height
width = 1600  # Specify the desired width
height = 1000  # Specify the desired height
image = image.resize((width, height), Image.ANTIALIAS)

# Convert the resized image to a Tkinter-compatible format
bg_image = ImageTk.PhotoImage(image)

# Set background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a label for title
title_label = tk.Label(root, text="FILE ORGANIZER", font=("Arial", 30, "bold italic"), bg="red", fg="white")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create a label for folder location entry
folder_prompt_label = tk.Label(root, text="Enter the location of the folder:", font=("italic", 20), bg="green", fg="white")
folder_prompt_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create an entry for folder location
folder_entry = tk.Entry(root, width=50, font=("Arial", 14))
folder_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Create a button to browse for folder
browse_button = tk.Button(root, text="Browse", command=browse_folder, bg="blue", fg="white", font=("Arial", 14, "bold"), width=15)
browse_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

# Create a button to submit folder location
submit_button = tk.Button(root, text="Organize", command=submit_folder, bg="green", fg="white", font=("Arial", 14, "bold"), width=15)
submit_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
