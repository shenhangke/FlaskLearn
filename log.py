'''

@File    :   log.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-07-03 10:04   shenhangke      1.0         None
---------------------
 
'''

"""
    this unit record the logger function and wrap a class to use log
    use basicConfig to set the level of log and whether save to file
"""

import logging

logging.basicConfig(level=logging.ERROR,filename="info.log")
logging.info("print info")
logging.warning("print warnning")
logging.error("there is a error")


