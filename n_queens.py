from pycryptosat import Solver
s = Solver()
print("please enter the size of the chess board")
n=int(input())
i=1
lst=[]
n_clause=0


#chess positions
while(i!=(n*n)+1):
	p=[]
	for j in range(n):
		p.append(i)
		print(i,end=" ")
		i+=1
	print(0)
	lst.append(p)
	s.add_clause(p)
	n_clause+=1


#rows
for i in range(n):
	for j in range(n):
		for k in range(j+1,n):
			print(-lst[i][j],-lst[i][k],0)
			s.add_clause([-lst[i][j],-lst[i][k]])
			n_clause+=1


#cols
for j in range(n):
	for i in range(n):
		for k in range(i+1,n):
			print(-lst[i][j],-lst[k][j],0)
			s.add_clause([-lst[i][j],-lst[k][j]])
			n_clause+=1


#left diagnols
for i in range(n):
	if(i!=0):
		q=[(0,i),(i,0)]
		for j in q:
			l=j[0]
			r=j[1]
			p=[]
			while(r!=n and l!=n):
				p.append(lst[l][r])
				l+=1
				r+=1
			for it in range(len(p)):
				for it1 in range(it+1,len(p)):
					print(-p[it],-p[it1],0)
					s.add_clause([-p[it],-p[it1]])
					n_clause+=1
	else:
		l=0
		r=0
		p=[]
		while(r!=n and l!=n):
				p.append(lst[l][r])
				l+=1
				r+=1
		for it in range(len(p)):
			for it1 in range(it+1,len(p)):
				print(-p[it],-p[it1],0)
				s.add_clause([-p[it],-p[it1]])
				n_clause+=1


#right diagnols
for i in range(1,n):
	q=[(0,i),(i,n-1)]
	for j in q:
		l=j[0]
		r=j[1]
		p=[]
		while(r!=-1 and l!=n):
			p.append(lst[l][r])
			l+=1
			r-=1
		for it in range(len(p)):
			for it1 in range(it+1,len(p)):
				print(-p[it],-p[it1],0)
				s.add_clause([-p[it],-p[it1]])
				n_clause+=1


#sat solver
sat, solution = s.solve()
print("Number of clauses: "+str(n_clause))
print("Satisfiability: "+str(sat))
print(solution)
st=""
if(sat==True):
	k=1
	for i in range(n):
		for j in range(n):
			if(solution[k]== True):
				st+=str(lst[i][j])+" "
				print(1,end=" ")
			else:
				st+=str(-lst[i][j])+" "
				print(0,end=" ")
			k+=1
		print()
	print(st)
