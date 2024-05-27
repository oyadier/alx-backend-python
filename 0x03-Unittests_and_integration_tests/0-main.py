#!/usr/bin/env python3
import utils

if __name__ == "__main__":
    
    nested_map={'oya':{'om':{'ro':'pat', 'is':'fat'}}}
    
    try:
        print(utils.access_nested_map(nested_map, ['oya','om', 'rob']))
    except KeyError:
        print("Key Error, it could'nt be found")
        
    response = utils.get_json("http://example.com")
    print(response)