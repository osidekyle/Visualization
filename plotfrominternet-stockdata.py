import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates



def bytespdate2num(encoding='utf-8'):
    def bytesconverter(b):
        s=b.decode(encoding)
        return mdates.datestr2num(s)
    return bytesconverter


def graph_data():
    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))





    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code=urllib.request.urlopen(stock_price_url).read().decode()

    stock_data=[]
    split_source=source_code.split('\n')
    for line in split_source[1:]:
        split_line=line.split(',')
        if len(split_line)==7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num()})


    plt.plot_date(date,closep,'-',label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
    plt.xlabel("Date")
    ax1.xaxis.label.set_color('g')
    ax1.yaxis.label.set_color('g')
    plt.ylabel("Price")
    ax1.set_yticks([250,500,750])
    ax1.fill_between(date,closep,closep[0],where=(closep>closep[0]),facecolor='g',alpha=0.3)
    ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r',alpha=.3)
    ax1.plot([],[],color='g',label="Gains")
    ax1.plot([], [], color='r', label="Loss")
    plt.subplots_adjust(bottom=.2)
    plt.legend()
    ax1.tick_params(axis='x',colors='g')
    ax1.tick_params(axis='y', colors='g')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('g')
    ax1.axhline(closep[0],linewidth=2,color='k')
    plt.title("Stock Price Over Time")
    plt.show()

graph_data()
