import pandas
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
from scipy.stats import norm


FILE_PATH = "files/IBM.csv"
OUTPUT_FILE_PATH = "files/results.csv"


def calculate_daily_stock_variance(open_value: float, close_value: float):
    return 100 * (open_value - close_value) / open_value


def main():
    content = pandas.read_csv(FILE_PATH)
    content["Daily Stock"] = 100 * (content["Open"] - content["Close"]) / content["Open"]
    content.to_csv(OUTPUT_FILE_PATH)


    

    Daily_stock = list(content.iloc[:,7])
    Daily_stock_freq = {}
    for val in Daily_stock:
      Daily_stock_freq[ val ] = Daily_stock.count(val)

    
    plt.bar(Daily_stock_freq.keys() , Daily_stock_freq.values(), width=0.8)
    plt.xlim(-15,25)
    plt.xticks(np.arange(-15,25,1))
    plt.xlabel("Daily Stocks")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.show() 
    
    mean,std = norm.fit(Daily_stock)
  
    sn.distplot( content.iloc[:,7], hist=True , rug=True )
    plt.xlim(-15,25)
    x= np.linspace(-15,25,100)
    y=norm.pdf(x,mean,std)
    plt.plot(x,y, color ='r')
    plt.xlabel('Daily stocks')
    plt.ylabel('Frequency')
    plt.text(-2,0.45,r"Gaussian fit on Stocks")
 
    #min, max values :
    min_stock = np.min(Daily_stock)
    max_stock = np.max(Daily_stock)
    
    
    
if __name__ == "__main__":
    main()
