import logging
import os
import random
from datetime import datetime, date, time
from configs import Configs
from globals import RunMode, LogMode


class LogNameGenearator():

    def gen_file_name(session_id):
        now = datetime.now()
        return f'{session_id}_{now.strftime("%m%d%Y_%H%M%S")}.log'

    def gen_dir_name(session_id):
        return "logs/" + LogNameGenearator.gen_file_name(session_id)


class LogConsoleColors():

    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    CYAN = "\x1b[36m"
    YELLOW = "\x1b[33m"


class LogExeption(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class LogFileNotCreated(LogExeption):

    def __init__(self, msg):
        super().__init__(f"Log file not created: {msg}")


class LogDirNotCreated(LogExeption):

    def __init__(self, msg):
        super().__init__(f"Log directory not created: {msg}")


class LogMgr():
    
    __CORE_LOG_DIRCTORY__ = None
    __LOG_SESSION_ID__ = None

    LOG = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

    def __init__(self, name, log_level=DEBUG):
        self.session_id = self.__create_logging_session()

        if LogMode.LOG_FILE in Configs.LOG_MODES:
            self.__file_log_init(name)
        if LogMode.LOG_CONSOLE in Configs.LOG_MODES:
            self.__console_log_init(name)
        
        self.set_log_level(log_level)

    def __file_log_init(self, name):

        self.file_logger = logging.Logger(name)

        try:
            dir_path = self.__create_logging_directory(self.session_id)
            self.__create_logging_file(dir_path, self.session_id)
        except LogFileNotCreated as ex:
            raise BaseException("Logger init error while log file create!")
        except LogDirNotCreated as ex:
            raise BaseException("Logger init error while log dir create!")

        f_handler = logging.FileHandler(self.log_filename)
        f_format = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]%(message)s')
        f_handler.setFormatter(f_format)
        self.file_logger.addHandler(f_handler)

    def __console_log_init(self, name):
        
        self.console_logger = logging.Logger(name)
        
        c_handler = logging.StreamHandler()

        cyan = LogConsoleColors.CYAN
        reset = LogConsoleColors.RESET
        c_format = logging.Formatter(f'[{cyan}%(name)s{reset}][%(levelname)s]%(message)s')
        c_handler.setFormatter(c_format)
        self.console_logger.addHandler(c_handler)

    def __create_logging_session(self):

        if LogMgr.__LOG_SESSION_ID__ == None:
            LogMgr.__LOG_SESSION_ID__ = str(random.randint(0, 10**6))[0:6]
        return LogMgr.__LOG_SESSION_ID__

    def __create_logging_directory(self, session_id):

        if LogMgr.__CORE_LOG_DIRCTORY__ == None:
            LogMgr.__CORE_LOG_DIRCTORY__ = LogNameGenearator.gen_dir_name(session_id)
            try:
                os.mkdir(LogMgr.__CORE_LOG_DIRCTORY__)
            except:
                raise LogFileNotCreated(f"{LogMgr.__CORE_LOG_DIRCTORY__} can not be created!")
        return LogMgr.__CORE_LOG_DIRCTORY__
    
    def __create_logging_file(self, dir, session_id):

        self.log_filename = LogNameGenearator.gen_file_name(session_id)
        self.log_filename = f"{LogMgr.__CORE_LOG_DIRCTORY__}/{self.log_filename}"
        try:
            with open(self.log_filename, "w+") as f:
                pass
        except FileNotFoundError as ex:
            raise LogFileNotCreated(f"{self.log_filename} can not be created!")
        return self.log_filename

    def __message_color(self, message, color, is_bold=False):

        reset = LogConsoleColors.RESET
        bold = LogConsoleColors.BOLD
        if is_bold:
            return f"{color}{bold}{message}{reset}"
        return f"{color}{message}{reset}"

    def __log_file(self, logging_level, message):
        if LogMode.LOG_FILE in Configs.LOG_MODES:
            self.file_logger.log(logging_level, message)

    def __log_console(self, logging_level, message):
        if LogMode.LOG_CONSOLE in Configs.LOG_MODES:
            self.console_logger.log(logging_level, message)

    def set_log_level(self, level):

        cur_level = None

        if level == LogMgr.LOG:
            cur_level = logging.INFO
        elif level == LogMgr.DEBUG:
            cur_level = logging.DEBUG
        elif level == LogMgr.ERROR:
            cur_level = logging.ERROR
        elif level == LogMgr.CRITICAL:
            cur_level = logging.CRITICAL
        elif level == LogMgr.WARNING:
            cur_level = logging.WARNING
        
        if cur_level != None:
            if LogMode.LOG_FILE in Configs.LOG_MODES:
                self.file_logger.setLevel(cur_level)
            if LogMode.LOG_CONSOLE in Configs.LOG_MODES:
                self.console_logger.setLevel(cur_level)

    def log_ok(self, message):

        green = LogConsoleColors.GREEN
        reset = LogConsoleColors.RESET
        bold = LogConsoleColors.BOLD
        self.__log_file(logging.INFO, f"[OK]{message}")
        self.__log_console(logging.INFO, f"[{green}{bold}OK{reset}]{message}")
    
    def log_error(self, message):

        red = LogConsoleColors.RED
        reset = LogConsoleColors.RESET
        bold = LogConsoleColors.BOLD
        self.__log_console(logging.INFO, f"[{red}{bold}ERROR{reset}]{message}")
        self.__log_file(logging.INFO, f"[ERROR]{message}")

    def log(self, message):
        
        self.__log_console(logging.INFO, message)
        self.__log_file(logging.INFO, message)

    def debug(self, message):

        if Configs.RUN_MODE == RunMode.DEBUG:
            self.__log_console(logging.DEBUG, message)
            self.__log_file(logging.DEBUG, message)
    
    def warning(self, message):

        self.__log_console(logging.WARNING, self.__message_color(message, LogConsoleColors.YELLOW))
        self.__log_file(logging.WARNING, message)
    
    def error(self, message):

        self.__log_console(logging.ERROR, self.__message_color(message, LogConsoleColors.RED))
        self.__log_file(logging.ERROR, message)

    def critical(self, message):
        
        self.__log_console(logging.CRITICAL, self.__message_color(message, 
                            LogConsoleColors.RED, is_bold=True))
        self.__log_file(logging.CRITICAL, message)

    def log_session_id(self):
        self.__log_console(logging.INFO, f"@@@ LOG SESSION ID: "
                    f"{LogConsoleColors.BOLD}{LogMgr.__LOG_SESSION_ID__}{LogConsoleColors.RESET} @@@")