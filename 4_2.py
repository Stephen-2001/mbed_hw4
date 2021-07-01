
import pyb, sensor, image, time, math
THRESHOLD = (0, 100)
BINARY_VISIBLE = True
enable_lens_corr = False
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.skip_frames(time = 2000)
clock = time.clock()
uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)
while(True):
   clock.tick()
   img = sensor.snapshot().binary([THRESHOLD]) if BINARY_VISIBLE else sensor.snapshot()
   line = img.get_regression([(255, 255) if BINARY_VISIBLE else THRESHOLD], robust=True)
   if (line):
      img.draw_line(line.line(), color=127)
      # info = (line.x1(), line.y1(), line.x2(), line.y2(), line.length(), line.theta(), line.rho())
      print(line)
      theta = line.theta()
      rho = line.rho()

      if (rho < 0):
         theta = 180 - theta
      magnitude = abs(rho) / math.cos(math.radians(theta))
      diff = magnitude - 40  # the spatial differenence between middle and present position
      if (abs(diff) <= 15 and theta < 30):
         print("gostraight")
         uart.write(("/goStraight/run 40 \n").encode())
      elif (abs(diff) >= 15 and diff < 0 and theta > 45):
         print("turn_left")
         uart.write(("/turn/run 40 0.75\n").encode())
      elif (abs(diff) >= 15 and diff > 0 and theta > 45):
         print("turn_right")
         uart.write(("/turn/run 40 -0.75\n").encode())
      #elif (abs(diff) <= 30):
         #print("gostraight")
         #uart.write(("/goStraight/run 40 \n").encode())
      elif (diff < 0):
         print("turn_left")
         uart.write(("/turn/run 40 0.75\n").encode())
      elif (diff > 0):
         print("turn_right")
         uart.write(("/turn/run 40 -0.75\n").encode())
      else:
         print("stop")
         uart.write(("/stop/run \n").encode())
      time.sleep_ms(100)
      print("diff = %d theta = %d \n" % (diff, theta))
   else:
      print("stop")
      uart.write(("/stop/run \n").encode())
      time.sleep_ms(100)
