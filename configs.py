from globals import RunMode, LogMode, TestAlgorithms

class Configs:
    RUN_MODE = RunMode.DEBUG
    LOG_MODES = [
        LogMode.LOG_CONSOLE, 
        LogMode.LOG_FILE
    ]
    TESTS = [
        TestAlgorithms.SHA1,
        TestAlgorithms.SHA256,
        TestAlgorithms.SHA512,
    ]
    