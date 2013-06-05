#coding: utf-8

import Tkinter

from Tkinter import Frame, Button, Label, Entry, Text, Radiobutton
from multilistbox import MultiListbox
from util import Input, SearchInput
from ttk import Combobox
from model import get_result, init

class Main(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.target_select_value = Tkinter.StringVar()
        self.search_string = Tkinter.StringVar()
        self.create_widget()
        self.pack_all()

    def create_widget(self):
        self.target_mlb = MultiListbox(self, (('mRNAname', 20),('score',20)), height=25)
        self.function_mlb = MultiListbox(self, (('target family', 20),('function',20)), height=25)
        self.RNA_in_input = SearchInput(self, text='输入microRNA名字:', 
                textvariable=self.search_string, 
                button_function=lambda:get_result(self.search_string, self.target_select_value, self.target_mlb, self.function_mlb))
        self.split_frame = Frame(self, height=1, width=680, bg='black')
        self.split_frame_2 = Frame(self, height=1, width=680, bg='black')
        self.query_target_label = Label(self, text='查询target')
        self.query_function_label = Label(self, text='查询功能')
        self.target_select_radiobutton = []
        self.target_select_radiobutton.append(Radiobutton(self, 
                variable = self.target_select_value,
                value = 'targetscan', text = 'targetscan'))
        self.target_select_radiobutton.append(Radiobutton(self, 
                variable = self.target_select_value,
                value = 'miRanda', text = 'miRanda'))
        self.target_select_radiobutton.append(Radiobutton(self, 
                variable = self.target_select_value,
                value = 'picTar', text = 'picTar'))
        for radiobutton in self.target_select_radiobutton:
            radiobutton['width'] = 6 


    def pack_all(self):
        self.RNA_in_input.grid(pady=10,row=0, column=0, columnspan=5)
        self.split_frame.grid(pady=5,row=1, column=0, columnspan=5)
        self.query_target_label.grid(pady=5, row=2, column=0, columnspan=3)
        self.query_function_label.grid(pady=5, row=2, column=3, columnspan=2)
        for i, radiobutton in enumerate(self.target_select_radiobutton):
            radiobutton.grid(pady=5, row=3, column=i)
        self.target_select_radiobutton[0].select()
        for i in range(2):
            Label(self, width=8).grid(pady=5, row=3, column=3+i)
        self.split_frame_2.grid(pady=5,row=4, column=0, columnspan=5)
        self.target_mlb.grid(pady=10, row=5, column=0, columnspan=3)
        self.function_mlb.grid(pady=10, row=5, column=3, columnspan=2)

        """
        self.search_entry.grid(pady=5, row=3, column=1)
        self.search_button.grid(pady=5, row=3, column=2)
        self.search_result_text.grid(pady=20, row=4, column=0, columnspan=3)
        """

def sql():
    init()
    root = Tkinter.Tk()
    root.geometry('800x600')
    root.title('microRNA查询工具')
    root.option_add("*Font", "helvetica -12")

    main = Main(root)
    main.pack()

    root.mainloop()

if __name__ == '__main__':
    sql()
