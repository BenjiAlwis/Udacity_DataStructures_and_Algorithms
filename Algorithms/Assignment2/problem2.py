import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_and_dirs = []
    if len(path) == 0:
        return []
    files_and_dirs = os.listdir(path)
    if suffix == '' or len(files_and_dirs) == 0:
        return []
    folders = [path+'/'+entry for entry in files_and_dirs if os.path.isdir(path+'/'+entry)]
    files = [path+'/'+entry for entry in files_and_dirs if os.path.isfile(path+'/'+entry) and entry.endswith('.' + suffix)]
    for folder in folders:
        files.extend(find_files(suffix,folder))
    return files
    
# Test Cases
temp_dir = os.getcwd() + '/temp'
print(find_files('py', temp_dir))
print(find_files('ods', temp_dir))
print(find_files('csv', temp_dir))

#Edge Cases
print(find_files('', temp_dir))#returns []
print(find_files('.', temp_dir))#returns []
print(find_files('%', temp_dir))#returns []
print(find_files('cccccccccccccccccccccccc', temp_dir))#returns []
