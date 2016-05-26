#This file holds all global variables to share across files

import queue

receivingQueue = queue.Queue()

startProgram = False
quitProgram = False


#Data From Pi

waterTemp = 0
subTemp = 0
buoyTemp = 0
subBattery = 0
buoyBattery = 0
depth = 0.0

xbox_a_pressed = False
xbox_b_pressed = False


