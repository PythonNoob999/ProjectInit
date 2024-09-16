from argparse import ArgumentParser, Namespace
import os, sys
from .funcs import *

def main():
    config()
    parser = ArgumentParser()
    #parser.add_argument("--", help="", type=str,required=False)
    # main options
    parser.add_argument("--generate", help=generate.__doc__, type=str, required=False)
    parser.add_argument("--add", help=add.__doc__, type=str, required=False)
    parser.add_argument("--export", help=export.__doc__, action="store_true", required=False)

    # main options options
    parser.add_argument("--multiple", help="the --add path is multiple templates in 1 directory", action="store_true", required=False, default=False)
    parser.add_argument("--output", help="the path you want to copy the template in (default = ./)", type=str, required=False, default=os.getcwd())
    parser.add_argument("--db", help="add a db in your project ['sqlite', 'kvsqlite', 'prisma']", type=str, choices=["sqlite", "kvsqlite", "prisma"], required=False, default=None)
    parser.add_argument("--execlude", help="choose what files to execlude from template, seperate them with commas,", type=str, required=False, default="")
    parser.add_argument("--overwrite", help="overwrites any existing templated in vault when using --add", action="store_true", required=False)
    args: Namespace = parser.parse_args()

    if not any([kwg[1] for kwg in args._get_kwargs()]):
        return

    main_option = sys.argv[1]

    if main_option == "--generate":
        generate(
            temp_name=args.generate,
            output_path=args.output,
            db=args.db,
            execulde=args.execlude.split(","),
            overwrite=args.overwrite
        )
    
    elif main_option == "--add":
        add(
            path=args.add,
            multiple=args.multiple,
            overwrite=args.overwrite
        )
    
    elif main_option == "--export":
        #print(vault_path, "./")
        export()

if __name__ == "__main__":
    main()