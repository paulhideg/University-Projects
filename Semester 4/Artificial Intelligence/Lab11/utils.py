# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:44:35 2020

@author: Alex
"""

class Utils:
    
    # header basically contains all the hardcoded stuff like you'd have in an excel header, i.e. "value1", "value2"...,"value24"
    HEADER = []
    
    def choose_category(result):
        if result>5:
            return 'Slight-Left-Turn'
        elif result<=5 and result>0:
            return 'Move-Forward'
        elif result<=0 and result>-5:
            return 'Sharp-Right-Turn'
        return 'Slight-Right-Turn'