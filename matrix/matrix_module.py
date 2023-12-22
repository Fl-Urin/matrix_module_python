#functions
def ones(n:int):
    return Matrix([[1 for _ in range(n)] for _ in range(n)])
def eye(n:int):
    return Matrix([[1 if i == j else 0 for i in range(n)] for j in range(n)])

def prod(nums):
    """
    DOCT:
    input: list with only number values
    output: product of all values in the list """
    assert all(isinstance(value, (float, int, complex)) for value in nums), "some value is not a number"

    inner_product = 1
    for val in nums:
        inner_product*=val
    return inner_product



#determinate functions
def gauss_algo(mat):
    if not isinstance(mat, Matrix):
        raise ValueError("the provided value is not a matrix")
    if mat.get_shape() == (0,0):
        return Matrix([[0]])

    def invers_finder(mat, n):
        """DOCT:
        this func finds the amount of how many times I neede to subtract the rows from each other
        
        mat[n][n] is the pivot, where as mat[m][n] is the element I want to find the inverse for"""
        return [mat[m][n]/mat[n][n] for m in range(n+1,shape)]
    
    def left_multi_finder(vals, shape, n):
        """DOCT:
        find the matrix I need to do left-sided multiplication with
        for the desired elementary row operation"""
        #first create lists with the same shape as the matrix, then replace with the elem row op vals
        inv_val_mat = [[1 if j == i else 0 for j in range(shape)] for i in range(shape)]
        for m in range(shape-n-1):
            inv_val_mat[m+n+1][n] = -1*vals[m]
        
        #to see the intermediate steps uncomment the print statements
        print(f"next elem mat:\n{Matrix(inv_val_mat)}\n")
        return Matrix(inv_val_mat)

    #as only quadratic matrices are being handeled
    next_mat = mat.get_matrix()
    shape = mat.get_shape()[0]

    for n in range(shape-1):
        left_mat = left_multi_finder(invers_finder(next_mat, n), shape, n)
        next_mat = left_mat * Matrix(next_mat)
        

        print(f"new mat after mult:\n{next_mat}\n")
        next_mat = next_mat.get_matrix()
        
    return Matrix(next_mat)

def laplace_expansion_recursive(matrix:list[list]) -> float:
    """DOCT:
    input: matrix
    output: det(matrix)
    
    this function finds the det of a provided matrix recursively using laplace expansion"""

    shape = len(matrix),len(matrix[0])

    #NOTE: Basecase
    if (1,1) == shape:
        return matrix[0][0]

    total = 0
    for col in range(shape[0]):
        m = [row[1:] for row in matrix[:col]+matrix[col+1:]]
        val = matrix[col][0]
        sgn = 1 if col%2 == 0 else -1
        total+= sgn*val*laplace_expansion_recursive(m)
    return total

def laplace_expansion(mat):
    "DOCT: returns the determinate if the matrix ∈ Mₙ(K) using laplace expansion"
    assert mat.get_shape()[0] == mat.get_shape()[1]
    
    return laplace_expansion_recursive(mat.get_matrix())

det_functions = {laplace_expansion, gauss_algo}



#Objects
class Matrix:
    def __init__(self, matrix_list):
        assert isinstance(matrix_list, list)
        assert matrix_list != [], "empty matrix provided"
        assert all(all(isinstance(val, (int, float, complex)) for val in row) for row in matrix_list), "some value is not an int or float"
        assert len(set(len(row) for row in matrix_list)) == 1, "inequal length of nested lists"
        assert any(row for row in matrix_list), "some list is empty"

        self.__matrix = tuple(matrix_list)
        self.__shape = len(matrix_list),len(matrix_list[0])


    #NOTE: reenabeling accessing privaticed attributes
    def get_matrix(self):
        return list(self.__matrix)
    
    def get_shape(self):
        return self.__shape
    
    def get_trans(self):
        return list(self.__trans)
    

    #NOTE:making matrices comparable and hashable
    def __eq__(A,B):
        if not isinstance(B, Matrix):
            return NotImplemented
        
        return all(A.__matrix[m] == B.__matrix[m] for m in range(A.__shape[0]))
    
    def __hash__(self):
        return hash((m for m in self.__matrix))
    

    #NOTE: representing Methods
    def __repr__(self):
        return f"Matrix({self.get_matrix()})"

    def __str__(self):
        return "]\n[".join(str(self.get_matrix()).split("], ["))


    #NOTE: operations for matrices
    def __add__(A, B):
        if not isinstance(B, Matrix):
            return NotImplemented
        
        if A.__shape != B.__shape:
            raise Warning("your matrices must have the same shapes")

        return Matrix([[A.__matrix[m][n]+B.__matrix[m][n] for n in range(A.__shape[1])]
                        for m in range(A.__shape[0])])
    
    def __sub__(A,B):
        if not isinstance(B, Matrix):
            return NotImplemented
        
        if A.__shape != B.__shape:
            raise Warning("your matrices must have the same shapes")
        
        return Matrix([[A.__matrix[m][n]-B.__matrix[m][n] for n in range(A.__shape[1])]
                        for m in range(A.__shape[0])])

    def __mul__(A, B):
        if not isinstance(B, (Matrix, int, float, complex)):
            return NotImplemented
        

        #NOTE: multiplying the whole matrix by some constant
        if isinstance(B, (int, float, complex)):
            return Matrix([[B*A.__matrix[m][n] for n in range(A.__shape[1])]for m in range(A.__shape[0])])
        
        if A.__shape[1] != B.__shape[0]:
            raise Warning("invalid shape for matrices")
        
        return Matrix([[
            sum(A.__matrix[m][i]*B.__matrix[i][n] for i in range(A.__shape[1]))
                for n in range(B.__shape[1])]
                    for m in range(A.__shape[0])])
    

    def trans(A):
        return Matrix([[A.__matrix[n][m] for n in range(A.__shape[1])] for m in range(A.__shape[0])])
    
    #NOTE: using the Gaussian Algorithm to find the det of a matrix
    def det(self, variant=gauss_algo):
        assert variant in det_functions, "not supported method to find determinate"
        if self.__shape[0] != self.__shape[1]:
            raise Warning("this module is not capable of calculating Minors of Matrices")
        
        #if the det has already been computed return the value
        try:
            return self.__det
        #else compute it and return it
        except AttributeError:
            if variant != gauss_algo: return variant(self)
            upper_mat = gauss_algo(self).get_matrix()
            self.__det = prod([upper_mat[i][i] for i in range(len(upper_mat[0]))])
            return self.det()
        

class Polynomial:
    field = "x"
    def __init__(self, coefs):
        assert isinstance(coefs, list) and coefs, "Coefficients needs to be a list and can't be empty"
        assert all(isinstance(coef, (int, float)) for coef in coefs), "some coef is not of type (int, float)"
        self.__coefs = tuple(coefs)
        self.__deg = len(coefs) -1


    def get_coefs(self):
        return list(self.__coefs).copy()
    
    def get_deg(self):
        return len(self.get_coefs())-1

    def __repr__(self):
        return f"Polynomial({self.get_coefs()})"
    
    def __str__(self):
        return " + ".join([str(coef)+f"{Polynomial.field}^{idx}" for idx,coef in enumerate(self.get_coefs())])
    

    #polynomial functions
    def __call__(self, val):
        return sum(coef* val** deg for deg, coef in enumerate(self.get_coefs()))

    def derivative(self):
        return Polynomial([idx*coef for idx, coef in enumerate(self.get_coefs())][1:])
    


x1 = Polynomial([1,2])
print(x1.derivative())
print(x1.derivative()(4))