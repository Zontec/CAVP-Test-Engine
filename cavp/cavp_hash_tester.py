from vectors.sha.sha_test_mgr import SHA_TestMgr
from globals import TestAlgorithms
from log_mgr import LogMgr
from vectors.vector_test_enums import VectorHashTestEnum

logger = LogMgr(__name__)

class CAVP_HashTester():
    
    def __sha_tests_run_classic(self, hash_func, hash_type, hash_size):

        test_passed_cnt = 0
        test_mgr = SHA_TestMgr()
        tests = test_mgr.load_classic(test_group_index=1, hash_type=hash_type)
        out = bytes(hash_size)

        data_in_name = VectorHashTestEnum.DATA_IN
        data_len_name = VectorHashTestEnum.DATA_LEN
        exp_name = VectorHashTestEnum.EXP

        for test_vector in tests:
            res = hash_func(test_vector[data_in_name], test_vector[data_len_name], out)
            if res == 0 and test_vector[exp_name] == out:
                logger.log_ok("Test pass")
                test_passed_cnt += 1
            else:
                logger.log_error("Test fail")

        return (test_passed_cnt, len(tests))

    def __sha_tests_run_monte(self, hash_func, hash_type, hash_size):
        
        test_passed_cnt = 0
        test_mgr = SHA_TestMgr()
        tests = test_mgr.load_classic(test_group_index=1, hash_type=hash_type)
        out = bytes(hash_size)

        data_in_name = VectorHashTestEnum.DATA_IN
        data_len_name = VectorHashTestEnum.DATA_LEN
        exp_name = VectorHashTestEnum.EXP

        for test_vector in tests:
            res = hash_func(test_vector[data_in_name], test_vector[data_len_name], out)
            if res == 0 and test_vector[exp_name] == out:
                logger.log_ok("Test pass")
                test_passed_cnt += 1
            else:
                logger.log_error("Test fail")

        return (test_passed_cnt, len(tests))

    def __sha_tests_run_bits(self, hash_func, hash_type, hash_size):
        
        test_passed_cnt = 0
        test_mgr = SHA_TestMgr()
        tests = test_mgr.load_bits(test_group_index=1, hash_type=hash_type)
        out = bytes(hash_size)

        data_in_name = VectorHashTestEnum.DATA_IN
        data_len_name = VectorHashTestEnum.DATA_LEN
        exp_name = VectorHashTestEnum.EXP

        for test_vector in tests:
            res = hash_func(test_vector[data_in_name], test_vector[data_len_name], out)
            if res == 0 and test_vector[exp_name] == out:
                logger.log_ok("Test pass")
                test_passed_cnt += 1
            else:
                logger.log_error("Test fail")

        return (test_passed_cnt, len(tests))

    def __sha_tests_run(self, hash_func, hash_type, hash_size):

        res = (0, 0)
        
        t_res = self.__sha_tests_run_classic(hash_func, hash_type, hash_size)
        res = (res[0] + t_res[0], res[1] + t_res[1])

        #t_res = self.__sha_tests_run_bits(hash_func, hash_type, hash_size)
        #res = (res[0] + t_res[0], res[1] + t_res[1])

        #t_res = self.__sha_tests_run_monte(hash_func, hash_type, hash_size)
        #res = (res[0] + t_res[0], res[1] + t_res[1])

        return res

    def tests_run(self, hash_func, hash_type, hash_size):

        if hash_type == TestAlgorithms.SHA512:
            test_runner = self.__sha_tests_run
        elif hash_type == TestAlgorithms.SHA256:
            test_runner = self.__sha_tests_run
        else:
            test_runner = self.__sha_tests_run

        return test_runner(hash_func, hash_type, hash_size)