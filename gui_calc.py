# gui calculator
from tkinter import *
from tkinter import messagebox
import time
import math
import os

def bind_unbind(ab):
    if ab == 1:
        win.bind("c",on_press_c)
        win.bind("d",on_press_d)
        win.bind("a",on_press_a)
        win.bind("p",on_press_p)
        win.bind("m",on_press_m)
        win.bind("s",on_press_s)
        win.bind("r",on_press_r)
        win.bind("e",on_press_e)
        win.bind("h",on_press_h)
    else:
        a = win.bind("c",int)
        a = win.bind("d",int)
        a = win.bind("a",int)
        a = win.bind("p",int)
        a = win.bind("m",int)
        a = win.bind("s",int)
        a = win.bind("r",int)
        a = win.bind("e",int)
        a = win.bind("h",int)
        win.unbind("c",a)
        win.unbind("d",a)
        win.unbind("a",a)
        win.unbind("p",a)
        win.unbind("m",a)
        win.unbind("s",a)
        win.unbind("r",a)
        win.unbind("e",a)
        win.unbind("h",a)

# -----To disable(off)/enable(on) the state of display-----------
def off():
    text1.config(state="disabled")
    text2.config(state="disabled")
def on():
    text1.config(state="normal")
    text2.config(state="normal")
