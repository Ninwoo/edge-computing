import sys
import time
import join_client
import commands
import answer
i=0
port2=10413
port=10412
host=sys.argv[1]
#listening the port 10412
#if get 'done,it means no task working or all done,so just continue to next loop
#if get msg (run$id),execute the command (run),then send the answer and its id to master 
while True:
	i=i+1	
	data=join_client.join(host,port)
	if data=='done':
		time.sleep(5)
		print 'done'
		continue
	msg=data.split('&')
	run=msg[0]
	id=msg[1]
	(status,output)=commands.getstatusoutput(run)
	get=answer.send(host,port2,output+'&'+id)
	if get=='success':
		print get
	else:
		print 'error'
