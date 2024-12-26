def matrix_solve(A, B):
    """
    Solves the system of linear equations A * X = B for X, where A and B are 3x3 matrices.

    Args:
        A: A 3x3 list representing the coefficients matrix.
        B: A 3x3 list representing the constants matrix.

    Returns:
        A 3x3 list representing the solution matrix X.
    """
    # Compute the determinant of A
    det = (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
        A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
        A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )

    if det == 0:
        raise ValueError("Matrix A is singular and cannot be inverted.")

    inv_det = 1.0 / det

    # Compute the adjugate and inverse of A
    adj = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[A[x][y] for y in range(3) if y != j] for x in range(3) if x != i]
            adj[j][i] = ((-1) ** (i + j)) * (
                minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            )
    
    A_inv = [[adj[i][j] * inv_det for j in range(3)] for i in range(3)]

    # Compute the product of A_inv and B
    X = [[sum(A_inv[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

    return X

def compute_transformation_matrix(triangle1, triangle2):
    """
    Computes the affine transformation matrix that maps triangle1 to triangle2.

    Args:
        triangle1: A list of three vertices [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)] for the source triangle.
        triangle2: A list of three vertices [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)] for the target triangle.

    Returns:
        A 3x3 list-based transformation matrix.
    """
    # Add a column of ones to the triangles to handle translation (homogeneous coordinates)
    triangle1_h = [
        [triangle1[0][0], triangle1[0][1], 1],
        [triangle1[1][0], triangle1[1][1], 1],
        [triangle1[2][0], triangle1[2][1], 1]
    ]

    triangle2_h = [
        [triangle2[0][0], triangle2[0][1], 1],
        [triangle2[1][0], triangle2[1][1], 1],
        [triangle2[2][0], triangle2[2][1], 1]
    ]

    # Compute the affine transformation matrix
    transformation_matrix = matrix_solve(triangle1_h, triangle2_h)  # Solves for M in T1 * M = T2

    return transformation_matrix

# Example usage
#triangle1 = [(2.0, 0.0, -4.0), (0.0, 3.0, -1.0), (0.0, 0.0, 0.0)]
#triangle2 = [(-0.0, 3.0, -1.0), (-2.0, -0.0, 4.0), (-0.0, 0.0, 0.0)]

#triangle1 = [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [-4.0, -1.0, 0.0]]
#triangle2 = [[-0.0, -2.0, -0.0], [3.0, -0.0, 0.0], [-1.0, 4.0, 0.0]]

transformation_matrix = compute_transformation_matrix(triangle1, triangle2)
print("Transformation Matrix:")
print(transformation_matrix)
transformation_matrix = [[round(x,10),round(y,10),round(z,1)] for x,y,z in transformation_matrix]
print(transformation_matrix)
