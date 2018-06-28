import numpy as np

#---------------------------CONCENTRATION------------------------------------
def delta(mat):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[a1,a2,a3,....,am]] = 2*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#ai is the total area of unit/division i
	if len(mat.shape)>2 or mat.shape[0]!=2:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:
		X_i=mat[0,]
		A_i=mat[1,]
		temp=(X_i/(X_i.sum()))-(A_i/(A_i.sum()))
		D=(0.5)*((np.abs(temp)).sum())
		return D;


def ACO(mat): #absolute concentration index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 3*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#ai is the total area of unit/division i
	#ti is the total population of unit/division i
	X_i=mat[0,mat[1,].argsort()]
	A_i=mat[1,mat[1,].argsort()]
	T_i=mat[2,mat[1,].argsort()]
	X=X_i.sum()
	if len(mat.shape)>2 or mat.shape[0]!=3 or (mat[0,]>mat[2,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T_i.sum()),"group population="+str(X))
		return(-100);
	else:
		N1= (X>np.cumsum(T_i))
		N2= (X>np.cumsum(T_i[::-1]))
		n1= N1.sum()+1
		n2= N2.sum()+1
		T1= T_i[:(n1-1)].sum()
		T2= T_i[(-1*n1):].sum()	
		temp1=((X_i*A_i/X).sum())-((T_i[:(n1-1)]*A_i[:(n1-1)]/T1).sum())
		temp2=((T_i[(-1*n1):]*A_i[(-1*n1):]/T2).sum())-((T_i[:(n1-1)]*A_i[:(n1-1)]/T1).sum())
		aco=1-(temp1/temp2)
		return aco;

def RCO(mat): #relative concentration index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[y1,y2,y3,....,ym],[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 4*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#yi is the actual number of group y in unit/division i
	#ai is the total area of unit/division i
	#ti is the total population of unit/division i
	X_i=mat[0,mat[2,].argsort()]
	Y_i=mat[1,mat[2,].argsort()]
	A_i=mat[2,mat[2,].argsort()]
	T_i=mat[3,mat[2,].argsort()]
	X=X_i.sum()
	Y=Y_i.sum()
	if len(mat.shape)>2 or mat.shape[0]!=4 or ((mat[0,]+mat[1,])>mat[3,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T_i.sum()),"group population="+str(X))
		return(-100);
	else:
		N1= (X>np.cumsum(T_i))
		N2= (X>np.cumsum(T_i[::-1]))
		n1= N1.sum()+1
		n2= N2.sum()+1
		T1= T_i[:(n1-1)].sum()
		T2= T_i[(-1*n1):].sum()
		temp1=((X_i*A_i/X).sum()/((Y_i*A_i/Y).sum()).sum())-1
		temp2=((T_i[:(n1-1)]*A_i[:(n1-1)]/T1).sum()/(T_i[(-1*n1):]*A_i[(-1*n1):]/T2).sum())-1
		rco=temp1/temp2
		return rco;
#a=np.random.rand(2,5)
#a[1,]+=a[0,]
#print('a',a)
#print(delta(a))

#a=np.random.rand(3,5)
#a[2,]+=a[0,]
#print(a)
#print(ACO(a))

#a=np.random.rand(4,5)
#a[3,]+=(a[0,]+a[1,])
#print(a)
#print(RCO(a))


