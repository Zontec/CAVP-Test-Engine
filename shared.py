import ctypes
import numpy
from log_mgr import LogMgr
from globals import ReturnStatus

logger = LogMgr(__name__)

class Shared():

    def __init__(self):
        self.library = None

    def load(self, path):

        ret_code = ReturnStatus.SUCCESS
        logger.log(f"Loading library from path: {path}")
        try:
            self.library = ctypes.cdll.LoadLibrary(path)
        except Exception as ex:
            logger.critical("Library not found or loading error!")
            ret_code = ReturnStatus.ERROR
        else:
            logger.log(f"Loading done!")
        logger.debug(f"Load library return code: {ret_code}")
        return ret_code

    def get_library(self):
        return self.library
        
        