#------The actions of all buttons defined here---------
def btn_click(value):
    global flag
    global opa
    global dot_flag
    bind_unbind(1)
    on()
    if flag == 1:
        text1.delete(0, END)
        text2.delete(0, END)
        dot_flag=1
    if value == "modulo": 
        if text1.get()[-1:]=='+' or text1.get()[-1:]=='-' or text1.get()[-1:]=='×' or text1.get()[-1:]=='÷' or text1.get()[-1:]=='%':
            pass 
        else:
            text1.insert("end", "%")
            dot_flag=1
        flag = 0
        off()
    elif value == "cl":
        a = text1.get()
        if a.find("+") != -1:
            b = a.split('+')
            op1 = b[0]
            text1.delete(0, END)
            text2.delete(0, END)
            text1.insert("end", op1 + "+")
        elif a.find("-") != -1:
            b = a.split('-')
            op1 = b[0]
            text1.delete(0, END)
            text2.delete(0, END)
            text1.insert("end", op1 + "-")
        elif a.find("×") != -1:
            b = a.split('×')
            op1 = b[0]
            text1.delete(0, END)
            text2.delete(0, END)
            text1.insert("end", op1 + "×")
        elif a.find("÷") != -1:
            b = a.split('÷')
            op1 = b[0]
            text1.delete(0, END)
            text2.delete(0, END)
            text1.insert("end", op1 + "÷")
        elif a.find("%") != -1:
            b = a.split('%')
            op1 = b[0]
            text1.delete(0, END)
            text2.delete(0, END)
            text1.insert("end", op1 + "%")
        dot_flag=1
        flag = 0
        off()
    elif value == "clear":
        text1.delete(0, END)
        text2.delete(0, END)
        dot_flag=1
        flag = 0
        off()
    elif value == "clear1":
        d = text1.get()[:-1]
        text1.delete(0, END)
        text1.insert("end", d)
        flag = 0
        if d.find("+") != -1 or d.find("-") != -1 or d.find("×") != -1 or d.find("÷") != -1 or d.find("%") != -1 or d.find(".") == -1:
            dot_flag = 1
        off()
    elif value == 7:
        text1.insert("end", "7")
        flag = 0
        off()
    elif value == 8:
        text1.insert("end", "8")
        flag = 0
        off()
    elif value == 9:
        text1.insert("end", "9")
        flag = 0
        off()
    elif value == "div":
        if text1.get()[-1:]=='+' or text1.get()[-1:]=='-' or text1.get()[-1:]=='×' or text1.get()[-1:]=='÷' or text1.get()[-1:]=='%':
            pass 
        else:
            text1.insert("end", "÷")
            dot_flag=1
        flag = 0
        off()
    elif value == 4:
        text1.insert("end", "4")
        flag = 0
        off()
    elif value == 5:
        text1.insert("end", "5")
        flag = 0
        off()
    elif value == 6:
        text1.insert("end", "6")
        flag = 0
        off()
    elif value == "mul":
        if text1.get()[-1:]=='+' or text1.get()[-1:]=='-' or text1.get()[-1:]=='×' or text1.get()[-1:]=='÷' or text1.get()[-1:]=='%':
            pass 
        else:
            text1.insert("end", "×")
            dot_flag=1
        flag = 0
        off()
    elif value == 1:
        text1.insert("end", "1")
        flag = 0
        off()
    elif value == 2:
        text1.insert("end", "2")
        flag = 0
        off()
    elif value == 3:
        text1.insert("end", "3")
        flag = 0
        off()
    elif value == "sub":
        if text1.get()[-1:]=='+' or text1.get()[-1:]=='-' or text1.get()[-1:]=='×' or text1.get()[-1:]=='÷' or text1.get()[-1:]=='%':
            pass 
        else:
            text1.insert("end", "-")
            dot_flag=1
        flag = 0
        off()
    elif value == "dot":
        if dot_flag==1:
            text1.insert("end", ".")
            dot_flag=0
        else:
            pass 
        flag = 0
        off()
    elif value == 0:
        text1.insert("end", "0")
        flag = 0
        off()
    elif value == "equal":
        a = text1.get()
        if a == "":
            off()
        elif a.find("×") != -1 or a.find("÷") != -1:
            exp = a.replace("×","*")
            exp1 = exp.replace("÷","/")
            result = eval(exp1)
        else:
            result = eval(a)
        
        if (str(result)[-2:])=='.0':
            text2.insert("end", a)
            txt1.set("= " + str(result).replace(".0",""))
            flag = 1
            dot_flag = 1
            off()
        else:
            text2.insert("end", a)
            txt1.set("= "+str(result))
            flag = 1
            dot_flag = 1
            off()
    elif value == "add":
        if text1.get()[-1:]=='+' or text1.get()[-1:]=='-' or text1.get()[-1:]=='×' or text1.get()[-1:]=='÷' or text1.get()[-1:]=='%':
            pass 
        else:
            text1.insert("end", "+")
            dot_flag=1
        flag = 0
        off()
    elif value == "opacity_plus":
        if opa <= 10:
            opa = opa + 1   
            win.attributes('-alpha',opa/10) 
        else:
            pass
        flag = 0
        off()
    elif value == "opacity_minus":
        if opa >= 2:
            opa = opa - 1 
            win.attributes('-alpha',opa/10) 
        else:
            pass
        flag = 0
        off()
    elif value == "square":
        x = text1.get()
        if x == "":
            off()
        y = float(x)*float(x)
        if (str(y)[-2:])=='.0':
            text2.insert("end","square("+x+")")
            txt1.set("= " + str(y).replace(".0",""))
            flag = 1
            dot_flag=1
            off()
        else:
            text2.insert("end","square("+x+")")
            txt1.set("= "+str(y))
            flag = 1
            dot_flag=1
            off()
    elif value == "sqroot":
        x = text1.get()
        if x == "":
            off()
        y = math.sqrt(float(x))
        if (str(y)[-2:])=='.0':
            text2.insert("end","squareRoot("+x+")")
            txt1.set("= " + str(y).replace(".0",""))
        else:
            text2.insert("end","squareRoot("+x+")")
            txt1.set("= "+str(y))
        flag = 1
        dot_flag=1
        off()


def on_enter1(e):
    btn_1['bg'] = "#DCDCDC"
def on_leave1(e):
    btn_1['bg'] = "#C0C0C0"

def on_enter2(e):
    btn_2['bg'] = "#DCDCDC"
def on_leave2(e):
    btn_2['bg'] = "#C0C0C0"

def on_enter3(e):
    btn_3['bg'] = "#DCDCDC"
def on_leave3(e):
    btn_3['bg'] = "#C0C0C0"

