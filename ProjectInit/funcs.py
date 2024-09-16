import os, shutil, pathlib

vault_path = pathlib.Path("\\".join(os.path.realpath(__file__).split("\\")[:-1]) + "\\vault\\")
dbs_path = pathlib.Path("\\".join(os.path.realpath(__file__).split("\\")[:-1]) + "\\dbs\\")

def ignore(_, files):
    return [file for file in files if file == "__pycache__"]

def export():
    '''used to export your current vault of templates'''
    shutil.copytree(vault_path, os.getcwd() + "\\vault", ignore=ignore)

def add(path: str, multiple: bool, overwrite: bool):
    '''used to add your template/s to your vault for easy reach'''
    template = pathlib.Path(os.getcwd())
    template = template / path
    to_move = [template]


    if not os.path.isdir(template):
        return print(f"{template} does not exist")

    if multiple:
        to_move = [template / item for item in os.listdir(template) if os.path.isdir(item)]
    
    for temp in to_move:
        temp_path = vault_path / path

        if os.path.isdir(temp_path) and not overwrite:
            print(f"skipped {temp_path}, already exists (if you want to continue anyway add --overwrite)")
            continue
        shutil.copytree(temp, temp_path, dirs_exist_ok=True)

def execulde_files(
    template: pathlib.Path,
    execlude: list[str]
):
    for file_or_dir in os.listdir(template):
        path = template/file_or_dir

        if os.path.isdir(path):
            if file_or_dir in execlude:
                shutil.rmtree(path, ignore_errors=True)
            else:
                execulde_files(path, execlude=[e.split("/")[-1] for e in execlude if e.startswith(file_or_dir)])
        
        elif os.path.isfile(path):
            if file_or_dir in execlude:
                os.remove(template/file_or_dir)

def generate(
    temp_name: str,
    output_path: str,
    db: str,
    execulde: list[str],
    overwrite: bool,
):
    '''used to generate your choosen template from your vault'''
    path = vault_path / temp_name
    output = pathlib.Path(output_path) / temp_name
    
    if not path.is_dir():
        print(f"{temp_name} does not exist in your vault")
        return

    if ((output).is_dir()) and not overwrite:
        print(f"{temp_name} already exists in {output_path} (add --overwrite to skip)")
        return

    shutil.copytree(path, output, dirs_exist_ok=True)
    if db:
        dbs = {
            "sqlite": "sqlite_db.py",
            "kvsqlite": "kv_db.py",
            "prisma": "schema.prisma"
        }
        db_file = dbs_path / (dbs[db])
        shutil.copy2(src=db_file, dst=output/dbs[db])    

    execulde_files(output, execlude=execulde)