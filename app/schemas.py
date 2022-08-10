from fastapi.params import Body
from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum 
import json
import pandas as pd
from decimal import Decimal
import pandas as pd
from pythonpancakes import PancakeSwapAPI
import csv
ps = PancakeSwapAPI()
import asyncio
import time


ps = PancakeSwapAPI()


afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"
#print(f"started at {time.strftime('%X')}")
tokens =  ps.tokens()
#asyncio.sleep(tokens)
#print(tokens)
#print(f"started at {time.strftime('%X')}")

data =tokens["data"] 

data2 = json.dumps(data)



#with open('compiled_code.json', 'w') as outfile:
   # json.dump(data, outfile)
    #compiled_code = outfile.read()
    #print(compiled_code)
    

with open("./compiled_code.json") as data_file:    
    data = json.load(data_file)
    data_file.close()
   
   
df = pd.DataFrame(list(data.items()))
#print(df[0][2])
class Coin_addr(str, Enum):
    coin_addr1 = df[0][0]
    coin_addr2 = df[0][1]
    coin_addr3 = df[0][2]
    coin_addr4 = df[0][3]
    coin_addr5 = df[0][4]
    coin_addr6 = df[0][5]
    coin_addr7 = df[0][6]
    coin_addr8 = df[0][7]
    coin_addr9 = df[0][8]
    coin_addr10 = df[0][9]
    coin_addr11 = df[0][9]
    coin_addr12 = df[0][10]
    coin_addr13 = df[0][11]
    coin_addr14 = df[0][12]
    coin_addr15 = df[0][13]
    coin_addr16 = df[0][14]
    coin_addr17 = df[0][15]
    coin_addr18 = df[0][16]
    coin_addr19 = df[0][17]
    coin_addr20 = df[0][18]
    coin_addr21 = df[0][19]
    coin_addr22 = df[0][20]
    coin_addr23 = df[0][21]
    coin_addr24 = df[0][22]
    coin_addr25 = df[0][23]
    coin_addr26 = df[0][24]
    coin_addr27 = df[0][25]
    coin_addr28 = df[0][26]
    coin_addr29 = df[0][27]
    coin_addr30 = df[0][28]
    coin_addr31 = df[0][29]
    coin_addr32 = df[0][30]
    coin_addr33 = df[0][31]
    coin_addr34 = df[0][32]
    coin_addr35 = df[0][34]
    coin_addr36 = df[0][35]
    coin_addr37 = df[0][36]
    coin_addr38 = df[0][37]
    coin_addr39 = df[0][37]
    coin_addr40 = df[0][38]
    coin_addr41 = df[0][39]
    coin_addr42 = df[0][40]
    coin_addr43 = df[0][41]
    coin_addr44 = df[0][42]
    coin_addr45 = df[0][43]
    coin_addr46 = df[0][44]
    coin_addr47 = df[0][45]
    coin_addr48 = df[0][46]
    coin_addr49 = df[0][47]
    coin_addr50 = df[0][48]
    coin_addr51 = df[0][49]
    coin_addr52 = df[0][50]
    coin_addr53 = df[0][51]
    coin_addr54 = df[0][52]
    coin_addr55 = df[0][53]
    coin_addr56 = df[0][54]
    coin_addr57 = df[0][55]
    coin_addr58 = df[0][56]
    coin_addr59 = df[0][57]
    coin_addr60 = df[0][58]
    coin_addr61 = df[0][59]
    coin_addr62 = df[0][60]
    coin_addr63 = df[0][61]
    coin_addr64 = df[0][62]
    coin_addr65 = df[0][63]
    coin_addr66 = df[0][64]
    coin_addr67 = df[0][65]
    coin_addr68= df[0][66]
    coin_addr69 = df[0][67]
    coin_addr70 = df[0][68]
    coin_addr71 = df[0][69]
    coin_addr72 = df[0][70]
    coin_addr73 = df[0][71]
    coin_addr74 = df[0][72]
    coin_addr75 = df[0][73]
    coin_addr76 = df[0][74]
    coin_addr77 = df[0][75]
    coin_addr78 = df[0][76]
    coin_addr79 = df[0][77]
    coin_addr80 = df[0][78]
    coin_addr81 = df[0][79]
    coin_addr82 = df[0][80]
    coin_addr83 = df[0][81]
    coin_addr84 = df[0][82]
    coin_addr85 = df[0][83]
    coin_addr86 = df[0][84]
    coin_addr87 = df[0][85]
    coin_addr88 = df[0][86]
    coin_addr89 = df[0][87]
    coin_addr90 = df[0][89]
    coin_addr91= df[0][90]




