import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.scrolledtext as ts 
import tkinter.messagebox as mb
import os



class Layout(tk.Tk):
    def __init__(self):

        super().__init__()
        print(os.getcwd)
        self.__title = "carrot app"
        self.__icon = "./carrot-icon.ico"
        self.__width = int(self.winfo_screenwidth())
        self.__height = int(self.winfo_screenheight())
        self.__close_message = "Kill carrot?"
        
        self.geometry(f"{self.__width}x{self.__height}")
        self.title(self.__title)
        self.attributes("-topmost", True) # Put the layout at the top of any window
        self.iconbitmap(self.__icon)

        # Layout protocols
        self.protocol("WM_DELETE_WINDOW", self.close_layout)

    def set_title(self, title):
        self.__title = title
        self.title(self.__title)

    def get_title(self):
        return self.__title

    def set_icon(self, icon):
        self.__icon = icon

    def get_icon(self):
        return self.__icon

    def set_dimensions(self, width, height):
        self.__width = width
        self.__height = height
        self.geometry(f"{self.__width}x{self.__height}")

    def get_dimensions(self):
        return self.__width, self.__height

    def close_layout(self):
        if mb.askokcancel(message=self.__close_message, title=self.__title):
            self.destroy()

    def put_it_all_together(self):
        self.mainloop()