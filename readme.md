ProjectInit: A Rapid Project Structure Generator
```
ProjectInit is a command-line tool designed to streamline the process of creating new projects by automatically generating basic project structures based on predefined templates.

It's a handy tool for developers who want to quickly get started on a new project without having to manually set up the initial files and directories.
```

## **Installation**
To install ProjectInit, use pip:

```bash
pip install projectinit
```

## **Usage**
```bash
projectinit --template <template_name> --output <output_directory> --db <supported_database>
```

`--template`: Specifies the desired template to use.

`--output`: Sets the output directory for the generated project.

`--db`: Adds a db file to manage the database with the your diserd DB

## Examples
Create a new telegram bot project:
```bash
projectinit --template TelegramBot --output my_python_project --db prisma
```

Generate a API structure:
```bash
projectinit --template API --output my_web_app --db sqlite
```

You can also make your own templates
```bash
projectinit --add PATH/TO/TEMPLATE
```


### Ready Templates
Currently, ProjectInit offers the following templates:

1. **TelegramBot (Simple/Large): a telegram bot project with pyrogram lib.**

2. **python-project: A Python project template with a main.py file and a readme.md file.**

3. **API (FastAPI/Flask): a python project with FastAPI or Flask.**

## **Contributing**
We welcome contributions! Feel free to submit pull requests or issues on our GitHub repository.

## **License**
ProjectInit is distributed under the MIT License.