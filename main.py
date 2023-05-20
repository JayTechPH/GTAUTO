import pyautogui
import time
import threading
import webbrowser
import atexit
import customtkinter as ctk

loop = 0
punch_wait = 0
punch_time = 0
threads = []

def cleanup():
    cancel()
    pyautogui.keyUp("right")
    pyautogui.keyUp("left")
    pyautogui.keyUp("space")
    webbrowser.open("https://www.youtube.com/@JayTechPH")  

def stop():
    if radio_var.get() == 0:
        global loop
        loop = 0
        threads.clear()
        radio_var.set(0)

def cancel():
    global loop
    loop = 0
    threads.clear()
    radio_var.set(0)
                                                
def d_press(direction):
    if direction == "right":
        pyautogui.keyDown("right")
        time.sleep(punch_time)
        pyautogui.keyUp("right")                  
    else:
        pyautogui.keyDown("left")
        time.sleep(punch_time)
        pyautogui.keyUp("left")

    time.sleep(punch_wait)
    pyautogui.keyUp("space")

def space_press():
    pyautogui.keyDown("space")
    time.sleep(0.001)

def movement():
    image = "image.png"
    direction = "right"
    image_detected_time = 0
    delay = 15

    while loop == 1:
        if time.time() - image_detected_time >= delay:
            location = pyautogui.locateOnScreen(image, confidence=0.5)
            if location is not None:
                image_detected_time = time.time()
                pyautogui.keyUp("space")
                pyautogui.keyDown("up")
                pyautogui.keyUp("space")
                time.sleep(1)
                pyautogui.keyUp("space")
                pyautogui.keyUp("up")
                pyautogui.keyUp("space")
                if direction == "right":
                    direction = "left"
                else:
                    direction = "right"
                                                                                                                                                               
                start_movement()

            else:
                image_detected_time = 0

        d_press(direction)
        space_press()
        stop()

    time.sleep(0.1)

def stop_movement():
    if len(threads) > 1:
        global loop
        loop = 0
        threads.clear()
        radio_var.set(0)

def start_movement():
    if len(threads) < 1:
        t = threading.Thread(target=movement)
        threads.append(t)
        t.start()

def on_minimize():
    global new_button
    minimize_button.pack_forget()
    new_button = ctk.CTkButton(top_frame, text="🔼", width=20, command=on_restore)
    new_button.pack(side="right")
    app.geometry("240x30")

def on_restore():
    new_button.pack_forget()
    minimize_button.pack(side="right")
    app.geometry("240x185")

def radiobutton_event():
    global loop, punch_wait, punch_time
    selected_option = radio_var.get()

    if selected_option == 1:
        loop = 0 
        punch_wait = 0.3
        punch_time = 0.001
        loop = 1
        stop_movement()
        start_movement()
    elif selected_option == 2:
        loop = 0
        punch_wait = 0.3
        punch_time = 0.04
        loop = 1
        stop_movement()
        start_movement()
    elif selected_option == 3:
        loop = 0
        punch_wait = 0.3
        punch_time = 0.06
        loop = 1
        stop_movement()
        start_movement()

app = ctk.CTk()
app.resizable(False, False)
ctk.set_appearance_mode("dark")
app.geometry("240x185+50+50")
app.iconbitmap("icon.ico")
app.wm_attributes("-topmost", True)
app.title("Auto Farm By JayTechPH")

top_frame = ctk.CTkFrame(app)
top_frame.pack(side="top", fill="x")

minimize_button = ctk.CTkButton(top_frame, text="🔽", width=20, command=on_minimize)
minimize_button.pack(side="right")
app_name_label = ctk.CTkLabel(top_frame, text="JayTechPH Auto Farm Menu")
app_name_label.pack(side="left", padx=10)

radio_var = ctk.IntVar(value=0)

option_1 = ctk.CTkRadioButton(app, text="Chandeliers", variable=radio_var, value=1, command=radiobutton_event)
option_2 = ctk.CTkRadioButton(app, text="Laser Grids", variable=radio_var, value=2, command=radiobutton_event)
option_3 = ctk.CTkRadioButton(app, text="Grass/Pepper/Sugar", variable=radio_var, value=3, command=radiobutton_event)
cancel_button = ctk.CTkButton(app, text="Cancel", command=cancel)
text = ctk.CTkLabel(app, text="Subscribe to JayTechPH                1.0.0v", cursor="hand2")

text.place(x=5, y=160)
option_1.place(x=5, y=40)
option_2.place(x=5, y=70)
option_3.place(x=5, y=100)
cancel_button.place(x=5, y=130)

app.mainloop()
atexit.register(cleanup)
        
