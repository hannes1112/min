#Hannes Fehre
#3.8.2

import tkinter as tk
from tkinter import messagebox
from tkinter import *

"""
def increase():
    value = lbl_value["text"]
    lbl_value["text"] = f"{value + 1}"


def decrease():
    print("1")
    #messagebox.showinfo("Title", "a Tk MessageBox")
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"
    btn_comp1 = tk.Button(master=window, text="hhh", command=confirm_exit("decrease_var") ,bg='#54FA9B')
    btn_comp1.grid(row=0, column=0, sticky="nsew")
    print("2")
"""
def confirm_exit(comp_id, status):
    print(comp_id)
    mesg_text = status + str(comp_id) + "?"
    MsgBox = tk.messagebox.askquestion ('Attention',mesg_text,icon = 'warning')
    if MsgBox == 'yes':
        print("yes")
    else:
        print("no")
        exit()
        
def redirection_on(ID):
    status = "set on "
    confirm_exit(ID, status)
    if ID == 0:
        pass
    elif ID == 1:
        pass
    elif ID == 2:
        pass
    elif ID == 3:
        pass
    elif ID == 4:
        pass
    elif ID == 5:
        pass
    elif ID == 6:
        pass
    elif ID == 7:
        pass
    elif ID == 8:
        pass
    elif ID == 9:
        pass
    elif ID == 10:
        pass 
    else:
        print("no task assigned")

def redirection_off(ID):
    status = "set off "
    confirm_exit(ID, status)
    if ID == 0:
        print("hallo i")
        pass
    elif ID == 1:
        pass
    elif ID == 2:
        pass
    elif ID == 3:
        pass
    elif ID == 4:
        pass
    elif ID == 5:
        pass
    elif ID == 6:
        pass
    elif ID == 7:
        pass
    elif ID == 8:
        pass
    elif ID == 9:
        pass
    elif ID == 10:
        pass 
    else:
        print("no task assigned")

def redirection_info(ID):
    status = "get info "
    confirm_exit(ID, status)
    
    if ID == 0:
        print("hallo i")
        pass
    elif ID == 1:#? fail - global windows 
        print("ich bin eine 1")
        #btn_comp1 = tk.Button(master=window, text="hhh", command=confirm_exit("decrease_var") ,bg='#54FA9B')
        btn_comp1 = ".!button31"
        btn_comp1 = tk.Button(master=window, text="jaa")
        print(btn_comp1)
        
        #window.configure(bg="blue")
        canvas = Canvas(master=window, width=3, height=3, borderwidth=6, highlightthickness=0, bg="BLUE")
        canvas.grid(row=4, column=0)

        #change text 
        value = lbl_value14["text"]
        lbl_value14["text"] = f"{hallo}"

    elif ID == 2:
        pass
    elif ID == 3:
        pass
    elif ID == 4:
        pass
    elif ID == 5:
        pass
    elif ID == 6:
        pass
    elif ID == 7:
        pass
    elif ID == 8:
        pass
    elif ID == 9:
        pass
    elif ID == 10:
        pass 
    else:
        print("no task assigned")
    
def init_basic_structure():
    global window
    window = tk.Tk()

    window.rowconfigure(0, minsize=0, weight=0)
    window.columnconfigure([0, 1, 2], minsize=0, weight=0)

    #------------------------------
    #window.configure(bg="blue")
    #canvas = Canvas(master=window, width=3, height=3, borderwidth=6, highlightthickness=0, bg="red")
    #canvas.grid(row=4, column=3)
    #canvas.create_line(0,0,3,3, fill="red")
    #canvas.create_line(0,2,3,-1, fill="red")
    #------------------------------


    #, sticky="wesn"

    repetition = -1
    number_of_unit = 0
    for i in range(10):
        repetition += 1
        number_of_unit += 1

        #headover
        text_var = "PC " + str(number_of_unit)
        #print(text_var)
        lbl_value = "lbl_value"+str(number_of_unit)#form
        lbl_value = tk.Label(master=window, text=text_var)
        lbl_value.grid(row=repetition, column=0, columnspan=4, sticky = "W")

        repetition += 1
        number_of_unit_under = 1
            
        btn_comp = "btn_comp"+str(number_of_unit)#form
        #btn_comp = tk.Button(master=window, text=btn_comp,bg='#54FA9B',command=lambda handover=number_of_unit, function=redirection_on: function(handover))
        #text=btn_comp
        btn_comp = tk.Button(master=window, text="ON", bg='#54FA9B', command=lambda handover=number_of_unit, function=redirection_on: function(handover))
        btn_comp.grid(row=repetition, column=0, sticky = "NSEW")

        number_of_unit_under += 1

        btn_comp = "btn_comp"+str(number_of_unit)+str(number_of_unit_under)#form
        btn_comp = tk.Button(master=window, text="OFF", bg="#FF0000", command=lambda handover=number_of_unit, function=redirection_off: function(handover))
        btn_comp.grid(row=repetition, column=1, sticky = "NSEW")

        number_of_unit_under += 1

        btn_comp = "btn_comp"+str(number_of_unit)+str(number_of_unit_under)#form
        btn_comp = tk.Button(master=window, text="INFO", bg="#FFFF00" , command=lambda handover=number_of_unit, function=redirection_info: function(handover))
        btn_comp.grid(row=repetition, column=2, sticky = "NSEW")

        #Text laste
        number_of_unit_under += 1
        
        lbl_value = "lbl_value"+str(number_of_unit)+str(number_of_unit_under)#form
        lbl_value = tk.Label(master=window, text=lbl_value)
        lbl_value.grid(row=repetition, column=3)

    number_of_unit_under += 1
    repetition += 1
    
    btn_comp = "btn_comp"+str(number_of_unit)+str(number_of_unit_under)#form
    btn_comp = tk.Button(master=window, text="fetch data", bg="#FFFF00" , command=lambda handover=number_of_unit, function=redirection_info: function(handover))
    btn_comp.grid(row=repetition, column=0, sticky = "NSEW")    

    window.mainloop()
        

def main():
    init_basic_structure()
    

if __name__ == '__main__':
    main()
