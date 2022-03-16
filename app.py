from tkinter import *
import cyberpi as cpi
import time
import datetime


text1= 'ค่าแรงสั่นสะเทือนที่วัดได้'
text2= 'วัดค่าแรงสั่นสะเทือนได้'
text3= 'หยุดการรับค่าแรงสั่นสะเทือน'
text4= 'เริ่มการวัดค่าใหม่อีกครั้ง'


def start():
    set_shake_val()
    task_.after(1000,start)
    

def stop():
    task_.destroy()
    reset_shake_val()
    

def set_shake_val():
    shake_val = cpi.get_shakeval()
    start_btn.config(text='{} {}%'.format(text1,shake_val))
    status_label.config(text='{} {}%'.format(text2,shake_val),bg='lightgreen')
    set_shake_level_color(shake_val)
    set_shake_level_LED(shake_val)
    set_shake_val_display(shake_val)
    
    
def reset_shake_val():
    start_btn.config(text='{}'.format(text4))
    status_label.config(text='{}'.format(text3),bg='red')
    reset_shake_level_color()
    reset_shake_level_LED()
    reset_shake_val_display()
    
       
def set_shake_level_color(shake_val):
    if shake_val >= 80:
        show_led1.configure(bg='lightgreen')   
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold') 
        show_led4.configure(bg='orange') 
        show_led5.configure(bg='Red')
    elif shake_val > 60 and shake_val < 80:
        show_led1.configure(bg='lightgreen')   
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold') 
        show_led4.configure(bg='orange') 
        show_led5.configure(bg='black')
    elif shake_val >= 40 and shake_val < 60:
        show_led1.configure(bg='lightgreen')   
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='gold') 
        show_led4.configure(bg='black') 
        show_led5.configure(bg='black')
    elif shake_val >= 20 and shake_val < 40:
        show_led1.configure(bg='lightgreen')   
        show_led2.configure(bg='yellow')
        show_led3.configure(bg='black') 
        show_led4.configure(bg='black') 
        show_led5.configure(bg='black')
    elif shake_val > 0 and shake_val < 20:
        show_led1.configure(bg='lightgreen')   
        show_led2.configure(bg='black')
        show_led3.configure(bg='black') 
        show_led4.configure(bg='black') 
        show_led5.configure(bg='black')
    elif shake_val <= 0:
        reset_shake_level_color()
        
def reset_shake_level_color():
    show_led1.configure(bg='black')   
    show_led2.configure(bg='black')
    show_led3.configure(bg='black') 
    show_led4.configure(bg='black') 
    show_led5.configure(bg='black')
    
def set_shake_level_LED(shake_val):
    if shake_val >= 80:
        cpi.led.on('c',id=1)
        cpi.led.on('g',id=2)
        cpi.led.on('y',id=3)
        cpi.led.on('o',id=4)
        cpi.led.on('r',id=5)
    elif shake_val > 60 and shake_val < 80:
        cpi.led.on('c',id=1)
        cpi.led.on('g',id=2)
        cpi.led.on('y',id=3)
        cpi.led.on('o',id=4)
        cpi.led.off(id=5)
    elif shake_val >= 40 and shake_val < 60:
        cpi.led.on('c',id=1)
        cpi.led.on('g',id=2)
        cpi.led.on('y',id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif shake_val >= 20 and shake_val < 40:
        cpi.led.on('c',id=1)
        cpi.led.on('g',id=2)
        cpi.led.off(id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif shake_val > 0 and shake_val < 20:
        cpi.led.on('c',id=1)
        cpi.led.off(id=2)
        cpi.led.off(id=3)
        cpi.led.off(id=4)
        cpi.led.off(id=5)
    elif shake_val <= 0:
        reset_shake_level_LED()

def reset_shake_level_LED():
    cpi.led.off(id='all')
    
def set_shake_val_display(shake_val):
    cpi.console.clear()
    cpi.console.println('Shake {} %'.format(shake_val))
    
def reset_shake_val_display():
    cpi.console.clear()
    cpi.console.println('Stop Detection')

    
app = Tk()
app.title("โปรแกรมวัดแรงสั่นสะเทือน")
app.option_add("*font","PSL-omyim 10")


photo1=PhotoImage(file="mi.png")
photo_stu=PhotoImage(file="stu.png")
imake=PhotoImage(file="imake.png")
_cyberpi=PhotoImage(file="cyberpi.png")

header=Label(text="Micropython CyperPi LED Gyro Project_1",image=photo1,compound=LEFT,bg='yellow',font="PSL-omyim 20")
header.grid(row=0,columnspan=8,sticky=NSEW)

stu_pic=Label(image=photo_stu)
stu_pic.grid(row=1,column=0,rowspan=3)
stu_name=Label(text="Nuuimm")
stu_name.grid(row=4,column=0)

start_btn = Button(text="เริ่มต้นการทำงาน",fg='green',command=start)
start_btn.grid(row=1,column=1,columnspan=2,sticky=NSEW)
stop_btn = Button(text="สิ้นสุดการทำงาน",fg='red',command=stop)
stop_btn.grid(row=1,column=3,columnspan="2",sticky=NSEW)

status_label = Label(text="สถานะการวัดการสั่นสะเทือน",bg='lightblue')
status_label.grid(row=2,column=1,columnspan=4,sticky=NSEW)

cyberpi_picture=Label(image=_cyberpi)
cyberpi_picture.grid(row=1,column=5,rowspan=2)

cyberpi_text=Label(text="CyberPi")
cyberpi_text.grid(row=3,column=5)

led1=Label(text='RBG LED Level 1',bg='lightgreen',width=10)
led1.grid(row=4,column=1,sticky=NSEW)

led2=Label(text='RBG LED Level 2',bg='yellow',width=10)
led2.grid(row=4,column=2,sticky=NSEW)

led3=Label(text='RBG LED Level 3',bg='gold',width=10)
led3.grid(row=4,column=3,sticky=NSEW)

led4=Label(text='RBG LED Level 4',bg='orange',width=10)
led4.grid(row=4,column=4,sticky=NSEW)

led5=Label(text='RBG LED Level 5',bg='red',width=10)
led5.grid(row=4,column=5,sticky=NSEW)

show_led1=Label(text='0-20',bg='black',width=15)
show_led1.grid(row=5,column=1,sticky=NSEW,rowspan=2)

show_led2=Label(text='20-40',bg='black',width=15)
show_led2.grid(row=5,column=2,sticky=NSEW,rowspan=2)

show_led3=Label(text='40-60',bg='black',width=15)
show_led3.grid(row=5,column=3,sticky=NSEW,rowspan=2)

show_led4=Label(text='60-80',bg='black',width=15)
show_led4.grid(row=5,column=4,sticky=NSEW,rowspan=2)

show_led5=Label(text='80-100',bg='black',width=15)
show_led5.grid(row=5,column=5,sticky=NSEW,rowspan=2)

logo_pic=Label(image=imake)
logo_pic.grid(row=6,column=0,sticky=SW)

task_ = Label()

app.mainloop()
