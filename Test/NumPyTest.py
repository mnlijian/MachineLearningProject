import numpy as np
# a = np.array([[1,2],[3,4]])
# print("多余一个维度的数组")
# print(a)
#
# a = np.array([1,2,3,4,5],ndmin=2)
# print(a)
#
# a = np.array([1,2,3],dtype=complex)
# print(a)
#
# dt = np.dtype(np.int32)
# print(dt)
#
# dt = np.dtype('i4')
#
# print(dt)

# dt = np.dtype([('age',np.int8)])

# a = np.array([(10,),(20,),(30,)],dtype=dt)
# print(a['age'])
# print(a)

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])

a = np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print(student)
print(a)
print(a('student'))
