import os 
import sys

import pandas as pd
import numpy as np
import pickle
from src.exception import CustomException

def save_object(file_path, obj):
   try :
      dir_parth = os.path.dirname(file_path)
      os.makedirs(dir_parth, exist_ok=True)

      with open (file_path, "wb") as file:
         pickle.dump(obj, file)
         
   except Exception as e:
      raise CustomException(e, sys)
