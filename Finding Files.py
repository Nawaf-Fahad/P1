import os

def find_files(suffix=None, path=None):
    if(suffix==None or path==None):
        return "There is some issues in suffix or path"
    files=[]
    
    
    current_files = os.listdir(path)
    
    for f in current_files:
        if os.path.isdir(path + "/" + f):
            files += find_files(suffix, path + "/" + f)
        elif f.endswith(suffix):
            files.append(path + "/" + f)

    return files

    return None

print(find_files(suffix=".txt",path='/Users/nxwaf/Desktop/CSC227_Course_Project')) #the files  in CSC227_Course_Project
print(find_files('.py')) #There is some issues in suffix or path
print(find_files('.py','')) #There is some issues in suffix or path
