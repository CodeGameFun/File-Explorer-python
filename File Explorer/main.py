import explorer__view 
from tkinter import *
import directory_manager as dm
import os

window = Tk()
window.title('File Explorer')

ico_path = os.path.join(os.getcwd(), 'Img\\icon.png')
ico = PhotoImage(file= ico_path)
window.iconphoto(False, ico)
window.geometry('800x600')
window.configure(bg='white')
view = explorer__view.View(window)

def defualt_view():
    fol_contents = dm.default_open()
    view.view(fol_contents)

if __name__ == '__main__':
    defualt_view()

window.mainloop()
    