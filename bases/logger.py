import logging.handlers
import time


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志级别
            cls.logger.setLevel(logging.INFO)

            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理器 文件
            file_name = "../log/log-{}.log".format(time.strftime("%Y_%m_%d %H_%M_%S"))
            th = logging.handlers.TimedRotatingFileHandler(filename=file_name,
                                                           when="midnight", interval=1, backupCount=30,
                                                           encoding="utf-8")
            # 获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] -%(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器添加到处理器
            sh.setFormatter(fmt)
            th.setFormatter(fmt)

            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger
