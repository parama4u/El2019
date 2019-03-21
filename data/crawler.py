'''
Created on Mar 19, 2019

@author: param
'''
import requests
import re



class HtmlDict():
    
    ignore=('!DOCTYPE','script') 
    
    def propDict(self,txt):
        res={}
        restxt=txt.split('=')
        res[restxt[0]]=restxt[1]
        return res
    
    def __init__(self, txt):
        pat=""
        self.process(txt)
        
    def process(self,txt):
        for line in self.get_lines(txt):
            tagS=re.match("(<)(.*?)(>)", line).group(2).split()
            tagL=len(tagS)
            if tagS[0] in self.ignore : continue
            if tagL>1:
                #TODO: Get the Tags Properties
                if tagS[0] in self.ignore : continue
                tagE='</' + tagS[0] + '>'
                self.__dict__[tagS[0]]={}
                for d in tagS[1:]:
                    if '=' in d:
                        self.__dict__[tagS[0]].update(self.propDict(d))
                    else:
                        pass  #TODO : add the field
                pass
            elif tagL==1: 
                content=re.match('(<'+tagS[0]+'>)(.*?)'+'(</'+tagS[0]+'>)', line).group(2).split()
                print(content)
            
            
            
        
        
    
    def get_lines(self,txt):
        for line in txt.split(chr(10)):
            yield line
        


        




lkURL='https://en.wikipedia.org/wiki/List_of_constituencies_of_the_Lok_Sabha'

obj=requests.get(lkURL).text

res=HtmlDict(obj)


pass