import tkinter as tk



def on_sundae():
    #making sundae window
    swindow=tk.Tk()
    swindow.title("Sundae Ordering Form")
    #set up frame
    swindow.geometry("500x500+300+300") #500x500 frame, 300 is padding
    swindow.resizable(False, False)
    swindow.configure(background="light yellow")

#sundae window
    #title
    s_title=tk.Label(swindow, text="Ike's Homemade Ice Cream Parlor", font="Arial 16 bold", bg= "light blue", fg= "#FFFFFF")
    s_subtitle=tk.Label(swindow, text="Sundaes", font= "Arial 14", bg="white", fg= "light blue")
    #scoop spinbox
    scoop_label= tk.Label(swindow, text= "how many scoops would you like", bg= "light yellow")
    scoop_input= tk.Spinbox(swindow, from_=1, to = 3, increment=1)
    #whipcream check box
    whip_check= tk.Checkbutton(swindow, text="check for whip cream", bg= "light yellow")
    #nuts check box
    nuts_check= tk.Checkbutton(swindow, text="check for nuts", bg= "light yellow")
    #cherry check box
    cherry_check= tk.Checkbutton(swindow, text="check for a cherry on top", bg= "light yellow")
    #submit button
    submit_button = tk.Button(swindow, text= "Submit Order", command = on_submit, bg= "light blue")
    #exit button
    exit_button=tk.Button(swindow, text="Restart Order", command=swindow.destroy, bg= "light blue")


#layout for sundae window
    #layout for row0
    s_title.grid(row=0, columnspan=2)
    #layout row1
    s_subtitle.grid(row=1, columnspan=2)
    #row 2
    scoop_label.grid(row =2, column =0)
    scoop_input.grid(row=2, column =1)
    #row 3
    whip_check.grid(row=3, columnspan =2)
    #row4
    nuts_check.grid(row=4, columnspan = 2)
    #row5
    cherry_check.grid(row=5, columnspan=2)
    #row 6
    submit_button.grid(row=6, column = 0)
    exit_button.grid(row=6, column=1)
    
def on_submit():
    print("order")
    return None

def on_milkshake():
    #making sundae window
    mwindow=tk.Tk()
    mwindow.title("Milkshake Ordering Form")
    #set up window
    mwindow.geometry("500x500+300+300") #500x500 frame, 300 is padding
    mwindow.resizable(False, False)
    mwindow.configure(background="light yellow")
#milkshake window
    #title
    m_title=tk.Label(mwindow, text="Ike's Homemade Ice Cream Parlor", font="Arial 16 bold", bg= "light blue", fg= "#FFFFFF")
    m_subtitle=tk.Label(mwindow, text="Milkshakes", font= "Arial 14", bg="white", fg= "light blue")
    #size listbox
    size_label=tk.Label(mwindow, text="What size milkshake?", bg= "light yellow")
    size_input=tk.Listbox(mwindow, height=3, bg= "light yellow", exportselection=0)
    size_choices= ("small", "medium", "large")
    #inserting sizes
    for choice in size_choices:
        size_input.insert(tk.END, choice)
    #flavor listbox
    flavor_label=tk.Label(mwindow, text="What flavor milkshake?", bg= "light yellow")
    flavor_input=tk.Listbox(mwindow, height=3, bg= "light yellow", exportselection=0)
    flavor_choices= ("strawberry", "chocolate", "vanilla")
    #inserting flavors
    for choice in flavor_choices:
        flavor_input.insert(tk.END, choice)
    #whipcream check box
    whip_check= tk.Checkbutton(mwindow, text="check for whip cream", bg= "light yellow")
    #nuts check box
    nuts_check= tk.Checkbutton(mwindow, text="check for nuts", bg= "light yellow")
    #cherry check box
    cherry_check= tk.Checkbutton(mwindow, text="check for a cherry on top", bg= "light yellow")
    #submit button
    submit_button = tk.Button(mwindow, text= "Submit Order", command = on_submit, bg= "light blue")
    exit_button=tk.Button(mwindow, text="Restart Order", command=mwindow.destroy, bg= "light blue")
#setting milkshake layout
    #row 0
    m_title.grid(row=0, columnspan=2)
    #row1
    m_subtitle.grid(row=1, columnspan=2)
    #row2
    size_label.grid(row=2, column=0)
    size_input.grid(row=2, column=1)
    #row3
    flavor_label.grid(row=3, column=0)
    flavor_input.grid(row=3, column=1)
    #row4
    whip_check.grid(row=4, columnspan=2)
    #row5
    nuts_check.grid(row=5, columnspan=2)
    #row6
    cherry_check.grid(row=6, columnspan=2)
    #row7
    submit_button.grid(row=7, column=0)
    exit_button.grid(row=7, column=1)              






#building window
root=tk.Tk()
root.title("Ike's Ice Parlor Online Ordering")
root.geometry("400x300+300+300") #400x300 frame, 300 is padding
root.resizable(False, False)
root.configure(background="light yellow")


#building widgets
#title widget
title=tk.Label(root, text="Ike's Homemade Ice Cream Parlor", font="Arial 16 bold", bg= "light blue", fg= "#FFFFFF")
subtitle=tk.Label(root, text="place your order below", font= "Arial 14", bg="white", fg= "light blue")

#building name label and text entry
name_lbl= tk.Label(root, text="enter the name for the order: ", bg= "light yellow")
name_ent= tk.Entry(root)

#sundae and milkshake buttons
button_lbl = tk.Label(root, text="please choose a sundae or a milkshake", bg= "light yellow")
sundae_button = tk.Button(root, text= "Sundae", command = on_sundae, bg= "light blue")
milkshake_button = tk.Button(root, text= "Milkshake", command = on_milkshake, bg= "light blue")

#exit button
exit_button=tk.Button(root, text="Exit", command=root.destroy, bg="light blue")









#layout for root window
#layout for row0
title.grid(row=0, columnspan=2)
#layout row1
subtitle.grid(row=1, columnspan=2)
#layout row 2
name_lbl.grid(row=2, column=0)
name_ent.grid(row=2, column=1)
#layout row 3
button_lbl.grid(row=3, columnspan=2)
#layout row 4
sundae_button.grid(row=4, column=0)
milkshake_button.grid(row=4, column=1)
#row 5
exit_button.grid(row=5, columnspan=2)