def on_enter4(e):
    btn_4['bg'] = "#DCDCDC"
def on_leave4(e):
    btn_4['bg'] = "#C0C0C0"

def on_enter5(e):
    btn_5['bg'] = "#DCDCDC"
def on_leave5(e):
    btn_5['bg'] = "#FAF9F6"

def on_enter6(e):
    btn_6['bg'] = "#DCDCDC"
def on_leave6(e):
    btn_6['bg'] = "#FAF9F6"

def on_enter7(e):
    btn_7['bg'] = "#DCDCDC"
def on_leave7(e):
    btn_7['bg'] = "#FAF9F6"

def on_enter8(e):
    btn_8['bg'] = "#DCDCDC"
def on_leave8(e):
    btn_8['bg'] = "#C0C0C0"

def on_enter9(e):
    btn_9['bg'] = "#DCDCDC"
def on_leave9(e):
    btn_9['bg'] = "#FAF9F6"

def on_enter10(e):
    btn_10['bg'] = "#DCDCDC"
def on_leave10(e):
    btn_10['bg'] = "#FAF9F6"

def on_enter11(e):
    btn_11['bg'] = "#DCDCDC"
def on_leave11(e):
    btn_11['bg'] = "#FAF9F6"

def on_enter12(e):
    btn_12['bg'] = "#DCDCDC"
def on_leave12(e):
    btn_12['bg'] = "#C0C0C0"

def on_enter13(e):
    btn_13['bg'] = "#DCDCDC"
def on_leave13(e):
    btn_13['bg'] = "#FAF9F6"

def on_enter14(e):
    btn_14['bg'] = "#DCDCDC"
def on_leave14(e):
    btn_14['bg'] = "#FAF9F6"

def on_enter15(e):
    btn_15['bg'] = "#DCDCDC"
def on_leave15(e):
    btn_15['bg'] = "#FAF9F6"

def on_enter16(e):
    btn_16['bg'] = "#DCDCDC"
def on_leave16(e):
    btn_16['bg'] = "#C0C0C0"

def on_enter17(e):
    btn_17['bg'] = "#DCDCDC"
def on_leave17(e):
    btn_17['bg'] = "#FAF9F6"

def on_enter18(e):
    btn_18['bg'] = "#DCDCDC"
def on_leave18(e):
    btn_18['bg'] = "#FAF9F6"

def on_enter19(e):
    btn_19['bg'] = "red"

def on_leave19(e):
    btn_19['bg'] = "#FF3131"

def on_enter20(e):
    btn_20['bg'] = "#DCDCDC"
def on_leave20(e):
    btn_20['bg'] = "#C0C0C0"

def on_enter21(e):
    btn_21['bg'] = "#DCDCDC"
def on_leave21(e):
    btn_21['bg'] = "#FAF9F6"

def on_enter22(e):
    btn_22['bg'] = "#DCDCDC"
def on_leave22(e):
    btn_22['bg'] = "#FAF9F6"

def on_enter23(e):
    btn_23['bg'] = "#DCDCDC"
def on_leave23(e):
    btn_23['bg'] = "#FAF9F6"

def on_enter24(e):
    btn_24['bg'] = "#DCDCDC"
def on_leave24(e):
    btn_24['bg'] = "#FAF9F6"

def on_click_lbl(e):
    messagebox.showinfo("About",
                        "This software is devoloped by Chandan Maurya\nFor any valuable feedback or contact us kindly mail me.\nEmail: cr3992@gmail.com")

