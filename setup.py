import os 
import logging 
from setuptools import setup,find_packages 
from typing import List 

def get_requirements()->List[str]: 
    requirements_lst:List[str]=[]
    try:    
        with open("requiremnets.txt","r") as f: 
            lines=f.readlines()
            for line in lines: 
                requirement=line.strip()
                if requirement and requirement != "-e .": 
                    requirements_lst.append(requirement)
    
    except FileNotFoundError: 
        print("requirements.txt not found........")

    return requirements_lst 

setup(
    version="0.0.1", 
    author="mayur", 
    packages=find_packages(), 
    install_requires=get_requirements()
)