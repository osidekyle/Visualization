import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style
style.use('ggplot')
MA1=10
MA2=30
def moving_average(values,window):
    weights=np.repeat(1.0,window)/window
    smas=np.convolve(values,weights,'valid')
    return smas
def high_minus_low(highs,lows):
    return highs-lows



def bytespdate2num(encoding='utf-8'):
    def bytesconverter(b):
        s = b.decode(encoding)
        return mdates.datestr2num(s)

    return bytesconverter


def graph_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num()})


    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    font_dict={'family':'serif',
               'color':'darkred',
               'size':15}
    bbox_props=dict(boxstyle="round",fc='w',ec='k',lw=1)



    ax1 = plt.subplot2grid((6, 1), (0, 0),rowspan=1,colspan=1)
    plt.title("Stock")
    plt.ylabel("H-L")
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1,sharex=ax1)
    plt.xlabel("Date")
    plt.ylabel("Price")
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1,sharex=ax1)
    plt.ylabel("MAvg")



    ax2.annotate(str(closep[0]), (date[0], closep[0]), xytext=(date[0], closep[0]), bbox=bbox_props)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(nbins=7,prune='upper'))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(nbins=4,prune='upper'))
    ax2.grid(True)

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.setp(ax1.get_xticklabels(),visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5,prune='lower'))


    ma1=moving_average(closep,MA1)
    ma2 = moving_average(closep, MA2)
    start=len(date[MA2-1:])
    candlestick_ohlc(ax2, ohlc[-start:], width=.4, colorup='g', colordown='r')
    h_1=list(map(high_minus_low,highp,lowp))
    ax1.plot_date(date[-start:],h_1[-start:],'-',label="H-L")
    ax3.plot(date[-start:],ma1[-start:],linewidth=1,label=(str(MA1)+"MA"))
    ax3.plot(date[-start:], ma2[-start:],linewidth=1,label=(str(MA2)+"MA"))
    ax3.fill_between(date[-start:],ma2[-start:],ma1[-start:],
                     where=(ma1[-start:]<ma2[-start:]),
                     facecolor='r',edgecolor='r',alpha=0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5)


    ax2v=ax2.twinx()
    ax2v.fill_between(date[-start:],0,volume[-start:],facecolor='blue',alpha=0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0,3*volume.max())
    ax2v.plot([],[],color='blue',label='Volume')


    ax1.legend()
    leg=ax1.legend(loc=9,ncol=2,prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    ax2v.legend()
    leg = ax2v.legend(loc=9, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)
    ax3.legend()
    leg = ax3   .legend(loc=9, ncol=2, prop={'size': 11})
    leg.get_frame().set_alpha(0.4)
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()



graph_data()
