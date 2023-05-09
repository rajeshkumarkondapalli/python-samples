# importing the modules
import os
import shutil

origin = '/home/dude/automation/sample/'
target = '/home/dude/automation/sample2/'

# Fetching the list of all the files
files = os.listdir(origin)

try:
    os.mkdir(target)

except IsADirectoryError as error: 
        pass
except Exception as error: 
        print(error) 
        # pass


# Fetching all the files to directory
for file_name in files:
    print(file_name)
    try:
        if os.path.isdir(origin + file_name):
            print(origin + file_name)
            print(target + file_name)
            os.mkdir(target + file_name)
        else :
            # copy each file
            shutil.copy(origin+file_name, target+file_name)
             
    except IsADirectoryError as error: 
        pass
    except Exception as error: 
        print(error) 
        # pass

print("Files are copied successfully")
