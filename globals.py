class DrvHashType:
    DRV_SHA1        = 1
    DRV_SHA224      = 2
    DRV_SHA256      = 3
    DRV_SHA384      = 4
    DRV_SHA512      = 5
    DRV_SHA3_224    = 6
    DRV_SHA3_256    = 7
    DRV_SHA3_384    = 8
    DRV_SHA3_512    = 9
    DRV_MD5         = 10

class HashSize:
    HASH_SIZE_MAP = {
        DrvHashType.DRV_SHA1     : 20,
        DrvHashType.DRV_SHA224   : 28,
        DrvHashType.DRV_SHA256   : 32,
        DrvHashType.DRV_SHA384   : 48,
        DrvHashType.DRV_SHA512   : 64,
        DrvHashType.DRV_SHA3_224 : 28,
        DrvHashType.DRV_SHA3_256 : 32,
        DrvHashType.DRV_SHA3_384 : 48,
        DrvHashType.DRV_SHA3_512 : 63,
        DrvHashType.DRV_MD5      : 16,
    }

    def get_hash_size(drv_hash_type):
        if drv_hash_type not in HashSize.HASH_SIZE_MAP:
            return 0
        return HashSize.HASH_SIZE_MAP[drv_hash_type]


class RunMode:
    RELEASE = 'release'
    DEBUG = 'test'
    TEST = 'debug'

class LogMode:
    LOG_FILE = 'log_file'
    LOG_CONSOLE = 'log_console'

class ReturnStatus:
    SUCCESS = 0
    ERROR = 1

class TestAlgorithms:
    SHA1 = "sha1_test"
    SHA224 = "sha224_test"
    SHA256 = "sha256_test"
    SHA384 = "sha384_test"
    SHA512 = "sha512_test"