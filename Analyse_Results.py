res = [0]*171
with open('Quant.txt', 'r') as f:
    lines = f.readlines()

for x in lines:
	x=x.strip('\n')
	data = int(x)
	if data<=170:
		res[data]=res[data]+1
print "Quant Results:"
for i in range(0,171):
	if(res[i]>0):
		print i,res[i]	

res2 = [0]*171
with open('Verb.txt', 'r') as f:
    lines = f.readlines()

for x in lines:
	x=x.strip('\n')
	data = int(x)
	if data<=170:
		res2[data]=res2[data]+1
print "Verbal Results:"
for i in range(0,171):
	if(res2[i]>0):
		print i,res2[i]	