def on_click_lbl1(e):
    root = Toplevel(win)
    root.geometry("450x500+820+150")
    root.title("Help")
    root.resizable(height=False,width=False)
    root.config(bg="white")
    root_lbl = Label(root,text="Shortcut Keys",font=("arial",12,"bold"),fg="white",bg="gray")
    root_lbl.pack()
    keys="A = About\nC = Change background color\nD = Default setting \n/ reset Transparency /reset default background color\n E = exit\nH = help \nM = Decrease Transparency\nP = Increase Transparency\n\n R = SquareRoot\n S = Square\ndelete = clear all"    
    text_lbl = Label(root,text=keys,font=("arial",10,"italic"),bg="lightgray",fg="darkblue")
    text_lbl.pack(pady=10)
    root_lbl1 = Label(root,text="Button locations",font=("arial",12,"bold"),fg="white",bg="gray")
    root_lbl1.pack(pady = 10)
    pic = PhotoImage(file = "help.png")
    root_lbl2 = Label(root,image=pic,bd=0)
    root_lbl2.pack(pady=5)
    root_lbl2.photo = pic
    text_lbl1 = Label(root,text="About",font=("arial",10,"bold"),bg="darkblue",fg="white")
    text_lbl1.place(x=20,y=0)
    text_lbl1.bind("<Button-1>",on_press_a)

def on_enter_lbl(e):
    lbl['bg'] = "#808080"
    lbl['text'] = "   About    "
def on_leave_lbl(e):
    lbl['bg'] = "#696969"
    lbl['text'] = "Calculator"

def on_enter_lbl1(e):
    lbl1['bg'] = "#808080"
def on_leave_lbl1(e):
    lbl1['bg'] = "#696969"

def press_0(e):
    frame_btn.after(0, on_enter18, e)
    btn_click(0)
    frame_btn.after(100, on_leave18, e)

def press_1(e):
    frame_btn.after(0, on_enter13, e)
    btn_click(1)
    frame_btn.after(100, on_leave13, e)

def press_2(e):
    frame_btn.after(0, on_enter14, e)
    btn_click(2)
    frame_btn.after(100, on_leave14, e)

def press_3(e):
    frame_btn.after(0, on_enter15, e)
    btn_click(3)
    frame_btn.after(100, on_leave15, e)

def press_4(e):
    frame_btn.after(0, on_enter9, e)
    btn_click(4)
    frame_btn.after(100, on_leave9, e)

def press_5(e):
    frame_btn.after(0, on_enter10, e)
    btn_click(5)
    frame_btn.after(100, on_leave10, e)

def press_6(e):
    frame_btn.after(0, on_enter11, e)
    btn_click(6)
    frame_btn.after(100, on_leave11, e)

def press_7(e):
    frame_btn.after(0, on_enter5, e)
    btn_click(7)
    frame_btn.after(100, on_leave5, e)

def press_8(e):
    frame_btn.after(0, on_enter6, e)
    btn_click(8)
    frame_btn.after(100, on_leave6, e)

def press_9(e):
    frame_btn.after(0, on_enter7, e)
    btn_click(9)
    frame_btn.after(100, on_leave7, e)

def press_add(e):
    frame_btn.after(0, on_enter20, e)
    btn_click("add")
    frame_btn.after(100, on_leave20, e)

def press_sub(e):
    frame_btn.after(0, on_enter16, e)
    btn_click("sub")
    frame_btn.after(100, on_leave16, e)

def press_mul(e):
    frame_btn.after(0, on_enter12, e)
    btn_click("mul")
    frame_btn.after(100, on_leave12, e)

def press_div(e):
    frame_btn.after(0, on_enter8, e)
    btn_click("div")
    frame_btn.after(100, on_leave8, e)

def press_dot(e):
    frame_btn.after(0, on_enter17, e)
    btn_click("dot")
    frame_btn.after(100, on_leave17, e)

def press_backspace(e):
    frame_btn.after(0, on_enter4, e)
    btn_click("clear1")
    frame_btn.after(100, on_leave4, e)

def press_enter(e):
    frame_btn.after(0, on_enter19, e)
    btn_click("equal")
    frame_btn.after(100, on_leave19, e)

def press_delete(e):
    frame_btn.after(0, on_enter3, e)
    btn_click("clear")
    frame_btn.after(100, on_leave3, e)
    
def col_change(e):
    global col
    win.config(bg=col_arr[col])
    col_lbl['bg']=col_arr[col]
    col = col+1
    if col == len(col_arr) - 1:
        col = 0

