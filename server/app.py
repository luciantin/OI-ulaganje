#import sys
#print('#Hello from python#')
#print('First param:'+sys.argv[1]+'#')
#print('Second param:'+sys.argv[2]+'#')
import json
with open('countries.json') as json_data:
 for entry in json_data:
  print(entry)