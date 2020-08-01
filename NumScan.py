import phonenumbers

from phonenumbers import geocoder

from phonenumbers import carrier

import requests

from time import sleep

Color1 = "\033[1;31;32m"

Color2 = "\033[1;31;31m"

Color3 = "\033[1;31;34m"

Color4 = "\033[1;31;36m"

Color5 = "\033[1;31;33m"
print(Color5+'''
      ??????????                    
  ????          ????                
  ??              ??                
??                  ??              
??                  ??              
??      NumScan     ??              
??                  ??              
??                  ??              
  ??              ??                
  ????          ??????              
      ??????????  ??????            
                    ??????          
                      ??????        
                        ??????      
                          ??????    
                            ??????  
                              ??????
                                ????''')
print("Coded By : @00017z & t8qu_ ")
print(Color4+"[+] Only KSA Numbers")
print(Color3+"[+] example : 50xxxxxxxx")
Code = '+966'
Number = input(Color2+"[+] Enter Target Number  : ")

all1 = Code + Number

ro_number = phonenumbers.parse(all1, "en")

Service = carrier.name_for_number(ro_number, "en")

Gdd = geocoder.description_for_number(ro_number, "en")


r = requests.get("http://146.148.112.105/caller/index.php/UserManagement/search_number?number=" + Number + "&country_code=SA")
r.raise_for_status()
data = r.json()
print("-----------/-----------")
for r in data['result']:
    print(Color4+"[+] Name : "+r['name'])
for r in data['result']:
    print(Color1+"[+] PhoneNumber : "+r['number'])
for r in data['result']:
    print(Color2+"[+] Country Code : "+r['country_code'])
for r in data['result']:
    print(Color3+"[+] ID : "+r['id'])
print(Color4+"[+] Carrier : ", Service )
print(Color5+"[+] Country Name : ", Gdd)
print("-----------/-----------")
if ('KeyError:') in data:
    print("Not Found")