def on_press_d(e):
    global opa
    win.config(bg="#D2B48C")
    col_lbl['bg']="#D2B48C"
    opa = 9
    btn_click("opacity_plus")

def on_press_p(e):
    btn_click("opacity_plus")
def on_press_m(e):
    btn_click("opacity_minus")
def on_press_s(e):
    btn_click("square")
def on_press_r(e):
    btn_click("sqroot")
def on_press_c(e):
    col_change(e)
def on_press_a(e):
    on_click_lbl(e)
def on_press_h(e):
    on_click_lbl1(e)

def on_press_hack(e):
    global hack
    if hack == 0:
        off()
        bind_unbind(1)
        hack = 1
    else:
        on()
        text2.insert("end","hacked!")
        text2['fg'] = "green"
        bind_unbind(0)
        hack = 0

def flash():
    global i
    if i == len(col_arr)-1:
        win.destroy()
    else:
        greet.config(bg=col_arr[i])
        txt_lbl['bg']=col_arr[i]
        txt_lbl['fg']=col_arr[i-1]
        win.config(bg=col_arr[i])
        i = i+1
        win.after(143,flash)
def on_press_e(e):
    global opa
    global txt_lbl
    global greet
    opa = 5
    btn_click("opacity_plus")
    greet = Toplevel(win)
    greet.geometry("360x150+425+300")
    greet.overrideredirect(True)
    txt_lbl = Label(greet,text="Thanks for using our software\nfor more information \ncheckout about button",font=("arial",15,"italic"),bg="white",fg="blue")
    txt_lbl.pack(pady=30)
    flash()
    

win = Tk()
win.title("Calculator")
win.geometry("400x500+400+150")
win.config(bg="#D2B48C")
win.resizable(width=False, height=False)
txt1 = StringVar()
txt2 = StringVar()
w = 10
h = 3
flag = 0
opa = 9
dot_flag = 1
col = 0
i = 0
hack = 0
ab = 1
col_arr = ['red','#FFA07A',"#FA8072","#E9967A","#F08080","#CD5C5C","#DC143C","#B22222","#8B0000","#800000","#FF6347","#FF4500","#DB7093","#F0F8FF","#E6E6FA","#B0E0E6","#ADD8E6","#87CEFA","#87CEEB","#00BFFF","#1E90FF","#6495ED","#4682B4","#5F9EA0","#7B68EE","#6A5ACD","#483D8B","#4169E1","#0000FF","#0000CD","#00008B","#000080","#191970","#8A2BE2","#4B0082","#D2B48C","#7CFC00","#7FFF00","#32CD32","#00FF00","#228B22","#008000","#006400","#ADFF2F","#9ACD32","#00FF7F","#00FA9A","#90EE90","#8FBC8F","#20B2AA","#808000","#556B2F","#6B8E23","#FFFFE0","#FAFAD2","#FFEFD5","#FFE4B5","#FFDAB9","#EEE8AA","#F0E68C","#BDB76B","#FFFF00","#CCCC00","#999900","#333300","#DCDCDC","#C0C0C0","#808080","#778899","#2F4F4F","#000000"]
frame_disp = Frame(win, bg="#696969", height=100, width=365, highlightbackground="#6495ED", highlightthickness=2)
frame_disp.grid(padx=15, pady=10)
lbl = Label(frame_disp, text="Calculator", fg="white", bd=0, font=("times new roman", 10, "normal"), bg="#696969",
            height=2)
lbl.grid(row=0, column=0)
lbl.bind("<Button-1>", on_click_lbl)
lbl.bind("<Enter>", on_enter_lbl)
lbl.bind("<Leave>", on_leave_lbl)
lbl1 = Label(frame_disp, text="Help", fg="white", bd=0, font=("times new roman", 10, "normal"), bg="#696969",
            height=2)
