import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv
from tkinter import *
from PIL import ImageTk, Image



#global variables
variables= dict()
records_saved=0
global sundae_image


#flags
#setting flag to see if milkshake or sundae has been selected 
button_flag=False
milkshake_flag=True
sundae_flag=True



#defining functions
#milkshake button clicked
def on_milkshake():
    mwhip_check["state"]="active" #activating milkshake options
    mcherry_check["state"]="active"
    mnuts_check["state"]="active"
    size_combobox["state"]= "active"
    flavor_combobox["state"]="active"
    scoop_input["state"]="disabled" #disabling sundae
    swhip_check["state"]="disabled"
    scherry_check["state"]="disabled"
    snuts_check["state"]="disabled"
    sundae_button["state"]= "disabled"
    button_flag= True #button has been pressed
    sundae_flag=False #not sundae
#sundae button clicked
def on_sundae(): 
    scoop_input["state"]="normal" #activating sundae options
    swhip_check["state"]="active"
    scherry_check["state"]="active"
    snuts_check["state"]="active"
    mwhip_check["state"]="disabled" #disabling milkshake
    mcherry_check["state"]="disabled"
    mnuts_check["state"]="disabled"
    size_combobox["state"]= "disabled"
    flavor_combobox["state"]="disabled"
    milkshake_button["state"]= "disabled"
    button_flag=True
    milkshake_flag=False

#submit button clicked
def on_submit():
    name= name_ent.get() #getting name from entry box
    if name == "": #making sure input box is not empty
        output_text["text"]="Please enter your name" 
    else:
        if scoop_input["state"]=="normal": #if ordered sundae
            print("sundae order for: "+name) #printing information
            print(scoop_input.get()+ " scoops on sundae")
            if s_whip.get()==1: #if boxed clicked
                print("add whip cream")
            if s_nuts.get()==1:
                print("add nuts")
            if s_cherry.get()==1:
                print("add a cherry on top")
            root.destroy() #closing ordering form
            thanks_window() #opening thank you message
        else: #if ordered milkshake
            if size_var.get()=="": #make sure box isnt empty
                output_text["text"]="Please select a size"
            elif flavor_var.get()== "": #make sure box isnt empty
                output_text["text"]="Please select a flavor"
            else:
                print("order for: "+name)
                print(size_var.get()+ " milkshake")
                print(flavor_var.get())
                if m_whip.get()==1: #if box clicked
                    print("add whip cream")
                if m_nuts.get()==1:
                    print("add nuts")
                if m_cherry.get()==1:
                    print("add a cherry on top")
                root.destroy()
                thanks_window()

def thanks_window(): #window pops up after order submmited, thanking customer
    #setting up window
    finished=tk.Tk()
    finished.title("Ike's Ice Parlor Online Ordering")
    finished.configure(background="light yellow")

    #new window
    title=tk.Label(finished, text="Ike's Homemade Ice Cream Parlor", font="Arial 16 bold", bg= "light blue", fg= "#FFFFFF", padx=10)
    subtitle=tk.Label(finished, text="Thank you for your order!", font= "Arial 14", bg="white", fg= "light blue")
    exit_button= tk.Button(finished, text= "Exit", command=finished.destroy) #button to exit
    
    #layout for row0
    title.grid(row=0, columnspan=1, padx=15, sticky= NSEW)
    #layout row1
    subtitle.grid(row=1, columnspan=1)
    #row 2
    exit_button.grid(row=2, columnspan=1)
#if rest button clicked; reverts to startup settings
def reset():
    #reverting flags 
    button_flag=False
    milkshake_flag=True
    sundae_flag=True
    #clearing all text and boxes
    name_ent.delete(0, END)
    scoop_var.set(1)
    s_whip.set(0)
    m_whip.set(0)
    s_nuts.set(0)
    m_nuts.set(0)
    s_cherry.set(0)
    m_cherry.set(0)
    size_var.set("")
    flavor_var.set("")
    #setting up controls; all options disabled except for name, milkshake and sundae buttons
    scoop_input["state"]="disabled"
    swhip_check["state"]="disabled"
    scherry_check["state"]="disabled"
    snuts_check["state"]="disabled"
    mwhip_check["state"]="disabled"
    mcherry_check["state"]="disabled"
    mnuts_check["state"]="disabled"
    size_combobox["state"]= "disabled"
    flavor_combobox["state"]="disabled"
    milkshake_button["state"]="active"
    sundae_button["state"]="active"
    
    





#root window
root=tk.Tk()
root.title("Ike's Ice Parlor Online Ordering")
 #400x300 frame, 300 is padding
root.resizable(False, False)
root.configure(background="light yellow")



#frames for sundae and milkshake options
swindow= tk.Frame(root, background="light yellow") #sundae (s) 
swindow.grid(row=6, column=0)

mwindow= tk.Frame(root, background="light yellow") #milkshake (m)
mwindow.grid(row=6, column=1)


#building widgets
#title widget
logo_img= tk.PhotoImage(file= "logo.png")
title = ttk.Label(root, image=logo_img)
logo_text=tk.Label(root, text="image alternate text: Ike's Logo", font= "Arial 6", bg="light yellow")
subtitle=tk.Label(root, text="Place your order below", font= "Arial 14", bg="white", fg= "light blue")

#building name label and text entry
name_lbl= tk.Label(root, text="Enter the name for the order: ", bg= "light yellow")
name_ent= tk.Entry(root)

