import os
import shutil
from extension import db_dict

#funtion for making folders and moving files into them
def operations(folder_type,file_name,cwd):

    if not os.path.exists(cwd+folder_type) :
        os.mkdir(cwd+folder_type)

    #current working dir of file
    source = cwd+file_name 

    #new dir path
    destn = cwd+folder_type+os.path.sep+file_name  

    shutil.move(source,destn)

#Segregates files into folders
def organize(cur_dir):
    for entry in os.scandir(cur_dir):
        if entry.is_file():
            file_extension = os.path.splitext(entry.name)[1]
            for key in db_dict:
                if file_extension in db_dict[key]:
                    operations(key,entry.name,cur_dir)
                    break