lbl1.place(x=320,y=0)
lbl1.bind("<Button-1>", on_click_lbl1)
lbl1.bind("<Enter>", on_enter_lbl1)
lbl1.bind("<Leave>", on_leave_lbl1)
col_lbl = Label(frame_disp,bg="#D2B48C")
col_lbl.place(x=20,y=7,width=15,height=15)
col_lbl.bind("<Button-1>",col_change)

text2 = Entry(frame_disp, textvariable=txt2, bg="white", justify=RIGHT, bd=0, font=("arial", 15, "bold"),
              state="disabled", cursor="arrow")
text2.grid(row=1, column=0, ipadx=70)
text1 = Entry(frame_disp, textvariable=txt1, bg="white", justify=RIGHT, bd=0, font=("arial", 15, "bold"),
              state="disabled", cursor="arrow")
text1.grid(row=2, column=0, ipadx=70)

frame_btn = Frame(win, bg='lightgray', height=480, width=320, highlightbackground='#6495ED', highlightthickness=2)
frame_btn.grid(padx=15, pady=5)
btn_1 = Button(frame_btn, width=w, height=h, text="%", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
               command=lambda: btn_click("modulo"))
btn_2 = Button(frame_btn, width=w, height=h, text="CE", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
               command=lambda: btn_click("cl"))
btn_3 = Button(frame_btn, width=w, height=h, text="C", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
               command=lambda: btn_click("clear"))
btn_4 = Button(frame_btn, width=w, height=h, text="<×", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
               command=lambda: btn_click("clear1"))
btn_5 = Button(frame_btn, width=w, height=h, text="7", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
               command=lambda: btn_click(7))
btn_6 = Button(frame_btn, width=w, height=h, text="8", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
               command=lambda: btn_click(8))
btn_7 = Button(frame_btn, width=w, height=h, text="9", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
               command=lambda: btn_click(9))
btn_8 = Button(frame_btn, width=w, height=h, text="÷", font=("arial", 10, "bold"), bg="#C0C0C0", fg="black",
               command=lambda: btn_click("div"))
btn_9 = Button(frame_btn, width=w, height=h, text="4", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
               command=lambda: btn_click(4))
btn_10 = Button(frame_btn, width=w, height=h, text="5", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(5))
btn_11 = Button(frame_btn, width=w, height=h, text="6", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(6))
btn_12 = Button(frame_btn, width=w, height=h, text="×", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
                command=lambda: btn_click("mul"))
btn_13 = Button(frame_btn, width=w, height=h, text="1", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(1))
btn_14 = Button(frame_btn, width=w, height=h, text="2", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(2))
btn_15 = Button(frame_btn, width=w, height=h, text="3", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(3))
btn_16 = Button(frame_btn, width=w, height=h, text="–", font=("arial", 10, "bold"), bg="#C0C0C0", fg="black",
                command=lambda: btn_click("sub"))
