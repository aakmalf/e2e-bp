import os 
import sys
from pathlib import Path

list_of_files = [
    "requirements.txt",
    "app.py", 
    "setup.py",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_modelling.py",
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/predict_pipeline.py",
    "experiments/experiment.ipynb"
]

for filepaths in list_of_files:
    path = Path(filepaths)
    file_dir, file_name = os.path.split(path)
    
    #check if it has folder to create folder
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    #check if file exists or not and the size of file is 0    
    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, 'w') as f:
            pass #create empty file