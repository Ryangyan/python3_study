THRESHOLD = (10, 40, 10, -17, 14, -29)
import sensor, image, time
from pyb import LED
import car
from pid import PID
rho_pid = PID(p=0.9, i=0)
theta_pid = PID(p=0, i=0)
LED(1).on()
LED(2).on()
LED(3).on()
sensor.reset()
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
while(True):
	clock.tick()
	img = sensor.snapshot().binary([THRESHOLD])
	line = img.get_regression([(100,100,0,0,0,0)], robust = True)
	if (line):
		rho_err = abs(line.rho())-img.width()/2
		if abs(rho_err) < 10:
			rho_pid._kp = 0.2
			rho_pid._ki = 0.0
			rho_pid._kd = 0.0
		else:
			rho_pid._kp = 0.8
			rho_pid._ki = 0.0
			rho_pid._kd = 0.0
		if line.theta()>90:
			theta_err = line.theta()-180
		else:
			theta_err = line.theta()
		img.draw_line(line.line(), color = 127)
		print(rho_err,line.magnitude(),rho_err)
		if line.magnitude()>8:
			rho_output = rho_pid.get_pid(rho_err,1)
			theta_output = theta_pid.get_pid(theta_err,1)
			output = rho_output+theta_output
			car.run(60+output, 60-output)
		else:
			car.run(0,0)
	else:
		car.run(0,0)
		pass