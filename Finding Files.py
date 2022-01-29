import os

def find_files(suffix, path):
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