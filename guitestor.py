
from Tkinter import Tk
import Tkinter
import time

top = Tkinter.Tk()
class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()
        self.button = Tkinter.Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.grid(row=0, column=0)
        
        self.left_forward = Tkinter.Button(frame, text="Left Forward", command=None)
        self.left_forward.grid(row=0, column=2)
        
        self.right_forward = Tkinter.Button(frame, text="Right Forward", command=None)
        self.right_forward.grid(row=0, column=5)

        self.shoulder_1_wake = Tkinter.Button(frame, text="Shoulder 1 Min", command=None)
        self.shoulder_1_wake.grid(row=1, column=0)
        self.shoulder_1_sleep = Tkinter.Button(frame, text="Shoulder 1 Max", command=None)
        self.shoulder_1_sleep.grid(row=1, column=1)

        self.elbow_1_wake = Tkinter.Button(frame, text="Elbow 1 Down", command=None)
        self.elbow_1_wake.grid(row=1, column=2)
        self.elbow_1_sleep = Tkinter.Button(frame, text="Elbow 1 Up", command=None)
        self.elbow_1_sleep.grid(row=1, column=3)

        self.wrist_1_wake = Tkinter.Button(frame, text="Wrist 1 Down", command=None)
        self.wrist_1_wake.grid(row=1, column=4)
        self.wrist_1_sleep = Tkinter.Button(frame, text="Wrist 1 Up", command=None)
        self.wrist_1_sleep.grid(row=1, column=5)

        self.shoulder_2_wake = Tkinter.Button(frame, text="Shoulder 2 Min", command=None)
        self.shoulder_2_wake.grid(row=2, column=0)
        self.shoulder_2_sleep = Tkinter.Button(frame, text="Shoulder 2 Max", command=None)
        self.shoulder_2_sleep.grid(row=2, column=1)

        self.elbow_2_wake = Tkinter.Button(frame, text="Elbow 2 Down", command=None)
        self.elbow_2_wake.grid(row=2, column=2)
        self.elbow_2_sleep = Tkinter.Button(frame, text="Elbow 2 Up", command=None)
        self.elbow_2_sleep.grid(row=2, column=3)

        self.wrist_2_wake = Tkinter.Button(frame, text="Wrist 2 Down", command=None)
        self.wrist_2_wake.grid(row=2, column=4)
        self.wrist_2_sleep = Tkinter.Button(frame, text="Wrist 2 Up", command=None)
        self.wrist_2_sleep.grid(row=2, column=5)

        self.shoulder_3_wake = Tkinter.Button(frame, text="Shoulder 3 Min", command=None)
        self.shoulder_3_wake.grid(row=3, column=0)
        self.shoulder_3_sleep = Tkinter.Button(frame, text="Shoulder 3 Max", command=None)
        self.shoulder_3_sleep.grid(row=3, column=1)

        self.elbow_3_wake = Tkinter.Button(frame, text="Elbow 3 Down", command=None)
        self.elbow_3_wake.grid(row=3, column=2)
        self.elbow_3_sleep = Tkinter.Button(frame, text="Elbow 3 Up", command=None)
        self.elbow_3_sleep.grid(row=3, column=3)

        self.wrist_3_wake = Tkinter.Button(frame, text="Wrist 3 Down", command=None)
        self.wrist_3_wake.grid(row=3, column=4)
        self.wrist_3_sleep = Tkinter.Button(frame, text="Wrist 3 Up", command=None)
        self.wrist_3_sleep.grid(row=3, column=5)
        
        self.left_shoulder_wake = Tkinter.Button(frame, text="Left Shoulder Min", command=None)
        self.left_shoulder_wake.grid(row=4, column=0)
        self.left_shoulder_sleep = Tkinter.Button(frame, text="Left Shoulder Max", command=None)
        self.left_shoulder_sleep.grid(row=4, column=1)

        self.left_elbow_wake = Tkinter.Button(frame, text="Left Elbow Down", command=None)
        self.left_elbow_wake.grid(row=4, column=2)
        self.left_elbow_sleep = Tkinter.Button(frame, text="Left Elbow Up", command=None)
        self.left_elbow_sleep.grid(row=4, column=3)

        self.left_wrist_wake = Tkinter.Button(frame, text="Left Wrist Down", command=None)
        self.left_wrist_wake.grid(row=4, column=4)
        self.left_wrist_sleep = Tkinter.Button(frame, text="Left Wrist Up", command=None)
        self.left_wrist_sleep.grid(row=4, column=5)

        self.shoulder_4_wake = Tkinter.Button(frame, text="Shoulder 4 Min", command=None)
        self.shoulder_4_wake.grid(row=5, column=0)
        self.shoulder_4_sleep = Tkinter.Button(frame, text="Shoulder 4 Max", command=None)
        self.shoulder_4_sleep.grid(row=5, column=1)

        self.elbow_4_wake = Tkinter.Button(frame, text="Elbow 4 Down", command=None)
        self.elbow_4_wake.grid(row=5, column=2)
        self.elbow_4_sleep = Tkinter.Button(frame, text="Elbow 4 Up", command=None)
        self.elbow_4_sleep.grid(row=5, column=3)

        self.wrist_4_wake = Tkinter.Button(frame, text="Wrist 4 Down", command=None)
        self.wrist_4_wake.grid(row=5, column=4)
        self.wrist_4_sleep = Tkinter.Button(frame, text="Wrist 4 Up", command=None)
        self.wrist_4_sleep.grid(row=5, column=5)

        self.shoulder_5_wake = Tkinter.Button(frame, text="Shoulder 5 Min", command=None)
        self.shoulder_5_wake.grid(row=6, column=0)
        self.shoulder_5_sleep = Tkinter.Button(frame, text="Shoulder 5 Max", command=None)
        self.shoulder_5_sleep.grid(row=6, column=1)

        self.elbow_5_wake = Tkinter.Button(frame, text="Elbow 5 Down", command=None)
        self.elbow_5_wake.grid(row=6, column=2)
        self.elbow_5_sleep = Tkinter.Button(frame, text="Elbow 5 Up", command=None)
        self.elbow_5_sleep.grid(row=6, column=3)

        self.wrist_5_wake = Tkinter.Button(frame, text="Wrist 5 Down", command=None)
        self.wrist_5_wake.grid(row=6, column=4)
        self.wrist_5_sleep = Tkinter.Button(frame, text="Wrist 5 Up", command=None)
        self.wrist_5_sleep.grid(row=6, column=5)

        self.shoulder_6_wake = Tkinter.Button(frame, text="Shoulder 6 Min", command=None)
        self.shoulder_6_wake.grid(row=7, column=0)
        self.shoulder_6_sleep = Tkinter.Button(frame, text="Shoulder 6 Max", command=None)
        self.shoulder_6_sleep.grid(row=7, column=1)

        self.elbow_6_wake = Tkinter.Button(frame, text="Elbow 6 Down", command=None)
        self.elbow_6_wake.grid(row=7, column=2)
        self.elbow_6_sleep = Tkinter.Button(frame, text="Elbow 6 Up", command=None)
        self.elbow_6_sleep.grid(row=7, column=3)

        self.wrist_6_wake = Tkinter.Button(frame, text="Wrist 6 Down", command=None)
        self.wrist_6_wake.grid(row=7, column=4)
        self.wrist_6_sleep = Tkinter.Button(frame, text="Wrist 6 Up", command=None)
        self.wrist_6_sleep.grid(row=7, column=5)
        
        self.right_shoulder_wake = Tkinter.Button(frame, text="Right Shoulder Min", command=None)
        self.right_shoulder_wake.grid(row=8, column=0)
        self.right_shoulder_sleep = Tkinter.Button(frame, text="Right Shoulder Max", command=None)
        self.right_shoulder_sleep.grid(row=8, column=1)

        self.right_elbow_wake = Tkinter.Button(frame, text="Right Elbow Down", command=None)
        self.right_elbow_wake.grid(row=8, column=2)
        self.right_elbow_sleep = Tkinter.Button(frame, text="Right Elbow Up", command=None)
        self.right_elbow_sleep.grid(row=8, column=3)

        self.right_wrist_wake = Tkinter.Button(frame, text="Right Wrist Down", command=None)
        self.right_wrist_wake.grid(row=8, column=4)
        self.right_wrist_sleep = Tkinter.Button(frame, text="Right Wrist Up", command=None)
        self.right_wrist_sleep.grid(row=8, column=5)


app = App(top)
top.mainloop()