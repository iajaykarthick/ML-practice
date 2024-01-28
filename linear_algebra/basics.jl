using LinearAlgebra

# Vector
x = [1, 2, 3]  # 64 bit integer vector; 3 x 1 vector
println(typeof(x)) # Array{Int64, 1}; 

x = Int8[1, 2, 3]  # 8 bit integer vector
println(typeof(x)) # Array{Int8, 1};
println(size(x)) # (3,)

# Julia primarily treats one-dimensional arrays as column vectors whenever an implicit conversion is expedient.

# To get a row vector, we can take conjugate transpose (adjoint) of a column vector 
println(adjoint(x), size(adjoint(x))) 
# we can also use transpose(x) or x' to get a row vector 
println(transpose(x), size(transpose(x)))
println(x', size(x')) # post-fix operator

# Treating a one-dimensional array as a column vector is helpful in matrix-vector multiplication
# Matrix-vector multiplication

# Matrix
A = [1 2; 3 4]  # m x n matrix; m=2 rows, n=2 columns
x = [1, 2]  # n x 1 vector; n=2 rows, 1 column
println(A * x) # m x 1 vector; m=2 rows, 1 column


# Matrix
A = [1 2 3; 5 3 4; 1 4 2]  # m x n matrix; m=3 rows, n=3 columns
B = [5 3 6; 7 10 8; 7 3 1]  # n x p matrix; n=3 rows, p=3 columns

println(typeof(A), " ", typeof(B))

m = 3
n = 3
p = 3
C = zeros(m, p)


# 1: Martix Product; Column-wise (Dot Product)
for i=1:p
    C[:, 1] = A * B[:, i]
end
println(C)


# 2: Martix Product; Row-wise (Dot Product)
for j=1:m
    C[j:j, :] = A[j:j, :] * B # A[j:j, :] is a row vector while A[j, :] is a column vector; 
    # Matrix first, vector second; Vector must be a column vector
    # Vector first, matrix second; Vector must be a row vector
end
println(C)

## Note:
# BLAS (Basic Linear Algebra Subprograms) functions
## In Julia, xGEMM and xGEMV are functions used for linear algebra computations, but they serve different purposes:

## xGEMM (generalized matrix-matrix multiplication):
## C = αA * B + βC
## A and B are matrices, C is the result matrix
## α and β are scalars
## used for multiplying two matrices and adding the result to a third matrix
## more computationally expensive than xGEMV due to the double matrix multiplication

## xGEMV (generalized matrix-vector multiplication):
## y = αA * x + βy
## A is a matrix, x and y are vectors
## α and β are scalars
## used for multiplying a matrix and a vector and adding the result to a vector
## less computationally expensive than xGEMM due to the single matrix multiplication

## Choosing between them:
## If you want to multiply two matrices, use xGEMM.
## If you want to multiply a matrix and a vector, use xGEMV.

A_f = convert(Array{Float64, 2}, A) 
B_f = convert(Array{Float64, 2}, B) 

# 2: Martix Product; Row-wise (Dot Product) Using BLAS xGEMV - accelerated version
for j=1:m
    # B_f is the matrix, A_f[j, :] is the column vector; BLAS.gemv returns B_f' * A_f[j, :]
    # gemv accepts Float64 type matrix and vector
    C[j, :] = BLAS.gemv('T', B_f, A_f[j, :]) 
end
println(C)


# Combining all approaches
C_1 = zeros(m, p)
C_2 = zeros(m, p)
C_3 = zeros(m, p)

for j=1:m
    # B_f is the matrix, A_f[j, :] is the column vector; BLAS.gemv returns B_f' * A_f[j, :]
    # gemv accepts Float64 type matrix and vector
    C_1[j, :] = BLAS.gemv('T', B_f, A_f[j, :]) 
    # Use Julia matrix multiplication operator; B' * A[j, :]
    C_2[j, :] = B' * A[j, :] 
    # Use Julia matrix multiplication operator; A[j, :] * B
    # A[j:j, :] is a row vector while B is a matrix;
    # Vector first, matrix second; Vector must be a row vector
    C_3[j:j, :] = A[j:j, :] * B
end
println(C_1)
println(C_2)
println(C_3)

# 3: Matrix Product; Inner Product
C = zeros(m, p)

for i=1:m
    for j=1:p
        C[i:i, j] = A[i:i, :] * B[:, j]
    end
end

# Potential Drawback:
# * Extracts 1xn and nx1 vectors from A and B for each iteration
# * Creates temporary 1x1 matrix for each iteration 
# * It can involve some overhead if the matrix is large
# * Performs a separate matrix multiplication (A[i:i, :] * B[:, j]) for each element of C
# * This might not fully utilize the BLAS optimization for larger matrix operations.

# 3.a Matrix Product; Inner Product Using BLAS optimized dot function (BLAS Level-1 routine)
C = zeros(m, p)
for i = 1:m
    for j = 1:p
        # dot function takes complex conjugate of the first argument
        C[i, j] = dot(conj(view(A, i, :)), view(B, :, j))
    end
end
println(C)


# 4: Matrix Product; Outer Product
C = zeros(m, p)
for k=1:n
    # A[:, k] is a column vector while B[k:k, :] is a row vector
    global C = C + A[:, k] * B[k:k, :]
end
println(C)

# Potential Drawback:
# Julia uses matrix-matrix multiplication for each iteration to compute the outer product
# This can be accelerated using BLAS xGER function (BLAS Level-2 routine)

# 4.a Matrix Product; Outer Product Using BLAS xGER function (BLAS Level-2 routine)
# Matrix-matrix multiplication via rank-1 updates
# C = αx * y' + C

A_f = convert(Array{Float64, 2}, A) 
B_f = convert(Array{Float64, 2}, B) 

# A_f = [1.0 2.0 3.0; 2.0 4.0 6.0; 1.0 5.0 2.0]
# B_f = [1.0 1.0 2.0; 2.0 3.0 1.0; 4.0 1.0 2.0]


C = zeros(m, p)
for k=1:n
    # x = A[:, k] is a vector of the elements from the kth column of A  -- Treated as a column vector by default in Julia
    # y = B[k, :] is a vector of the elements from the kth row of B -- Treated as a column vector by default in Julia
    # α = 1.0
    # BLAS.ger! performs the rank-1 update of the matrix C as C = αx * y' + C
    BLAS.ger!(1.0, A_f[:, k], B_f[k, :], C)
    # println(A_f[:, k], B_f[k, :])
    # println(C)
end
println(C)