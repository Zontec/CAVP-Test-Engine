from vectors.sha.sha_test_mgr import SHA_TestMgr
from log_mgr import LogMgr
from hash_drv import HashDrv
from cavp.cavp_hash_tester import CAVP_HashTester
from globals import DrvHashType, HashSize, TestAlgorithms

logger = LogMgr(__name__)

class CAVP_Mgr():

    def __init__(self, driver_lib):
        self.__init_handlers()
        self.drv_lib = driver_lib

    def __init_handlers(self):
        self.handlers = {
                TestAlgorithms.SHA1     :   self.sha1_test,
                TestAlgorithms.SHA256   :   self.sha256_test,
                TestAlgorithms.SHA512   :   self.sha512_test
            }

    def __getitem__(self, index):
        if index not in self.handlers:
            return None
        return self.handlers[index]

    def __hash_test(self, hash_type, drv_hash_type):

        hash_tester = CAVP_HashTester()
        hash_drv = HashDrv()    
        hash_drv.set_library(self.drv_lib)

        hash_function = hash_drv.get_instance(drv_hash_type)
        return hash_tester.tests_run(hash_function, hash_type, HashSize.get_hash_size(drv_hash_type))

    def sha512_test(self):
        return self.__hash_test(TestAlgorithms.SHA512, DrvHashType.DRV_SHA512)

    def sha1_test(self):
        return self.__hash_test(TestAlgorithms.SHA1, DrvHashType.DRV_SHA1)

    def sha256_test(self):
        return self.__hash_test(TestAlgorithms.SHA256, DrvHashType.DRV_SHA256)
    
    