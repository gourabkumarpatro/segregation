import numpy as np


#---------------------------CENTRALIZATION------------------------------------
def PCC(mat): #basic centralization index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[c1,c2,c3,....,cm]] = 2*m 2D-numpy-matrix
	#xi is the population of group x in unit/division i
	#ci is the boolean value
	#ci=1 => unit/division i comes within the boundaries of central city
	#ci=0 => unit/division i doesn't come within the boundaries of central city
	if len(mat.shape)>2 or mat.shape[0]!=2:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:	
		X_i=mat[0,]
		C_i=(mat[1,]==1)
		pcc=(X_i[C_i]).sum()/X_i.sum()
		return pcc;

#a=np.random.rand(2,10)
#a[1,]=(a[1,]>0.6)
#print(a)
#print(PCC(a))

def RCE(mat): #relative centralization index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[y1,y2,y3,....,ym],[c1,c2,c3,....,cm]] = 3*m 2D-numpy-matrix
	#xi is the population of group x in unit/division i
	#yi is the population of group y in unit/division i
	#ci is the distance of unit i from the center
	if len(mat.shape)>2 or mat.shape[0]!=3:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:	
		x_i=mat[0,mat[2,].argsort()]/(mat[0,].sum())
		y_i=mat[1,mat[2,].argsort()]/(mat[1,].sum())
		X_i=np.cumsum(x_i)
		Y_i=np.cumsum(y_i)
		rce=(X_i[1:]*Y_i[:-1]).sum()-(X_i[:-1]*Y_i[1:]).sum()
		return rce;

#a=np.random.rand(3,5)
#print(a)
#print(RCE(a))


def ACE(mat): #absolute centralization index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[a1,a2,a3,....,am],[c1,c2,c3,....,cm]] = 3*m 2D-numpy-matrix
	#xi is the population of group x in unit/division i
	#ai is the area of unit/division i
	#ci is the distance of unit i from the center
	if len(mat.shape)>2 or mat.shape[0]!=3:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:	
		x_i=mat[0,mat[2,].argsort()]/(mat[0,].sum())
		a_i=mat[1,mat[2,].argsort()]/(mat[1,].sum())
		X_i=np.cumsum(x_i)
		A_i=np.cumsum(a_i)
		ace=(X_i[1:]*A_i[:-1]).sum()-(X_i[:-1]*A_i[1:]).sum()
		return ace;

#a=np.random.rand(3,5)
#print(a)
#print(ACE(a))

