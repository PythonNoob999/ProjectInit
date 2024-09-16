from setuptools import setup, find_packages

setup(
    name="ProjectInit",
    version="0.0.1beta",
    description="a tool to insta-create your project structure",
    author="SpicyPenguin",
    packages=find_packages(include=["ProjectInit", "ProjectInit.vault", "ProjectInit.dbs"]),
    package_data={"": ["*.prisma", "*.json", "vault"]},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "project-init=ProjectInit.cli:main"
        ]
    },
    install_requires=["kvsqlite", "prisma", "pyrogram", "flask", "fastapi"]
)