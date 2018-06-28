import numpy as np


#---------------------------EXPOSURE------------------------------------
def interaction(mat):
	#The extent to which members of group X are exposed to members of group Y
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[y1,y2,y3,....,ym],[t1,t2,t3,....,tm]] = 3*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#yi is the actual number of group y in unit/division i
	#ti is the total number in unit/division i
	X_i=mat[0,]#X_i = numpy array of population of group X in unit i
	Y_i=mat[1,]#Y_i = numpy array of population of group Y in unit i
	T_i=mat[2,]#T_i = numpy array of total population in unit i
	if len(mat.shape)>2 or mat.shape[0]!=3 or ((mat[0,]+mat[1,])>mat[2,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T_i.sum()),"two group total population="+str(X_i.sum()+Y_i.sum()))
		return(-100);
	else:	
		P=((X_i/(X_i.sum()))*(Y_i/T_i)).sum()	
		return P;
def isolation(mat):
	#The extent to which members of group X are exposed to one-another
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#ti is the total number in unit/division i
	X_i=mat[0,]#X_i = numpy array of population of group X in unit i
	T_i=mat[1,]#T_i = numpy array of total population in unit i
	if len(mat.shape)>2 or mat.shape[0]!=2 or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T_i.sum()),"group population="+str(X_i.sum()))
		return(-100);
	else:
		P=((X_i/(X_i.sum()))*(X_i/T_i)).sum()
		return P;

def correlation_ratio(mat):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#ti is the total number in unit/division i
	X_i=mat[0,]#X_i = numpy array of population of group X in unit i
	T_i=mat[1,]#T_i = numpy array of total population in unit i
	if len(mat.shape)>2 or mat.shape[0]!=2 or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T_i.sum()),"group population="+str(X_i.sum()))
		return(-100);
	else:
		I=((X_i/(X_i.sum()))*(X_i/T_i)).sum()
		P=(X_i.sum())/(T_i.sum())
		#print('P',P)
		C=(I-P)/(1-P)
		return C;

a=np.random.rand(3,5)
a[2,]+=(a[0,]+a[1,])
print(a)
#print(interaction(a))
#print(isolation(a[[0,2],]))
#print(correlation_ratio(a[[0,2],]))

#def distance_adjusted_interaction_prob():
