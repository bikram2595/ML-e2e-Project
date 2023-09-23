import os #for generic folder path
from pathlib import Path
import logging #basic logging

logging.basicConfig(level=logging.INFO) #Basic logging info

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py", #create a source folder and __init__.py to package it
    f"src/{project_name}/components/data_ingestion.py", #creating components folder
    f"src/{project_name}/components/data_transformation.py", #creating components
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py", #__init__ because when we compile it, it should become a package
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/pipelines/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating folder: {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


else:
    logging.info(f"{filename} already exists")

#anyfile present in the list ,will not get created and if not present in the list then the folder and file will be created