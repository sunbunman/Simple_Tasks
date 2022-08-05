def FilenameEdit(path,old_str,new_str):
    """
    Changes all instances of 'old_str' into 'new_str' for all files in directory 'path'.
    """
    import os

    os.chdir(path)
    files = os.listdir()

    for i in range(len(files)):
        os.replace(files[i],files[i].replace(old_str,new_str))
