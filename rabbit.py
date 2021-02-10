import tkinter as tk
import tkinter.font as tkFont
import tkinter.scrolledtext as ts 
from tkinter import messagebox
import os
import time as t
import subprocess as sb
import simpleaudio as sa
from PIL import Image, ImageTk # NON-STANDARD Allows the use of different image formats
import vlc # NON-STANDARD

# Layout (tk.Tk) -> Rabbit (tk.Canvas)

class Layout(tk.Tk):
    def __init__(self):

        super().__init__()

        self.__title = "rabbit app"
        self.__icon = "assets//rabbit-icon.ico"
        self.__width = 200#int(self.winfo_screenwidth())
        self.__height = 100#int(self.winfo_screenheight())
        self.__close_message = "Kill rabbit?"
        
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
        if messagebox.askokcancel(message=self.__close_message, title=self.__title):
            self.destroy()

    def put_it_all_together(self):
        self.mainloop()


#

class Rabbit(tk.Canvas):
    def __init__(self, layout):

        self.__layout = layout
        self.__bkg = "assets//meadow-bkg.png"
        self.__width = 200
        self.__height = 100
        self.__border_width = 1

        super().__init__(self.__layout, width = self.__width, height = self.__height)

        self.smallFont = tkFont.Font(family="Open Sans", size=8)
        self.mediumFont = tkFont.Font(family="Open Sans", size=12)
        self.bigFont = tkFont.Font(family="Open Sans Semibold", size=25)

        self.bkg = Image.open(self.__bkg)
        self.bkg = self.bkg.resize((self.__width, self.__height))
        self.img = ImageTk.PhotoImage(self.bkg)
        self.create_image(0, 0, anchor = tk.NW, image=self.img)
        self.spawn_rabbit()
        

    def set_bkg(self, bkg):
        self.__bkg = bkg
        self.spawn_rabbit()
    
    def get_bkg(self):
        return self.__bkg

    def set_border_width(self, border_width):
        self.__border_width = border_width
        self.spawn_rabbit()
    
    def get_border_width(self):
        return self.__border_width
    
    def add_widget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def add_styled_button(self, text, anchor, bcolor, fcolor, w, h, bd, style, command, x, y):
        h = self.add_widget(tk.Button(self, 
                                text = text, 
                                anchor = anchor,
                                bg = bcolor,
                                foreground = fcolor,
                                width = w,
                                height = h,
                                bd = bd,
                                font = style,
                                command = command), x, y)
        
        self.spawn_rabbit()

    def add_text(self, content, anchor, style, fcolor, x, y):
        self.create_text(x,y, fill=fcolor,
                                    text=content,
                                    justify = anchor,
                                    font = style)
        self.spawn_rabbit()
    #def add_text_box(self, )


    def go_page(self, new_page):
        self.pack_forget()
        new_page.spawn_rabbit()
        

    def spawn_rabbit(self):
        self.pack()

Root = Layout()

StartPage = Rabbit(Root)
SecondPage = Rabbit(Root)

StartPage.set_bkg("assets//test-bkg.png")


StartPage.add_styled_button(
                                    text="p1", 
                                    anchor = tk.CENTER,
                                    bcolor = "#FE8C33",
                                    fcolor = "#B4301A",
                                    w = "20",
                                    h = "1",
                                    bd = "1",
                                    style = StartPage.smallFont,
                                    command = lambda : StartPage.go_page(SecondPage), 
                                    x = 25, y = 25)

SecondPage.add_styled_button(
                                    text="p2", 
                                    anchor = tk.CENTER,
                                    bcolor = "#59c6ee",
                                    fcolor = "#B4301A",
                                    w = "20",
                                    h = "1",
                                    bd = "1",
                                    style = SecondPage.smallFont,
                                    command = lambda : SecondPage.go_page(StartPage), 
                                    x = 2, y = 25)

Root.put_it_all_together()

'''

         # Entrar Button
        self.addWidget(tk.Button(self, 
                                    text="Entrar", 
                                    anchor = tk.CENTER,
                                    bg = "#FE8C33",
                                    foreground = "#B4301A",
                                    width = "99",
                                    height = "0",
                                    bd = "3",
                                    font = self.fontStyle,
                                    command = self.go_next_page), 979, 1000)

        # Author text  
        self.create_text(1759,900, fill="black",
                                        text="Desarrollado por Jorge Flores",
                                        justify = tk.RIGHT,
                                        font = self.fontStyle2)


        # CANVAS Geometry Manager
        
    
    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def go_next_page(self):
        
        SuertePage(self.ROOT, "assets\\suerte-bkg.png")
        self.destroy()

'''