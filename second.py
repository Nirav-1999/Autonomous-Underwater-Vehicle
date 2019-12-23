import time

import pigpio


def arm():
    print ("Arming")

    pi = pigpio.pi() # Connect to local Pi.
    pi.set_servo_pulsewidth(4, 1500) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 1500) # Minimum throttle.
    pi.set_servo_pulsewidth(27, 1500) # Minimum throttle.
    pi.set_servo_pulsewidth(22, 1500) # Minimum throttle.
    pi.set_servo_pulsewidth(26, 1500) # Minimum throttle.
    pi.set_servo_pulsewidth(13, 1500) # Minimum throttle.

    time.sleep(3)

    pi.set_servo_pulsewidth(4, 2000) # Maximum throttle.
    pi.set_servo_pulsewidth(17, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(27, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(22, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(26, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(13, 2000) # Minimum throttle.

    time.sleep(5)


    print ("Armed")

arm()

