
import draw_chartc as dc
import math
import pandas as pd
print(pd.__version__) # for the record

import mplfinance as mpf
print(mpf.__version__) # for the record

import time
from datetime import timezone
from datetime import datetime  
from datetime import timedelta

from threading import Event, Thread
from matplotlib.pyplot import plot, draw, show

#global to execute
tick_sec30_cnt = 0
member_30sec = 0
tick_30s = False

class RepeatedTimer:

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.start()

    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)

    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def stop(self):
        self.event.set()
        self.thread.join()

def main():
    timer = dc.RepeatedTimer(5, dc.execute) #5 sec
    print("Hello World!")

if __name__ == "__main__":
    main()



msg = "Hello World"
print(msg)


def execute():
    """Execute this code every timer tick (seconds) """
    sym_name = ["BNB", "ETH", "LTC", "XRP", "XMR", "EOS","ZEC","XLM","BCH","ADA","DASH","IOTA","BTC"]
    #global tick_cnt    # Needed to modify global copy of tick_cnt
    global tick_sec30_cnt
    global member_30sec
    global tick_30s


    #symbol prices every tick of 5 sec
    #print("tick_cnt,tick_sec30_cnt,tick_1d_cnt",gv.tick_cnt,tick_sec30_cnt,tick_1d_cnt)
    
    print("tick_sec30_cnt, member_30sec",tick_sec30_cnt,member_30sec)
    if   tick_30s :
        #print("0: member_30sec = ",member_30sec)
        for j in range(13) : #0:3-1
            if j == member_30sec:
                #'C:/CHART_FILES/narae/Desktop/alice.txt'
                f_name = sym_name[j]
                file_name = 'C:/CHART_FILES/' + f_name + '.cvs'
                print("file_name",file_name)
                df = pd.read_csv(file_name,index_col=0,parse_dates=True)
                df.index.name = 'Date'
                df.shape
                df.head(3)
                df.tail(3)
                (20, 5)   #, figratio=(10,5)   (20, 5)

                swH      = df.loc[:,'swH']
                reddec   = df.loc[:,'reddec']
                print("reddec",reddec)
                greenasc = df.loc[:,'greenasc']
                print("greenasc",greenasc)
                stmac     = df.loc[:,'STMACD']
                stsig     = df.loc[:,'STSIG']
                sigdn     = df.loc[:,'crsDn']
                sigup     = df.loc[:,'crsUp']

                apd = [
                         mpf.make_addplot(swH,scatter=True), 
                         mpf.make_addplot(greenasc,linestyle='dashdot',color='g') #dashdot lines for bollinger
                         #mpf.make_addplot(df['sigdn'],scatter=True,markersize=100,marker='v',color='c'),
                         #mpf.make_addplot(df['sigup'],scatter=True,markersize=100,marker='^',color='m'),
                         #mpf.make_addplot((df['stmac']),panel='lower',color='g',linestyle='dotted',secondary_y=False),
                         #mpf.make_addplot((df['stsig']),panel='lower',color='#e41a1c',linestyle='dotted',secondary_y=False)
                       ]
                mpf.plot(df,mav=(5,10,20),addplot=apd, type='candle',figratio=(10,5), style='starsandstripes',
                         savefig='candlestick_mpf_mav.png')

                #apd  = mpf.make_addplot(red1ine)
                #mpf.make_addplot(red1ine,linestyle='dashdot',color='r'), #dashdot lines for bollinger
                #mpf.plot(df,mav=(5,10,20),alines=two_points, addplot=apd, type='ohlc',title=sym_name[j]) #type='candle'
                #mpf.plot(df,mav=(5,10,20),type='ohlc',title=sym_name[j],alines=red1ine,style='charles') #type='candle'


                print("tick_sec30_cnt, member_30sec",tick_sec30_cnt,member_30sec)

        if member_30sec == 12:
            member_30sec = 0 
        else:
            member_30sec += 1 
    
    tick_30s = False;
    if tick_sec30_cnt == 6 :#every 30 sec 1m kline symbol
        tick_sec30_cnt = 0
        tick_30s = True
    else:
        tick_sec30_cnt += 1

# start timer and execute Excute with 0 arguments
#print("R:gv.tick_cnt = ",gv.tick_cnt)

# stop timer
# timer.stop()









