# WeatherStation

import matplotlib.pyplot as plt
import matplotlib.animation as anm
import Adafruit_DHT as adp
import time

sensor = adp.DHT11
pin = 2

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)


ax2 = fig.add_subplot(2,1,2)


h, t = list(), list()

def animate(i):
    
    (temp,hum)=adp.read_retry(sensor,pin)

    l = 0

    if temp and hum:
        l = len(t)

        if l > 100:
        
            with open('data.txt','a') as f:
                for hm, tp in zip(h,t): 
                    f.write('{} {}\n'.format(hm,tp))
                        
            del h[:]
            del t[:]

    t.append(temp), h.append(hum)

    ax1.clear()
    ax2.clear()
    ax1.plot(i, temp, color='r')
    ax1.set_title('Live GRAPHS')
    ax1.set_xlabel('Time')
    ax2.set_ylabel('Temperature *c')
    ax2.plot(i, hum, color='b')
    ax1.set_ylabel('Relative Humidity %')
    ax2.set_xlabel('Time')

    
    
if __name__ == '__main__':

    ani = anm.FuncAnimation(fig, animate, interval=1000)
    plt.xlabel('Time')
    
    plt.show()
