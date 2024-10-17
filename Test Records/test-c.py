import os

#TCP TEST
#os.system('sudo ifconfig eth0 195.20.1.31')
#os.system('sudo ifconfig eth0')
#os.system('sudo iperf3 -c 195.20.1.19 -b 100M -n 200G')


#UDP TEST
os.system('sudo ifconfig eth0 195.20.1.31')
os.system('sudo ifconfig eth0')
os.system('sudo iperf3 -c 195.20.1.19 -b 100M -n 50G -u -t 5')
