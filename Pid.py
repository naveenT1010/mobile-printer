import serial 
import pyautogui
import time


class PID(object):
	def __init__(self, P=0.2, I=0.001, D=0.001, Derivator=(0,0) ,Integrator=(0,0)):
		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=(Derivator[0],Derivator[1])
		self.Integrator=(Integrator[0],Integrator[1])
		self.set_point=(0,0)
		self.error=(0,0)

	def update(self,current_value):
		self.error =(self.set_point[0] - current_value[0],self.set_point[1]-current_value[1])
				
		self.P_value =(self.Kp * self.error[0],self.Kp * self.error[1])
		self.D_value =(self.Kd * ( self.error[0] - self.Derivator[0]),self.Kd * (self.error[1] - self.Derivator[1]))
		self.Derivator =(self.error[0],self.error[1])
		self.Integrator =(self.Integrator[0] + self.error[0],self.Integrator[1]+self.error[1])
		self.I_value = (self.Integrator[0]* self.Ki,self.Integrator[1] * self.Ki)
		PID =(int(self.P_value[0] + self.I_value[0] + self.D_value[0]),int(self.P_value[1] + self.I_value[1] + self.D_value[1]))
		return PID

	def setPoint(self,set_point):
		self.set_point =(set_point[0],set_point[1])
		

	def setIntegrator(self, Integrator):
		self.Integrator =(Integrator[0],Integrator[1])

	def setDerivator(self, Derivator):
		self.Derivator =(Derivator[0],Derivator[1])

	def setKp(self,P):
		self.Kp=P

	def setKi(self,I):
		self.Ki=I

	def setKd(self,D):
		self.Kd=D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getIntegrator(self):
		return self.Integrator

	def getDerivator(self):
		return self.Derivator
controller=PID()
controller.setPoint((500,500))
print str(pyautogui.position()) + "reference"
while True:
	current_pos=pyautogui.position()
	control=controller.update(current_pos)
	a=str(control[0])
	b=str(control[1])
	print control
	ser=serial.Serial()
	ser.baudrate=9600
	ser.port='/dev/ttyACM0'
	ser.open()
	ser.write(a)
	ser.write(',')
	ser.write(b)
	ser.write(' ')
	ser.close()
	time.sleep(1)
	
	
	

