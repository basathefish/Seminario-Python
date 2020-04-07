pal=input()
ln=[]
lnc=[]

for let in pal:
	print(let)
	ln.append(let)
	
ln.sort()
print('\n',ln)
print(len(set(ln)),'\n')

ln.append("zzz")

i=0
for n in range(len(set(ln))-1):
	
	l=ln[i]
	j=0
	while l==ln[i]:
		j+=1
		i+=1
	print(i)
	print(n,'n','\n')
		
	lnc.append([l,j])
	
print(lnc)
