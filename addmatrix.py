# import numpy module

import numpy as np

 

# import python standard library module - random

import random

 

# Routine for printing a 2x2 matrix

def PrintMatrix(matrix_in):

    for x in range(0, matrix_in.shape[0]):

        for y in range(0, matrix_in.shape[1]):

            print("%d \t"%(matrix_in[x][y]), end='')

            if(y%3>1):

                print("\n")   

 

# Function to populate a 2x2 matrix with random data

def FillMatrix(matrix_in):

    for x in range(0, matrix_in.shape[0]):

        for y in range(0, matrix_in.shape[1]):

            matrix_in[x][y] = random.randrange(2, 10) + 2

 

# Create matrices using ndarray

matrix1 = np.ndarray((3,3))

matrix2 = np.ndarray((3,3))

 

# Fill the matrices i.e., the two dimensional arrays created using ndarray objects

FillMatrix(matrix1)

FillMatrix(matrix2)

 

# Add two matrices - two nd arrays

add_results = matrix1.__add__(matrix2)

 

# Print Matrix1

print("Matrix1:")

PrintMatrix(matrix1)

 

# Print Matrix2

print("Matrix2:")

PrintMatrix(matrix2)

 

# Print the results of adding two matrices

print("Result of adding Matrix1 and Matrix2:")

PrintMatrix(add_results)
