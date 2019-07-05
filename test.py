'''

@File    :   test.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-07-01 22:39   shenhangke      1.0         None
---------------------
 
'''

import os.path

def bytesToStr(bytes):
    return str(bytes)

if __name__ == "__main__":
    print(os.path.abspath("."))
    print(os.path.curdir)  # os.path.curdir is .
    print(bytesToStr(b'\xa80\xc1fr\xc9\xcb\xf8+\xec\xa8\x85+5\x96u'))
