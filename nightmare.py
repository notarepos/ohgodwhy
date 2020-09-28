import os
import random

#fuck you
#I made this
#this exists
#deal with it
#TODO:
#everything, jackass

'''
for i in range(0,100):
    os.system("say -v Alex -r 500 'nightmare'")
'''

def annoy(voicename,min,max):
    nightmare =  " "
    for i in range(min,max):
        nightmare += "nightmare"
    for i in range(min,max):
        os.system("say -v " + voicename + " " + " -r 700 '" + nightmare + " '")


annoy("Alex",0,100)