# The Ultimate NumPy Cheat Sheet for AI/ML Mathematics

## Why NumPy for AI?

## *Vectorization: It applies math to entire arrays at once, skipping slow Python for loops.

## *Broadcasting: It mathematically aligns arrays of different shapes automatically.

## *C-Backend: It runs near the speed of C, handling millions of data points instantly.

# 1. Array Creation & Tensors (The Foundations)

In AI, data (images, text, prices) is converted into N-dimensional arrays (Tensors).

import numpy as np

# 1D Array (Vector) - e.g., A single house's features
v = np.array([1, 2, 3]) 

# 2D Array (Matrix) - e.g., A batch of 3 houses, each with 3 features
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 

# Zeros & Ones - Great for initializing neural network weights or biases
zeros = np.zeros((3, 3))   # 3x3 matrix of 0s
ones = np.ones((2, 4))     # 2x4 matrix of 1s

# Sequences - Great for creating X-axes for plotting graphs
x = np.linspace(0, 10, 100)  # 100 evenly spaced numbers from 0 to 10
steps = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]


2. Shape, Reshaping, & Dimensionality

Neural networks are extremely strict about data shapes. You will use these constantly to fix "Shape Mismatch" errors.

# Check dimensions
print(M.shape)  # Returns (3, 3)

# Reshape data (Crucial for feeding images into neural networks)
# e.g., Flattening a 2x2 image into a 1D vector of 4 pixels
img = np.array([[255, 0], [0, 255]])
flat_img = img.reshape(4)  # Now [255, 0, 0, 255]

# Add a dimension (Often needed to create "Batch" dimensions for PyTorch/TF)
v_batch = np.expand_dims(v, axis=0)  # Changes shape from (3,) to (1, 3)

# Transpose (Flipping rows to columns - crucial for Dot Products)
M_T = M.T  


3. Linear Algebra (Days 1–30)

The geometric engine of Machine Learning.

A = np.array([1, 2])
B = np.array([3, 4])

# Element-wise Operations (Day 1)
add = A + B       # [4, 6]
multiply = A * B  # [3, 8] (Hadamard Product)

# Dot Product (Day 2) - The core of Neural Networks & Cosine Similarity
dot_prod = np.dot(A, B)      # 1*3 + 2*4 = 11
dot_prod_alt = A @ B         # Modern Python syntax for Dot Product

# Vector Magnitude / L2 Norm (Day 3 & 4) - Length of a vector
length = np.linalg.norm(A)   # sqrt(1^2 + 2^2)

# Matrix Stacking (Day 5) - Combining vectors into a single matrix
matrix_A = np.column_stack([A, B]) 

# Advanced Algebra (Upcoming in Phase 2 & 3)
inverse = np.linalg.inv(matrix_A)          # Matrix Inverse
eigenvals, eigenvecs = np.linalg.eig(matrix_A) # Eigenvalues/Vectors (PCA)


4. Probability & Statistics (Days 56–85)

How AI handles uncertainty, distributions, and error calculation.

data = np.array([10, 20, 30, 40, 50, 100])

# Core Descriptive Stats
mean = np.mean(data)      # Average
median = np.median(data)  # Middle value (robust to the '100' outlier)
variance = np.var(data)   # How spread out the data is
std_dev = np.std(data)    # Standard deviation (sqrt of variance)

# Min/Max and Argmax (CRITICAL for Classification)
# In AI, outputting probabilities [0.1, 0.8, 0.1], argmax tells you "Index 1 is the prediction"
max_val = np.max(data)      # Returns 100
pred_idx = np.argmax(data)  # Returns 5 (the index where 100 is located)

# Randomness (For initializing Neural Network weights randomly)
rand_uniform = np.random.rand(3, 3)   # Random numbers between 0 and 1
rand_normal = np.random.randn(3, 3)   # Random numbers from a Gaussian Bell Curve


5. Calculus & Core ML Functions (Days 31–55, 86–100)

The math of Backpropagation and Activation Functions.

x = np.array([0.001, 1, 2, 3])

# Exponentials & Logarithms 
# Crucial for Cross-Entropy Loss and Softmax functions
exp_x = np.exp(x)  # e^x
log_x = np.log(x)  # Natural log (ln)

# Gradients (Basic numerical derivative)
# AI uses automatic differentiation, but NumPy can calculate discrete differences
dy_dx = np.gradient(exp_x) 

# Clipping (Preventing "Exploding Gradients" in deep learning)
# Forces all values to stay within a specific min and max range
safe_x = np.clip(x, a_min=0.5, a_max=2.5) 


💡 The "Golden Rules" of NumPy for AI

Never use for loops if you can avoid it. If you are looping through numbers to add them together, you are doing it wrong. Use np.sum() or vector addition A + B.

Always check .shape. 90% of bugs in AI/ML engineering are "Shape Mismatch" errors where you try to multiply a (3, 2) matrix by a (4, 1) matrix. Print your shapes constantly!

Beware of memory. Doing A = A + B creates a copy in memory. If your arrays are massive (like high-res images), this crashes computers.