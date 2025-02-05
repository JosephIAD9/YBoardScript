import tkinter as tk
from tkinter import filedialog, messagebox
#!Base()#
root = tk.Tk()
root.title("YBoardScript")
root.configure(background='#ffffb1')
root.state('zoomed')
def move_frame(event, frame):
    x = event.x_root - frame.winfo_width() // 2
    y = event.y_root - frame.winfo_height() // 2
    if x < 0:
        x = 0
    elif x > root.winfo_width() - frame.winfo_width():
        x = root.winfo_width() - frame.winfo_width()
    if y < 0:
        y = 0
    elif y > root.winfo_height() - frame.winfo_height():
        y = root.winfo_height() - frame.winfo_height()
    frame.place(x=x, y=y)
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
#!Glob()#
glob_frame = tk.Frame(root, bg='#ffffb1', bd=2, relief='groove')
global_label = tk.Label(glob_frame, text="!Glob()", fg='#000000', bg='#ffffb1')
global_label.pack(pady=5)
global_text = tk.Text(glob_frame, height=7, width=30)
global_text.pack(pady=5)
glob_frame.place(x=1, y=1)
glob_frame.bind("<B1-Motion>", lambda event: move_frame(event, glob_frame))
#!Add()#
add_frame = tk.Frame(root, bg='#ffffb1', bd=2, relief='groove')
additional_label = tk.Label(add_frame, text="!Add()", fg='#000000', bg='#ffffb1')
additional_label.pack(pady=5)
additional_text = tk.Text(add_frame, height=7, width=30)
additional_text.pack(pady=5)
add_frame.place(x=1033, y=1)
add_frame.bind("<B1-Motion>", lambda event: move_frame(event, add_frame))
#!Script()#
scrip_frame = tk.Frame(root, bg='#ffffb1', bd=2, relief='groove')
script_label = tk.Label(scrip_frame, text="!Script()", fg='#000000', bg='#ffffb1')
script_label.pack(pady=5)
script_text = tk.Text(scrip_frame, height=7, width=30)
script_text.pack(pady=5)
scrip_frame.place(x=516.5, y=424)
scrip_frame.bind("<B1-Motion>", lambda event: move_frame(event, scrip_frame))
#!Notes()#
not_frame = tk.Frame(root, bg='#ffffb1', bd=2, relief='groove')
notes_label = tk.Label(not_frame, text="!Notes()", fg='#000000', bg='#ffffb1')
notes_label.pack(pady=5)
notes_text = tk.Text(not_frame, height=7, width=30)
notes_text.pack(pady=5)
not_frame.place(x=36, y=400)
not_frame.bind("<B1-Motion>", lambda event: move_frame(event, not_frame))
#!List#
list_frame = tk.Frame(root, bg='#ffffb1', bd=2, relief='groove')
list_label = tk.Label(list_frame, text="!List", fg='#000000', bg='#ffffb1')
list_label.pack(pady=5)
list_text = tk.Text(list_frame, height=7, width=30)
list_text.pack(pady=5)
initial_text0 = "!Glob() = G : GCeiling(Number),GWall(Number),GFloor(Number),GLight(Number),GEnter(Number),GExit(Number),GFinalExit(Number),GFinalExit(Number)."
initial_text1 = "\n!Add() : In(Number),Out(Number),HBtn(Number),FBtn(Number)."
list_text.insert(tk.END, initial_text0)
list_text.insert(tk.END, initial_text1)
list_text.config(state=tk.DISABLED)
list_frame.place(x=1030, y=483)
list_frame.bind("<B1-Motion>", lambda event: move_frame(event, list_frame))
#!Import()#
import_button = tk.Button(root, text="Import from .txt file", command=import_text)
import_button.place(relx=0.5, y=605, anchor='center')
#!Export()#
export_button = tk.Button(root, text="Export as .txt file", command=export_text)
export_button.place(relx=0.5, y=633, anchor='center')
#!Start()!
root.mainloop()
