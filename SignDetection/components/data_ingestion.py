from SignDetection import logger
from SignDetection.exception import CustomException
import os ,sys
try:
    a= 3/"S"
except Exception as e:
    raise CustomException(e ,sys)