import math
import sys

ok = False

start = sys.argv[1]

end = sys.argv[2]

start = int(start)

end = int(end)



n=end

primes=[]
sum=0

while n>=start:

	cur = n

	i=1

	ctc=0

	while i<=math.sqrt(cur):

		if cur%i==0:

			ctc = ctc+1

		i=i+1

	if ctc==1:

		primes.append(cur)
		sum=sum+cur

	n = n-1

flag = False

for prime in primes:

	if prime==1:

		flag=True

if (not flag and start<=1):

	primes.append(1)


print sum 
