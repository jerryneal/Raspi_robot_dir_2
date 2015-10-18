

import matplotlib

def main():

	# make up an elbow trajectory (pretend this was recorded in an experiment)
	t = linspace(0,1,200)
	theta = sin(2*pi*t/4)
	figure()
	subplot(2,3,(1,2))
	plot(t,theta*180/pi)
	xlabel('TIME (sec)')
	ylabel('ELBOW ANGLE (deg)')
	# compute hand position Hx,Hy
	l = 0.45
	Hx = l * cos(theta)
	Hy = l * sin(theta)
	subplot(2,3,(4,5))
	plot(t,Hx,'b-')
	plot(t,Hy,'r-')
	xlabel('TIME (sec)')
	ylabel('HAND POSITION (m)')
	legend(('Hx','Hy'),loc='lower right')
	subplot(2,3,(3,6))
	plot((0,Hx[0]),(0,Hy[0]),'g-')
	plot((0,Hx[-1]),(0,Hy[-1]),'r-')
	plot(Hx[0:-1:10],Hy[0:-1:10],'k.')
	xlabel('X (m)')
	ylabel('Y (m)')
	axis('equal')

main()