import logging 
import os 
import sys 

log_str="[%(asctime)s:%(module)s:%(filename)s:%(message)s]"

log_dir="logs"

log_path=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=log_str, 
    handlers=[
        logging.FileHandler(log_path), 
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger("loan_approval_prediction_logger")