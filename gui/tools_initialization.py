# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:04:03 2019

@author: immm
"""

import XPS_Q8_drivers
import visa
import time

from gui_variables import DelayLines


class DelayLine():
    def __init__(self, controller, **kwargs):
        
        self.controller = controller
        
        # Delay Line initialization
        self.myxps = XPS_Q8_drivers.XPS()    # Connect to the XPS
        self.socketId = self.myxps.TCP_ConnectToServer('192.168.0.254', 5001, 20)   # Check connection passed
        if (self.socketId == -1):
            print ('Connection to XPS failed, check IP & Port')
            
        for delay_line in DelayLines:
            group = delay_line.split('.', 1)[0]
            self.myxps.GroupKill(self.socketId, group)    # Kill the group
            self.myxps.GroupInitialize(self.socketId, group)  # Initialize the group
            self.myxps.GroupHomeSearch(self.socketId, group)  # Home search
        
        
    def move_to(self, position):
        self.myxps.GroupMoveAbsolute(self.socketId, self.controller.positioner,
                                     [position]
                                     )
    def set_velocity(self, velocity):
        [Error, Velocity, Acceleration, MinimumJerkTime, MaximumJerkTime] = self.myxps.PositionerSGammaParametersGet(
                self.socketId, self.controller.positioner)
        self.myxps.PositionerSGammaParametersSet(
                self.socketId, self.controller.positioner, velocity,
                Acceleration, MinimumJerkTime, MaximumJerkTime
                )
        

class LIA():
    def __init__(self, **kwargs):
        
        # Initialization of LIA
        self.rm = visa.ResourceManager()
        self.rm.list_resources()
        self.lock_in = self.rm.open_resource('')
        time.sleep(0.02)
        
        # Parameters setup
        self.lock_in.timeout = 10000
        time.sleep(0.02)
        self.lock_in.write('OUTX1')
        time.sleep(0.02)
        self.lock_in.write('KLCK?1')
        time.sleep(0.02)
    
    # Lock in communication functions, already working for sr830 via GPIB interface
    def get_idn(self):
        return self.lock_in.query('*IDN?')
        time.sleep(0.02)
       
    def trigger(self):
        self.lock_in.write('TRIG')
        time.sleep(0.02)
        
    def set_sens(self, value):
        self.lock_in.write('SENS '+str(value))
        time.sleep(0.02)
        
    def set_tconst(self, value):
        self.lock_in.write('OFLT '+str(value))
        time.sleep(0.02)
        
    def set_auxv2(self, value):
        self.lock_in.write('AUXV2,'+str(value))
        time.sleep(0.02)
        
    def start_acqusition(self):
        self.lock_in.write('DDEF 1,0,0')
        time.sleep(0.02)
        self.lock_in.write('DDEF 2,0,0')
        time.sleep(0.02)
        self.lock_in.write('REST')
        time.sleep(0.02)
        self.lock_in.write('SRAT14')
        time.sleep(0.02)
        self.lock_in.write('SEND0')
        time.sleep(0.02)
        self.lock_in.write('STRT')
        time.sleep(0.02)
    
    def get_tconst(self):
        return int(self.lock_in.query('OFLT?'))
        time.sleep(0.02)
        
    def get_sens(self):
        return int(self.lock_in.query('SENS?'))
        time.sleep(0.02)
            
    def get_buffer_len(self):
        return int(self.lock_in.query('SPTS?'))
        time.sleep(0.02)
        
    def get_channel_one(self, bufferlength):
        return self.lock_in.query('TRCA?1,0,'+ str(bufferlength))
        time.sleep(0.02)
        
    def get_channel_two(self, bufferlength):
        return self.lock_in.query('TRCA?2,0,'+ str(bufferlength))
        time.sleep(0.02)

    def get_R(self):
        return float(self.lock_in.query('OUTP?3'))


if __name__ == "__main__":
    # Get the list of the devices
    rm = visa.ResourceManager()

    print(rm.list_resources())

    # Connect to Lock-in, put the GPIB address of LIA enclosed in ''
    lock_in = rm.open_resource('')

    # Check connection by requesting ID
    lock_in.query('*IDN?')

    # If you recieve the correct IDN of LIA, you should change the line 129 argument, i.e. everything inside brackets ()
    # by line's 129 argument(). Then, you can proceed by uncommenting the following code and re-running the program

    # lia = LIA()
    # print(lia.get_idn())
    # print(lia.get_tconst()
    # lia.set_sens(1)

    ## If the sensitivity was changed and IDN and a number were printed in console, the LIA is ready to work.
    ## We will proceed with Delay Line setup, by uncommenting the code below

    # myxps = XPS_Q8_drivers.XPS()    # Connect to the XPS
    # socketId = myxps.TCP_ConnectToServer('192.168.0.254', 5001, 20)   # Check connection passed
    # if (socketId == -1):
    #     print ('Connection to XPS failed, check IP & Port')