'''
Created on Mar 19, 2019

@author: param
'''
import requests

class Crawler(object):
    
    
    def myDict(self,txt):
        try:
            res={}
            res[txt.split('=')[0]]=(txt.split('=')[1]).replace('>','')
            return res
        except IndexError:
            pass
    
    
    def __init__(self, txt):
        
#         for line in txt:
#             print(line +',' + str(ord(line)))
#         
        for line in txt.split(chr(10)):
            blk=line.split()
            tag=blk[0]split.replace('<','').replace('!','')
            vals=blk[1:]
            if len(blk)>2:
                self.__dict__[tag]={}
                for d in vals:
                    self.__dict__[tag].update(self.myDict(d))
            
            
        pass
    
        




lkURL='https://en.wikipedia.org/wiki/List_of_constituencies_of_the_Lok_Sabha'

obj=requests.get(lkURL).text

res=Crawler(obj)


pass