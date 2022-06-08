__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil


def clean_cache():
    path=os.getcwd()+'/files/cache' # home/winc is mijn huidige map
    try:
        os.mkdir(path)
    except OSError:
        try:
            shutil.rmtree(path)
            os.mkdir(path)
        except OSError:
            return 'Error, geen rechten om map te verwijderen of te creëren'

def cache_zip(zip_file_path, cache_dir_path):
    try:
        os.mkdir(cache_dir_path)
    except OSError:
        try:
            shutil.rmtree(cache_dir_path)
            os.mkdir(cache_dir_path)
        except OSError:
            return 'Error, geen rechten om map te verwijderen of te creëren'
    try:
        shutil.unpack_archive(zip_file_path, cache_dir_path, "zip")
    except OSError:
         return 'bestand bestaat niet'

def cached_files():
    path=os.getcwd()+'/files/cache'
    files_in_cache = [path+'/'+file for file in os.listdir(path) if os.path.isfile(path+'/'+file)]
    return files_in_cache

def find_password(cached_files):
    search_for_string='password:'
    for filename in cached_files:
        try:
            file_read = open(filename, "r")
            lines = file_read.readlines()
            for line in lines:
                if search_for_string in line:
                    found_line = line
        except:
            return 'bestand bestaat niet'
    password=found_line[found_line.find(' ')+1:found_line.find('/')]
    return password


#clean_cache()

#bestand='/home/bob.engelen_/Winc/files/data.zip'
#doel_map='/home/bob.engelen_/Winc/files/cache'

#cache_zip(bestand, doel_map)

#print(cached_files())

#print(find_password(cached_files()))
