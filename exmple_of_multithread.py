from threading import *
import time
import threading

def venue(venues):
    print(threading.get_ident())
    for i in venues:                        
        if i != 'noavailable':
            print('venue fixed at :',i)
        else:
            print('venu not fixed:')

def wedding_card():
    print(threading.get_ident())
    print('bride name : anushka')
    print('groom name : virat')
    print('wedding date: 22/09/2021')        # join work as a await work in js 
    t1.join()                                # first decide venue then venue will print on card
    print('venue location printed:')

def card_distribution():
    print(threading.get_ident())
    print('list of people')
    print('group people by region')
    print('select which person to go in which region')
    t2.join()                               # first print card then we will distribute
    print('cards distributed')

venues=['noavailable','noavailable','noavailable','noavailable','noavailable','ttd']

t1=Thread(target=venue,args=(venues,))  
t2=Thread(target=wedding_card)
t3=Thread(target=card_distribution)     
t1.start()
t2.start()
t3.start()                        #these three thread(t1,t2,t3) execute parrallel
