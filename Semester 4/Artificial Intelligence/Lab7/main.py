# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:27:05 2020

@author: Alex
"""

from controller import Controller

def main():
    ctrl = Controller('data.txt')
    mean_error = ctrl.run()
    print("Error with scientific notation:{}".format(mean_error))
    print("Error with standard notation:{:.25f}".format(mean_error))
main()