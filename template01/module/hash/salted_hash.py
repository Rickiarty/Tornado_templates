#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SaltingHashFactory:

    @staticmethod
    def get_hasher(salt_val):
        return SaltingHashFactory._Hasher(salt_val)
    
    class _Hasher:
        __salt = ''
        
        def __init__(self, salt_val):
            self.__salt = salt_val
        
        def hash_value(self, src_val):
            pass

if __name__ == '__main__':
    # for unit test
    hash_obj = SaltingHashFactory.get_hasher('666')
    hash_val = hash_obj.hash_value('Satan')
    print(str(hash_val))