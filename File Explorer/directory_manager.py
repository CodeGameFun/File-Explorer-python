import os
import shutil




def default_open():
    default_dir = os.getcwd()
    fol_contents = os.listdir(default_dir)
    return fol_contents
    

def open(folder):
    previous_dir = os.getcwd()
    global directory
    directory = os.path.join(previous_dir, folder)
    fol_contents = os.listdir(directory)
    os.chdir(directory)
    return fol_contents, directory
    
    
    

def close():
    current_dir = os.getcwd()
    previous_dir = os.path.split(current_dir)[0]
    fol_contents = os.listdir(previous_dir)
    os.chdir(previous_dir)
    return fol_contents, previous_dir


def create(fol_name):
    new_path = os.path.join(os.getcwd(), fol_name)
    os.makedirs(new_path)

def remove():
    try:
        path = os.getcwd()
        dirs = os.path.split(path)[1]
        fol_contents, previous_dir = close()
        fol_contents.pop(fol_contents.index(dirs))
        shutil.rmtree(path)
        return fol_contents, previous_dir
    except:
        pass
    

def return_cwd():
    return os.getcwd()