#coding:utf-8
'''
get segmentation parameters for prime number 
you can change the number of task list in here,just like that 300!
'''
import sys
def div(start,end):
	#n=countip.count()
	ti=(end-start+1)/(300)
	pa=[]
	t=0
	while t<(15):
		ends=start+ti
		if ends>end:
			ends=end
		pa.append((start,ends))
		start=start+ti+1
		t=t+1
	return pa

