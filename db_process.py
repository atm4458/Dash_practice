from functools import wraps
import os
import pandas as pd
import pickle
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
def path_exist(func):
    @wraps(func)
    def wrap_func(args):
        if not os.path.exists(args):
            return None
        return func(args)
    return wrap_func

def create_folder(folder_path:str) -> object:
    if os.path.exists(folder_path): return None
    os.mkdir(folder_path)
    return folder_path

@path_exist
def read_files(folder_path:str) -> object:
    files = os.listdir(folder_path)
    pickle_files = []
    for file in files:
        if file.endswith("pickle"):
            read_file = os.path.join(folder_path, file)
            pickle_files.append(read_file)
    if len(pickle_files) == 0:
        return None
    return pickle_files

def combine_pickle(files_path:list) -> pd.DataFrame:
    df = []
    for file_path in files_path:
        with open(file_path, "rb") as f:
            tmp_df = pickle.load(f)
        df.append(tmp_df)
    df = pd.concat(df).reset_index(drop=True)
    folder = os.path.split(file_path)[0]
    up_folder = os.path.join(folder, "template")
    if not os.path.exists(up_folder): os.mkdir(up_folder)
    dump_pickle = os.path.join(up_folder, "_combined_template.pickle")
    with open(dump_pickle, "wb") as f:
        pickle.dump(df, f)
    return df

def save_files(files:FileStorage, folder_path:str):
    for file in files:
        file_name = secure_filename(file.filename)
        save_target = os.path.join(folder_path, file_name)
        file.save(save_target)



if __name__ == "__main__":
    files_path = read_files("static")
    df = combine_pickle(files_path)