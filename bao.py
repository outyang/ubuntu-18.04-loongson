#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:56:06 2021

@author: yang
"""
import os 
import shutil 
image_path = '/home/yang'
for root, dirs, files in os.walk(image_path):
    for file in files:
        tmp, ext  = os.path.splitext(file)
        fb=root+'/'+tmp+'.conton'
        tmp2=tmp.replace('_','-')
        if (ext== '.buildinfo') and (not os.path.exists(fb)):
            for itm in dirs:
                if itm in tmp2:
                    fa=root+'/'+itm+'/debian/control'
                    if os.path.exists(fa):
                        print(fb)
                        shutil.copyfile(fa,fb)
