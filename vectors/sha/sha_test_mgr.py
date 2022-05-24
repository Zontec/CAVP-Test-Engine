import re
import os
from log_mgr import LogMgr
from globals import TestAlgorithms


logger = LogMgr(__name__)

class SHA_TestMgr():

    ABS_PATH = os.path.dirname(os.path.realpath(__file__))
    name_resolve_lookup = {
                'Msg' : 'Msg',
                'Len' : 'Len',
                'MD' : 'Exp',
            }
            
    def __read_and_parse(self, path, tests):
        with open(path, "r") as f:
            vector = {}
            for i in f:
                #bytes.fromhex(s)
                if re.match('[^\[].+ = .+', i) != None:
                    tmp = i.strip('\n').split(' ')
                    """"""
                    if tmp[0] == 'Len':
                        tmp[2] = int(tmp[2])
                    else:
                        tmp[2] = bytes.fromhex(tmp[2])
                    vector[SHA_TestMgr.name_resolve_lookup[tmp[0]]] = tmp[2]
                if len(vector) == 3:
                    tests += [vector.copy()]
                    vector = {}

    def load_classic(self, test_group_index, hash_type):
        tests = []
        if TestAlgorithms.SHA512 == hash_type:
            sha_type = "SHA512"
        elif TestAlgorithms.SHA256 == hash_type:
            sha_type = "SHA256"
        else:
            sha_type = "SHA1"

        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabytetestvectors/{sha_type}ShortMsg.rsp", tests)
        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabytetestvectors/{sha_type}LongMsg.rsp", tests)

        return tests
    
    def load_monte(self, test_group_index, hash_type):
        tests = []
        if TestAlgorithms.SHA512 == hash_type:
            sha_type = "SHA512"
        elif TestAlgorithms.SHA256 == hash_type:
            sha_type = "SHA256"
        else:
            sha_type = "SHA1"

        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabytetestvectors/{sha_type}ShortMsg.rsp", tests)
        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabytetestvectors/{sha_type}LongMsg.rsp", tests)

        return tests
    
    def load_bits(self, test_group_index, hash_type):
        tests = []
        if TestAlgorithms.SHA512 == hash_type:
            sha_type = "SHA512"
        elif TestAlgorithms.SHA256 == hash_type:
            sha_type = "SHA256"
        else:
            sha_type = "SHA1"

        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabittestvectors/{sha_type}ShortMsg.rsp", tests)
        self.__read_and_parse(SHA_TestMgr.ABS_PATH + f"/test_group{test_group_index}/shabittestvectors/{sha_type}LongMsg.rsp", tests)

        return tests