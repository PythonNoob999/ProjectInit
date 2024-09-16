## Main Options
1. `--generate`: pass the template name to generate it
2. `--add`: pass the PATH to your own template and it will be saved in your device
3. `--export`: exports all of your current templates to share with your friend

## Geenrate Options
1. `--output`: pass the path that you want to generate the template in (defaults to current path)
2. `--db`: pass one of the supported database options Sqlite,Kvsqlite,Prisma (defaults to None)
3. `--execlude`: path the name of file that you want to NOT generate with the template (defaults to None)
4. `--overwrite`: copys the template anyway if it already exists in your output_path

## Add Options
1. `--multiple`: set to true if the PATH you are passing is a folder of multiple templates
2. `--overwrite`: copys the template anyway if it already exists in your vault