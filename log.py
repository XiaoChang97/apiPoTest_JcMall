import logging
import time
import os

class Logger:
    def __init__(self,name,CmdLevel=logging.INFO, FileLevel=logging.INFO):
        # 创建一个 logger
        self.logger = logging.getLogger(name)
        # 设置Log等级总开关
        self.logger.setLevel(CmdLevel)
        # 创建 handler，用于日志写入
        currTime = time.strftime("%Y-%m-%d")
        log_path = os.path.abspath(os.path.join(os.getcwd(), "")) + '/Logs/'
        log_name = log_path + currTime + '.log'
        fh = logging.FileHandler(log_name, mode='a')  # mode = 'a' 为在原日志上追加，'w'为覆盖 输出日志到文件
        fh.setLevel(FileLevel) # 输出到 file 的日志等级
        ch = logging.StreamHandler() # 输出日志到控制台
        ch.setLevel(FileLevel) # 输出到控制台的日志等级
        # 定义日志handler的输出格式
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        # 添加 logger 到 handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)