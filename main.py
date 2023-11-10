import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import threading
import time

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        root.geometry("710x400")

        # Load and resize the image to 200x200 pixels
        image = tk.PhotoImage(file="clock.png").subsample(3)  # Replace with the actual path to your image
        image_label = ttk.Label(root, image=image)
        image_label.image = image  # To prevent the image from being garbage collected
        image_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Set alarm label
        self.title = ttk.Label(root, text="Alarm Clock", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.label = ttk.Label(root, text="Enter Alarm Time (24-hour format):", font=("Helvetica", 12))
        self.label.pack(pady=40)

        # Entry for alarm time
        self.entry = ttk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        # Set alarm button
        self.button = ttk.Button(root, text="Set Alarm", command=self.set_alarm, style="TButton")
        self.button.pack(pady=20)

        # Status label
        self.status_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        # Center all widgets
        for child in root.winfo_children():
            child.pack_configure(anchor='center')

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            datetime.strptime(alarm_time, "%H:%M:%S")
        except ValueError:
            self.status_label.configure(text="Invalid time format. Please use HH:MM:SS.")
            return

        self.status_label.configure(text=f"Alarm set for {alarm_time}.")
        threading.Thread(target=self.check_alarm, args=(alarm_time,), daemon=True).start()

    def check_alarm(self, alarm_time):
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            else:
                self.status_label.configure(text=f"Current time: {current_time}. Waiting for {alarm_time}.")
                time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)

    # Style for the button
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))

    root.mainloop()
