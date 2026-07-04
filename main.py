import customtkinter as ctk
from tkinter import messagebox
from CTkListbox import CTkListbox

# ----------------------------------------------------
# Appearance
# ----------------------------------------------------
ctk.set_appearance_mode("Light")       
ctk.set_default_color_theme("blue")

# ----------------------------------------------------
# Window
# ----------------------------------------------------
app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("700x650")
app.resizable(False, False)

tasks = []

# ----------------------------------------------------
# Functions
# ----------------------------------------------------
def update_list():
    task_list.delete("ALL")

    for task in tasks:
        icon = "✅" if task["completed"] else "⬜"
        task_list.insert("END", f"{icon} {task['task']}")


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    update_list()
    entry.delete(0, "end")


def complete_task():
    selected = task_list.curselection()

    if selected is None:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    tasks[selected]["completed"] = True
    update_list()


def delete_task():
    selected = task_list.curselection()

    if selected is None:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    del tasks[selected]
    update_list()


# ----------------------------------------------------
# Layout
# ----------------------------------------------------
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

# ---------------- Header ----------------
header = ctk.CTkFrame(app, fg_color="transparent")
header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,10))

title = ctk.CTkLabel(
    header,
    text="📝 TO-DO LIST",
    font=("Segoe UI", 30, "bold")
)
title.pack()

subtitle = ctk.CTkLabel(
    header,
    text="Stay organized. Stay productive.",
    font=("Segoe UI", 14)
)
subtitle.pack()

# ---------------- Input ----------------
input_frame = ctk.CTkFrame(app)
input_frame.grid(row=1, column=0, sticky="ew", padx=20)

input_frame.grid_columnconfigure(0, weight=1)

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Enter a new task...",
    height=40,
    font=("Segoe UI", 14)
)

entry.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky="ew"
)

entry.bind("<Return>", lambda e: add_task())

add_btn = ctk.CTkButton(
    input_frame,
    text="Add Task",
    width=120,
    height=40,
    command=add_task
)

add_btn.grid(
    row=0,
    column=1,
    padx=(0,15),
    pady=15
)

# ---------------- List ----------------
list_frame = ctk.CTkFrame(app, corner_radius=15)
list_frame.grid(
    row=2,
    column=0,
    padx=20,
    pady=20,
    sticky="nsew"
)

list_frame.grid_rowconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1)

task_list = CTkListbox(
    list_frame,
    font=("Segoe UI", 14),
    hover_color="#2563EB",
    highlight_color="#1D4ED8"
)

task_list.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
)

# ---------------- Buttons ----------------
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=20,
    pady=(0,20)
)

button_frame.grid_columnconfigure((0,1), weight=1)

complete_btn = ctk.CTkButton(
    button_frame,
    text="✔ Complete",
    fg_color="#16A34A",
    hover_color="#15803D",
    height=45,
    font=("Segoe UI", 15, "bold"),
    command=complete_task
)

complete_btn.grid(
    row=0,
    column=0,
    padx=10,
    sticky="ew"
)

delete_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Delete",
    fg_color="#DC2626",
    hover_color="#B91C1C",
    height=45,
    font=("Segoe UI", 15, "bold"),
    command=delete_task
)

delete_btn.grid(
    row=0,
    column=1,
    padx=10,
    sticky="ew"
)

# ----------------------------------------------------
# Start
# ----------------------------------------------------
app.mainloop()