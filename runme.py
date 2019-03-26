'''
Created on Mar 19, 2019
@author: param
'''


import matplotlib.pyplot as plt
import pandas as pd


class DataReader:
    
    @staticmethod
    def test():
        data=pd.read_csv('data//loksabha.csv',delimiter=',')
        print(data)
        
    @staticmethod    
    def tn_by_party():
        data=pd.read_csv('data//loksabha.csv',delimiter=',')
        #tn=data[data.NAME.str.contains('Tamil')][data.Position<4][['Year','PARTY','PCNAME','Position']]
        tn=data[data.NAME.str.contains('Tamil')][data.Position<4][['Year','PARTY','PCNAME','Position','CVOTES']]
        tn2=tn.groupby('PARTY').cumsum()
        for r in tn2:
            print(r)
        
        
    


if __name__ == '__main__':
    DataReader.tn_by_party()