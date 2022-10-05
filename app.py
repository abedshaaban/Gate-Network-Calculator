from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

and_gate_img = Image.open(r"assets/AND_Gate.png")
or_gate_img = Image.open(r"assets/OR_Gate.png")
xor_gate_img = Image.open(r"assets/XOR_Gate.png")
not_gate_img = Image.open(r"assets/NOT_Gate.png")

binary_options = ["0","1"]

window = Tk()
# window settings
window.title('Gate Networks by Shaaban\'s Industries')
window.geometry('400x300')
window.minsize(width=400, height=300)
window.resizable(False, False)

global_window = []

def close_all_windows():
    try:
        global_window[0].destroy()

    except Exception:
        pass

def And_gate_window():
    close_all_windows()

    def calculate_output(self):
        input1 = int(first_imput.get())
        input2 = int(seconds_imput.get())
        output_value = input1 * input2
        
        output.config(text=f"{output_value}")
        example.config(text=f"example: input-1 = {input1} and input-2 = {input2}, output = {input1} x {input2} = {output_value}")

    and_gate_frame = Frame(window,width=400,height=300)

    global_window.clear()
    global_window.append(and_gate_frame)

    resize_image = and_gate_img.resize((162, 97))
    main_image = ImageTk.PhotoImage(resize_image)

    first_imput = ttk.Combobox(window, value= binary_options, width=1)
    first_imput.current(0)
    first_imput.bind("<<ComboboxSelected>>", calculate_output)
    first_imput.place(x=90,y=61)

    seconds_imput = ttk.Combobox(window, value= binary_options, width=1)
    seconds_imput.current(0)
    seconds_imput.bind("<<ComboboxSelected>>", calculate_output)
    seconds_imput.place(x=90,y=99)

    image = Label(master= and_gate_frame, image = main_image)
    image.main_image = main_image
    image.place(x=117 , y=20)

    output = Label(master= and_gate_frame, text="0")
    output.place(x=283, y=60)
    


    Label(master=and_gate_frame, text="Role of the AND Gate:").place(x=10, y=130)
    Label(master=and_gate_frame, text="The And Gate takes 2 inputs then outputs their product.").place(x=10, y=150)

    example = Label(master=and_gate_frame, text="example: input-1 = 0 and input-2 = 0, output = 0 x 0 = 0")
    example.place(x=10, y=170)

    and_gate_frame.pack()

def Or_gate_window():
    close_all_windows()

    def calculate_output(self):
        input1 = int(first_imput.get())
        input2 = int(seconds_imput.get())
        output_value = 0

        if (input1 + input2 ) == 2:
            output_value = 1
        else:
            output_value = input1 + input2

        output.config(text=f"{output_value}")
        example.config(text=f"example: input-1 = {input1} and input-2 = {input2}, output = {input1} + {input2} = {output_value}")

    or_gate_frame = Frame(window,width=400,height=300)

    global_window.clear()
    global_window.append(or_gate_frame)


    resize_image = or_gate_img.resize((162, 97))
    main_image = ImageTk.PhotoImage(resize_image)

    first_imput = ttk.Combobox(window, value= binary_options, width=1)
    first_imput.current(0)
    first_imput.bind("<<ComboboxSelected>>", calculate_output)
    first_imput.place(x=90,y=61)

    seconds_imput = ttk.Combobox(window, value= binary_options, width=1)
    seconds_imput.current(0)
    seconds_imput.bind("<<ComboboxSelected>>", calculate_output)
    seconds_imput.place(x=90,y=99)

    image = Label(master= or_gate_frame, image = main_image)
    image.main_image = main_image
    image.place(x=117 , y=20)

    output = Label(master= or_gate_frame, text="0")
    output.place(x=283, y=60)
    


    Label(master=or_gate_frame, text="Role of the OR Gate:").place(x=10, y=130)
    Label(master=or_gate_frame, text="The OR Gate takes 2 inputs then outputs their sum.\nBut if the sum is equal to 2, the outout is 1").place(x=10, y=150)

    example = Label(master=or_gate_frame, text="example: input-1 = 0 and input-2 = 0, output = 0 + 0 = 0")
    example.place(x=10, y=190)

    or_gate_frame.pack()

