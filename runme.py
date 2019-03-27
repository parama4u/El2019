'''
Created on Mar 19, 2019
@author: param
'''


import matplotlib.pyplot as plt
import pandas as pd
from unittest.mock import inplace


class DataReader:
    
    @staticmethod
    def test():
        data=pd.read_csv('data//loksabha.csv',delimiter=',')
        print(data)
        
    @staticmethod
        
    def tn_by_party():
        data=pd.read_csv('data//loksabha.csv',delimiter=',')
        tn=data[data.NAME.str.contains('TAMILNADU')][['Year','PARTY','CVOTES']]
        tn2=tn.groupby(['Year','PARTY'])['CVOTES'].sum().unstack().plot(kind='bar',stacked=True)
        
        ax=plt.gca()
        ax.ticklabel_format(axis='y',style='plain',useOffset=False)
        plt.legend(loc='center left', bbox_to_anchor=(0.9, 0.5),
          ncol=2, fancybox=True, shadow=True)
        plt.show()
        
    


if __name__ == '__main__':
    DataReader.tn_by_party()