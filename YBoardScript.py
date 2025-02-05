import tkinter as tk
from tkinter import filedialog, messagebox
#!Base()#
root = tk.Tk()
root.title("YBoardScript")
root.configure(background='#ffffb1')
root.state('zoomed')
#!Glob()#
global_label = tk.Label(root, text="!Glob()", fg='#000000')
global_label.place(x=10, y=10)
global_text = tk.Text(root, height=7, width=36)
global_text.place(x=10, y=30)
#!Add()#
additional_label = tk.Label(root, text="!Add()", fg='#000000')
additional_label.place(relx=1.0, y=10, anchor='ne')
additional_text = tk.Text(root, height=7, width=36)
additional_text.place(relx=1.0, y=30, anchor='ne')
#!Script()#
script_label = tk.Label(root, text="!Script()", fg='#000000')
script_label.place(x=640, y=330, anchor='center')
script_text = tk.Text(root, height=10, width=47)
script_text.place(x=640, y=424, anchor='center')
#!Notes()#
notes_label = tk.Label(root, text="!Notes()", fg='#000000')
notes_label.place(x=199, y=330, anchor='center')
notes_text = tk.Text(root, height=10, width=47)
notes_text.place(x=199, y=424, anchor='center')
#!Import()#
def import_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            parts = content.split("#!")
            for part in parts:
                if "Glob()" in part:
                    global_text.delete("1.0", tk.END)
                    global_text.insert(tk.END, part.split("\n", 1)[1].strip())
                elif "Add()" in part:
                    additional_text.delete("1.0", tk.END)
                    additional_text.insert(tk.END, part.split("\n", 1)[1].strip())
                elif "Script()" in part:
                    script_text.delete("1.0", tk.END)
                    script_text.insert(tk.END, part.split("\n", 1)[1].strip())
                elif "Notes()" in part:
                    notes_text.delete("1.0", tk.END)
                    notes_text.insert(tk.END, part.split("\n", 1)[1].strip())
        messagebox.showinfo("Yes!", "The information was successfully imported!")
import_button = tk.Button(root, text="Import from .txt file", command=import_text)
import_button.place(relx=0.5, y=520, anchor='center')
#!Export()#
def export_text():
    glob_content = global_text.get("1.0", tk.END).strip()
    add_content = additional_text.get("1.0", tk.END).strip()
    script_content = script_text.get("1.0", tk.END).strip()
    notes_content = notes_text.get("1.0", tk.END).strip()
    export_content = f"#!Glob()#\n{glob_content}\n#!Add()#\n{add_content}\n#!Script()#\n{script_content}\n#!Notes()#\n{notes_content}"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(export_content)
        messagebox.showinfo("Yes!", "The information was successfully exported!")
export_button = tk.Button(root, text="Export as .txt file", command=export_text)
export_button.place(relx=0.5, y=550, anchor='center')
#!Start()!
root.mainloop()
