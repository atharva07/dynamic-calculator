from tkinter import *
import tkinter.font as font

# creating the main window
root = Tk()

# Assigning the desired geometry
root.geometry("380x400")

# naming the window
root.title("Calculator")

# window can be resizable if needed
root.resizable(0,0)

inp = StringVar()
myFont = font.Font(size=15)

screen = Entry(root, text=inp, width=30,
                justify='right', font=(10), bd=4)

screen.grid(row=0, columnspan=4, padx=15, pady=15, ipady=5)

# key_matrix contains all the keys
key_matrix = [["c", u"\221A", "/", "<-"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", 0, ".", "="]]

# creating a dictionary for buttons
btn_dict = {}

# VAriables to store our results
ans_to_print = 0

# defining the for calculation 
def Calculate(event):
    button = event.widget.cget("text")

    global key_matrix, ans_to_print, inp

    try:
        if button == u"\221A":
            ans = float(inp.get())**(0.5)
            ans_to_print = str(ans)
            inp.set(str(ans))

        elif button == "c": # clear button
            inp.set("")
        
        elif button == "!": # factorial
            def fact(n): 
                return 1 if n == 0 else n*fact(n-1)
            inp.set(str(fact(inp(inp.get))))

        elif button == "<-": # backspace
            inp.set(inp.get()[:len(inp.get())-1])
        
        elif button == "=":
            ans_to_print = str(eval(inp.get()))
            inp.set(ans_to_print)

        else:
            inp.set(inp.get()+str(button))

    except:
        inp.set("Wrong Operation")

# creating buttons using for loop 
# Number of rows containing buttons
for i in range(len(key_matrix)):
    # number of columns
    for j in range(len(key_matrix[i])):

        # creating and adding the buttons to dictionary
        btn_dict["btn_"+str(key_matrix[i][j])] = Button(
            root, bd=1, text=str(key_matrix[i][j]), font=myFont)

        # positioning buttons
        btn_dict["btn_"+str(key_matrix[i][j])].grid(
            row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)

        # Assigning an action to the button
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate)

root.mainloop()
