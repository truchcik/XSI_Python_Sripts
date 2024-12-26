ap = Application
oObj = ap.selection[0]

def get_point_array(oObj):
	ppos = list(oObj.activeprimitive.geometry.points.PositionArray)
	ppos = [ [round(x,10),round(y,10),round(z,10)] for x,y,z in ppos]
	#print(ppos)
	return(ppos)

def dstack(lista):
	nlista = []
	for k,v in enumerate(lista[0]):
		nlista.append([x[k] for x in lista])
	return(nlista)


def multiply_vector_by_matrix(vector, matrix):
	nvector =  []
	for k in range(3):
		nvector.append(vector[k]*matrix[k][0] + vector[k]*matrix[k][1]  + vector[k]*matrix[k][2])
	return nvector
	
triangle1 = get_point_array(oObj)
triangle1 = dstack(triangle1)
print 'Triangle0', triangle1


#tmatrix = [[-0.466, 0.531, -0.088], [-0.791, -0.532, 0.894], [-0.347, -0.182, 1.0]]
#tmatrix = [[1, 0, 0], [0, -1, 0], [0, 0, -1.0]] #180 stopni
#tmatrix = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
tmatrix = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
#tmatrix = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]


ntriangle = []
for vector in triangle1: ntriangle.append(multiply_vector_by_matrix(vector, tmatrix))
print 'Triangle1', ntriangle

ntriangle = dstack(ntriangle)
oObj.activeprimitive.geometry.Points.PositionArray = ntriangle
print ' ' 



#sin90 = 1
#cos90 = 0

#cos -sin 0
#sin cos 0
#0 0 1

