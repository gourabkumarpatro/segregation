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


#---------------------------EVENNESS------------------------------------
def bi_dissimilarity(mat):
	#according to https://en.wikipedia.org/wiki/Index_of_dissimilarity
	#format mat=[[a1,b1],[a2,b2],....,[am,bm]] = 2*m 2D-numpy-matrix
	#ai and bi are the actual number of group a and b in unit/division i
	if len(mat.shape)>2 or mat.shape[0]!=2:
		print("invalid matrix size ",mat.shape)
		return(-100);
	else:
		n_units=mat.shape[1]
		dis=0
		A=(mat[0,]).sum().sum()+0.0
		B=(mat[1,]).sum().sum()+0.0
		#print(A,B)
		for i in range(n_units):
			#print(abs((mat[0,i]/A)-(mat[1,i]/B)))
			dis+=abs((mat[0,i]/A)-(mat[1,i]/B))
		dis/=2
		return dis;


def self_dissimilarity(mat):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#ai is the actual number of group a in unit/division i
	#ti is the total number in unit/division i
	P=(mat[0,]).sum().sum()+0.0 #total group population
	T=(mat[1,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=2 or P>T or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T),"group population="+str(P))
		return(-100);
	else:
		#n_units=mat.shape[1]
		#dis=0
		#for i in range(n_units):
			#dis+=abs((mat[0,i]*T)-(P*mat[1,i]))
		#print('dis1',dis)
		#dis/=(2*P*(T-P))
		#print('dis2',dis)
		x=mat[0,]*T
		y=mat[1,]*P
		temp=np.absolute(x-y).sum()
		#print('dis1',temp)
		dis=temp/(2*P*(T-P))
		#print('dis2',dis)
		return dis;
		


def gini(mat):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#ai is the actual number of group a in unit/division i
	#ti is the total number in unit/division i
	P=(mat[0,]).sum().sum()+0.0 #total group population
	T=(mat[1,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=2 or P>T or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T),"group population="+str(P))
		return(-100);
	else:
		#n_units=mat.shape[1]
		#dis=0
		#for i in range(n_units):
			#for j in range(n_units):
				#dis+=abs((mat[0,i]*mat[1,j])-(mat[0,j]*mat[1,i]))
		#print('dis1',dis)
		#dis/=(2*P*(T-P))
		#print('dis2',dis)
		x=np.mat(mat[0,])
		y=np.mat(mat[1,]) 
		temp=np.absolute(((x.T)*y-(y.T)*x))
		#print('dis1',temp.sum().sum())
		gn=temp.sum().sum()/(2*P*(T-P))
		#print('dis2',dis)
		return gn;
		
def entropy(mat):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#ai is the actual number of group a in unit/division i
	#ti is the total number in unit/division i
	P=(mat[0,]).sum().sum()+0.0 #total group population
	T=(mat[1,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=2 or P>T or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T),"group population="+str(P))
		return(-100);
	else:
		E=(P*np.log((T-P)/P)+T*np.log(T/(T-P)))/T #total group a entropy
		#print('total entropy',E)
		P_i=mat[0,] #unit-wise group a population
		#print("unit-wise group population",P_i)
		T_i=mat[1,] #unit-wise total population
		#print("unit-wise total population",T_i)
		E_i=(P_i*np.log((T_i-P_i)/P_i)+T_i*np.log(T_i/(T_i-P_i)))/T_i #unit-wise group a entropy
		#print("unit-wise group a entropy",E_i)
		H=(T_i*(E-E_i)/(E*T)).sum()
		#print("unit-wise unit weighted deviation",H)
		return H;


def atkinson(mat,b):
	#according to https://www.jstor.org/stable/2579183 and https://www.census.gov/hhes/www/housing/resseg/pdf/app_b.pdf
	#format mat=[[a1,a2,a3,....,am],[t1,t2,t3,....,tm]] = 2*m 2D-numpy-matrix
	#ai is the actual number of group a in unit/division i
	#ti is the total number in unit/division i
	#b=shape parameter
	#0<b<1
	#0<b<0.5 => gives more weights to areas under-represented by group a i.e. (p_i/t_i)<(P/T)
	#0.5<b<1 => gives more weights to areas over-represented by group a i.e. (p_i/t_i)>(P/T)
	P=(mat[0,]).sum().sum()+0.0 #total group population
	T=(mat[1,]).sum().sum()+0.0 #total population
	if len(mat.shape)>2 or mat.shape[0]!=2 or P>T or (mat[0,]>mat[1,]).sum()!=0:
		print("invalid matrix or population or both","matrix size="+str(mat.shape),'total population='+str(T),"group population="+str(P))
		return(-100);
	else:
		P_i=mat[0,] #unit-wise group a population
		#print("unit-wise group population",P_i)
		T_i=mat[1,] #unit-wise total population
		#print("unit-wise total population",T_i)
		temp=((((T_i-P_i)**(1-b))*(P_i**b)).sum()/P)**(1/(1-b))
		#print("temp",temp)
		A=1-((P/(T-P))*temp)
		return A;


a=np.random.rand(2,5)
a[1,]+=a[0,]
print('a',a)
#print(bi_dissimilarity(a))
#print(self_dissimilarity(a))
#print(gini(a))
#print(entropy(a))
#print(atkinson(a,0.3))



#def inequality():


