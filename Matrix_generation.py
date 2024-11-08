import numpy as np

class MatrixGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def random_matrix(self, min_val=0, max_val=10):
        """Generates a random matrix with values between min_val and max_val."""
        return np.random.randint(min_val, max_val, (self.rows, self.cols))

    def identity_matrix(self):
        """Generates an identity matrix (only possible if it's square)."""
        if self.rows != self.cols:
            raise ValueError("Identity matrix can only be generated for square matrices.")
        return np.identity(self.rows)

    def zero_matrix(self):
        """Generates a matrix filled with zeros."""
        return np.zeros((self.rows, self.cols))

    def ones_matrix(self):
        """Generates a matrix filled with ones."""
        return np.ones((self.rows, self.cols))

    def custom_matrix(self):
        """Allows user to manually input values for each element in the matrix."""
        print("Enter matrix values row by row, separated by spaces:")
        matrix = []
        for i in range(self.rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != self.cols:
                raise ValueError("Incorrect number of elements in row.")
            matrix.append(row)
        return np.array(matrix)

    def display_matrix(self, matrix):
        """Prints the matrix in a readable format."""
        print("Matrix:")
        for row in matrix:
            print(" ".join(f"{val:5.2f}" for val in row))

    def add_matrices(self, matrix_a, matrix_b):
        """Adds two matrices."""
        if matrix_a.shape != matrix_b.shape:
            raise ValueError("Matrices must have the same dimensions to add.")
        return matrix_a + matrix_b

    def multiply_matrices(self, matrix_a, matrix_b):
        """Multiplies two matrices."""
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError("Number of columns in first matrix must equal number of rows in second.")
        return np.dot(matrix_a, matrix_b)

# Main Program to Demonstrate Functionality
if __name__ == "__main__":
    # Define matrix dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    generator = MatrixGenerator(rows, cols)

    # Generating different types of matrices
    random_mat = generator.random_matrix()
    zero_mat = generator.zero_matrix()
    ones_mat = generator.ones_matrix()

    print("\nRandom Matrix:")
    generator.display_matrix(random_mat)

    print("\nZero Matrix:")
    generator.display_matrix(zero_mat)

    print("\nOnes Matrix:")
    generator.display_matrix(ones_mat)

    # Generate identity matrix if possible
    if rows == cols:
        identity_mat = generator.identity_matrix()
        print("\nIdentity Matrix:")
        generator.display_matrix(identity_mat)

    # Custom matrix
    custom_mat = generator.custom_matrix()
    print("\nCustom Matrix:")
    generator.display_matrix(custom_mat)

    # Demonstrate addition and multiplication if dimensions allow
    try:
        sum_matrix = generator.add_matrices(random_mat, ones_mat)
        print("\nSum of Random Matrix and Ones Matrix:")
        generator.display_matrix(sum_matrix)
    except ValueError as e:
        print(e)

    if cols == rows:
        product_matrix = generator.multiply_matrices(random_mat, custom_mat)
        print("\nProduct of Random Matrix and Custom Matrix:")
        generator.display_matrix(product_matrix)
    else:
        print("Matrix multiplication requires the first matrix's columns to match the second matrix's rows.")
