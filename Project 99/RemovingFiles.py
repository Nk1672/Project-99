import os
import shutil
import time

def main():
    deleted_folders_count=0
    deleted_files_count=0

    path="C:/Users/nares/Desktop/deletefile/"
    does_exist=os.path.exists(path)
    print(does_exist)

    days=30

    seconds=time.time()-(days*24*60*60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds>=get_file_or_folder_age(root_folder):
                
                remove_folder(root_folder)
                deleted_folders_count +=1

                break

            else:

                for folder in folders:

                    folder_path=os.path.join(root_folder, folder)

                    if seconds>=get_file_or_folder_age(folder_path):
                        
                        remove_folder(root_folder)
                        deleted_folders_count +=1

                for file in files:
                    file_path=os.path.join(root_folder, file)
                    if seconds>=get_file_or_folder_age(file_path):
                        
                        remove_file(file_path)
                        deleted_files_count +=1

        else:

            if seconds>=get_file_or_folder_age(file_path):
                        
                remove_file(file_path)
                deleted_files_count +=1

    else:
        print("path is not found")

    print("total folders deleted: ")
    print(deleted_folders_count)
    print("total files deleted: ")
    print(deleted_files_count)

def remove_folder(path):
    
    if not shutil.rmtree(path):

        print("Folder deleted successfully")

    else:

        print("Unable to delete the folder")

def remove_file(path):

    if not os.remove(path):
        
        print("File deleted successfully")

    else:

        print("Unable to delete the file")

def get_file_or_folder_age(path):

    ctime=os.stat(path).st_ctime


    return ctime

if __name__ == '__main__':
    main()