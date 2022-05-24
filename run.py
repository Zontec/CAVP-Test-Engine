import sys
from shared import Shared
from globals import DrvHashType, ReturnStatus
from cavp_mgr import CAVP_Mgr
from log_mgr import LogMgr
from version import get_version_string
from configs import Configs
import argparse

logger = LogMgr(__file__)

def drv_init(drivers):
    pass

def main(argv):

    logger.log_session_id()
    logger.log("CAVP Tester started!")
    logger.log(f"Version: {get_version_string()}")

    lib = Shared()
    if lib.load('./targets/target.so') != ReturnStatus.SUCCESS:
        logger.error("Critical error when loading library!")
        return ReturnStatus.ERROR

    mgr = CAVP_Mgr(lib.get_library())
    logger.log("CAVP_Mgr ready")

    logger.log("Running tests!")

    cnt = 1
    tests_result_array = []
    for i in Configs.TESTS:
        logger.log(f"Test round: {cnt}")
        logger.log(f"Tests type: {i}")
        res = mgr[i]()
        tests_result_array += [{i : res}]
        cnt += 1
    
    logger.log("Testing done!")
    logger.log("Final result:")
    for result in tests_result_array:
        for key in result:
            logger.log(f"{key} - {result[key][0]} of {result[key][1]}")

    


if __name__ == "__main__":
    main(sys.argv)