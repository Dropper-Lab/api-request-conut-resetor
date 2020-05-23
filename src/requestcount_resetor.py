#!/usr/bin/env python3

"""
version : v1.0.0

MIT License

Copyright (c) 2020 Dropper Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
    connection = pymysql.connect(host=mysql_requestcount_property.hostname, user=mysql_requestcount_property.user,
                                 password=mysql_requestcount_property.password, db=mysql_requestcount_property.database,
                                 charset=mysql_requestcount_property.charset)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    logger.info("database connection opened")

    cursor.execute("UPDATE APIKey SET currentReqCount = 0;")
    logger.info("currentRecCount reseted in APIKey")

    connection.commit()
    connection.close()
    logger.info("database connection closed")

    logger.info("operation ended")
