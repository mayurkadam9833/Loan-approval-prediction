import os 
from box.exceptions import BoxValueError 
import yaml
from src.loan_approval.logging import logger
import json 
import joblib 
from ensure import ensure_annotations 
from box import config_box 
from pathlib import Path 
from typing import List


@ensure_annotations 
def read_ymal(path_to_ymal:Path)->config_box:
    try: 
        with open(path_to_ymal,"r")as ymal_file:
            content=yaml.safe_load(ymal_file)
            logger.info(f"yaml file {path_to_ymal} load sucessfully.....")
            return config_box(content)
    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e: 
        raise e 

@ensure_annotations 
def create_directorires(path_to_dir:list,verbose=True): 
    for path in path_to_dir: 
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"creating directory at {path}")