#print(df[0][0])
class Coin_symbol(str, Enum):
    coin_smbol00 = "AFCASH"
    coin_smbol0 = df[1][0]['symbol']
    coin_smbol1 = df[1][1]['symbol']
    coin_smbol2 = df[1][2]['symbol']
    coin_smbol3 = df[1][3]['symbol']
    coin_smbol4 = df[1][4]['symbol']
    coin_smbol5 = df[1][5]['symbol']
    coin_smbol6 = df[1][6]['symbol']
    coin_smbol7 = df[1][7]['symbol']
    coin_smbol8 = df[1][8]['symbol']
    coin_smbol9 = df[1][9]['symbol']
    coin_smbol10 = df[1][10]['symbol']
    coin_smbol11 = df[1][11]['symbol']
    coin_smbol12 = df[1][12]['symbol']
    coin_smbol13 = df[1][13]['symbol']
    coin_smbol14 = df[1][14]['symbol']
    coin_smbol15 = df[1][15]['symbol']
    coin_smbol16 = df[1][16]['symbol']
    coin_smbol17 = df[1][17]['symbol']
    coin_smbol18 = df[1][18]['symbol']
    coin_smbol19 = df[1][19]['symbol']
    coin_smbol20 = df[1][20]['symbol']
    coin_smbol21 = df[1][21]['symbol']
    coin_smbol22 = df[1][22]['symbol']
    coin_smbol23 = df[1][23]['symbol']
    coin_smbol24 = df[1][24]['symbol']
    coin_smbol25 = df[1][25]['symbol']
    coin_smbol26 = df[1][26]['symbol']
    coin_smbol27 = df[1][27]['symbol']
    coin_smbol28 = df[1][28]['symbol']
    coin_smbol29 = df[1][29]['symbol']
    coin_smbol30 = df[1][30]['symbol']
    coin_smbol31 = df[1][31]['symbol']
    coin_smbol32 = df[1][32]['symbol']
    coin_smbol33 = df[1][33]['symbol']
    coin_smbol34 = df[1][34]['symbol']
    coin_smbol35 = df[1][35]['symbol']
    coin_smbol36 = df[1][36]['symbol']
    coin_smbol37 = df[1][37]['symbol']
    coin_smbol38 = df[1][38]['symbol']
    coin_smbol39 = df[1][39]['symbol']
    coin_smbol40 = df[1][40]['symbol']
    coin_smbol41 = df[1][41]['symbol']
    coin_smbol42 = df[1][42]['symbol']
    coin_smbol43 = df[1][43]['symbol']
    coin_smbol44 = df[1][44]['symbol']
    coin_smbol45 = df[1][45]['symbol']
    coin_smbol46 = df[1][46]['symbol']
    coin_smbol47 = df[1][47]['symbol']
    coin_smbol48 = df[1][48]['symbol']
    coin_smbol49 = df[1][49]['symbol']
    coin_smbol50 = df[1][50]['symbol']
    coin_smbol51 = df[1][51]['symbol']
    coin_smbol52 = df[1][52]['symbol']
    coin_smbol53 = df[1][53]['symbol']
    coin_smbol54 = df[1][54]['symbol']
    coin_smbol55 = df[1][55]['symbol']
    coin_smbol56 = df[1][56]['symbol']
    coin_smbol57 = df[1][57]['symbol']
    coin_smbol58 = df[1][58]['symbol']
    coin_smbol59 = df[1][59]['symbol']
    coin_smbol60 = df[1][60]['symbol']
    coin_smbol61 = df[1][61]['symbol']
    coin_smbol62 = df[1][62]['symbol']
    coin_smbol63 = df[1][63]['symbol']
    coin_smbol64 = df[1][64]['symbol']
    coin_smbol65 = df[1][65]['symbol']
    coin_smbol66 = df[1][66]['symbol']
    coin_smbol67 = df[1][67]['symbol']
    coin_smbol68 = df[1][68]['symbol']
    coin_smbol69 = df[1][69]['symbol']
    coin_smbol70 = df[1][70]['symbol']
    coin_smbol71 = df[1][71]['symbol']
    coin_smbol72 = df[1][72]['symbol']
    coin_smbol73 = df[1][73]['symbol']
    coin_smbol74 = df[1][74]['symbol']
    coin_smbol75 = df[1][75]['symbol']
    coin_smbol76 = df[1][76]['symbol']
    coin_smbol77 = df[1][77]['symbol']
    coin_smbol78 = df[1][78]['symbol']
    coin_smbol79 = df[1][79]['symbol']
    coin_smbol80 = df[1][80]['symbol']
    coin_smbol81 = df[1][81]['symbol']
    coin_smbol82 = df[1][82]['symbol']
    coin_smbol83 = df[1][83]['symbol']
    coin_smbol84 = df[1][84]['symbol']
    coin_smbol85 = df[1][85]['symbol']
    coin_smbol86 = df[1][86]['symbol']
    coin_smbol87 = df[1][87]['symbol']
    coin_smbol88 = df[1][88]['symbol']
    coin_smbol89 = df[1][89]['symbol']
    coin_smbol90 = df[1][90]['symbol']
    
    



"""
class web_hook(BaseModel):
    web_url: str = Field( None)
"""

class Tx_user(BaseModel):
    account_from: int = Body(None)
    account_to: int = Body(None)
    value_to_send: float = Body(None)
    private_key: int = Body(None)



#print(Coin_symbol)
