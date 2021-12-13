import os
import imghdr
def folder_exist (path):
        if os.path.isdir(path):
            return True

def create_folder_for_user(path):
     os.chdir('F:\webproject')
    
     
     
     if not folder_exist(path):
         print("i am here dada")
         os.mkdir(path)
def folderSucessfully_created(path,folder_name):
    if folder_exist(path,folder_name):
        return True
    else:
        return False
def correctFormat(filename):
    
    format=imghdr.what(filename)
    if(format=="jpeg" or format=="png"):
        return True
    else:
        return False
        

def issuccessfuluploadimage(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False



