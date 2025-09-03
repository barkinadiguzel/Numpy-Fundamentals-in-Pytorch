# =========================================
# NumPy Fundamentals - Beginner to Intermediate
# =========================================

# 1️⃣ Creating Arrays
import numpy as np

# From Python list
my_list = [1, 2, 3, 4, 5, 6]
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=int)
print(a)  # array of integers
print(type(a))  # <class 'numpy.ndarray'>

# 1D slicing
print(a[:3])  # first 3 elements
print(a[::2])  # every second element

# 2D array
b = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12]])
print(b)
print(np.shape(a))  # shape of 1D array
print(np.shape(b))  # shape of 2D array

# Creating arrays using functions
np2 = np.arange(0, 10, 2)  # 0 to 10 with step 2
print(np2)
np3 = np.zeros(10)  # array of zeros
print(np3)
np4 = np.zeros((3, 10))  # 2D zeros array (3 rows, 10 columns)
print(np4)
np5 = np.full((12), 6)  # array filled with 6
print(np5)
np6 = np.array(my_list)  # convert list to np array
print(np6)

# Reshaping arrays
np8 = a.reshape(2, 2, 3)  # reshape to 3D array
print(np8)
np9 = np8.reshape(-1)  # flatten to 1D
print(np9)

# =========================================
# 2️⃣ Array Operations
np1 = np.array([-4, 0, 1, 2, 3, 4, 5, 6, 7])
print(np1[1:5])  # slicing
print(np.sqrt(np.absolute(np1)))  # sqrt only works with non-negative numbers
print(np.absolute(np1[0]))  # absolute value
print(np.exp(np1))  # exponential, e^x
print(np.sign(np1))  # returns -1,0,1 based on sign
print(max(np1))  # python built-in max function

# Views vs Copies
np2 = np1.view()  # creating a view, changes affect original array
np3 = np1.copy()  # creating a copy, independent from original

# =========================================
# 3️⃣ Indexing, Boolean Masking and Sorting
np2 = np.array([6, -2, 8, 9, 10, 11, -2])
np3 = np.sort(np2)  # sorted array
print(np3)

# Boolean indexing
nptf = [True, True, False, False, False, False, False]
print(np2[nptf])  # selects elements where True

# Where function
y = np.where(np2 == -2)
print(y[0])
print(np2[y[0]])  # selects elements matching condition

# Iterating arrays
np1 = np.array([[[1,2,3], [2,3,4],[3,4,5],[4,5,6]]])
for x in np.nditer(np1):
    print(x)

# Sum along axis
print(np.sum(np1, axis=1))  # sum along columns of 2D slice

# =========================================
# 4️⃣ Conditional Selection
ages = np.array([[12, 43, 23, 43, 232, 13, 13, 4, 3, 2],
                 [21, 314, 53, 63, 31, 21, 21, 342, 32, 24]])
teenagers = ages[ages < 18]  # select elements < 18
print(teenagers)

# np.where with ternary
print(np.where(ages >= 18, ages, -1))  # if >=18 keep value else -1

# =========================================
# 5️⃣ Random Numbers
rng = np.random.default_rng()  # create random generator
print(rng.integers(low=1, high=7, size=1))  # random int between 1-6
print(np.random.uniform())  # random float between 0-1

# =========================================
# 6️⃣ Key Notes
# - np.array() converts Python lists into NumPy arrays
# - Shape, slicing, reshaping are fundamental for ML/AI preprocessing
# - Boolean indexing allows easy selection
# - np.where is very powerful for conditional replacement
# - np.random.default_rng() is preferred over np.random.seed()
