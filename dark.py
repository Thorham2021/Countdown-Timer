import tkinter as tk
import tkinter.messagebox
from playsound import playsound


class Application(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.configure(bg="#1c1c1c")
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        self.master.bind("<Return>", lambda x: self.test())

        self.instruction=tk.Label(self, text="Enter time in seconds", font=("Space Mono", 12), padx=10)
        self.instruction.grid(row=0, column=1, pady=5)
        self.instruction.configure(bg='#1c1c1c', fg='#f0f0f0')

        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=1, column=1)
        self.time_entry.configure(bg='#1c1c1c', fg='#f0f0f0')

        self.clock = tk.Label(self, text="00:00:00", font=("Space Mono", 20), width=10)
        self.clock.grid(row=2, column=1, sticky="WE")
        self.clock.configure(bg='#1c1c1c', fg='#f0f0f0')

        self.time_label = tk.Label(self, text="hour:min:sec", font=("Space Mono", 10), width=15)
        self.time_label.grid(row=3, column=1, sticky="N", padx=30)
        self.time_label.configure(bg='#1c1c1c', fg='#f0f0f0')

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=4, column=1, sticky='NW', pady=5, padx=20)
        self.power_button.configure(bg='#1c1c1c', fg='#f0f0f0')

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=4, column=1, sticky="NE", pady=5, padx=20)
        self.reset_button.configure(bg='#1c1c1c', fg='#f0f0f0')

    def calculate(self):
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def test(self):
        self.time = int(self.time_entry.get())
        self.clock.configure(text=self.calculate())

    def update(self):
        """Checks if valid time entered and updates the timer"""
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="TIME'S UP!")
                playsound('/home/shishir/Documents/Coding/Python/Countdown Timer/Notification.wav')
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Timer")
    root.resizable(False, False)
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
