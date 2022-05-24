import ctypes
from globals import DrvHashType, HashSize, ReturnStatus
from log_mgr import LogMgr

logger = LogMgr(__name__)

class HashDrv():

    def __init__(self):
        self.lib = None
        self.__init_lookup()
        logger.debug("Hash driver lookup ready")

    def __init_lookup(self):
        self.lookup = {
                DrvHashType.DRV_SHA1     : 'sha1',
                DrvHashType.DRV_SHA224   : 'sha224',
                DrvHashType.DRV_SHA256   : 'sha256',
                DrvHashType.DRV_SHA384   : 'sha384',
                DrvHashType.DRV_SHA512   : 'sha512',
                DrvHashType.DRV_SHA3_224 : 'sha3_224',
                DrvHashType.DRV_SHA3_256 : 'sha3_256',
                DrvHashType.DRV_SHA3_384 : 'sha3_384',
                DrvHashType.DRV_SHA3_512 : 'sha3_512',
                DrvHashType.DRV_MD5      : 'md5',
            }

    def __get_instance(self, hash_type):

        hash_function_name = self.lookup[hash_type]
        def hash_func(data, data_len, hash_out):

            self.lib[hash_function_name].argtypes = (ctypes.c_char_p,ctypes.c_int,ctypes.c_char_p)
            tmp = ctypes.create_string_buffer(HashSize.get_hash_size(hash_type))
            din = ctypes.create_string_buffer(data)

            if data == None or data_len < 0:
                logger.error(f"Incorrect hash function input: \n{data_len}\n{data}")
                return ReturnStatus.ERROR
            return self.lib[hash_function_name](din, data_len, hash_out)
        return hash_func

    def set_library(self, library):
        self.lib = library

    def get_instance(self, hash_type=DrvHashType.DRV_SHA256):
        if hash_type not in self.lookup:
            logger.error(f"Unknown driver hashtype: {hash_type}")
            return ReturnStatus.ERROR
        return self.__get_instance(hash_type)
