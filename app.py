# Import required libraries
from tkinter import *
import cyberpi as cpi

# Thai text for tkinter label
# Due the fact that mBlock5 IDE hard to edit Thai alphabet
text1 = 'ค่าแรงสั่นสะเทือนที่วัดได้'
text2 = 'วัดค่าแรงสั่นสะเทือนได้'
text3 = 'หยุดการรับค่าแรงสั่นสะเทือน'
text4 = 'เริ่มการวัดค่าใหม่อีกครั้ง'


# Callback function when click tkinter button (start button)
def start():
    # Call " set_shake_val" function
    set_shake_val()
    # Loop this function every 1 sec (Call start function after 1000 millisecond)
    task_.after(1000, start)


# Callback function when click tkinter button (stop button)
def stop():
    # Destroy this widget will stop the start function loop
    task_.destroy()
    # Call "reset_shake_val" function
    reset_shake_val()


# This function called inside "start" function
def set_shake_val():
    # Get shake values from CyberPi
    shake_val = cpi.get_shakeval()

    # Replace text widget with Thai text and shake values from CyberPi
    # Config start button
    start_btn.config(text='{} {}%'.format(text1, shake_val))
    # Config status label and change background color to green
    status_label.config(text='{} {}%'.format(text2, shake_val), bg='lightgreen')
    # Call 3 function and passing shake values as parameter
    set_shake_level_color(shake_val)
    set_shake_level_LED(shake_val)
    set_shake_val_display(shake_val)


# This function called inside "stop" function
def reset_shake_val():
    # Replace text widget with Thai text and shake values from CyberPi
    # Config start button
    start_btn.config(text='{}'.format(text4))
    # Config status label and change background color to red
    status_label.config(text='{}'.format(text3), bg='red')
    # Call 3 function and passing shake values as parameter
    reset_shake_level_color()
    reset_shake_level_LED()
    reset_shake_val_display()


# Check the shake values then config color label to indicate danger level
def set_shake_level_color(shake_val):
    if shake_val >= 80:
        show_led1.configure(bg='lightgreen')
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold')
        show_led4.configure(bg='orange')
        show_led5.configure(bg='Red')
    elif 60 < shake_val < 80:
        show_led1.configure(bg='lightgreen')
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold')
        show_led4.configure(bg='orange')
        show_led5.configure(bg='black')
    elif 40 <= shake_val < 60:
        show_led1.configure(bg='lightgreen')
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold')
        show_led4.configure(bg='black')
        show_led5.configure(bg='black')
    elif 20 <= shake_val < 40:
        show_led1.configure(bg='lightgreen')
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='black')
        show_led4.configure(bg='black')
        show_led5.configure(bg='black')
    elif 0 < shake_val < 20:
        show_led1.configure(bg='lightgreen')
        show_led2.configure(bg='black')
        show_led3.configure(bg='black')
        show_led4.configure(bg='black')
        show_led5.configure(bg='black')
    # Reset the color label by calling "reset_shake_level_color" function
    # When shake values is 0 or less (in case CyberPi can't get shake values)
    elif shake_val <= 0:
        reset_shake_level_color()


# Set all color label to black
def reset_shake_level_color():
    show_led1.configure(bg='black')
    show_led2.configure(bg='black')
    show_led3.configure(bg='black')
    show_led4.configure(bg='black')
    show_led5.configure(bg='black')


