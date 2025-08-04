# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:52:27 2024

@author: Jackson
"""

import tkinter as tk
    
def getData():
    
    inputList = []
    
    def on_submit():
        inputList.append(int(dimE.get()))
        inputList.append(int(numA.get()))
        inputList.append(genFAM.get())
        inputList.append(int(numS.get()))
        inputList.append(bool(three_d_P.get()))
        inputList.append(bool(top_P.get()))
        inputList.append(bool(front_P.get()))
        print('submitted: ', inputList)
        root.destroy()

    root = tk.Tk()
    root.geometry("600x500")
    root.title("Legendrian Knot Visualizer")
    
    tk.Label(root, text="Dimension of E:").grid(row=0, column=0)
    optionListE = (1, 2, 3, 4, 5)
    dimE = tk.StringVar()
    dimE.set(optionListE[0])
    menuE = tk.OptionMenu(root, dimE, *optionListE)
    menuE.grid(row=0, column=1)
    
    tk.Label(root, text="Number of control variables:").grid(row=1, column=0, padx=15)
    optionListA = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    numA = tk.StringVar()
    numA.set(optionListA[1])
    menuA = tk.OptionMenu(root, numA, *optionListA)
    menuA.grid(row=1, column=1)
    
    tk.Label(root, text="Genfam:").grid(row=2, column=0, padx=15)
    genFAM = tk.Entry(root)
    genFAM.grid(row=2, column=1, padx=15)
    genFAM.insert(tk.END, '(a1-x**2)*e1 - e1**3')
    
    tk.Label(root, text="Number of subfunctions:").grid(row=3, column=0, padx=15)
    numS = tk.Entry(root)
    numS.grid(row=3, column=1, padx=15)
    numS.insert(tk.END, '0')
    
    
    three_d_P = tk.BooleanVar(value='True')
    threeDProj = tk.Checkbutton(root, text='3D Plot', variable=three_d_P)
    threeDProj.grid(row=4, columnspan=2, padx=30)
    
    top_P = tk.BooleanVar(value='True')
    topProj = tk.Checkbutton(root, text='Top Projection', variable=top_P)
    topProj.grid(row=5, columnspan=2, padx=30)
    
    front_P = tk.BooleanVar(value='True')
    frontProj = tk.Checkbutton(root, text='Front Projection', variable=front_P)
    frontProj.grid(row=6, columnspan=2, padx=30)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=7, columnspan=2, pady=10)
    
    root.mainloop()
    return inputList
    
    

    