def Xor_gate_window():
    close_all_windows()

    def calculate_output(self):
        input1 = int(first_imput.get())
        input2 = int(seconds_imput.get())
        output_value = 0

        if (input1 + input2 ) == 2:
            output_value = 0
        else:
            output_value = input1 + input2

        output.config(text=f"{output_value}")
        example.config(text=f"example: input-1 = {input1} and input-2 = {input2}, output = {input1} + {input2} = {output_value}")

    xor_gate_frame = Frame(window,width=400,height=300)

    global_window.clear()
    global_window.append(xor_gate_frame)


    resize_image = xor_gate_img.resize((162, 97))
    main_image = ImageTk.PhotoImage(resize_image)

    first_imput = ttk.Combobox(window, value= binary_options, width=1)
    first_imput.current(0)
    first_imput.bind("<<ComboboxSelected>>", calculate_output)
    first_imput.place(x=90,y=61)

    seconds_imput = ttk.Combobox(window, value= binary_options, width=1)
    seconds_imput.current(0)
    seconds_imput.bind("<<ComboboxSelected>>", calculate_output)
    seconds_imput.place(x=90,y=99)

    image = Label(master= xor_gate_frame, image = main_image)
    image.main_image = main_image
    image.place(x=117 , y=20)

    output = Label(master= xor_gate_frame, text="0")
    output.place(x=283, y=60)
    


    Label(master=xor_gate_frame, text="Role of the XOR Gate:").place(x=10, y=130)
    Label(master=xor_gate_frame, text="The XOR Gate takes 2 inputs then outputs their sum.\nBut if the sum is equal to 2, the outout is 0").place(x=10, y=150)

    example = Label(master=xor_gate_frame, text="example: input-1 = 0 and input-2 = 0, output = 0 + 0 = 0")
    example.place(x=10, y=190)

    xor_gate_frame.pack()

def Not_gate_window():
    close_all_windows()

    def calculate_output(self):
        input1 = int(first_imput.get())
        output_value = 0

        if input1  == 1:
            output_value = 0
        else:
            output_value = 1

        output.config(text=f"{output_value}")
        example.config(text=f"example: input-1 = {input1} , output = {output_value}")

    not_gate_frame = Frame(window,width=400,height=300)

    global_window.clear()
    global_window.append(not_gate_frame)


    resize_image = not_gate_img.resize((162, 97))
    main_image = ImageTk.PhotoImage(resize_image)

    first_imput = ttk.Combobox(window, value= binary_options, width=1)
    first_imput.current(0)
    first_imput.bind("<<ComboboxSelected>>", calculate_output)
    first_imput.place(x=90,y=81)


    image = Label(master= not_gate_frame, image = main_image)
    image.main_image = main_image
    image.place(x=117 , y=20)

    output = Label(master= not_gate_frame, text="1")
    output.place(x=283, y=60)
    


    Label(master=not_gate_frame, text="Role of the NOT Gate:").place(x=10, y=130)
    Label(master=not_gate_frame, text="The NOT Gate takes 1 input then outputs the opposite of it.").place(x=10, y=150)

    example = Label(master=not_gate_frame, text="example: input-1 = 0 , output = 1")
    example.place(x=10, y=170)

    not_gate_frame.pack()

def change_window(self):
    
    if menu.get() == "AND gate" :
        print("and gate")
        And_gate_window()

    elif menu.get() == "OR gate" :
        print("or gate")
        Or_gate_window()

    elif menu.get() == "XOR gate" :
        print("xor gate")
        Xor_gate_window()

    elif menu.get() == "NOT gate" :
        print("not gate")
        Not_gate_window()

    else :
        print("pass")


gate_options = ["AND gate", "OR gate", "XOR gate", "NOT gate"]

# code

menu = ttk.Combobox(window, value= gate_options)
menu.current(0)
menu.bind("<<ComboboxSelected>>", change_window)
menu.pack(side=TOP)



window.mainloop()