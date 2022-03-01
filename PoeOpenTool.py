import os
import sys
import subprocess

global __author__
global __Version__

__author__ = 'Wade.Yeh'
__Version__ = '20220302A'

def main():
    os.chdir(r'D:/Game/3.BIG/online/POE/Tool/Awakened.PoE.Trade')
    os.system(r'"D:\Game\3.BIG\online\POE\Tool\Awakened.PoE.Trade\Awakened.PoE.Trade.3.17.10004.1.exe"')
    os.chdir(r'D:/Game/3.BIG/online/POE/°ê»ÚªA/POE-Trades-Companion/POE-Trades-Companion-AHK-v1-15-BETA_9995')
    os.system(r'"D:\Game\3.BIG\online\POE\Tool\Awakened.PoE.Trade\Awakened.PoE.Trade.3.17.10004.1.exe"')
    return


if __name__ == "__main__":
    print '=========== Script Start =========='
    print 'Run Script: '+sys.argv[0]
    print 'Script Version: '+ __Version__ + '(' + __author__ + ')'
    main()
    print '============ Script End ===========  '+ __Version__ + '(' + __author__ + ')'
    os.system("pause")
    sys.exit()
