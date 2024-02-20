import numpy as np
from scipy.linalg import inv, eig

def matrix_operations():
    # user input for the dimensions of the matrix
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))

    # user input for the matrix elements
    print("Enter the matrix elements row-wise:")
    matrix = []
    for i in range(rows):
        row = [float(input()) for _ in range(cols)]
        matrix.append(row)

    # Convert the list of lists to a NumPy array
    matrix = np.array(matrix)

    # Display the original matrix
    print("\nOriginal Matrix:")
    print(matrix)

    # matrix operations
    while True:
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Inverse")
        print("5. Adjoint")
        print("6. Eigenvalues")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            # Addition
            matrix2 = np.array([[float(input()) for _ in range(cols)] for _ in range(rows)])
            result = matrix + matrix2
            print("\nResult of Addition:")
            print(result)
        elif choice == 2:
            # Subtraction
            matrix2 = np.array([[float(input()) for _ in range(cols)] for _ in range(rows)])
            result = matrix - matrix2
            print("\nResult of Subtraction:")
            print(result)
        elif choice == 3:
            # Multiplication
            matrix2 = np.array([[float(input()) for _ in range(cols)] for _ in range(rows)])
            result = np.dot(matrix, matrix2)
            print("\nResult of Multiplication:")
            print(result)
        elif choice == 4:
            # Inverse
            try:
                inverse_matrix = inv(matrix)
                print("\nInverse Matrix:")
                print(inverse_matrix)
            except np.linalg.LinAlgError:
                print("Matrix is not invertible.")
        elif choice == 5:
            # Adjoint
            determinant = np.linalg.det(matrix)
            adjoint_matrix = np.linalg.inv(matrix) * determinant
            print("\nAdjoint Matrix:")
            print(adjoint_matrix)
        elif choice == 6:
            # Eigenvalues
            eigenvalues = eig(matrix)[0]
            print("\nEigenvalues:")
            print(eigenvalues)
        elif choice == 7:
            # Exit
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


matrix_operations()
