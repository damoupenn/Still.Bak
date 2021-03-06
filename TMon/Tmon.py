import ue9
from time import time,sleep

ipAddress = '192.168.216.104'

def V2K(V): return V*100.
def get_jd(): return ( time() / 86400.) + 2440587.5 
def get_temps():
	_T = []
	_T.append(str(d.getTemperature()))
	Tb = 0.
	for i in (2,3):
		Tb += 0.5 * V2K(d.readRegister(i))
	_T.append(str(Tb))
	return '\t'.join(_T)
def get_Tstring():
	return '%s\t%s'%(get_jd(),get_temps())

#Define Sampling and writing rates.

SperSamp = 0.5 #Seconds per sample
SperInt  = 10  #Seconds per integration
MperFile = 59.5   #Minutes per file

OutDir = '/home/obs/TempData' 

#Write the files.

NperFile = int( 60.* MperFile / SperInt )
NperInt = int(SperInt / SperSamp)
	
d = ue9.UE9(ethernet=True,ipAddress=ipAddress)
print d.commConfig()
Filename = '%s/temp.%s.txt'%(OutDir,str(get_jd()))
print 'Writing to %s'%Filename
f = open(Filename,'w')
i_int = 0
while i_int < NperFile:
	i_samp = 0
	jd,t1,t2 = 0.,0.,0.
	while i_samp < NperInt:
		try:	
			_jd,_t1,_t2 = get_Tstring().split('\t')
			jd += float(_jd)
			t1 += float(_t1)
			t2 += float(_t2)
			i_samp += 1
		except(IndexError): pass
		sleep(SperSamp)
	i_samp = float(i_samp)
	Tstr = '%f\t%f\t%f\n'%(jd/i_samp,t1/i_samp,t2/i_samp)
	f.write(Tstr)
	i_int += 1
f.close()
