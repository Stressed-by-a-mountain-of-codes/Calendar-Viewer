import tkinter as tk
from tkinter import StringVar
import calendar
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def show_calendar():
    try:
        month = int(month_entry.get().strip())
        year = int(year_entry.get().strip())

        if 1 <= month <= 12 and year > 0:
            cal_text = calendar.month(year, month)
            result_var.set(cal_text)
            copy_str.set(cal_text)
            current_display.set(f"Showing: {calendar.month_name[month]} {year}")
        else:
            result_var.set("❌ Enter a valid month (1-12) and year (e.g., 2025)")
            current_display.set("")
    except ValueError:
        result_var.set("❌ Month and year must be numbers")
        current_display.set("")

def speak_calendar():
    text = current_display.get()
    if text:
        speak(text)

def copy_calendar():
    app.clipboard_clear()
    app.clipboard_append(copy_str.get())
    app.update()

def toggle_dark_mode():
    style.theme_use("darkly" if style.theme.name == "flatly" else "flatly")

app = ttk.Window(themename="flatly")
app.title("📆 Calendar Viewer")
app.geometry("800x600")  # ✅ Wide and spacious
app.resizable(False, False)

style = ttk.Style()

ttk.Label(app, text="📆 Calendar Viewer", font=("Segoe UI", 24, "bold")).pack(pady=20)

input_frame = ttk.Frame(app)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Month (1-12):", font=("Segoe UI", 12)).grid(row=0, column=0, padx=10, pady=5)
month_entry = ttk.Entry(input_frame, width=10, font=("Segoe UI", 12))
month_entry.grid(row=0, column=1, padx=10)

ttk.Label(input_frame, text="Year (e.g., 2025):", font=("Segoe UI", 12)).grid(row=0, column=2, padx=10)
year_entry = ttk.Entry(input_frame, width=10, font=("Segoe UI", 12))
year_entry.grid(row=0, column=3, padx=10)

ttk.Button(app, text="📅 Show Calendar", command=show_calendar, bootstyle=SUCCESS).pack(pady=10)

current_display = StringVar()
ttk.Label(app, textvariable=current_display, font=("Segoe UI", 13)).pack()

result_var = StringVar()
copy_str = StringVar()

calendar_display = ttk.Label(app, textvariable=result_var, font=("Consolas", 13), justify="left")
calendar_display.pack(pady=15)

button_frame = ttk.Frame(app)
button_frame.pack(pady=20)

ttk.Button(button_frame, text="🔊 Speak", command=speak_calendar, bootstyle=INFO).grid(row=0, column=0, padx=15)
ttk.Button(button_frame, text="📋 Copy", command=copy_calendar, bootstyle=PRIMARY).grid(row=0, column=1, padx=15)
ttk.Button(button_frame, text="🌓 Dark Mode", command=toggle_dark_mode, bootstyle=SECONDARY).grid(row=0, column=2, padx=15)

app.mainloop()
