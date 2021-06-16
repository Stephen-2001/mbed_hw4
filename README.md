# mbed_hw4

## Part 1 in the folder hw4_1 and hw4_1_2
#### How to use XBEE to control the BBcar
This part, I use two method to control the BBcar. I will explain the difference later.

##### How to compile and execute the code (method1)
1. go to the directory `cd ~/ee2405/mbed_hw4/hw4_1`
2. compile the main.cpp `sudo mbed compile --source . --source ~/ee2405/mbed-os-build/ -m B_L4S5I_IOT01A -t GCC_ARM -f`
3. compile the car_control.py `sudo python3 car_control.py /dev/ttyUSB0`

##### How does it work
1. First, the user should enter the parameters about distance and direction. For example, (30, 30, west).
2. The first parameter is the distance between car and parking space in north and south direction. The second parameter is the distance between the two in east and west direction. The third string is determined the relative position of the parking space.
3. The information will read by `car_control.py` and then start to control the car to enter the parking space.
4. I use different value of `time.sleep(time)` to control the time the car should move. 
## Part 2 in the folder hw4_2_2
## Part 3 in the folder hw4_3