btn_17 = Button(frame_btn, width=w, height=h, text=".", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click("dot"))
btn_18 = Button(frame_btn, width=w, height=h, text="0", font=("arial", 10, "bold"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click(0))
btn_19 = Button(frame_btn, width=w, height=h, text="=", font=("arial", 10, "normal"), bg="#FF3131", fg="black",
                command=lambda: btn_click("equal"))
btn_20 = Button(frame_btn, width=w, height=h, text="+", font=("arial", 10, "normal"), bg="#C0C0C0", fg="black",
                command=lambda: btn_click("add"))
btn_21 = Button(frame_btn, width=w, height=h, text="op+", font=("arial", 10, "normal"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click("opacity_plus"))
btn_22 = Button(frame_btn, width=w, height=h, text="op-", font=("arial", 10, "normal"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click("opacity_minus"))
btn_23 = Button(frame_btn, width=w, height=h, text="√x", font=("arial", 10, "normal"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click("sqroot"))
btn_24 = Button(frame_btn, width=w, height=h, text="x²", font=("arial", 10, "normal"), bg="#FAF9F6", fg="black",
                command=lambda: btn_click("square"))
btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)
btn_4.grid(row=0, column=3)
btn_5.grid(row=1, column=0)
btn_6.grid(row=1, column=1)
btn_7.grid(row=1, column=2)
btn_8.grid(row=1, column=3)
btn_9.grid(row=2, column=0)
btn_10.grid(row=2, column=1)
btn_11.grid(row=2, column=2)
btn_12.grid(row=2, column=3)
btn_13.grid(row=3, column=0)
btn_14.grid(row=3, column=1)
btn_15.grid(row=3, column=2)
btn_16.grid(row=3, column=3)
btn_17.grid(row=4, column=0)
btn_18.grid(row=4, column=1)
btn_19.grid(row=5, column=3)
btn_20.grid(row=4, column=3)
btn_21.grid(row=5, column=0)
btn_22.grid(row=5, column=1)
btn_23.grid(row=5, column=2)
btn_24.grid(row=4, column=2)
btn_1.bind("<Enter>", on_enter1)
btn_2.bind("<Enter>", on_enter2)
btn_3.bind("<Enter>", on_enter3)
btn_4.bind("<Enter>", on_enter4)
btn_5.bind("<Enter>", on_enter5)
btn_6.bind("<Enter>", on_enter6)
btn_7.bind("<Enter>", on_enter7)
btn_8.bind("<Enter>", on_enter8)
btn_9.bind("<Enter>", on_enter9)
btn_10.bind("<Enter>", on_enter10)
btn_11.bind("<Enter>", on_enter11)
btn_12.bind("<Enter>", on_enter12)
btn_13.bind("<Enter>", on_enter13)
btn_14.bind("<Enter>", on_enter14)
btn_15.bind("<Enter>", on_enter15)
btn_16.bind("<Enter>", on_enter16)
btn_17.bind("<Enter>", on_enter17)
btn_18.bind("<Enter>", on_enter18)
btn_19.bind("<Enter>", on_enter19)
btn_20.bind("<Enter>", on_enter20)
btn_21.bind("<Enter>", on_enter21)
btn_22.bind("<Enter>", on_enter22)
btn_23.bind("<Enter>", on_enter23)
btn_24.bind("<Enter>", on_enter24)

btn_1.bind("<Leave>", on_leave1)
btn_2.bind("<Leave>", on_leave2)
btn_3.bind("<Leave>", on_leave3)
btn_4.bind("<Leave>", on_leave4)
btn_5.bind("<Leave>", on_leave5)
btn_6.bind("<Leave>", on_leave6)
btn_7.bind("<Leave>", on_leave7)
btn_8.bind("<Leave>", on_leave8)
btn_9.bind("<Leave>", on_leave9)
btn_10.bind("<Leave>", on_leave10)
btn_11.bind("<Leave>", on_leave11)
btn_12.bind("<Leave>", on_leave12)
btn_13.bind("<Leave>", on_leave13)
btn_14.bind("<Leave>", on_leave14)
btn_15.bind("<Leave>", on_leave15)
btn_16.bind("<Leave>", on_leave16)
btn_17.bind("<Leave>", on_leave17)
btn_18.bind("<Leave>", on_leave18)
btn_19.bind("<Leave>", on_leave19)
btn_20.bind("<Leave>", on_leave20)
btn_21.bind("<Leave>", on_leave21)
btn_22.bind("<Leave>", on_leave22)
btn_23.bind("<Leave>", on_leave23)
btn_24.bind("<Leave>", on_leave24)

win.bind('1', press_1)
win.bind('2', press_2)
win.bind('3', press_3)
win.bind('4', press_4)
win.bind('5', press_5)
win.bind('6', press_6)
win.bind('7', press_7)
win.bind('8', press_8)
win.bind('9', press_9)
win.bind('0', press_0)
win.bind('+', press_add)
win.bind('-', press_sub)
win.bind('*', press_mul)
win.bind('/', press_div)
win.bind('.', press_dot)
win.bind('<BackSpace>', press_backspace)
win.bind('<Return>', press_enter)
win.bind('<Delete>', press_delete)
win.bind("`",on_press_hack)
bind_unbind(1)
win.mainloop()