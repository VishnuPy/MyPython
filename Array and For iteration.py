# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
parents, babies = (1, 1)
while babies < 10:
    print ("This generation has {0} babies".format (babies))
    parents, babies = (babies, parents+babies)