#sundae and milkshake buttons
button_lbl = tk.Label(root, text="Please choose a sundae or a milkshake", bg= "light yellow")
sundae_button = tk.Button(root, text= "Sundae", bg= "light blue", command= on_sundae)
milkshake_button = tk.Button(root, text= "Milkshake", bg= "light blue", command= on_milkshake)


#sundaes
#scoop spinbox
scoop_label= tk.Label(swindow, text= "How many scoops would you like?", bg= "light yellow")
scoop_var=IntVar()
scoop_input= tk.Spinbox(swindow, from_=1, to = 3, increment=1, textvariable=scoop_var)
#whipcream check box
s_whip=tk.IntVar()
swhip_check= tk.Checkbutton(swindow, text="Check for whip cream", bg= "light yellow", variable= s_whip)
#nuts check box
s_nuts=tk.IntVar()
snuts_check= tk.Checkbutton(swindow, text="Check for nuts", bg= "light yellow", variable=s_nuts)
#cherry check box
s_cherry= IntVar()
scherry_check= tk.Checkbutton(swindow, text="Check for a cherry on top", bg= "light yellow", variable=s_cherry)




#milkshakes
#size combobox
size_values= ["small", "medium", "large"]
variables["Size"] = tk.StringVar()
size_label= ttk.Label(mwindow, text="Size")
size_var = tk.StringVar()
size_combobox= ttk.Combobox(mwindow, state= 'readonly', textvariable = size_var, values=size_values)
size_label=tk.Label(mwindow, text="What size milkshake?", bg= "light yellow")


#flavor combobox
flavor_values= ["vanilla", "chocolate", "strawberry"]
variables["Flavor"] = tk.StringVar()
flavor_label= ttk.Label(mwindow, text="Flavor")
flavor_var = tk.StringVar()
flavor_combobox= ttk.Combobox(mwindow, textvariable = flavor_var, values=flavor_values, state= "readonly")
flavor_label=tk.Label(mwindow, text="What flavor milkshake?", bg= "light yellow")

#whipcream check box
m_whip= IntVar()
mwhip_check= tk.Checkbutton(mwindow, text="check for whip cream", bg= "light yellow", variable= m_whip)
#nuts check box
m_nuts= IntVar()
mnuts_check= tk.Checkbutton(mwindow, text="check for nuts", bg= "light yellow", variable= m_nuts)
#cherry check box
m_cherry= IntVar()
mcherry_check= tk.Checkbutton(mwindow, text="check for a cherry on top", bg= "light yellow", variable= m_cherry)



#sumbit, reset, exit buttons
submit_button = tk.Button(root, text= "Submit Order", bg= "light blue", command= on_submit)
restart_button= tk.Button(root, text= "Restart Order", bg= "light blue", command= reset)
exit_button=tk.Button(root, text="Exit", command=root.destroy, bg= "light blue")


#output text line for if a box is left blank
output_text=tk.Label(root, text= " ", bg="light yellow")

#botttom image
my_img= tk.PhotoImage(file= "icecream.png")
img_lbl = ttk.Label(root, image=my_img)
my_img_text= tk.Label(root, text= "image alternate text: different ice cream cones in a row", font = "Arial 6", bg= "light yellow")



#requires buttons to be selected before sundae or milkshake options can be selected; customer can't pick toppings for sundae and then click the milkshake button
if button_flag==False:
    scoop_input["state"]="disabled"
    swhip_check["state"]="disabled"
    scherry_check["state"]="disabled"
    snuts_check["state"]="disabled"
    mwhip_check["state"]="disabled"
    mcherry_check["state"]="disabled"
    mnuts_check["state"]="disabled"
    size_combobox["state"]= "disabled"
    flavor_combobox["state"]="disabled"






#layout for root window
#layout for row0 and 1
title.grid(row=0, columnspan=2, padx=15, sticky= NSEW)
logo_text.grid(row= 1, columnspan=2)
#layout row2
subtitle.grid(row=2, columnspan=2)
#layout row 3
name_lbl.grid(row=3, column=0)
name_ent.grid(row=3, column=1)
#layout row 4
button_lbl.grid(row=4, columnspan=2)
#layout row 5
sundae_button.grid(row=5, column=0)
milkshake_button.grid(row=5, column=1)

#row 6 is where sundae and milkshake frames are

#sundae frame
#row 0 and 1
scoop_label.grid(row =0, column =0)
scoop_input.grid(row=1, column =0)
#row 2
swhip_check.grid(row=2)
#row3
snuts_check.grid(row=3, columnspan = 1)
#row4
scherry_check.grid(row=4, columnspan=2)

#milkshake frame
#row 0 and 1
size_label.grid(row=0, column=0)
size_combobox.grid(row=1, column=0)
#row3
flavor_label.grid(row=2, column=0)
flavor_combobox.grid(row=3, column=0)
#row4
mwhip_check.grid(row=4, columnspan=1)
#row5
mnuts_check.grid(row=5, columnspan=1)
#row6
mcherry_check.grid(row=6, columnspan=1)

#back to root window
#row 7
submit_button.grid(row=7, columnspan=2)
#row 8
restart_button.grid(row=8, column=0)
exit_button.grid(row=8, column=1)
#row 9
output_text.grid(row=9, columnspan=2)
#row 10
img_lbl.grid(row=10, columnspan=2)
#row 11
my_img_text.grid(row=11, columnspan=2)