# Turn on/off CyberPi LED  by passing shake values
def set_shake_level_LED(shake_val):
    if shake_val >= 80:
        cpi.led.on('c', id=1)
        cpi.led.on('g', id=2)
        cpi.led.on('y', id=3)
        cpi.led.on('o', id=4)
        cpi.led.on('r', id=5)
    elif 60 < shake_val < 80:
        cpi.led.on('c', id=1)
        cpi.led.on('g', id=2)
        cpi.led.on('y', id=3)
        cpi.led.on('o', id=4)
        cpi.led.off(id=5)
    elif 40 <= shake_val < 60:
        cpi.led.on('c', id=1)
        cpi.led.on('g', id=2)
        cpi.led.on('y', id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif 20 <= shake_val < 40:
        cpi.led.on('c', id=1)
        cpi.led.on('g', id=2)
        cpi.led.off(id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif 0 < shake_val < 20:
        cpi.led.on('c', id=1)
        cpi.led.off(id=2)
        cpi.led.off(id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif shake_val <= 0:
        reset_shake_level_LED()


# Turn off all CyberPi LED
def reset_shake_level_LED():
    cpi.led.off(id='all')


# Display shake values in CyberPi OLED
def set_shake_val_display(shake_val):
    # Clear previous text before insert values
    cpi.console.clear()
    # Print shake values one line
    cpi.console.println('Shake {} %'.format(shake_val))


# Display text to CyberPi OLED
def reset_shake_val_display():
    # Clear previous text before insert text
    cpi.console.clear()
    # Print message "STOP Detection" to CyberPi OLED
    cpi.console.println('Stop Detection')


# Create Tkinter GUI
# Crate root window
app = Tk()
# Change window title
app.title("โปรแกรมวัดแรงสั่นสะเทือน")
# Set font inside window
app.option_add("*font", "PSL-omyim 10")

# Add Tkinter image
photo1 = PhotoImage(file="mi.png")
photo_stu = PhotoImage(file="stu.png")
imake = PhotoImage(file="imake.png")
_cyberpi = PhotoImage(file="cyberpi.png")

# Create Title Label and display
header = Label(text="Micropython CyperPi LED Gyro Project_1", image=photo1, compound=LEFT, bg='yellow',
               font="PSL-omyim 20")
header.grid(row=0, columnspan=8, sticky=NSEW)

# Left image and label
stu_pic = Label(image=photo_stu)
stu_pic.grid(row=1, column=0, rowspan=3)
stu_name = Label(text="Nuuimm")
stu_name.grid(row=4, column=0)

# Start button
start_btn = Button(text="เริ่มต้นการทำงาน", fg='green', command=start)
start_btn.grid(row=1, column=1, columnspan=2, sticky=NSEW)
# Stop button 
stop_btn = Button(text="สิ้นสุดการทำงาน", fg='red', command=stop)
stop_btn.grid(row=1, column=3, columnspan=2, sticky=NSEW)

# Status label
status_label = Label(text="สถานะการวัดการสั่นสะเทือน", bg='lightblue')
status_label.grid(row=2, column=1, columnspan=4, sticky=NSEW)

# CyberPi image and label
cyberpi_picture = Label(image=_cyberpi)
cyberpi_picture.grid(row=1, column=5, rowspan=2)
cyberpi_text = Label(text="CyberPi")
cyberpi_text.grid(row=3, column=5)

# Danger indicator (Color Label)
led1 = Label(text='RBG LED Level 1', bg='lightgreen', width=10)
led1.grid(row=4, column=1, sticky=NSEW)

led2 = Label(text='RBG LED Level 2', bg='yellow', width=10)
led2.grid(row=4, column=2, sticky=NSEW)

led3 = Label(text='RBG LED Level 3', bg='gold', width=10)
led3.grid(row=4, column=3, sticky=NSEW)

led4 = Label(text='RBG LED Level 4', bg='orange', width=10)
led4.grid(row=4, column=4, sticky=NSEW)

led5 = Label(text='RBG LED Level 5', bg='red', width=10)
led5.grid(row=4, column=5, sticky=NSEW)

# Danger indicator (Text Label)
show_led1 = Label(text='0-20', bg='black', width=15)
show_led1.grid(row=5, column=1, sticky=NSEW, rowspan=2)

show_led2 = Label(text='20-40', bg='black', width=15)
show_led2.grid(row=5, column=2, sticky=NSEW, rowspan=2)

show_led3 = Label(text='40-60', bg='black', width=15)
show_led3.grid(row=5, column=3, sticky=NSEW, rowspan=2)

show_led4 = Label(text='60-80', bg='black', width=15)
show_led4.grid(row=5, column=4, sticky=NSEW, rowspan=2)

show_led5 = Label(text='80-100', bg='black', width=15)
show_led5.grid(row=5, column=5, sticky=NSEW, rowspan=2)

# iMake image
logo_pic = Label(image=imake)
logo_pic.grid(row=6, column=0, sticky=SW)

# this widget for loop event or get destroy in order to stop the loop 
# no need to display 
task_ = Label()

# Loop this GUI forever
app.mainloop()
