# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import RPi.GPIO as GPIO



ESC1 = 4    #4
ESC2 = 17   #6   
ESC3 = 27   #7  
ESC4 = 22   #8
ESC5 = 26   #2nd last
ESC6 = 13   #4th last
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0) 

max_value = 2500 #change this if your ESC's max value is different or leave it be
min_value = 500  #change this if your ESC's min value is different or leave it be
print "For first time launch, select calibrate"
print "Type the exact word for the function you want"
print "calibrate OR manual OR control OR arm OR stop"

def manual_drive(ESC): #You will use this function to program your ESC if required
    print "You have selected manual option so give a value between 0 and you max value"    
    while True:
        inp = raw_input()
        if inp == "stop":
            stop(ESC)
            break
        elif inp == "control":
            control(ESC)
            break
        elif inp == "arm":
            arm(ESC)
            break	
        else:
            pi.set_servo_pulsewidth(ESC,inp)
                
def calibrate(ESC):   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print "Arming ESC now..."
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print "See.... uhhhhh"
            control(ESC) # You can change this to any other function you want
            
def control(ESC): 
    print "I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'"
    time.sleep(1)
    speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
    print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = raw_input()
        
        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100    # incrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print "speed = %d" % speed
        elif inp == "stop":
            stop(ESC)          #going for the stop function
            break
        elif inp == "manual":
            manual_drive(ESC)
            break
	elif inp == "arm":
		arm()
		break	
        else:
            print "WHAT DID I SAID!! Press a,q,d or e"
            
def arm(ESC): #This is the arming procedure of an ESC 
    pi.set_servo_pulsewidth(ESC, 0)
    time.sleep(1)
    pi.set_servo_pulsewidth(ESC,max_value)
    time.sleep(1)
    pi.set_servo_pulsewidth(ESC, min_value)
    time.sleep(1)
        
        #control(ESC)
        
        
def stop(ESC): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()
    os.system ("sudo killall pigpiod") #Launching GPIO library


def initialise():
    arm(ESC1)
    #arm(ESC2)
    #arm(ESC3)
    #arm(ESC4)
    #arm(ESC5)
    #arm(ESC6)


# #This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.    
# inp = raw_input()
# if inp == "manual":
#     manual_drive(ESC1)
# elif inp == "calibrate":
#     calibrate(ESC1)
# elif inp == "arm":
#     arm(ESC1)
# elif inp == "control":
#     control(ESC1)
# elif inp == "stop":
#     stop(ESC1)
# else :
#     print "Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!"

def reverse():
    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(19,GPIO.OUT)

    GPIO.output(19,GPIO.HIGH) # to run motor in clockwise direction

    GPIO.setup(13,GPIO.OUT) # put it high to rotate motor in anti-clockwise direction

    GPIO.output(13,GPIO.HIGH)
    
    GPIO.setup(6,GPIO.OUT) # put it high to rotate motor in anti-clockwise direction

    GPIO.output(6,GPIO.HIGH)
    
#reverse()
initialise()