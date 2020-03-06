import logging
from logging.handlers import RotatingFileHandler

import time

import pymysql 
import mysql_requestcount_property

logging.Formatter.converter = time.gmtime
logger = logging.getLogger(__name__)
fileHandler = RotatingFileHandler('./log/requestcount_resetor.log', maxBytes=1024 * 1024 * 1024 * 9, backupCount=9)
fileHandler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] >> %(message)s'))
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
logger.info("every package loaded and start logging")

if __name__ == '__main__':
    connection = pymysql.connect(host=mysql_requestcount_property.hostname, user=mysql_requestcount_property.user, password=mysql_requestcount_property.password, db=mysql_requestcount_property.database, charset=mysql_requestcount_property.charset)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    logger.info("database connection opened")

    cursor.execute("UPDATE APIKey SET currentReqCount = 0;")
    logger.info("currentRecCount reseted in APIKey")

    connection.commit()
    connection.close()
    logger.info("database connection closed")

    logger.info("operation ended")
