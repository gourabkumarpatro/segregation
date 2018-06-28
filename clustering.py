#MIT License

#Copyright (c) [2018] [GOURAB KUMAR PATRO]
'''
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
'''
#Gourab Kumar Patro
#https://www.linkedin.com/in/gourabgggg/
#https://gourabkumarpatro.github.io/

import numpy as np


#---------------------------CLUSTERING------------------------------------
def ACL(mat,C): #absolute clustering index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#ti is the total number in unit/division i
	#format C=[Cij] = m*m 2D-numpy-matrix
	#Cij=exp(-dij)
	#dij is the distance between centroids of units i and j
	X=(mat[0,]).sum().sum()+0.0 #total group population
	T=(mat[1,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=2 or X>T or (mat[0,]>mat[1,]).sum()!=0 or C.shape[0]!=mat.shape[1] or C.shape[1]!=mat.shape[1]:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T),"group population="+str(X))
		return(-100);
	else:
		X_i=mat[0,]
		T_i=mat[1,]
		n=mat.shape[1]
		temp1=((X_i/X)*np.matmul(C,X_i)).sum()-(X*(C.sum().sum())/(n*n))
		temp2=((X_i/X)*np.matmul(C,T_i)).sum()-(X*(C.sum().sum())/(n*n))
		acl=temp1/temp2
		return acl;

#a=np.random.rand(2,5)
#a[1,]+=a[0,]
#b=np.random.rand(5,5)
#b=0.5*(b+b.T)	
#print(ACL(a,b))

def SPI(mat,C): #spatial proximity index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[y1,y2,y3,....,ym],[t1,t2,t3,....,tm]] = 3*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#yi is the actual number of group y in unit/division i
	#ti is the total number in unit/division i
	#format C=[Cij] = m*m 2D-numpy-matrix
	#Cij=exp(-dij)
	#dij is the distance between centroids of units i and j
	X=(mat[0,]).sum().sum()+0.0 #total group x population
	Y=(mat[1,]).sum().sum()+0.0 #total group y population
	T=(mat[2,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=3 or X>T or ((mat[0,]+mat[1,])>mat[2,]).sum()!=0 or C.shape[0]!=mat.shape[1] or C.shape[1]!=mat.shape[1]:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:
		X_i=mat[0,]
		Y_i=mat[1,]
		T_i=mat[2,]
		P_xx=(X_i*np.matmul(C,X_i)/(X*X)).sum()
		P_yy=(Y_i*np.matmul(C,Y_i)/(Y*Y)).sum()
		P_tt=(T_i*np.matmul(C,T_i)/(T*T)).sum()
		spi=(X*P_xx+Y*P_yy)/(T*P_tt)
		return spi;

#a=np.random.rand(3,5)
#a[2,]+=(a[0,]+a[1,])
#b=np.random.rand(5,5)
#b=0.5*(b+b.T)	
#print(SPI(a,b))


def RCL(mat,C): #relative clustering index
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[x1,x2,x3,....,xm],[y1,y2,y3,....,ym]] = 2*m 2D-numpy-matrix
	#xi is the actual number of group x in unit/division i
	#yi is the actual number of group y in unit/division i
	#format C=[Cij] = m*m 2D-numpy-matrix
	#Cij=exp(-dij)
	#dij is the distance between centroids of units i and j
	X=(mat[0,]).sum().sum()+0.0 #total group x population
	Y=(mat[1,]).sum().sum()+0.0 #total group y population
	if len(mat.shape)>2 or mat.shape[0]!=2 or C.shape[0]!=mat.shape[1] or C.shape[1]!=mat.shape[1]:
		print("invalid matrix or population or both","matrix size="+str(mat.shape))
		return(-100);
	else:
		X_i=mat[0,]
		Y_i=mat[1,]
		P_xx=(X_i*np.matmul(C,X_i)/(X*X)).sum()
		P_yy=(Y_i*np.matmul(C,Y_i)/(Y*Y)).sum()
		rcl=(P_xx/P_yy)-1
		return rcl;


#a=np.random.rand(2,5)
#b=np.random.rand(5,5)
#b=0.5*(b+b.T)	
#print(RCL(a,b))

