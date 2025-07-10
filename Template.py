from pathlib import Path
import os 
import logging 

project_name="loan_approval" 

logging.basicConfig(level=logging.INFO,format="[%(asctime)s:%(message)s]")

list_of_file=[ 
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.ymal",
    "params.ymal", 
    "schema.ymal", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_file: 
    filepath=Path(filepath)
    file_dir,filename=os.path.split(filepath)

    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating {file_dir} for {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath,"w") as f:
            pass 
        logging.info(f"creating empty file for {filename}")

    else: 
        logging.info(f"{filename} is already exists") 



