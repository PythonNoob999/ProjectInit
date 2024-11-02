project-init: A Rapid Project Structure Generator 
```
project-init is a command-line tool designed to streamline the process of creating new projects by automatically generating basic project structures based on predefined templates.

It's a handy tool for developers who want to quickly get started on a new project without having to manually set up the initial files and directories.
```

## **Installation**
To install project-init, use pip:

```bash
pip install project-init
```

## **Usage**
```bash
project-init --generate <template_name> --output <output_directory> --db <supported_database>
```

`--generate`: Specifies the desired template to use.

`--output`: Sets the output directory for the generated project.

`--db`: Adds a db file to manage the database with the your diserd DB

## Examples
Create a new telegram bot project:
```bash
project-init --generate TelegramBot --output my_python_project --db prisma
```

Generate a API structure:
```bash
project-init --generate API --output my_web_app --db sqlite
```

You can also make your own templates
```bash
project-init --add PATH/TO/TEMPLATE
```

then generate it
```bash
project-init --add MyTemplates/WebApp
# saved in vault ✅
project-init --generate WebApp
```

## TODO
1. remove ready templates [ ✔️ ]
2. let user edit vault path & move it [ ]
3. add a marketplace for templates [ ]

## **Contributing**
We welcome contributions! Feel free to submit pull requests or issues on our GitHub repository.

## **License**
project-init is distributed under the MIT License.
