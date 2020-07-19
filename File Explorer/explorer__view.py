from tkinter import *
from functools import partial
import directory_manager as dm
import os
import imghdr

class View:
    def __init__(self, master):
        self.window = master #Window
        self.window.geometry()

        self.directory = StringVar(self.window) #Directory
        self.directory.set("C:\\")

        self.path = Label(self.window,width=100, height=2, textvariable=self.directory).place(anchor='s', rely=0.6, relx=0.5)
        self.namebox = Entry(self.window, width=35, bd=3)
        self.frame = Frame(self.window).grid(row=1) #Widgets (Frame contaning buttons(folders), Label showing current path)
        self.button_list = []
        self.image_types = ['rgb', 'gif', 'png', 'jpeg', 'jpg', 'bmp']
                

    def open_view(self, fol_name): #When button (folder button) is clicked...
        try:
            self.forget()  #Destroys existing buttons preventing overlap
            fol_contents, fol_path = dm.open(fol_name) #Getting contents and the path of the folder
            self.view(fol_contents) #Going to view function
            self.directory.set(f'{fol_path}') #Setting the directory to the folder one
        except:
            pass

    def naming(self):
        self.namebox.place(anchor='s', rely=0.8, relx=0.5)
        self.ok = Button(self.window, text='Ok', command=self.makedir)
        self.ok.place(anchor='s', rely=0.8, relx=0.7),

    def makedir(self):
        name = str(self.namebox.get())
        self.namebox.destroy()
        self.ok.destroy()
        dm.create(name)
        print(os.getcwd())
        self.view(os.listdir(os.getcwd()))
        
    def remove_dir(self):
        contents, previous_dir = dm.remove()
        os.chdir(previous_dir)
        self.view(contents)
        self.directory.set(f'{previous_dir}')

    def view(self, fol_contents): #Creating button
        row = 1
        col = 0
        self.contents = fol_contents  

        all_img_path_root = os.path.split(__file__)[0]
        self.fol = PhotoImage(file= os.path.join(all_img_path_root, "Img\\folder.png"))
        self.close = PhotoImage(file= os.path.join(all_img_path_root, "Img\\close.png"))
        self.exe = PhotoImage(file= os.path.join(all_img_path_root, "Img\\exe.png"))
        self.doc = PhotoImage(file=os.path.join(all_img_path_root, "Img\\icon.png"))
        self.photo = PhotoImage(file= os.path.join(all_img_path_root, "Img\\photos.png"))
        self.remove = PhotoImage(file= os.path.join(all_img_path_root, "Img\\remove_folder.png"))
        self.new = PhotoImage(file= os.path.join(all_img_path_root, "Img\\new_folder.png"))

        for content in self.contents:
            self.result = partial(self.open_view, content)
            content_path = os.path.join(os.getcwd(), content)

            try:
                if os.path.isdir(content_path):
                    self.img = self.fol
                elif os.path.splitext(content_path)[1] == '.lnk' or os.path.splitext(content_path)[1] == '.exe':
                    self.img = self.exe
                    self.result = None
                elif imghdr.what(content_path) in self.image_types:
                    self.img = self.photo
                    self.result = None

                else:
                    self.img = self.doc
                    self.result = None
            except PermissionError:
                self.img = self.doc

            
            self.button = Button(self.frame, text=content, bd=0, bg='white', command=self.result, padx=15,width= 100,  image= self.img, compound=LEFT, anchor='w')
            self.button_list.append(self.button)
            self.button.grid(row=row, column=col)  
                  
            if row == 8:
                row = 1
                col += 1
            else:
                row += 1

        self.close_button = Button(self.frame, bd=0, bg='white', command=self.close_view, width=100,  image= self.close,  anchor='w')  
        self.button_list.append(self.close_button)
        self.close_button.grid(row=row, column=col)

        self.new_fol = Button(self.window, bd=0, bg='white', command=self.naming, image=self.new).place(anchor='s', rely=0.7, relx=0.4)
        self.remove_fol = Button(self.window, bd=0, bg='white', command=self.remove_dir, image=self.remove).place(anchor='s', rely=0.7, relx=0.6)

    def close_view(self):
        self.forget()
        fol_contents, fol_path = dm.close()
        self.view(fol_contents)
        self.directory.set(f'Directory: {fol_path}')


    def forget(self): #Function to destroy
        for button in self.button_list:
            button.destroy()