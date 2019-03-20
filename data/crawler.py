'''
Created on Mar 19, 2019

@author: param
'''
import requests
import re



class HtmlDict():
    
    def __init__(self, txt):
        for line in self.get_lines(txt):
            tagS=re.match("(<)(.*?)(>)", line).group(2).split()
            
            if len(tagS)>1:
                #TODO: Get the Tags Properties
                tagE='</' + tagS[0] + '>'
                self.__dict__[tagS]={}
                for d in tagS:
                    if '=' in d:
                        pass #TODO get the k,v pair
                    else:
                        pass  #TODO : add the field
                pass
            else:
                pass  #TODO:WhatGonnaDo?
            
            
            tagE='</'+tagS+'>'
            if tagE in txt[txt.find(line):]:
                pass #TODO: Get the data inside tags
            
            print(line)
            
        
        
    
    def get_lines(self,txt):
        for line in txt.split(chr(10)):
            yield line
        


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
            tag=blk[0].replace('<','').replace('!','')
            vals=blk[1:]
            if len(blk)>2:
                self.__dict__[tag]={}
                for d in vals:
                    self.__dict__[tag].update(self.myDict(d))
            
            
        pass
    
        




lkURL='https://en.wikipedia.org/wiki/List_of_constituencies_of_the_Lok_Sabha'

obj=requests.get(lkURL).text

res=HtmlDict(obj)


pass