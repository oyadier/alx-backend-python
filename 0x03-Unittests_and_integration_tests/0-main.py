#!/usr/bin/env python3

nested = __import__('utils').access_nested_map

if __name__ == "__main__":
    
    nested_map={'oya':{'om':{'ro':'pat', 'is':'fat'}}}
    print(nested(nested_map, ['oya','om']))